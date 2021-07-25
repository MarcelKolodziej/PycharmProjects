# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)
#
# usernames = ['a','b','c']
# greet_users(usernames)

def show_messages(unsend_msg, completed_msg):
    while unsend_msg:
        current_sending = unsend_msg.pop()
        print(f"sending msg {current_sending}")
        completed_msg.append(current_sending)

def show_sent_messages(completed_msgs):
    print("\nFallowing msg was sented to your phone:")
    for completed_msg in completed_msgs:
        print(completed_msg)

unsend_msg = ['Welcome', 'Hello', 'Hi']
completed_msg = []

show_messages(unsend_msg, completed_msg)
show_sent_messages(completed_msg)


