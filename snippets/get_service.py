import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_creds():
    """
    Gets the Google API credentials
    """
    SCOPES = [
        "https://www.googleapis.com/auth/calendar",
        "https://www.googleapis.com/auth/gmail",
    ]

    creds = False
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    if not creds:
        raise Exception("Unable to get Google Credentials")

    return creds


def get_service(service: str):
    """
    Returns the service object based on the service requested
    re-uses the creds from get_creds()
    """
    creds = get_creds()
    if service == "calendar":
        service = build("calendar", "v3", credentials=creds)
    elif service == "mail":
        service = build("gmail", "v1", credentials=creds)
    else:
        raise Exception("no service provided")

    return service
