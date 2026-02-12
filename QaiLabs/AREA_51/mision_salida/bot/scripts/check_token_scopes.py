
import pickle
import os
import json

TOKEN_PATH = r'c:\Users\abustamante\.qai\gdrive\token.pickle'

def check_scopes():
    if not os.path.exists(TOKEN_PATH):
        print(f"❌ No token found at {TOKEN_PATH}")
        return

    try:
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)

        print(f"✅ Token loaded from {TOKEN_PATH}")
        if hasattr(creds, 'scopes'):
            print(f"Scopes: {creds.scopes}")
        else:
            print("No scopes attribute found on credentials")
            
        # Also print valid status
        print(f"Valid: {creds.valid}")
        print(f"Expired: {creds.expired}")

    except Exception as e:
        print(f"❌ Error loading token: {e}")

if __name__ == "__main__":
    check_scopes()
