import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from helper_funcs import get_service


def main():
    mail_service = get_service(service="mail")


if __name__ == "__main__":
    main()
# [END calendar_quickstart]
