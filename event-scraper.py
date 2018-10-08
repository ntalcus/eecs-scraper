
#libraries
import requests
from lxml import html

url = "https://eecs.berkeley.edu/turing-colloquium/schedule" 

def maxlength(strList):
    maxList = None
    maxLength = 0
    for string in strList:


page = requests.get(url)
tree = html.fromstring(page.content)
speakers = []
titles = []
dates = []
for i in range(0,12):
    speaker_xpath = '//*[@id="block-system-main"]/div/div/section/div[1]/div[1]/div/div/div/div/h3[' + str(1 + i) + ']/a/text()'
    speakers.append(tree.xpath(speaker_xpath))
    title_xpath = '//*[@id="block-system-main"]/div/div/section/div[1]/div[1]/div/div/div/div/h4[' + str(1 + i) + ']/strong/a/text()'
    title = tree.xpath(title_xpath)
    if (len(title) == 0):
        title_xpath = '//*[@id="block-system-main"]/div/div/section/div[1]/div[1]/div/div/div/div/h4[' + str(1 + i) + ']/strong/text()'
        title = tree.xpath(title_xpath)
        print("triggered", title)
    titles.append(title)
    date_xpath = '//*[@id="block-system-main"]/div/div/section/div[1]/div[1]/div/div/div/div/p[' + str(3 + i) + ']/span[2]/strong/text()'
    date = tree.xpath(date_xpath)
    if(len(date) == 0):
        date_xpath = '//*[@id="block-system-main"]/div/div/section/div[1]/div[1]/div/div/div/div/p[' + str(3 + i) + ']/strong[1]/text()'
        date = tree.xpath(date_xpath)
    dates.append(date)
for i in range(0,12):
    print("lecture # ", str(i))
    print("speakers: ", speakers[i])
    print("titles: ", titles[i])
    print("dates: ", dates[i])
