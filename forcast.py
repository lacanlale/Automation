#! python3
# Opens tab for weather report
import webbrowser, pyperclip, sys

if len(sys.argv) > 1:
    cl_input = ' '.join(sys.argv[1:])
else:
    cl_input = 'Northridge, CA'

print("-=* Retrieving weather forecast for {} *=-".format(cl_input))
city = cl_input[:cl_input.index(',')].strip().replace(' ','-').lower()
state = cl_input[1+cl_input.index(','):].strip().lower()
desired = state+'/'+city

base_url = "https://www.wunderground.com/weather/us/"
location = base_url+desired
webbrowser.open(location)
