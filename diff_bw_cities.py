def ret_dist_bw_cities():
    """
        INPUT: User input for two cities, and a distance unit in ['km','miles']
        
        OUTPUT : The distances between the cities in the required distance metric
        
    """
    
    from math import cos, asin, sqrt, pi
    import requests
    import bs4
    import geopy.distance
    
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

    def ret_distance(lat1,lon1,lat2,lon2,unit):
        
        if unit == 'km':
            return geopy.distance.distance((lat1,lon1),(lat2,lon2)).km
        
        elif unit == 'miles':
            return geopy.distance.distance((lat1,lon1),(lat2,lon2)).miles
        
        else:
            raise ValueError(f"Distance metric should be either 'km' or 'miles' not '{unit}'")
        
        
    def ret_coords(coord_str):
        coords =  [float("".join([el for el in coord if el.isdigit() or el=='.'])) for coord in coord_str.split(',')]
        Direction = [coord[-1] for coord in coord_str.split(',')]
        
        for direc in Direction:
            if direc == 'S':
                coords[0] *= -1
            if direc == 'W':
                coords[1] *= -1
        
        return coords
        
        
    city1 = input("Enter the name of city 1 : ").rstrip().replace(" ",'+')
    city2 = input("Enter the name of city 2 : ").rstrip().replace(" ",'+')
    unit = input("Enter the unit to calculate the distance in (Eg. km, miles): \n")
    
    req_string_1 = "https://www.google.com/search?q={}+coordinates".format(city1)
    req_1 = request_with_connection_check(req_string_1)
    soup_1 = bs4.BeautifulSoup(req_1.text,features='lxml')
    coord_1 = soup_1.select('.BNeawe.iBp4i.AP7Wnd')[0].get_text()
    
    req_string_2 = "https://www.google.com/search?q={}+coordinates".format(city2)
    req_2 = request_with_connection_check(req_string_2)
    soup_2 = bs4.BeautifulSoup(req_2.text,features='lxml')
    coord_2 = soup_2.select('.BNeawe.iBp4i.AP7Wnd')[0].get_text()
    
    lat1,lon1 = ret_coords(coord_1)
    lat2,lon2 = ret_coords(coord_2)
    
    city1 = city1.replace('+',' ').title()
    city2 = city2.replace('+',' ').title()
    
    prefix_str = "\nDistance between {} and {} is ".format(city1,city2)
    if unit == 'km':   
        suf_str = 's'
    else:
        suf_str = ''
        
    print(prefix_str + str(round(ret_distance(lat1,lon1,lat2,lon2,unit))) + ' ' + unit + suf_str)

if __name__ == "__main__":
    ret_dist_bw_cities()