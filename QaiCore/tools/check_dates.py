from tools.gmail import GmailTool
import sys

def main():
    query = sys.argv[1] if len(sys.argv) > 1 else None
    tool = GmailTool()
    messages = tool.list_messages(query=query, max_results=10)
    print(f"{'ID':<20} | {'Date':<30} | {'Subject'}")
    print("-" * 80)
    for msg in messages:
        details = tool.get_message(msg['id'])
        print(f"{msg['id']:<20} | {details.get('date', 'N/A'):<30} | {details.get('subject', 'N/A')}")

if __name__ == '__main__':
    main()
