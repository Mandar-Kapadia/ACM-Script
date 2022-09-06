import smtplib
from unicodedata import name
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

EMAIL_ADDRESS = 'Mandarkapadia@gmail.com'
EMAIL_PASSWORD ='trxozzzzhnmvdbyl'
counter = 54
reg = "stuff!A"

name = input("enter your firstname: ")
email = input("enter your email: ")


with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject = 'ACM '
    body ='Hello, \n Everyone and thank you for joining ACM. We are very exited for you to join our club and hope to see you in all the events. Please join our discord with the link below \n https://discord.gg/UTEWFEAqec \n (if you have any questions contact us by emailing ACM@uml.edu or asking in our discord\n sincerly,\n ACM'
    msg = f'Subject: {subject} \n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS,email,msg)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'acmregistration-45d98f4c8a60.json'
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1A5EvapCNMf9_BJ26OmYgraDk3nke4J_GDSKosjVd5a8'




# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
aoa = [[name,email]]
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
range_ = reg + str(counter)
sheet = service.spreadsheets()
result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_, valueInputOption="USER_ENTERED", body={"values":aoa}).execute()
counter+=1

