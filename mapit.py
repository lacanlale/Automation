#! python3
# Maps an address given in the command line
# using Google maps
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    cl_input = ' '.join(sys.argv[1:])
else:
    cl_input = pyperclip.paste()

print("-=~* Mapping {} *~=-".format(cl_input))
cl_input = cl_input.replace(",", "").replace(" ", "+")[:-6].strip()
base_url = "https://www.google.com/maps/place/{}/".format(cl_input)
webbrowser.open(base_url)
