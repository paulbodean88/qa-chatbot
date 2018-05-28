"""
Convert natural language into code
"""
from fuzzywuzzy import fuzz


def chat_executor(topic, qa_flow, threshold):
    """

    :param threshold:
        - Levenshtein distance between two strings
        - Matches the similarity between user input and its corresponding value saved in bot brain
        - an alternative to Regex (if any(re.findall(r'set|now', "NOW SEARCH FOR DESIGN PATTERNS", re.IGNORECASE)))
    :param qa_flow: qa flow to be executed while running the bot
    :param topic: user input to be processed by chat executor
    :return: the processed topic
    """
    if fuzz.partial_ratio(topic, "open firefox browser") > threshold:
        return qa_flow.open_page()
    elif fuzz.partial_ratio(topic, "set full screen") > threshold:
        return qa_flow.set_full_screen()
    elif fuzz.partial_ratio(topic, "now search for design patterns") > threshold:
        return qa_flow.set_query("design patterns")
    elif fuzz.partial_ratio(topic, "click search button") > threshold:
        return qa_flow.click_search()
    elif fuzz.partial_ratio(topic, "close the browser") > threshold:
        return qa_flow.close_browser()
    elif fuzz.partial_ratio(topic, "minimize browser") > threshold:
        return qa_flow.minimize_screen()
    elif fuzz.partial_ratio(topic, "now close the browser") > threshold:
        return qa_flow.close_browser()
    else:
        return topic
