def conv_units(unit_1,unit_2,measure_1=None,measure_2=None):
    
    import requests, bs4
    
    def request_with_connection_check(req_string):
        flag = True
        while True:
            try:
                request = requests.get(req_string)
                break
            except Exception:
                if flag:
                    print("\nConnectionError! No internet connection detected. Please connect to the internet to proceed")
                    flag = False
                continue
        return request
    
    if measure_1 == None:
        req_string = 'https://www.google.com/search?q={num}+{unit1}+to+{unit2}&oq={num}+{unit1}+to+{unit2}'.format(num=measure_2,unit1=unit_2,unit2=unit_1)
        req = request_with_connection_check(req_string)
        soup = bs4.BeautifulSoup(req.text,features='lxml')
        prefix_text = "{num} {unit} = ".format(num=measure_2,unit=unit_2)
        if measure_2 == 1:
            print(prefix_text + soup.select('.BNeawe')[1].get_text())
        else:
            print(prefix_text.replace(" =",'s =') + soup.select('.BNeawe')[1].get_text())
        
    if measure_2 == None:
        req_string = 'https://www.google.com/search?q={num}+{unit1}+to+{unit2}&oq={num}+{unit1}+to+{unit2}'.format(num=measure_1,unit1=unit_1,unit2=unit_2)
        req = request_with_connection_check(req_string)
        soup = bs4.BeautifulSoup(req.text,features='lxml')
        prefix_text = "{num} {unit} = ".format(num=measure_1,unit=unit_1)
        if measure_1 == 1:
            print(prefix_text + soup.select('.BNeawe')[1].get_text())
        else:
            print(prefix_text.replace(" =",'s =')+ soup.select('.BNeawe')[1].get_text())

if __name__ == "__main__":
    conv_units("gallon","litre",measure_1=1)