
from google.adk.tools.tool_context import ToolContext
import datetime
from zoneinfo import ZoneInfo
from .helper_funcs import get_service


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


def get_todays_events(tool_context: ToolContext) -> list[dict]:
    """
    Gets a list of events for today. 
    Today is inferred between the system time and timeZone set on the calendar.

    returns:
        events: List of Dicts of the events
    """


    calendar_service, _ = get_service(tool_context)
    time_zone = calendar_service.calendars().get(calendarId="primary").execute()['timeZone']
    today = datetime.datetime.now(ZoneInfo(time_zone))

    start_of_today = datetime.datetime(today.year, today.month, today.day, 0, 0, 0, tzinfo=ZoneInfo(time_zone))
    start_of_tomorrow = start_of_today + datetime.timedelta(days=1)

    # Format as RFC3339 timestamps
    time_min = start_of_today.isoformat()
    time_max = start_of_tomorrow.isoformat()

    print(f'Getting events from {time_min} to {time_max}')

    # Call the Calendar API events.list method
    events_result = calendar_service.events().list(
        calendarId='primary',
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result['items']

    return events