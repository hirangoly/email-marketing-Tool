import smtplib,time,datetime,math,re,random
import _mysql
from _mysql_exceptions import OperationalError 
try: 
  db1=_mysql.connect("localhost","root","simple","colombus")
  db1.query("SELECT EMAIL_TXT,ID FROM colombus.cb_emails WHERE FLAG=0 AND (EMAIL_TXT LIKE '%@gmail.com' OR EMAIL_TXT LIKE '%@yahoo.com' OR EMAIL_TXT LIKE '%@live.com' OR EMAIL_TXT LIKE '%@hotmail.com')  AND (SELECT COUNT(*) FROM cb_gmail WHERE FLAG=0)>=20 ORDER BY RAND()")

  r=db1.use_result()  
except Exception, e:
  time.sleep(0.1)  
i=1
for row in r.fetch_row(350):
  EMAIL_TXT=row[0]
  ID=row[1]
  time.sleep(random.randrange(1,20))

  try: 
    db2=_mysql.connect("localhost","root","simple","colombus")
    db2.query("SELECT USERNAME,PASSWORD,FULLNAME_TXT,PROFILE_URL_TXT FROM colombus.cb_gmail WHERE FLAG=0 ORDER BY RAND() LIMIT 1")
  
    r2=db2.use_result()  
  except Exception, e:
    time.sleep(0.1)  
  for row2 in r2.fetch_row(1000):
  
    gmail_user=str(row2[0].replace('\n',''))
    gmail_pwd=str(row2[1].replace('\n',''))
    
    fullname_txt=row2[2]
    profile_url_txt=row2[3]

    print 'From:'+gmail_user+'/'+gmail_pwd

    #smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)  

    smtpserver.set_debuglevel(1)

    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    
    try:
      smtpserver.login(gmail_user, gmail_pwd)
    except Exception,e :
      time.sleep(1.0)
      db5=_mysql.connect("localhost","root","simple","colombus")
      db5.query("UPDATE colombus.cb_gmail SET FLAG='1' WHERE USERNAME='"+str(gmail_user)+"'")
  
    welcome=['Hi','Hello','Dear Sir/Madam','Dear','Good morning','Good Afternoon','Morning']
    close=['Thanks','Thank you','Best','Regards','Best Regards','Yours','Kind regards','Cheers','Thanks and regards','Look forward to talk with you','I am looking forward to speak with you','Thank you very much','Thank you for your time'] 
    sub=['About your resume','About your CV','About your profile','Interested by your profile','Regarding your services','Interested by your services']     
      
    to = str(EMAIL_TXT)
    header = 'MIME-Version: 1.0\r\nContent-type: text/html;charset=utf-8\r\nTo:' + to + '\n'+'Subject:'+ sub[random.randrange(0,sub.__len__())]+' \n\n'
    print header
    msg = header + welcome[random.randrange(0,welcome.__len__())]+',<br /><br />I saw your resume online, and I will be interested to speak with you about a project.<br/><br/>Please add me as connection on eZdia, this is my profile: <a href="'+str(profile_url_txt)+'?utm_source=colombus">'+str(profile_url_txt)+'</a>.<br /><br />'+close[random.randrange(0, close.__len__())]+'<br />'+str(fullname_txt)
    
    try:
      smtpserver.sendmail(gmail_user, to, msg)
      print 'done!'  
      db4=_mysql.connect("localhost","root","simple","colombus")
      db4.query("UPDATE colombus.cb_emails SET FLAG='1',TIMESTAMP=CURRENT_TIMESTAMP WHERE ID='"+str(ID)+"'")
      time.sleep(0.5)
      db4.close()
    except Exception, e:
      time.sleep(0.1)  
   
smtpserver.close() 
print 'server is closed!'  
