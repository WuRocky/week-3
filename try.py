######### Question 1 ##########
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
  data=json.load(response)
clist=data["result"]["results"]

with open("data.csv","w",encoding="utf-8") as file:
  for item in clist:
    if item["xpostDate"] >= "2015/01/01":
      itemFile = item["file"]
      splitUrl = itemFile.split("https://")
      firstUrl = "https://"+ splitUrl[1]
      file.write(item["stitle"]+","+item["address"][5:8]+","+item["longitude"]+","+item["latitude"]+","+firstUrl+"\n")


######### Question 2 ##########
import urllib.request as req
def getData(url):
  request=req.Request(url,headers={
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
  })
  with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
  import bs4
  root=bs4.BeautifulSoup(data,"html.parser")
  titles=root.find_all("div",class_="title")
  goodMoive = []

  with open("moive.txt","a",encoding="utf-8") as file:
    for i in titles:
      if i.a != None:
        if i.a.string[0:4] == "[好雷]":
          goodMoive = i.a.string + "\n"
          file.write(goodMoive)

  nextLink=root.find("a",string="‹ 上頁")
  return (nextLink["href"])

####function time####
movieUrl="https://www.ptt.cc/bbs/movie/index.html"
movieUrl ="https://www.ptt.cc" + getData(movieUrl)

count = 0
while count < 9: 
  movieUrl ="https://www.ptt.cc" + getData(movieUrl)
  count += 1


def getData(url):
  request=req.Request(url,headers={
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
  })
  with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
  import bs4
  root=bs4.BeautifulSoup(data,"html.parser")
  titles=root.find_all("div",class_="title")
  goodMoive = []


  with open("moive.txt","a",encoding="utf-8") as file:
    for i in titles:
      if i.a != None:
        if i.a.string[0:4] == "[普雷]":
          goodMoive = i.a.string + "\n"
          file.write(goodMoive)

  nextLink=root.find("a",string="‹ 上頁")
  return (nextLink["href"])

####function time####
movieUrl="https://www.ptt.cc/bbs/movie/index.html"
movieUrl ="https://www.ptt.cc" + getData(movieUrl)

count = 0
while count < 9: 
  movieUrl ="https://www.ptt.cc" + getData(movieUrl)
  count += 1


def getData(url):
  request=req.Request(url,headers={
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
  })
  with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
  import bs4
  root=bs4.BeautifulSoup(data,"html.parser")
  titles=root.find_all("div",class_="title")
  goodMoive = []

  with open("moive.txt","a",encoding="utf-8") as file:
    for i in titles:
      if i.a != None:
        if i.a.string[0:4] == "[負雷]":
          goodMoive = i.a.string + "\n"
          # print(goodMoive)
          file.write(goodMoive)
  nextLink=root.find("a",string="‹ 上頁")
  return (nextLink["href"])

####function time####
movieUrl="https://www.ptt.cc/bbs/movie/index.html"
movieUrl ="https://www.ptt.cc" + getData(movieUrl)

count = 0
while count < 9:
  movieUrl ="https://www.ptt.cc" + getData(movieUrl)
  count += 1