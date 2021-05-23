#!/usr/bin/python3

# Pull a google calendar
# Fletcher Boyd (fletcher.boyd@artifactory.org.au)
# Last modified: 23-05-2021
# Probably best not to leave this in your web directory, adjust the write as needed

import requests

calurl = "https://calendar.google.com/calendar/embed?src=q9bs8ul7umfnm4m02eq535114o%40group.calendar.google.com&ctz=Australia%2FPerth"

r = requests.get(calurl)

# add our css
page = r.text.replace('</head>', '<link rel="stylesheet" href="../calendar/calendar.css"></head>')

# adjust relative import from google

page = page.replace('src="/calendar/','src="https://calendar.google.com/calendar/')

with open("./calendar/calendar.html", 'w') as f:
    f.write(page)