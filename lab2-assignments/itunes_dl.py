from urllib.request import urlopen
from bs4 import BeautifulSoup 
import pyexcel
from collections import OrderedDict

url = "https://www.apple.com/itunes/charts/songs/"
#1. Download  the page

#1.1 Open connection
conn = urlopen(url)
#1.2 Read data
raw_data = conn.read()
#1.3 Decode data
content = raw_data.decode("utf8")

# print(content)

f = open("itunes.html", "wb")
f.write(raw_data)
f.close()
# 2. Find ROI
soup = BeautifulSoup(content, "html.parser")
itunes = soup.find("section", "section chart-grid") 
li_list = itunes.find_all("li")



itunes_chart = []
for li in li_list:
    order = li.strong.string
    song = li.h3.a.string
    artist = li.h4.a.string
    
    
    songs = OrderedDict({
            "order": order,
            "song": song,
            "artist":artist
        })
    print(itunes_chart)
    itunes_chart.append(OrderedDict(songs))
    print("---------------------")
pyexcel.save_as(records= itunes_chart, dest_file_name="itunes.xls")