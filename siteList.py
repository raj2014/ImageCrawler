import os
# Address Collection of the sights  from the URls
def createSiteList():    
    t=open('C:/output/SightList.txt','w')
    metaDict={}
    for root, dirs, files in os.walk('C:/photourls'):
        for name in files:
            print(os.path.join(root, name))
            f=open(os.path.join(root, name))
            for line in f:
                if line.startswith('@')==True:
                    metaData=line.split('#')
                    if metaData[0][1:].split(':')[1]!='':
                        t.write(metaData[0][1:]+'\n')   
        
#createSiteList()