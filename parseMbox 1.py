import mailbox

def extract_messages_from_mbox(mbox_file):
    messages = []
    mbox = mailbox.mbox(mbox_file)
    for message in mbox:
        messages.append(message)
    return messages

# Example usage:
mbox_file = 'Juntas de ESCOM.mbox'
messages = extract_messages_from_mbox(mbox_file)
for idx, message in enumerate(messages, start=1):
    print(f"Message {idx}:")
    print("From:", message['From'])
    print("Subject:", message['Subject'])
    print("Date:", message['Date'])
    print("Body:", message.get_payload())
    print("="*80)
