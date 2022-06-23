from colored import fg, attr
import sys
import requests
import pyfiglet
import os

os.system('cls' if os.name == 'nt' else 'clear')
jarvis = pyfiglet.figlet_format("Jarvis")
print(jarvis)
print("Simple directory brute-forcer made by: Giulliano Amaral")
print("")



try:
    target = sys.argv[1]
    wordlist = sys.argv[2]
    ext = sys.argv[3].split(',')

    if "http://" in target:
        pass
    elif "https://" in target:
        pass
    else:
        target = "https://"+target

except:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(jarvis)
    print("")
    print("Usage: jarvis-dirb.py [URL] [PATH-TO-WORDLIST] [EXTENSIONS]")
    print("Example: jarvis-dirb.py http://scanme.nmap.org /usr/share/wordlists/directory-list-2.3-medium.txt php,js,php5")
    sys.exit()



def main():
    word = open(wordlist, 'r')
    for file in word:
        guess = word.readline(10).strip()
        url = target+"/"+guess
        
        r = requests.get(url)
        if r.status_code != 404:
                message = print(f"{url} - %s[{r.status_code}]%s found !" % (fg('green'), attr('reset')))
        else:
            pass

        for i in range(0,len(ext)):
            url_extended = target+"/"+guess+"."+ext[i]
            r_extended = requests.get(url_extended)
            if r_extended.status_code != 404:
                message_extended = print(f"{url_extended} - %s[{r_extended.status_code}]%s found !" % (fg('green'), attr('reset')))
            else:
                pass


main()




