import os
import pytz
import time
import requests
from datetime import datetime
from colorama import Fore, Style, init
from fake_useragent import UserAgent

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m------------[SeedMine Bot]-------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def load_tokens(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_headers(token):
    ua = UserAgent()
    return {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'content-length': '0',
        'dnt': '1',
        'origin': 'https://cf.seeddao.org',
        'priority': 'u=1, i',
        'referer': 'https://cf.seeddao.org/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'telegram-data': token,
        'user-agent': ua.random
    }

def login(token):
    url = "https://elb.seeddao.org/api/v1/profile2"
    url_2 = "https://elb.seeddao.org/api/v1/profile/balance"
    headers = get_headers(token)

    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        response_2 = requests.get(url_2, headers=headers, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        data_2 = response_2.json()
        balance = data_2.get("data")/1000000000
        print(f"{Fore.GREEN + Style.BRIGHT}Balance: {Fore.WHITE + Style.BRIGHT}{balance:.3f}")
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")

def daily_bonus(token):
    url = "https://elb.seeddao.org/api/v1/login-bonuses"
    url_streak = "https://elb.seeddao.org/api/v1/streak-reward"
    headers = get_headers(token)
    try:
        response = requests.post(url, headers=headers, allow_redirects=True)     
        status_code = response.status_code
        data = response.json()
        reward = data.get("data", {}).get("amount")  
        
        if status_code == 200:
            print(f"{Fore.GREEN + Style.BRIGHT}Daily Reward Claimed Successfully")
            print(f"{Fore.YELLOW + Style.BRIGHT}Reward: {Fore.WHITE + Style.BRIGHT}{int(reward)/1000000000}")        
        elif status_code == 400:
            print(f"{Fore.YELLOW + Style.BRIGHT}Daily Reward Already Claimed")
        else:
            print(f"{Fore.RED + Style.BRIGHT}Error: {data}")
            print(f"{Fore.RED + Style.BRIGHT}Status Code: {status_code}")
    except requests.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}")

def claim(token):
    url = "https://elb.seeddao.org/api/v1/seed/claim"
    headers = get_headers(token)
    try:
        response = requests.post(url, headers=headers, allow_redirects=True)
        data = response.json()
        status_code = response.status_code
        amount = data.get("data", {}).get("amount")
        
        if status_code == 200:
        	print(f"{Fore.GREEN + Style.BRIGHT}Seed Claimed Successful")
        	print(f"{Fore.CYAN + Style.BRIGHT}Claimed Amount: {Fore.WHITE + Style.BRIGHT}{int(amount)/1000000000}")
        
        elif status_code == 400:
        	print(f"{Fore.YELLOW + Style.BRIGHT}Seed Already Claimed")
        
        else:
        	print(f"{Fore.RED + Style.BRIGHT}Error: {data}")
        	print(f"{Fore.RED + Style.BRIGHT}Status Code: {status_code}")
    
    except requests.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")

def spin(token):
    url_ticket = "https://elb.seeddao.org/api/v1/spin-ticket"
    url_spin = "https://elb.seeddao.org/api/v1/spin-reward"
    headers = get_headers(token)
    
    try:
        response = requests.get(url_ticket, headers=headers)
        response.raise_for_status()
        tickets_data = response.json()
        tickets = tickets_data.get('data', [])
        ticket_ids = [ticket['id'] for ticket in tickets]
        
        if not ticket_ids:
            print(f"{Fore.MAGENTA + Style.BRIGHT}No tickets available")
            return
        for ticket_id in ticket_ids:
            body_spin = {
                'ticket_id': ticket_id
            }
            response = requests.post(url_spin, headers=headers, json=body_spin)
            response.raise_for_status()
            data = response.json()
            spin_reward = data.get("data", {}).get("type")
            print(f"{Fore.CYAN + Style.BRIGHT}Spin Reward: {spin_reward}")
    
    except requests.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")

def task(token):
    get_task_url = "https://elb.seeddao.org/api/v1/tasks/progresses"
    headers = get_headers(token)
    try:
        response_1 = requests.get(get_task_url, headers=headers, allow_redirects=True)
        data_1 = response_1.json()
        tasks = data_1.get('data', [])
        task_ids = [task['id'] for task in tasks]
        
        for task_id in task_ids:
        	comp_task_url = f"https://elb.seeddao.org/api/v1/tasks/{task_id}"
        	response_2 = requests.post(comp_task_url, headers=headers, allow_redirects=True)
        	data_2 = response_2.json()
        	if response_2.status_code == 200:
        	    print(f"{Fore.YELLOW + Style.BRIGHT}Task Completed")
        	else:
        	    print(f"{Fore.RED + Style.BRIGHT}{response_2.json()}")
        	time.sleep(5)
    except requests.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

def main():
    
    clear_terminal()
    art()

    run_task = input("Do you want to run task(token)? (y/n): ").strip().lower()
    while True:
        tokens = load_tokens('data.txt')
        

        clear_terminal()
        art()

        for i, token in enumerate(tokens, start=1):
            print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{i}------{Style.RESET_ALL}")
            login(token)
            daily_bonus(token)
            claim(token)
            spin(token)
            if run_task == 'y':
                task(token)

        countdown_timer(1 * 60 * 60)

if __name__ == "__main__":
    main()
