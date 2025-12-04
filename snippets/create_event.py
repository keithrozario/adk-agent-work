import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from get_service import get_service


def main():
    service = get_service(service="calendar")
    event = {
        "summary": "Google I/O 2025 -- new!!",
        "location": "800 Howard St., San Francisco, CA 94103",
        "description": "A chance to hear more about Google's developer products.",
        "start": {
            "dateTime": "2025-12-05T09:00:00-07:00",
            "timeZone": "America/Los_Angeles",
        },
        "end": {
            "dateTime": "2025-12-05T17:00:00-07:00",
            "timeZone": "America/Los_Angeles",
        },
        "recurrence": ["RRULE:FREQ=DAILY;COUNT=2"],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},
                {"method": "popup", "minutes": 10},
            ],
        },
    }

    event = service.events().insert(calendarId="primary", body=event).execute()
    # print("Event created: %s" % (event.get("htmlLink")))


if __name__ == "__main__":
    main()
# [END calendar_quickstart]
