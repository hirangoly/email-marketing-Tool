#http://stackoverflow.com/questions/1059640/facebook-offline-access-step-by-step
#https://www.facebook.com/developers/createapp.php
#from BeautifulSoup import BeautifulSoup, NavigableString
import urllib
#import re
import _mysql
import MySQLdb
import time
#import sys

filehandle=''

conn=MySQLdb.connect("localhost","root","simple","scraper")
cursor = conn.cursor ()
cursor.execute("SELECT email,ID FROM emails WHERE fb_status = 0 ORDER BY RAND() LIMIT 999")
results = cursor.fetchall()
conn.close()

for row in results:

  email = row[0]
  email = str(email)
  email = email.replace('(','')
  email = email.replace(')','')
  email = email.replace(',','')
  email = email.replace('\'','')
  email = email.replace('\\n','')
  ID=row[1]

  print email
  print ID
  try:
    #https://graph.facebook.com/search?q=jainrangoli@yahoo.co.in&type=user&access_token=243515335674266|e7f6358e5131a036c29804dd.1-1490892266|wAbhaoFiOK462CdtmqltUcvcVEI
    #filehandle = urllib.urlopen('https://graph.facebook.com/search?q='+kws+'&type=user&access_token=2227470867|2.pOW6_GzWHHsNlp2gcC5C5w__.3600.1296028800-1207315306|gKG3YrKRAliMu-1GG7I2CTM_GCk'+'&fields=id')
    filehandle = urllib.urlopen('https://graph.facebook.com/search?q='+email+'&type=user&access_token=243515335674266|e7f6358e5131a036c29804dd.1-1490892266|wAbhaoFiOK462CdtmqltUcvcVEI')
  except IOError:
    print 'dropped'
  except NameError:
    print 'dropped'  
  for lines in filehandle.readlines():
    #lines=lines.replace('{"data":[{"id":"','')
    #lines=lines.replace('"}]}','')
    print lines
    print lines.find('"id":')
    if lines.find('error')==-1 and lines.find('[]')==-1 and lines.find('OAuthException')==-1 and lines.find('"id":') != -1:
	print 'registered'
	#inserting email, title and description to the database
	db2=_mysql.connect("localhost","root","simple","scraper")		
	db2.query("UPDATE scraper.emails SET fb_status = 2 WHERE ID='"+str(ID)+"'")  
    else:
	if lines.find('OAuthException')!=-1:
		print 'OAuthException'
		time.sleep(15)
	else:
		print 'not registered'
		#inserting email, title and description to the database
		db3=_mysql.connect("localhost","root","simple","scraper")		
		db3.query("UPDATE scraper.emails SET fb_status = 1 WHERE ID='" +str(ID)+"'")  

db.close()
