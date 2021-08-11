from user_agents import parse

def parse_device_type(user_agent_text):
    return define_device_type(parse(user_agent_text))

def parse_browser_type(user_agent_text):
    return parse(user_agent_text).browser.family

def parse_browser_version(user_agent_text):
    return parse(user_agent_text).browser.version_string

def define_device_type(agent):
    if agent.is_mobile:
        return 'Mobile'
    elif agent.is_tablet:
        return 'Tablet'
    elif agent.is_pc:
        return 'Computer'
    elif agent.is_bot:
        return 'Bot'
    else:
        return 'Other'