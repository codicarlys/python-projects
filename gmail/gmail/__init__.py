__version__ = '0.1.0'


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from importlib_metadata import install

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
credential = 'gmail-service-account.json'


def main():

    creds = None

    if os.path.exists(credential):
        creds = Credentials.from_authorized_user_file(credential, SCOPES)
    
    if not creds or not creds.valid:
        creds.refresh(Request())
    
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            credential, SCOPES)
        creds = flow.run_local_server(port=0)
    
    with open(credential,'w') as token:
        token.write(creds.to_json())

    try:
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().lables().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])
    
    except HttpError as error:
        print(f'An errorr occurred: {error}')

if __name__ == '__name__':
    main()

        