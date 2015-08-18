library(wordcloud)
mydata<-read.table('C:/output/treeMap.txt',header=FALSE,sep='\t')
wordcloud(mydata$V1,mydata$V2,colors=rainbow(nrow(mydata)),ordered.colors=TRUE)