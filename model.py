from pyspark.sql import SparkSession
from pyspark.sql.functions import col,lit, udf
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.ml.classification import LogisticRegression
from pyspark.mllib.util import MLUtils

from user_agent_extractor import parse_device_type, parse_browser_type, parse_browser_version

def parse_device_type_function(agent):
    return parse_device_type(agent)

def parse_browser_type_function(agent):
    return parse_browser_type(agent)

def parse_browser_version_function(agent):
    return parse_browser_version(agent)

spark = SparkSession.builder.master("local[4]").getOrCreate()

parse_device_type_f = udf(parse_device_type_function)
parse_browser_type_f = udf(parse_browser_type_function)
parse_browser_version_f = udf(parse_browser_version_function)

events = (spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("sample_data/events.csv")
    .withColumn("DEVICE_TYPE", parse_device_type_f(col("USER_AGENT")))
    .withColumn("BROWSER_TYPE", parse_browser_type_f(col("USER_AGENT")))
    .withColumn("BROWSER_VERSION", parse_browser_version_f(col("USER_AGENT"))))

conversions = (spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("sample_data/conversions.csv")
    .withColumn("CONVERTED", lit(1.0)))


labeled_events = events.join(conversions, "ID", "left")

labeled_events.printSchema()
labeled_events.show()


as_double = (lambda v: float(v) if v is not None else 0.0)

featureData = (labeled_events.rdd.map(lambda r: LabeledPoint(
          as_double(r["CONVERTED"]),
          Vectors.dense(
              as_double(r["HOTEL_CITY_ID"]),
              as_double(r["TIME_TO_ARRIVAL"]),
              as_double(r["TIME_SPENT_ON_SITE"]))))).toDF()

training_and_test_data = MLUtils.convertVectorColumnsToML(featureData).randomSplit([0.7, 0.3])

lr = LogisticRegression(probabilityCol = "probability")

model = lr.fit(training_and_test_data[0])

auc = model.summary.areaUnderROC
print('Training AUC: ' + str(auc))

test = model.transform(training_and_test_data[1])
test.select("features", "label", "probability").show()




spark.stop()