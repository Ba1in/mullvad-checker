import requests
import json
import time
import colorama
from os import system
from rich.console import Console



system("title " + "Mullvad Checker by @ba1in")

def get_login_details(login_number, proxy_url=None):
    url = "https://api.mullvad.net/www/accounts/" + login_number
    
    try:
        if proxy_url:
            response = requests.get(url, proxies={'http': proxy_url})
        else:
            response = requests.get(url)
        response.raise_for_status()
        login_details = response.json()
        return login_details
    except (requests.exceptions.ProxyError, requests.exceptions.ConnectionError) as err:
        print(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}Proxy connection error:{colorama.Fore.WHITE} {err}")
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f"{colorama.Style.BRIGHT}! {colorama.Fore.RED}Login number {colorama.Style.BRIGHT}{colorama.Fore.WHITE}{login_number}{colorama.Fore.RED} is invalid. Not a real account.{colorama.Style.RESET_ALL}")
            time.sleep(10)
        elif response.status_code == 503:
            print(f"{colorama.Style.BRIGHT}! {colorama.Fore.RED}Server error:{colorama.Fore.WHITE} {err}{colorama.Style.RESET_ALL}")
            time.sleep(10)
        else:
            print(f"{colorama.Style.BRIGHT}! {colorama.Fore.RED}HTTP error occurred:{colorama.Fore.WHITE} {err}{colorama.Style.RESET_ALL}")
            time.sleep(10)
    except json.decoder.JSONDecodeError as err:
        print(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}Error decoding JSON response:{colorama.Fore.WHITE} {err}{colorama.Style.RESET_ALL}")
    
    return None

def main():
    filename = "acc_numbers.txt"
    delay = int(input(f"{colorama.Style.BRIGHT}? {colorama.Fore.LIGHTBLUE_EX}Enter delay in seconds between requests {colorama.Fore.WHITE}({colorama.Fore.LIGHTBLUE_EX}default is 10{colorama.Fore.WHITE}){colorama.Fore.LIGHTBLUE_EX}:{colorama.Fore.WHITE} ") or 10)
    
    with open(filename, "r") as file:
        console = Console()
        with console.status("[bold green]Loading...") as status:
            time.sleep(delay)
            for line in file:
                login_number = line.strip()
            
                login_details = get_login_details(login_number)
            
                if login_details is None:
                    continue

                url = "https://api.mullvad.net/www/accounts/" + login_number
                active_status = login_details['account']['active']
                expiry_date = login_details['account']['expires']
            
                if active_status:
                    print(f"✓ {colorama.Style.BRIGHT}{colorama.Fore.GREEN}acc-number: {colorama.Fore.WHITE}{login_number} {colorama.Fore.GREEN}Expires: {colorama.Fore.WHITE}{expiry_date} {colorama.Fore.LIGHTBLUE_EX}{url}{colorama.Style.RESET_ALL}")
                    with open("active_acc_numbers.txt", "a") as file:
                        file.write(f"login_number: {login_number} | expiry_date: {expiry_date}\n")
                else:
                    print(f"{colorama.Style.BRIGHT}✗ {colorama.Fore.RED}acc-number: {colorama.Fore.WHITE}{login_number} {colorama.Fore.RED}Expired. {colorama.Fore.LIGHTBLUE_EX}{url}{colorama.Style.RESET_ALL}")
            
                time.sleep(delay)

        input(f"{colorama.Style.DIM}Done! Press Enter to exit...{colorama.Style.RESET_ALL}")

if __name__ == "__main__":
    print(f'''
       {colorama.Fore.BLUE}:!J5GBBBBBBG5J!:       
    {colorama.Fore.BLUE}.75B####BB########B57.    
  {colorama.Fore.BLUE}.?G###B5J{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}7!!7{colorama.Style.RESET_ALL}{colorama.Fore.BLUE}5PBBBBBB##G?.           {colorama.Style.BRIGHT}{colorama.Fore.YELLOW}__  ___      ____                __{colorama.Style.RESET_ALL}
 {colorama.Fore.BLUE}:P##BB5{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}~^^^^^^!.{colorama.Style.RESET_ALL}{colorama.Fore.BLUE}7GBBB#####P:         {colorama.Style.BRIGHT}{colorama.Fore.YELLOW}/  |/  /_  __/ / /   ______ _____/ /{colorama.Style.RESET_ALL}
{colorama.Fore.BLUE}:G#BB#G{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}^^^^^^^^{colorama.Style.RESET_ALL}{colorama.Fore.WHITE}##{colorama.Fore.BLUE}!?JYPPPPP55G:       {colorama.Style.BRIGHT}{colorama.Fore.YELLOW}/ /|_/ / / / / / / | / / __ `/ __  / {colorama.Style.RESET_ALL}
{colorama.Fore.BLUE}Y#BBBBB{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}!^^^^^^~!{colorama.Style.RESET_ALL}{colorama.Fore.YELLOW}JJ??777777{colorama.Fore.WHITE}##{colorama.Fore.BLUE}B5      {colorama.Style.BRIGHT}{colorama.Fore.YELLOW}/ /  / / /_/ / / /| |/ / /_/ / /_/ /  {colorama.Style.RESET_ALL}
{colorama.Fore.BLUE}BBBBBB#G{colorama.Style.BRIGHT}{colorama.Fore.YELLOW}!^~!{colorama.Style.RESET_ALL}{colorama.Fore.YELLOW}7?JJ?77777777J{colorama.Fore.BLUE}GBBB     {colorama.Style.BRIGHT}{colorama.Fore.YELLOW}/_/__//////,_/_/_/ |___/\//,_/\__,_/   {colorama.Style.RESET_ALL}
{colorama.Fore.BLUE}BBBBBBB#{colorama.Fore.YELLOW}PJJJ??777777777?{colorama.Fore.BLUE}PB#BBB      {colorama.Style.BRIGHT}{colorama.Fore.YELLOW}/ ____/ /_  ___  _____/ /_____  _____{colorama.Style.RESET_ALL}
{colorama.Fore.BLUE}Y#BBBBB#{colorama.Fore.YELLOW}P7777?JJJ???7{colorama.Fore.BLUE}JPB#BBB#5     {colorama.Style.BRIGHT}{colorama.Fore.YELLOW}/ /   / __ \/ _ \/ ___/ //_/ _ \/ ___/{colorama.Style.RESET_ALL}
{colorama.Fore.BLUE}:G#BBBB#{colorama.Fore.YELLOW}Y777777?????{colorama.Fore.BLUE}JB#BBBB#G:    {colorama.Style.BRIGHT}{colorama.Fore.YELLOW}/ /___/ / / /  __/ /__/ ,< /  __/ /    {colorama.Style.RESET_ALL}
 {colorama.Fore.BLUE}:P##BB{colorama.Fore.YELLOW}5777777777777?{colorama.Fore.BLUE}5BBB##P:     {colorama.Style.BRIGHT}{colorama.Fore.YELLOW}\____/_/ /_/\___/\___/_/|_|\___/_/     {colorama.Style.RESET_ALL}
  {colorama.Fore.BLUE}.?G#{colorama.Fore.YELLOW}BY?777777777777J{colorama.Fore.BLUE}G##G?.              {colorama.Style.BRIGHT}{colorama.Fore.WHITE}by: @ba1in{colorama.Style.RESET_ALL}
    {colorama.Fore.BLUE}.75BB{colorama.Fore.YELLOW}G5YJJJJJY5{colorama.Fore.BLUE}PB#B57.    
       {colorama.Fore.BLUE}:!J5GBBBBBBG5J!:   {colorama.Style.RESET_ALL}    
''')
    main()
