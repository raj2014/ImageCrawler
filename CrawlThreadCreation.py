import threading
import time
import urllib2
from bs4 import BeautifulSoup
import codecs

# Spider class for running the 
class mySpider(threading.Thread):
    
    def __init__(self,siteurl,cityName):
        threading.Thread.__init__(self)
        self.siteUrl = siteurl
        self.cityName = cityName
    def run(self):
        print "Starting " + self.cityName
        getNextlevelUrls(self.siteUrl,self.cityName)
        print "Exiting " + self.cityName
        
def getNextlevelUrls(siteurl,cityName):
    f=codecs.open('C:\\photourls\\'+cityName+'.txt','w',encoding='utf8')
    cityName=cityName.replace(' ','%20').replace(',','%2C')
    try:
        response = urllib2.urlopen(siteurl+'/explore?cat=sights&mode=url&near='+cityName,timeout=10)
    except urllib2.URLError, e:
        print "Oops, timed out?",e
    soup=BeautifulSoup(response)
    links=soup.findAll('a') 
    linkCount=0
    for link in links:
        if link['href'].find('/v')!=-1:
            linkCount+=1
    if linkCount==0:
        imagePerLink= int (500/(linkCount+1))
    else:
        imagePerLink= int (500/(linkCount))
    #print (cityName+':',imagePerLink)
    for link in links:
        if link['href'].find('/v')!=-1:
            #print link['href']
            # f.write("@"+link.string+'\n')
            #getpics(link['href'],link.string)
           
            url=siteurl+'/'+link['href']+'/photos'
            
            try:
                response = urllib2.urlopen(url,timeout=10)
            except urllib2.URLError, e:
                print "Oops, timed out?",e
            soup=BeautifulSoup(response)
            photos=soup.findAll('img')
            contents1=soup.findAll('div',attrs={'class':'adr'})
            s=''+cityName.replace('%20',' ').replace('%2C',',')+':'
            for child in contents1:
                     #print child.contents
                     for item in child:
                         if item.string!='':
                             s=s+item.string
            #print('@'+s)                
            f.write('@'+s)
            metaData=soup.findAll('div',attrs={'class':'categories'})
            s=''
            for child in metaData:
                  #print child.contents
                  for item in child:
                      if item.string!='':
                             s=s+item.string
            f.write('#'+s+'\n')
            photoCount=0
            #print cityName,len(photos)
            for photo in photos:
                if photo['src'].find('general')!=-1:
                    f.write(photo['src']+'\n')
                    photoCount+=1
                    if photoCount>=imagePerLink+3:
                        break
        #=======================================================================
        # else:
        #     print (cityName+'Pics Missing')
        #=======================================================================
def crawl(url,city,cityList):
   
    threads=[]
    if city=='All':
        for city in cityList:
            try:
                t=mySpider(url,city)
                threads.append(t)
            except Exception as errtxt:
                print errtxt
        
    else:
            getNextlevelUrls(url,city)
    [t.start() for t in threads]
    [t.join() for t in threads]
    print "Main Thread Completed!!" 
#===============================================================================
# st=time.time()
# crawl('https://foursquare.com','All')
# # #crawl()
# print time.time()-st
#===============================================================================