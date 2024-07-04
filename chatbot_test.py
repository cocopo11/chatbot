from chatbot import Chat, register_call
import os
import warnings
import wikipedia

warnings.filterwarnings("ignore")



@register_call("wiki")
def who_is(session=None, query='South Korea'):
    try:
        return wikipedia.summary(query)
    except Exception:
        pass
    return "I don't know about " + query


@register_call("do_you_know")
def do_you_know(session=None, query=None):
    return "I do not know about " + query


first_question = "Hi, how are you?"
chat = Chat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "chatbot_test.template"))
chat.converse(first_question)