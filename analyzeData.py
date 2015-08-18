import os
# Metadata Collection about the sights in our collection
def analyzeMetadata():
    t=open('C:/output/treeMap.txt','w')
    metaDict={}
    for root, dirs, files in os.walk('C:/photourls'):
        for name in files:
            print(os.path.join(root, name))
            f=open(os.path.join(root, name))
            for line in f:
                if line.startswith('@')==True:
                    metaData=line.split('#')
                    if metaData[1].count(',')>0:
                        keyWords=metaData[1].split(',')
                        for key in keyWords:
                            key=key.rstrip().replace(' ','')
                            if key!='':
                                if key in metaDict:
                                    metaDict[key]=metaDict[key]+1
                                else:
                                    metaDict[key]=1
                    else:
                        key=metaData[1].rstrip().replace(' ','')
                        if key!='':
                            if key in metaDict:
                                    metaDict[key]=metaDict[key]+1
                            else:
                                    metaDict[key]=1
    for key in metaDict:
        t.write(key+'\t'+str (metaDict[key])+'\n')
        
#analyzeMetadata()