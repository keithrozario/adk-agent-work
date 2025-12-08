from google.adk.agents import Agent
from google.adk.apps.app import App
from googleapiclient.discovery import build

from .helper_funcs import get_creds
from .tools import set_weather

root_agent = Agent(
    name="julian_gregory_day",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[set_weather],
)


app = App(root_agent=root_agent, name="julian_gregory")