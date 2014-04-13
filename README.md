email-marketing-Tool
====================

Framework to send mass email to users based on the keyword search. e.g I want to notify all the php programmers of different cities for a job opening on odesk website. i.e keyword is php programmer

Steps to follow:
* Based on keyword provided generate google queries for the combination 5 different providers and 100 different cities. This will generate 500 google queries to search in the google e.g keyword is php programmer, providers are (gmail, live, yahoo...etc), cities are (san francisco, los angeles, NY...etc) i.e google query will be "php programmer" "gmail.com" "san francisco, "php programmer" "live.com" "san francisco"", , "php programmer" "yahoo.com" "los angeles" and so on
script: index.php
* Search for the pages in google for the google queries and extract url from those pages and store it into the database
script: scraper.py
* Scrap email from the url stored in the database
script: email-scraper.py
* Check the validity of those emails in facebook. Use of facebook API, remember to get the access token to use the API
script: email-validator-facebook.py
* Finally send email to the valid email ids in timely manner, limited emails at a time. Email sent would be unique/personalized and randomly generated some of the parts of the body
* This will also show following statics over screen:
   * # of emails are in queue
   * # of gmail accounts are still available
   * # of pages are in queue
   * # of email has been sent today
   * # of users are expected to register (61% of total email sent)
   * # of new users (new users registered)
* Cron job will be scheduled to run scripts automatically  
