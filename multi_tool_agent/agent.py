import datetime

from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from google.oauth2.credentials import Credentials
from google.adk.apps.app import App

from googleapiclient.discovery import build
from .helper_funcs import get_creds


def get_service(tool_context: ToolContext):
    """
    Returns the Google Calendar and GMail service for API interaction
    """
    try:
        oauth_token = tool_context.state['calendarauth']
        creds = Credentials(token=oauth_token)
    except:  ## if the calendar auth doesn't exists, then we're on a local machine testing
        creds = get_creds()
    
    calendar_service = build("calendar", "v3", credentials=creds)
    gmail_service = build("gmail", "v1", credentials=creds)

    return calendar_service, gmail_service


def set_weather(city: str, weather: str, tool_context: ToolContext) -> dict:
    """
    Sets a calendar entry for the weather.
    """

    calendar_service, gmail_service = get_service(tool_context)
    timezone = calendar_service.calendarList().get(calendarId="primary").execute()['timeZone']
    event = {
        "summary": "Weather Update",
        "location": city,
        "description": weather,
        "start": {
            "dateTime": "2025-12-05T09:00:00",
            "timeZone": timezone

        },
        "end": {
            "dateTime": "2025-12-05T17:00:00",
            "timeZone": timezone
        },
    }
    
    event = calendar_service.events().insert(calendarId="primary", body=event).execute()
    return {
        "status": "success",
        "report": "All done"
    }



def get_weather(city: str, tool_context: ToolContext) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                f"The weather in New York is with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (f"Sorry, I don't have timezone information for {city}."),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time, set_weather],
)


app = App(root_agent=root_agent, name="multi_tool_agent")