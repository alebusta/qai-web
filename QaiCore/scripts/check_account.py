
import pickle
import os
from googleapiclient.discovery import build

TOKEN_PATH = r'c:\Users\abustamante\.qai\gmail\token_gmail.pickle'

def get_profile():
    if not os.path.exists(TOKEN_PATH):
        print("Token not found")
        return
    with open(TOKEN_PATH, 'rb') as token:
        creds = pickle.load(token)
    
    service = build('gmail', 'v1', credentials=creds)
    profile = service.users().getProfile(userId='me').execute()
    print(f"Authenticated Email: {profile.get('emailAddress')}")

if __name__ == "__main__":
    get_profile()
