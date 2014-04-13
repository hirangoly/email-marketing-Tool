CREATE DATABASE `colombus` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
 CREATE  TABLE  `colombus`.`cb_emails` (  `ID` bigint( 8  )  NOT  NULL  auto_increment ,
 `EMAIL_TXT` varchar( 255  )  NOT  NULL ,
 `FLAG` int( 1  )  NOT  NULL ,
 `TIMESTAMP` timestamp NOT  NULL  default CURRENT_TIMESTAMP ,
 PRIMARY  KEY (  `ID`  ) ,
 UNIQUE  KEY  `EMAIL_TXT` (  `EMAIL_TXT`  )  ) ENGINE  =  MyISAM  DEFAULT CHARSET  = latin1 AUTO_INCREMENT  =27845;
 CREATE  TABLE  `colombus`.`cb_gmail` (  `ID` bigint( 8  )  NOT  NULL  auto_increment ,
 `USERNAME` varchar( 255  )  NOT  NULL ,
 `PASSWORD` varchar( 255  )  NOT  NULL ,
 `FULLNAME_TXT` varchar( 255  )  NOT  NULL ,
 `PROFILE_URL_TXT` varchar( 255  )  NOT  NULL ,
 `FLAG` int( 1  )  NOT  NULL default  '0',
 PRIMARY  KEY (  `ID`  )  ) ENGINE  =  MyISAM  DEFAULT CHARSET  = latin1 AUTO_INCREMENT  =36;
 CREATE  TABLE  `colombus`.`cb_pages` (  `ID` bigint( 8  )  NOT  NULL  auto_increment ,
 `PAGE_URL_TXT` varchar( 255  )  NOT  NULL ,
 `FLAG` int( 1  )  NOT  NULL ,
 `TIMESTAMP` timestamp NOT  NULL  default CURRENT_TIMESTAMP ,
 PRIMARY  KEY (  `ID`  ) ,
 UNIQUE  KEY  `PAGE_URL_TXT` (  `PAGE_URL_TXT`  )  ) ENGINE  =  MyISAM  DEFAULT CHARSET  = latin1 AUTO_INCREMENT  =36572;
 CREATE  TABLE  `colombus`.`cb_sources` (  `ID` bigint( 8  )  NOT  NULL  auto_increment ,
 `SOURCE_URL_TXT` varchar( 255  )  NOT  NULL ,
 `TIMESTAMP` timestamp NOT  NULL  default CURRENT_TIMESTAMP ,
 PRIMARY  KEY (  `ID`  ) ,
 UNIQUE  KEY  `SOURCE_URL_TXT` (  `SOURCE_URL_TXT`  )  ) ENGINE  =  MyISAM  DEFAULT CHARSET  = latin1 AUTO_INCREMENT  =800;

 CREATE DATABASE `colombusScraper` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;

CREATE TABLE `colombusScraper`.`keywords` (
`ID` bigint( 8 ) NOT NULL AUTO_INCREMENT ,
`keyword` varchar( 255 ) NOT NULL ,
`website_url` varchar( 100 ) default NULL ,
`job_ID` bigint( 8 ) NOT NULL ,
`status` int( 1 ) NOT NULL ,
PRIMARY KEY ( `ID` ) 
) ENGINE = MYISAM DEFAULT CHARSET = latin1 AUTO_INCREMENT =8001;

CREATE TABLE `colombusScraper`.`urls` (
`ID` bigint( 8 ) NOT NULL AUTO_INCREMENT ,
`url` varchar( 255 ) NOT NULL ,
`position` int( 2 ) NOT NULL ,
`date` timestamp NOT NULL default CURRENT_TIMESTAMP ,
`keyword` varchar( 255 ) NOT NULL ,
`website_url` varchar( 100 ) default NULL ,
`emailscraping` int( 1 ) NOT NULL ,
PRIMARY KEY ( `ID` ) ,
FULLTEXT KEY `url` ( `url` ) 
) ENGINE = MYISAM DEFAULT CHARSET = latin1 AUTO_INCREMENT =32946;
