#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import atexit
from flask import Flask, request
from time import time, sleep
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

start_time = time()

def slack_webhook():
	wekbook_url = "https://hooks.slack.com/services/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"

	data = {"text": ":poop: Check the freezer! :poop:"}

	response = requests.post(
		wekbook_url, data=json.dumps(data), headers={"Content-Type": "application/json"}
	)
	print(f"Slack message sent - {data}.")


def background_function():
	global start_time
	if int(time() - start_time) > 600:
		print(f"Difference in time is {int(time() - start_time)}.")
		slack_webhook()

cron = BackgroundScheduler(daemon=True)
cron.add_job(func=background_function, trigger="interval", minutes=2)
cron.start()

# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))


@app.route("/hello", methods=["GET"])
def index():
    start_time = time()
    return ("Hi!", 200, None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
