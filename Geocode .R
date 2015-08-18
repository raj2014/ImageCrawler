library(RgoogleMaps)
vecLat<-c()
vecLong<-c()
cityVector<-scan(file="FinalCityNames.txt",what=character(),sep='\n')
for (city in cityVector)
  {
    #print (city)
    result<-getGeoCode(city)
    lat<-result[1]
    long<-result[2]
    vecLat<-append(vecLat,lat)
    vecLong<-append(vecLong,long)
  }
myMap<-GetMap(center=c(0,0),zoom=1,SCALE=1)
PlotOnStaticMap(myMap, lat = vecLat,lon = vecLong,cex=1,pch=20,dest='locmap.jpg',col=rainbow(length(vecLong)), add=TRUE)


