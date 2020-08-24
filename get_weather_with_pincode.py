import requests, bs4

def get_loc():
    loc_req = requests.get('https://www.google.com/search?q=current+location&oq=current+location')
    loc_soup = bs4.BeautifulSoup(loc_req.text,features='lxml')
    loc = loc_soup.select('.BNeawe.tAd8D.AP7Wnd')[0]
    location = str(loc.select('a')[0])
    l1 = location.find('q=')
    l2 = location[l1:].find(';') + l1
    location = location[l1:l2]
    loc_1 = location[location.find('=')+1:location.find(',')]
    loc_2 = location[location.find(',')+1:location.find('&')].replace('+',' ').lstrip()
    return loc_1 + ', ' + loc_2

def get_pincode(location):
    if type(location) is not str:
        raise TypeError(f"The location should be a string, not {type(location)}")
        
    pin_req = requests.get(f'https://www.google.com/search?q={location}+pincode&oq={location}+pincode')
    pin_soup = bs4.BeautifulSoup(pin_req.text,features='lxml')
    return pin_soup.select('.BNeawe.iBp4i.AP7Wnd')[0].get_text()

def get_weather(pincode=get_pincode(get_loc())):
    if type(pincode) is not str:
        raise ValueError(f"Pincode should be a string, not {type(pincode)}")
#     if len(pincode) is not 6:
#         raise ValueError(f"The pincode should be a string of 6 numbers, not {len(pincode)} numbers")
    wthr_req = requests.get(f"https://www.google.com/search?q=weather+for+{pincode}&oq=weather+for+{pincode}")
    wthr_soup = bs4.BeautifulSoup(wthr_req.text,features='lxml')
    temp = wthr_soup.select(".BNeawe.iBp4i.AP7Wnd")[0].get_text()
    loc = wthr_soup.select('.BNeawe.tAd8D.AP7Wnd')[0].get_text()
    forecast = wthr_soup.select('.BNeawe.tAd8D.AP7Wnd')[1].get_text()
    
    
    print(f"Forecast for {loc}\n{'*'*int(len(loc)*1.65)}\nAmbient Temperature = {temp}\n{forecast}")

if __name__ == "__main__":
    get_weather()
    get_weather(pincode='01003')