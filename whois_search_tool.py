from country_from_ip import find_My_IP

def ret_Whois(IP = find_My_IP()):
	print("Current IP :", IP)
	import requests, bs4
	req = requests.get('https://who.is/whois-ip/ip-address/'+str(IP))
	Soup = bs4.BeautifulSoup(req.text,features='lxml')

	ret_str = str(Soup.select(".col-md-12.queryResponseBodyKey"))
	ret_str = ret_str[ret_str.find('>',ret_str.find('>')+1)+1:]
	print(f"\t\t\t   WHO IS {IP}\n\n{'*'*80}\n\n"+ret_str)

if __name__ == "__main__":
	ret_Whois()