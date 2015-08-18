import Tkinter as tk
import tkMessageBox
from CrawlThreadCreation import *
from ImageThreadLoader import *  
from analyzeData import *
from siteList import *

class ImageCrawler(tk.Frame):
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=400,
                          height=300)
        # Set the title
        self.master.title('Image Crawler')
 
        # This allows the size specification to take effect
        self.pack_propagate(0)
 
        # We'll use the flexible pack layout manager
        self.pack()
 
        #Fill the  Website List
        self.webSiteList=['https://foursquare.com']
        #Fill the city List
        self.cityEntries=['Orlando,US',
                                                'Sydney,Australia',
                                                'Paris,France',
                                                'London,England',
                                                'Venice,Italy',
                                                'Manhattan,US',
                                                'Cape Town,South Africa',
                                                'Las Vegas,US',
                                                'Rome,Italy',
                                                'Reef Australia',
                                                'Maldives',
                                                'Hawaii,US',
                                                'Crete,Greece',
                                                'Grand Canyon,US',
                                                'San Diego,US',
                                                'Niagara Falls,Canada',
                                                'San Francisco,US',
                                                'Rio de Janeiro, RJ, Brazil',
                                                'Los Angeles,US',
                                                'Dubai,UAE',
                                                'Auckland,New Zealand',
                                                'Singapore',
                                                'Puerto Rico',
                                                'Bali,Indonesia',
                                                'Durban,South Africa',
                                                'Bangkok,Thailand',
                                                'Iceland',
                                                'WhitSundays,Australia',
                                                'Costa Del Sol,Spain',
                                                'Cairns,Australia',
                                                'Budapest',
                                                'Melbourne,Australia',
                                                'Mallorca,Spain',
                                                'Giza,Egypt',
                                                'Lake District,England',
                                                'Cambodia',
                                                'Ho Chi Minh City, Vietnam',
                                                'Copenhagen',
                                                'Sharm El Sheikh ,Egypt', 
                                                'New York,US',
                                                'Madrid,Spain',
                                                'Zermatt,Switzerland',
                                                'Algarve,Portugal',
                                                'Victoria Falls,Zimbabwe',
                                                'Marbella,Spain',
                                                'St. Petersburg, Russia',
                                                'Vienna, Austria',
                                                'Chichen Itza,Mexico',
                                                'Florence,Italy',
                                                'Disney World,Florida,US',
                                                'Puerto Banus,Spain',
                                                'Toronto,Canada',
                                                'China',
                                                'Agra,India',
                                                'Edinburgh,Scotland',
                                                'Menorca,Spain',
                                                'Istanbul, Turkey',
                                                'Luxor',
                                                'Hong Kong',
                                                'Banff,Canada',
                                                'Sorrento,Italy',
                                                'Key West,US',
                                                'Cancun, QR, Mexico',
                                                'Koh Samui,Thailand',
                                                'Nice,France',
                                                'Machu Picchu,Peru',
                                                'Yosemite National Park,US',
                                                'Oahu,US',
                                                'Florida Keys,US',
                                                'Easter Islands',
                                                'Dublin,Ireland',
                                                'Vancouver,Canada',
                                                'Ayers Rock,NT',
                                                'Hawaii',
                                                'Naples,Italy',
                                                'St Pete Beach,US',
                                                'Amritsar,India',
                                                'Barcelona, Spain',
                                                'Ibiza,Spain',
                                                'Montreal,Canada',
                                                'Costa Blanca,Spain',
                                                'Adelaide,Australia',
                                                'Airlie Beach,Australia',
                                                'Buenos Aires,Argentina',
                                                'Prague,Czech Republic',
                                                'Lisbon, Portugal',
                                                'Cuba',
                                                'Cyprus',
                                                'costa Rica',
                                                'Ecuador',
                                                'Isle of Man,Europe',
                                                'Kusadasi,Turkey',
                                                'Chamonix,France',
                                                'Beijing,China',
                                                'Cannes,France',
                                                'Amsterdam,Netherlands',
                                                'Bodrum,Turkey',
                                                'Courchevel,France',
                                                'Berlin,Germany',
                                                'Corfu,Greece']
        # Website Selection Menu
        self.default_website = tk.StringVar()        
        self.default_website.set('Please Select the Websites to crawl')
        self.websiteDropdown = tk.OptionMenu(self,
                                      self.default_website,*self.webSiteList)
                                     
        # City Selection Menu
        self.default_city=tk.StringVar()
        self.default_city.set('Please Select the sites to crawl')
        self.cityList = tk.OptionMenu(self,
                                      self.default_city,"All",
                                      *self.cityEntries)      
 
        
        # Declaring the buttons and linking the functions
        self.textBox=tk.Text(xscrollcommand=set(),yscrollcommand=set(),height=5,width=5)
        
        self.crawl_button = tk.Button(self,
                                   text='CRAWL',
                                   command=self.initiateCrawl,height=2,width=15)
        
        self.metadata_button = tk.Button(self,
                                   text='ANALYZE METADATA',
                                   command=self.analyzeMetadata,height=2,width=25)
        self.loadImages_button = tk.Button(self,
                                   text='LOAD IMAGES',
                                   command=self.imageDownloader,height=2,width=25)
        self.fetchSite_button = tk.Button(self,
                                   text='FETCH SIGHT LOCATIONS',
                                   command=self.createSiteList,height=2,width=25)
 
       
        
       
        # Put the controls on the form
        
        self.websiteDropdown.pack(fill=tk.X, side=tk.TOP)
        self.cityList.pack(fill=tk.X,side=tk.TOP)
        self.crawl_button.pack(fill=tk.X,side=tk.TOP)
        self.metadata_button.pack(fill=tk.X,side=tk.TOP)
        self.fetchSite_button.pack(fill=tk.X,side=tk.TOP)
        self.loadImages_button.pack(fill=tk.X,side=tk.TOP)        
        self.textBox.pack(fill=tk.X,side=tk.TOP)
        
        
     # Crawl handling  routine 
    def initiateCrawl(self):                     
        crawl(self.default_website.get().title().lower(),self.default_city.get().title(),self.cityEntries)
        tkMessageBox.showinfo("Crawling Status","Crawling Completed Successfully!!")
        self.textBox.insert('1.0',"Crawling Completed Successfully!!","a")
     
     # Metadata Collection routine   
    def analyzeMetadata(self):
        analyzeMetadata()
        tkMessageBox.showinfo("MetaData Collection Status","Metadata Collected Successfully!!")
        self.textBox.insert('1.0',"Metadata Completed Successfully!!","a")
     
     # Image Collection Routine
    def imageDownloader(self):
        ImageLoader()  
        tkMessageBox.showinfo("SiteList Collection  Status","Images Collected Successfully!!")
        self.textBox.insert('1.0',"Images Collected Successfully!!","a")
     
     # Sight Address Collection Routine   
    def createSiteList(self): 
        createSiteList()
        tkMessageBox.showinfo("SiteList Collection  Status","All sight Addresses Collected Successfully!!")
        self.textBox.insert('1.0',"Sights Address Collected Successfully!!","a")
          
    def run(self):
        ''' Run the app '''        
        self.mainloop()
 
app = ImageCrawler(tk.Tk())
app.run()