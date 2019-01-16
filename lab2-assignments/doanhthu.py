from urllib.request import urlopen
from bs4 import BeautifulSoup 
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
#1. Download  the page

#1.1 Open connection
conn = urlopen(url)
#1.2 Read data
raw_data = conn.read()
#1.3 Decode data
content = raw_data.decode("utf8")

# print(content)

f = open("doanhthu.html", "wb")
f.write(raw_data)
f.close()
# 2. Find ROI
soup = BeautifulSoup(content, "html.parser")
table_doanhthu = soup.find("table", id="tableContent") 
tr_list = table_doanhthu.find_all("tr")

# soup = BeautifulSoup(page_content,"html.parser")
# table=soup.find("table",id="tableContent")
# tr_list=table.find_all("tr")



doanhthu_list = []
for tr in tr_list:
    td_list = tr.find_all("td", "b_r_c")
    for td in td_list:
        td = td.string 
        page_content = {
           "":td
        }
        doanhthu_list.append(page_content)
    
print(doanhthu_list)
pyexcel.save_as(records= doanhthu_list, dest_file_name="doanhthu.xls")