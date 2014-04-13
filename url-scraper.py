# -*- coding: iso-8859-1 -*- 
import shutil,os,time,datetime,math,urllib,re,urllib2
from BeautifulSoup import BeautifulSoup
import _mysql
from _mysql_exceptions import OperationalError 

soup=''
source=''
anchor_txt=''
anchor_href=''

j=0
while(j<=1):

  try: 
    db1=_mysql.connect("localhost","root","simple","scraper")
    db1.query("SELECT keyword,ID FROM keywords WHERE status=0 ORDER BY RAND() LIMIT 5")
    r=db1.use_result()
  
    i=0
    while 1:  
      
      row = r.fetch_row()[0] 
      keyword=row[0]
      ID=row[1]
        
      keyword=keyword.replace(' ','+')        
      source='http://www.google.com/search?sclient=psy&hl=en&source=hp&q='+str(keyword)
      print '----------------'
      print 'Job #'+str(i)+' has started'
      print str(source)
      print '----------------'
      
      try:
        headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0' }
        req = urllib2.Request(str(source), None, headers)
        page=urllib2.urlopen(req)
	print 'ok'
      except Exception, e:
        time.sleep(0.1)    
      
      soup = BeautifulSoup(page)
      #print soup      

      for links in soup.findAll('a', href=True):
       
       if links['href'].find('http://')!=-1 and links['href'].find('google')==-1 and links['href'].find('aclk')==-1 and links['href'].find('youtube')==-1 :
        link=links['href']
          
        #print str(ID)
        print str(link)
    
        try: 
         db2=_mysql.connect("localhost","root","simple","scraper")
         db2.query("INSERT IGNORE urls(url,position,keyword) VALUES('"+str(link)+"','"+str(i)+"','"+str(keyword)+"') ")
        except Exception, e:
         time.sleep(0.1)
            
      try: 
        db3=_mysql.connect("localhost","root","simple","scraper")
        db3.query("UPDATE keywords SET status=1 WHERE ID='"+str(ID)+"'")
      except Exception, e:
        time.sleep(0.1)        
      i=i+1
  
  except Exception, e:
    time.sleep(0.1)
  j=j+1
