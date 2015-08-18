## Image Collection carried out using threads
import urllib
import os
import threading
def ImageLoader():  
    threads=[]  
    for root, dirs, files in os.walk('C:/photourls'):       
        for name in files:
            baseURL=os.path.join(root, name)
            targetURL=getRepositoryLocation(root, name)
            try:
                t=myImageLoaderThread(baseURL,targetURL)
                threads.append(t)
            except Exception as errtxt:
                print errtxt
    [t.start() for t in threads]
    [t.join() for t in threads]
            
#ImageLoader()
def imageDownloader(url,targetURL):
    f=open(url)
    count=0
    for line in f:
        count+=1
        if line.startswith('@')!=True and line!='':
            try:
                urllib.urlretrieve(line[:-1],targetURL+'/'+str(count)+'.jpg')
                #print line
            except Exception,e:
                print "Oops, timed out?",e
 
#Creating a Folder for each city   
def getRepositoryLocation(root,name):
    try:
        os.mkdir('C:'+'/'+'output'+'/'+name[:-4].replace(',','_'))
    except Exception,e:
                print e
    return 'C:'+'/'+'output'+'/'+name[:-4].replace(',','_')

#Image processing thread
class myImageLoaderThread(threading.Thread):
    
    def __init__(self,fileurl,targetURL):
        threading.Thread.__init__(self)
        self.fileurl = fileurl
        self.targetURL=targetURL
    def run(self):
        print "Starting " + self.fileurl
        imageDownloader(self.fileurl,self.targetURL)
        print "Exiting " + self.fileurl
#ImageLoader()
