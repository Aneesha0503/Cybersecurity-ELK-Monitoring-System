import random
import time
import json
from datetime import datetime

users = ["aneesha", "deepak", "admin", "vaishnavi", "faceless"]
ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12", "10.10.10.5"]
actions = ["LOGIN_SUCCESS", "LOGIN_FAILED", "OPEN_EMAIL", "VISIT_WEBSITE", "DOWNLOAD_FILE", "LOGOUT"]

with open("C:/elastic_stack/logs/activity.log", "a") as log_file:
    while True:
        log = {
            "timestamp": str(datetime.now()),
            "user": random.choice(users),
            "ip": random.choice(ips),
            "action": random.choice(actions)
        }

        log_file.write(json.dumps(log) + "\n")
        log_file.flush()

        print(log)

        time.sleep(2)