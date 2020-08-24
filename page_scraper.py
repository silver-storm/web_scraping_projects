# CODE FOR SCRAPING IMAGES AND LINKS FROM A GIVEN WEBPAGE

def scrape_Page(page_link = 'https://bulbapedia.bulbagarden.net/wiki/Necrozma_(Pok%C3%A9mon)'):
    
    import os, shutil, requests, bs4
    from PIL import Image
    from io import BytesIO
    
    def get_Image_Name(url):
        if type(url) is not str:
            raise TypeError(f"The URL hould be a string, not {type(url)}")
        temp = []
        flag = False
        for letter in url[::-1]:
            if letter is '.':
                flag = True
            if letter.isalnum() or letter is '.':
                temp.append(letter)
            elif flag:
                break

        return "".join(temp)[::-1]
    
    Scrape_req = requests.get(page_link)
    Scrape_soup = bs4.BeautifulSoup(Scrape_req.text,features='lxml')
    
    if "Scraped" not in os.listdir():
        os.mkdir("Scraped")
    if "Scraped_Images" not in os.listdir("./Scraped"):
        os.mkdir("Scraped/Scraped_Images")
    
    links = []
    count = 1
    for img in Scrape_soup.select('img') :
        try:
            req = requests.get("https:"+ img['src'])    
        except: continue
        img = Image.open(BytesIO(req.content))
        img_name = get_Image_Name(req.url)
        if img_name in os.listdir("Scraped/Scraped_Images/"):
            img_name = img_name[:-4] + "_"+str(count) + img_name[-4:]
            count += 1
        img.save(fp = "Scraped/Scraped_Images/"+ img_name)
    
    links = []
    for link in Scrape_soup.select('link') + Scrape_soup.select('a'):
        try:
            links.append(link['href'])
        except:
            continue
            
    links = list(set(links))
    f = open("links.txt","w")
    for link in links:
        f.write(link)
    f.close()
    
    shutil.move('links.txt','./Scraped/')
    print(f"Scraped URL : {page_link} successfully!")

if __name__ == "__main__":
    scrape_Page()