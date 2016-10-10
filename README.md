# TA-proofpoint_TAP
#### Splunk TA for proofpoint TAP alerts
#### TA Created by Bryan Fisher (brf2010@med.cornell.edu, bryan.fisher797@gmail.com)


# Requirements:
- python 3.3+ (only tested on 3.4 and 3.5)
- Unix-y OS
- The super-awesome requests library (pip install requests)


# Setup:
### On the box that will be doing the data collection:
1. Install the TA
2. Copy default/inputs.conf to local/inputs.conf
3. In inputs.conf, change `disabled = true` to `disabled = false`
4. Examine bin/starter_script.sh and make sure that the paths to the app directory and to the python3 executable are correct
5. (re)start splunk

### On the search head:
1. Install the TA
2. Enjoy Proofpoint logs responsibly
