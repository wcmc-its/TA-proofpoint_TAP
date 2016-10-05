import requests
import datetime
import json
from pprint import pprint

# credentials for the proofpoint API
username = "redacted"
password  = "redacted"

# size of the time interval to retrieve from proofpoint
time_range_minutes = 1

# base proofpoint TAP API url
base_url = "https://tap-api.proofpoint.com/v1/siem/all?format=JSON?interval="

#now = datetime.datetime.now() # get current time
now = datetime.datetime(year=2016, month=10, day=4, hour=12, minute=12) # temporary static time for testing
now = now - datetime.timedelta(microseconds=now.microsecond) # chop off the microseconds because stupid
minute = datetime.timedelta(minutes=time_range_minutes) # create a time delta object to represent one minute
then = now - minute # get the time 1 minute ago
ISO_interval = then.isoformat() + "-0400" + "/" + now.isoformat() + "-0400" # format an ISO8601-compliant interval string for the API

# query the API
page = requests.get('https://tap-api-v2.proofpoint.com/v2/siem/all?format=JSON&interval=%s' %(ISO_interval), auth=(username, password))

# convert API output to JSON object
api_output = json.loads(page.text)



# print each of our objects output
# malicious URLs that were blocked
for click in api_output["clicksBlocked"]:
    print(click["clickTime"] + " clickBlocked " + str(click))

# malicious URLs that were clicked on but not blocked
for click in api_output["clicksPermitted"]:
    print(click["clickTime"] + " clickPermitted " + str(click))

# malicious messages that were blocked
for message in api_output["messagesBlocked"]:
    print(message["messageTime"] + " messageBlocked " + str(message))

# malicious messages that were delivered
for message in api_output["messagesDelivered"]:
    print(message["messageTime"] + " messageDelivered " + str(message))


# print the shit
#print(page.url)
pprint(api_output)
