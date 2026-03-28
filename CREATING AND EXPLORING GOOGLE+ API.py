from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Use minimal required permission (best practice)
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main():
    try:
        # Authenticate user
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES
        )
        creds = flow.run_local_server(port=0)

        # Connect to Google Drive API
        service = build('drive', 'v3', credentials=creds)

        # Fetch file list
        results = service.files().list(pageSize=10).execute()
        items = results.get('files', [])

        # Display results
        if not items:
            print("No files found in your Google Drive.")
        else:
            print("Files in your Google Drive:\n")
            for i, item in enumerate(items, start=1):
                print(f"{i}. {item['name']} (ID: {item['id']})")

    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
