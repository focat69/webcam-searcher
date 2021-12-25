import os
from time import sleep
try:
    from colorama import Fore, Back, Style
except:
    print("You need colorama to use this program.\nOpen Command Prompt and type \"pip install colorama\" and wait for it to finish.\nThen, rerun this program.")
    print("\nClosing in 10 seconds...")
    sleep(10)
    quit()
try:
    from googlesearch import search
except:
    print("You need the \"googlesearch\" module installed to use this program.\nOpen Command Prompt and type \"pip install googlesearch-python\" and wait for it to finish.\nThen, rerun this program.")
    print("\nClosing in 10 seconds...")
    sleep(10)
    quit()
try:
    import requests
except:
    print("You need the \"requests\" module installed to use this program.\nOpen Command Prompt and type \"pip install requests\" and wait for it to finish.\nThen, rerun this program.")
    print("\nClosing in 10 seconds...")
    sleep(10)
    quit()

os.system("cls")

_ = open("settings.txt") # gives error in vs code, see "wcs_vscode.py" via wcs_dev.py
settings = _.read()
_.close()
if "checkForUpdatesWhenLaunched = True" in settings:
    headers = {'Accept-Encoding': 'identity'}
    rq = requests.get("https://raw.githubusercontent.com/Code1Tech/webcam-searcher/main/README.md",headers=headers)
    content = rq.text
    if "# webcam-searcher v1.0.0" in content:
        input(Fore.GREEN + "No updates are required,\nyou are using the latest version of wcs.py.\nPress enter to continue.")
        os.system("cls")
    elif not "# webcam-searcher v1.0.0" in content:
        print(Fore.YELLOW + "There is a new update available for wcs.py, you can download it at the GitHub page.\nhttps://github.com/Code1Tech/webcam-searcher\n\n")
    else:
        print(Fore.RED + "An error has occured while finding the latest update.\n\n")
elif "checkForUpdatesWhenLaunched = False" in settings:
    if "promptToEnableAU = True" in settings:
        input(Fore.YELLOW + "Auto-Update check is disabled. You can re-enable it in \"settings.txt\".\nPress enter to continue.")
    else:
        pass # do nothing

version = "v1.0.0"

print(Fore.RESET + f"Webcam Searcher {version}")

input(Back.YELLOW + Fore.BLACK + "Warning: If you attempt to get any further information on your target using the information you already have on them,\nthat is considered RECON.\nRecon is illegal and anything that you do with this program\nwill not be held/blamed on the author Code1Tech.\n\nPress enter to agree.")
os.system("cls")
print(Fore.RESET + Back.RESET + f"Webcam Searcher {version} | wcs.py")
r = input(Fore.GREEN + "How many results would you like to show? > ")
r = int(r)
try:
    _ = open("query.txt") # gives error in vs code, see "wcs_vscode.py" via wcs_dev.py
except:
    print(Fore.RESET + "Could not fine query.txt. Is it in the same place as wcs.py?\n\n(If you find any errors please make an issue or a pull request via GitHub.)")
    input("\nPress enter to quit.")
    quit()
print(Fore.YELLOW + "Reading query.txt...")
sleep(1)
query = _.read()
_.close()
os.system("cls")
print(Fore.RED + "Finding results..")
for _r in search(query, num_results=r):
    print(Fore.BLUE + _r)
print(Fore.RESET + f"\n{r} results on the webcam search query ({query}) have been listed above.")
input(Fore.GREEN + "Press enter to quit.")
print(Fore.RESET + "See you next time!")
quit()