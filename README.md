## Black Crow AI Simple Model - Python

### Dependencies

* Python 3.7
* Spark 2.4.8

### Installation
1. Use `cd` to navigate to the `./bcai-simple-model-pyspark-main` directory
1. Use `virtualenv` or `Miniconda` to setup a `Python3.7` environment
1. Download Spark 2.4.8 (`spark-2.4.8-bin-hadoop2.7.tgz`) from [Spark Release Archive](https://archive.apache.org/dist/spark/spark-2.4.8/)
1. Unzip the `.tgz` and move the folder to it to `/opt` folder
    ```
      tar -xzf spark-2.4.8-bin-hadoop2.7.tgz
      mv spark-2.4.8-bin-hadoop2.7  /opt/spark-2.4.8
    ```
1. Create a symbolic link for the Spark binary
    ```
      ln -s /opt/spark-2.4.8 /opt/spark
    ```
1. Install python dependencies for project
    ```
      pip install -r requirements.txt
    ```
1. Allow `Jupyther Notebook` to use `pyspark` and `Spark` by adding the following lines to `~/.bashrc` (or `~/.zshrc`)
    ```
    # Setup Java, Spark, PyStark and Jupyter Notebook
    export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
    export SPARK_HOME=/opt/spark
    export PATH=$SPARK_HOME/bin:$PATH
    export PYSPARK_DRIVER_PYTHON=jupyter
    export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
    ```
1. Use the environment variables as created above:
    ```
      source ~/.bashrc # (or ~/.zshrc`)
    ```
1. Start PySpark in the terminal:
    ```
      pyspark
    ```
1. The Jupyter Notebook Web UI will be available at [http://localhost:8888/](http://localhost:8888/)
1. Use the `model.ipynb` to step through the lines

### Testing
The test for the useragent extractor can be run with the following command:
    ```
      python -m unittest tests.py
    ```