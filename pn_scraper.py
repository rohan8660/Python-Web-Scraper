# Python Version : Python 3.9.7
# Author : Rachana Kampli

# imports of required packages
import csv  # for handling csv files
import time # for time delay in program execution 
from selenium import webdriver  # webdriver to handle chrome
from webdriver_manager.chrome import ChromeDriverManager    # chrome manager to start and scroll site in chrome

# initialising chrome manager
driver = webdriver.Chrome(ChromeDriverManager().install())
# maximizing chrome window
driver.maximize_window()
# HTTP GET request to the required website
driver.get(url="https://www.vijaysales.com/mobiles-and-tablets/audio-accessories")

# scrolling to get more elements
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# delaying the process/program / to let it fetch more elements
time.sleep(10)

# targetting and fetching required elements by their class

# fetching product names
nameList = driver.find_elements_by_class_name('Dynamic-Bucket-ProductName')
# fetching product prices
priceList=driver.find_elements_by_class_name('Dynamic-Bucket-vsp.dvpricepdlft')
# fetching product mrps
mrpList=driver.find_elements_by_class_name('Dynamic-Bucket-mrp.dvpricepdlft')
# fetching product discounts
offerpercentList=driver.find_elements_by_class_name('offer-btn.dvpricepdlft')
# fetching product emis
emiList=driver.find_elements_by_class_name('Dynamic-Bucket-EMI')
# fetching product links
linkList=driver.find_elements_by_class_name('vj-cur-pnter.nabprod')
# fetching image links
#imgLinkList=driver.find_elements_by_class_name('img-responsive Dynamic-Bucket-img lazy b-loaded')
imgLinkList=driver.find_elements_by_tag_name('img')

# data formatting / correction , removing of rupee symbol and unwanted text for first 100 elements
for i in range(100):
    
    y=list(str(emiList[i].text))
    x=""
    for w in y:
        if w.isdigit():
            x+=w
    emiList[i]=x
    # print("emi "+x)

    pl=str(priceList[i].text)
    pl=pl[1:]
    priceList[i]=pl
    # print("price "+pl)

    ml=str(mrpList[i].text)
    ml=ml[1:]
    mrpList[i]=ml
    # print("mrp "+ml)
    

filename="output.csv"
# f=open(filename,"w")
# headers="Product_Name,Price,MRP,Off_Per,EMI\n"
# f.write(headers)


# initialising csv file by opening with csv writer
writer=csv.writer(open(filename,'wb'))
header=['Product_Name','Price','MRP','Offer Percentage','EMI starts from','Link','img_link']

# row wise data entry for first 100 elements
with open(filename, 'w', newline='', encoding="utf-8") as product_file:
    writer = csv.writer(product_file)
    # writing header to csv file
    writer.writerow(header)
    for i in range(100):
        print(len(imgLinkList))#[i].get_property('src'))
        # writing 100 rows of data to csv file
        writer.writerow([nameList[i].text, priceList[i], mrpList[i], offerpercentList[i].text, emiList[i], linkList[i].get_property('href'),imgLinkList[i].get_attribute('src')])


# for i in range(100):
#     print("----------------------------------------------------------------------------------------------")
#     print(i+1)
#     print(nameList[i].text)
#     print(priceList[i].text)
#     print(mrpList[i].text)
#     print(offerpercentList[i].text)
#     print(emiList[i].text)
#     print(linkList[i].get_property('href'))
#     print()
#     print("----------------------------------------------------------------------------------------------")

# print(len(nameList))
# print(len(priceList))
# print(len(mrpList))
# print(len(offerpercentList))
# print(len(emiList))
# print(len(linkList))

# closing csv file 
product_file.close()

# closing selenium chrome driver
driver.close()
