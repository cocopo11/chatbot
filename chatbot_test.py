import python_weather
from chatbot import Chat, register_call
import asyncio
import os

import warnings
warnings.filterwarnings("ignore")


async def get_weather(city='New York'):
    global weather_string
    async with python_weather.Client() as client:
        weather = await client.get(city)
        await client.close()
    weather_string = ""
    for hourly in list(weather.daily_forecasts)[0].hourly_forecasts:
        weather_string = weather_string + str(hourly.time) + " " + str(hourly.temperature) + " deg.C " + str(hourly.description) + "\n"

@register_call("weather")
def call_weather(session=None, city='New York'):
    global weather_string
    try:
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(get_weather(city))
    except Exception:
        weather_string = "I do not know the weather"
    return weather_string



@register_call("do_you_know")
def do_you_know(session=None, query=None):
    return "I do not know about " + query


first_question = "Hi, how are you?"
chat = Chat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "chatbot_test.template"))
chat.converse(first_question)

