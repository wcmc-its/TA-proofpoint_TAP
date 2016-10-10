#!/bin/sh

cd $SPLUNK_HOME/etc/apps/TA-proofpoint_TAP/bin

env -i /usr/bin/python3.5 $SPLUNK_HOME/etc/apps/TA-proofpoint_TAP/bin/PP_TAP_logs.py
