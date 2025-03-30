import requests
from bs4 import BeautifulSoup
import time
import random
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
]
proxies=[
    "13.213.38.187",
    "130.193.35.242",
    "101.66.198.110",
    "101.71.143.237",
    "103.126.119.246",
    "130.61.139.145",
    "140.245.85.78",
    "135.225.231.41",
    "130.245.32.202",
    "101.255.149.202",
    "1.94.31.35",
    "132.22.40.2",		
]
c=0
for i in range(4000):
    try:
        for j in range(5):
            c+=1
            print(f"Vote number {c}")
            # Step 1: Get the page where the form is located
            session = requests.Session()
            url1 = "https://www.radionrjfm.com/vote/3"
            response = session.get(url1)

            # Step 2: Parse the page to extract the token
            soup = BeautifulSoup(response.text, "html.parser")
            csrf_token = soup.find("input", {"name": "_token"})["value"]
            print(f"Extracted CSRF Token: {csrf_token}")
            url="https://www.radionrjfm.com/pvote"
            res=session.get('https://www.radionrjfm.com/pvote')

            xtoken=res.cookies.get_dict()['XSRF-TOKEN']
            web_session=res.cookies.get_dict()['webground_session']
            headers = {
                "authority": "www.radionrjfm.com",
                "method": "POST",
                "path": "/pvote",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "max-age=0",
                "content-type": "application/x-www-form-urlencoded",
                "cookie": f"XSRF-TOKEN={xtoken}; webground_session={web_session}",
                "origin": "https://www.radionrjfm.com",
                "referer": "https://www.radionrjfm.com/vote/5",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": random.choice(USER_AGENTS),
                "X-XSRF-TOKEN": xtoken  # Including XSRF token in headers
            }
            payload = {
        "gidvnrj": "3",
            "sex": "1",
            "age": "3",
            "_token": csrf_token,  # Use the extracted token
            "answers[428]": "1"
                    }
            res2=session.post(url,headers=headers,data=payload)
            print(res2.status_code)
    except(Exception ) as e:
        print(e)
    time.sleep(5)
    # O9B2MGLWFErMmu0xj0k3E95zQe4LKm15bXfx7rI0