#! python3
# Opens social media sites from
# media_sites.txt

import webbrowser

with open('media_sites.txt', 'r') as site_file:
    for site in site_file:
        print(f"-=* Opening {site} *=-")
        webbrowser.open(site)
