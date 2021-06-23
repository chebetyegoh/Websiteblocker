import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"

websites = ["www.facebook.com", "facebook.com" 
            "www.instagram.com", "instagram.com" 
            "www.youtube.com", "youtube.com"]


def website_blocker(opening_hours, closing_hours):
    global websites
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, opening_hours) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, closing_hours):
            print("Working hours")
            with open(hosts_path, "r+") as file:
                content = file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    # mapping hostnames to the local host
                    file.write(redirect + " " + site + '\n')
        else:
            with open(hosts_path, "r+") as file:
                content = file.readline()
                file.seek(0)
                for line in content:
                    if not any(site in line for site in websites):
                        file.write(line)
                file.truncate()

            print("Good time")
        time.sleep(5)


website_blocker(18, 22)


