
import os

def send_messages(send_message,sent_messages):
    while send_message:
        current_message=send_message.pop()
        print(f"Printing messages: {current_message}")
        sent_messages.append(current_message)


send_message =['show','person', 'country', 'day']
sent_messages=[]

send_messages(send_message[:],sent_messages)
print(f"Printing send_message: {send_message}")
print(f"Printing sent_messages: {sent_messages}")

os.system('pause')