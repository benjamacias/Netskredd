import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pdb
from twitter_upload import create_tweet
from linkedin_upload import subir_linkedin
from datetime import datetime
from tik_tokUpload import tiktok_upload


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "15Jikqp9P20ECGJbi9tpg2Y2NzvtkfH5tKsRbN6mM0vc" # id de la hoja de calculo
SAMPLE_RANGE_NAME = "Sheet1!A1:I19" # rango de celdas a leer

now = datetime.now()
datetime = now.strftime("%d_%m")

def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "client_secret.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return
    
    for row in values:
        #print(f"{row[0]}, {row[4]}") 
        if row[2] == datetime:
            print(f"nombre: {row[1]} fecha: {row[2]} tiktok:{row[3]}	instagram:{row[4]}  facebook:{row[5]}	twitter:{row[6]}	linkedin:{row[7]} youtube:{row[8]}")
            actions = {
              'instagram': {row[4]} ,
              'facebook': {row[5]},
              'twitter': {row[6]},
              'linkedin': {row[7]},
              'youtube': {row[8]},
              'tiktok': {row[3]}
            }

            if actions["tiktok"] == "x":
              tiktok_upload(row[2], row[9])

            if actions["twitter"] == "x":
              create_tweet(row[2], row[9])
            
            if actions["linkedin"] == "x":
              subir_linkedin()
            
            if actions["facebook"] == "x":
              print("facebook")
            
            if actions["instagram"] == "x":
              print("instagram")
            
            if actions["youtube"] == "x":
              print("youtube")
            
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()