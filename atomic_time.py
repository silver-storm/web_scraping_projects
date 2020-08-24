import requests
import bs4
from IPython.display import clear_output

req_time = requests.get('https://www.timeanddate.com/time/international-atomic-time.html')
Time_soup = bs4.BeautifulSoup(req_time.text,features='lxml')
date = Time_soup.select(".ctm-date")[0].get_text()
hour_min = Time_soup.select(".ctm-hrmn")[0].get_text()
seconds = Time_soup.select(".ctm-sec")[0].get_text()

print("Atomic Clock Time\n*****************\n"+date.lstrip()+"\n"+hour_min+':'+seconds)