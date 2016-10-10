#!/usr/bin/python3

import requests
from datetime import datetime, timezone, timedelta
import json
from pprint import pprint
from urllib.parse import quote_plus
#import os, sys

# credentials for the proofpoint API
username = "redacted"
password  = "redacted"

# size of the time interval to retrieve from proofpoint
time_range_minutes = 1

# base proofpoint TAP API url
base_url = "https://tap-api.proofpoint.com/v1/siem/all?format=JSON?interval="

now = datetime.now(timezone.utc) # get current time
#now = datetime(year=2016, month=10, day=4, hour=12, minute=12, tzinfo=timezone.utc) # temporary static time for testing
now = now - timedelta(microseconds=now.microsecond) # chop off the microseconds because stupid
time_range = timedelta(minutes=time_range_minutes) # create a time delta object to represent our time range
then = now - time_range # get the time 1 minute ago
ISO_interval = then.isoformat() + "/" + now.isoformat() # format an ISO8601-compliant interval string for the API
ISO_interval = quote_plus(ISO_interval) # encode the ISO interval for the http request

# query the API
page = requests.get('https://tap-api-v2.proofpoint.com/v2/siem/all?format=JSON&interval=%s' %(ISO_interval), auth=(username, password))
#print(page.url)
#print(page.text)
# convert API output to JSON object
api_output = json.loads(page.text)

# open log file for writing
#log_file = open(os.path.dirname(os.path.realpath(sys.argv[0])) + "/PP_TAP_logs.txt", "w")

# print each of our objects output
# malicious URLs that were blocked
for click in api_output["clicksBlocked"]:
    click["time"] = api_output['queryEndTime']
    click["action"] = "clickBlocked"
    print(json.dumps(click))

# malicious URLs that were clicked on but not blocked
for click in api_output["clicksPermitted"]:
    click["time"] = api_output['queryEndTime']
    click["action"] = "clickPermitted"
    print(json.dumps(click))

# malicious messages that were blocked
for message in api_output["messagesBlocked"]:
    message["time"] = api_output['queryEndTime']
    message["action"] = "messageBlocked"
    print(json.dumps(message))

# malicious messages that were delivered
for message in api_output["messagesDelivered"]:
    message["time"] = api_output['queryEndTime']
    message["action"] = "messageDelivered"
    print(json.dumps(message))

#log_file.close()

# print the shit
#print(page.url)
#pprint(api_output)
