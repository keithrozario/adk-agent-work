from helper_funcs import get_creds
from googleapiclient.discovery import build
import datetime
from zoneinfo import ZoneInfo

def get_service():
    creds = get_creds()
   
    calendar_service = build("calendar", "v3", credentials=creds)
    gmail_service = build("gmail", "v1", credentials=creds)

    return calendar_service, gmail_service

def get_todays_events():
    calendar_service, gmail_service = get_service()
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

calendar_service, gmail_service = get_service()
primary_calendar = calendar_service.calendars().get(calendarId="primary").execute()['timeZone']
print(primary_calendar)