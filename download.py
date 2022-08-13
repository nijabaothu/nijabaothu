from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main(user_email):
    // CREATE DRIVE SERVICE WITH SERVICE ACCOUNT
    creds = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_ACCOUNT_FILE_PATH,
    scopes=['https://www.googleapis.com/auth/drive'])
    creds = creds.create_delegated(user_email)
    drive_service = build('drive', 'v3', credentials=creds)

    // DOWNLOAD FILE
    file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print "Download %d%%." % int(status.progress() * 100)

if __name__ == '__main__':
    user_email = "something@example.com"
    main(user_email)