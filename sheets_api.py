import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = os.path.join('config', 'ghostsheet_credentials.json')
SPREADSHEET_ID = '1_nC6i66nIYPbYSYHX65CA-ECe40QtSBN_TTBUFxp2Zw'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

def append_to_sheet(sheet, values):
    body = {'values': [values]}
    return service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{sheet}!A1",
        valueInputOption="RAW",
        body=body
    ).execute()

def read_sheet(sheet):
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{sheet}!A1:Z1000"
    ).execute()
    return result.get('values', [])
def post_data(sheet, values_dict):
    values = [values_dict.get("BotID", ""), values_dict.get("PayloadID", ""), values_dict.get("Status", ""), values_dict.get("Timestamp", "")]
    append_to_sheet(sheet, values)
def update_sheet(sheet, row, col, value):
    body = {
        'values': [[value]]
    }
    range_name = f"{sheet}!{chr(65 + col)}{row + 1}"
    return service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()
