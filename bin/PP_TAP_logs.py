#!/usr/bin/python3

import requests
from datetime import datetime, timezone, timedelta
import json
from urllib.parse import quote_plus

# credentials for the proofpoint API
username = "redacted"
password  = "redacted"

# size of the time interval to retrieve from proofpoint
time_range_minutes = 1


now = datetime.now(timezone.utc) # get current time
#now = datetime(year=2016, month=10, day=4, hour=12, minute=12, tzinfo=timezone.utc) # temporary static time for testing
now = now - timedelta(microseconds=now.microsecond) # chop off the microseconds because stupid
time_range = timedelta(minutes=time_range_minutes) # create a time delta object to represent our time range
then = now - time_range # get the time 1 minute ago
ISO_interval = then.isoformat() + "/" + now.isoformat() # format an ISO8601-compliant interval string for the API
ISO_interval = quote_plus(ISO_interval) # encode the ISO interval for the http request


# query the API
page = requests.get('https://tap-api-v2.proofpoint.com/v2/siem/all?format=JSON&interval=%s' %(ISO_interval), auth=(username, password))

# convert API output to JSON object
api_output = json.loads(page.text)


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
