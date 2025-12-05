import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def get_creds():
    """
    Gets the Google API credentials
    This function is only executed when running locally. It should never be needed when running on Agent Engine
    """
    
    # SCOPES are set in the Authorizer of Gemini Enterprise, it's baked into the Auth URI setting.
    # For local execution we create it here.
    SCOPES = [
        "https://www.googleapis.com/auth/calendar",
        "https://mail.google.com/",
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