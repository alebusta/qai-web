from tools.gmail import GmailTool
import sys

def main():
    tool = GmailTool()
    msg_id = sys.argv[1]
    details = tool.get_message(msg_id)
    print(f"ID: {msg_id}")
    print(f"Date: {details.get('date', 'N/A')}")
    print(f"Subject: {details.get('subject', 'N/A')}")
    print(f"From: {details.get('from', 'N/A')}")

if __name__ == '__main__':
    main()
