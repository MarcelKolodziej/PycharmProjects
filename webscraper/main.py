#! python3
# mapIT.pu

import webbrowser, sys, pyperclip

print("sys", sys.argv)
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    #Get address from clipboard
    address = pyperclip.paste()

#url 'https://www.google.com/maps/place/your_address_string'
    webbrowser.open('https://www.google.com/maps/place/' + address)

