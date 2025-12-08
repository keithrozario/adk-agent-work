
from google.adk.tools.tool_context import ToolContext
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