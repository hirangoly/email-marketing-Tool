from BeautifulSoup import BeautifulSoup
import _mysql
from _mysql_exceptions import OperationalError 
import time,datetime,math,urllib,urllib2,re,sys
from urlparse import urlparse

soup=''

try: 
  db1=_mysql.connect("localhost","root","simple","scraper")
  db1.query("SELECT url,ID FROM urls WHERE emailscraping=0 ORDER BY RAND() LIMIT 10")

  r=db1.use_result()  
except Exception, e:
  time.sleep(0.1)  
i=1
for row in r.fetch_row(400):
  PAGE_URL_TXT=row[0]
  ID=row[1]
  
  print PAGE_URL_TXT
  try:
    page = urllib2.urlopen(str(PAGE_URL_TXT))
    soup = BeautifulSoup(page)
  except Exception, e: 
    time.sleep(1.0) 

  email_pattern = re.compile('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')
  for match in email_pattern.findall(str(soup)):
    output=match[0]    
    print output
    try:
      db3=_mysql.connect("localhost","root","simple","colombus")
      db3.query("INSERT IGNORE colombus.cb_emails(EMAIL_TXT) VALUES('"+str(output.lower())+"')")
      time.sleep(0.1)
      db3.close()
    except Exception, e:
      time.sleep(0.1)  

  try:
    db4=_mysql.connect("localhost","root","simple","scraper")
    db4.query("UPDATE urls SET emailscraping='1' WHERE ID='"+str(ID)+"'")
    time.sleep(0.1)
    db4.close()
  except Exception, e:
    time.sleep(0.1)  

  
  i=i+1
db1.close()
