#!/bin/sh

cd $SPLUNK_HOME/etc/apps/PP_TAP_logs/bin

env -i /usr/bin/python3.5 $SPLUNK_HOME/etc/apps/PP_TAP_logs/bin/PP_TAP_logs.py

