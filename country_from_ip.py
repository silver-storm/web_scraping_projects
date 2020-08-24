import requests, bs4, time

def check_IP(IP):
    try:
        IP = IP.split('.')
        if len(IP) != 4:
            return False
        for sub_ip in IP:
            if int(sub_ip)>255 or int(sub_ip)<0:
                return False

        return True
    except:
        return False

def find_My_IP():
    while True:
        try :
            res = requests.get("https://www.myip.com/")
            break
        except:
            print("Turn on your internet connection please!")
        time.sleep(5)
    S = bs4.BeautifulSoup(res.text,features='lxml')
    IP = S.find('span',id='ip').get_text()
    print("Current IP :", IP)
    return IP

def find_country_from_IP(IP = find_My_IP()):
    if type(IP) is not str:
        print(f"Entered IP is should be a string, not {type(IP)}")
        return None
    
    res = requests.get(f"https://ipinfo.asytech.cn/check-ip/{IP}")
    Soup = bs4.BeautifulSoup(res.text,features='lxml')
    try:
        Loc = Soup.select('.text-primary')[0].get_text()
    except :
        print("Unregistered IP!")
        return None
    
    print(f"This IP Address {IP} is registered in",Loc)

if __name__ == "__main__":
    ch = input("Enter Y to enter IP of your choice or N to use current IP : \n").lower()
    if ch == 'y':
        IP = input("Enter an IP of your choice : ")
        if check_IP(IP):
            find_country_from_IP(IP = IP)
        else:
            print("Entered IP is invalid, defaulting to current IP!")
            find_country_from_IP()

    elif ch == 'n':
        find_country_from_IP()