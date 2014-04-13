<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>     
  <head>       
    <meta http-equiv="content-type" content="text/html; 
charset=windows-1250">       
    <meta name="generator" content="PSPad editor, www.pspad.com">       
    <title>    
    </title>          
    <style>     body{   font-family: helvetica, arial, sans-serif; 
font-size: 12px; color: #616161; line-height: 1.6em; background:#EEE; }         
input[type="text"]{   width: 365px; height: 30px; border: solid 1px 
#B1B1B1; font-size: 12px; padding: 5px 4px; color: #343434; 
margin-right: 5px; }             input[type="submit"]{   width: 100px; 
height: 30px; border: solid 1px #B1B1B1; font-size: 12px; padding: 5px 
4px; color: #343434; margin-right: 5px;          
    </style>        
  </head>     
  <body>     <h2>Welcome to the Colombus project</h2>     <h3>Who is 
your audience today?</h3>            
    <form action="" method="POST">    
      <input type="text" name="kw">           
      <input type="hidden" name="upload">    
      <input type="submit" value="Bulk Invite!">          
    </form>    
    <ul>             
      <li>We will create a list of Google queries based on your keyword:       
      </li>             
      <ul>               
        <li>Concatenated with the 5 top email providers.         
        </li>               
        <li>Concatenated with the top 100 U.S cities.         
        </li>                
        <li>An example of query is: "i am freelancer" "@gmail.com" "los 
angeles"         
        </li>             
      </ul>              
    </ul>        
    <ul>            
      <li>We will then send the 500 Google queries to Scraper.       
      </li>                
      <ul>                  
        <li>We run 14 Google queries per minute.         
        </li>            
      </ul>       
    </ul>         
    <ul>            
      <li>Each results found on Google will be scraped, and we will 
store the email addresses found on the pages.       
      </li>           
    </ul>           
    <ul>            
      <li>The data will be synchronised with the email marketing 
process.       
      </li>                    
      <ul>                  
        <li>Each message sent is unique (some parts of the email body 
are generated randomly).         
        </li>                  
        <li>We send 200 messages per hour.         
        </li>                  
        <li>We use random Gmail SMTP         
        </li>            
      </ul>          
    </ul>         
  </body>
</html>
<?php
if(isset($_POST['upload'])){
$link = mysql_connect('localhost', 'root', 'simple');
mysql_select_db('scraper',$link);
$keyword='"'.$_POST['kw'].'"';
$cities=array('new york',
'los angeles',
'chicago',
'houston',
'philadelphia',
'phoenix',
'san diego',
'san antonio',
'dallas',
'detroit',
'san jose',
'indianapolis',
'jacksonville',
'san francisco',
'columbus',
'austin',
'memphis',
'baltimore',
'milwaukee',
'fort worth',
'charlotte',
'el paso',
'boston',
'seattle',
'washington',
'denver',
'nashville-davidson',
'portland',
'oklahoma',
'las vegas',
'tucson',
'long beach',
'albuquerque',
'new orleans',
'cleveland',
'fresno',
'sacramento',
'kansas',
'virginia beach',
'mesa',
'atlanta',
'omaha',
'oakland',
'tulsa',
'honolulu cdp',
'miami',
'minneapolis',
'colorado springs',
'arlington',
'wichita',
'santa ana',
'anaheim',
'st. louis',
'pittsburgh',
'tampa',
'cincinnati',
'raleigh',
'toledo',
'aurora',
'buffalo',
'riverside',
'st. paul',
'corpus christi',
'newark',
'stockton',
'bakersfield',
'anchorage',
'lexington-fayette',
'louisville',
'st. petersburg',
'plano',
'norfolk',
'jersey',
'birmingham',
'lincoln',
'glendale',
'greensboro',
'hialeah',
'baton rouge',
'fort wayne',
'madison',
'garland',
'scottsdale',
'rochester',
'henderson',
'akron',
'chandler',
'chesapeake',
'modesto',
'lubbock',
'fremont',
'glendale',
'montgomery',
'orlando',
'chula vista',
'durham',
'shreveport',
'laredo',
'yonkers',
'tacoma');
$i=0;
while($i<sizeof($cities))
{
$providers=array('@gmail.com','@yahoo.com','@hotmail.com','@live.com','@aol.com');
$j=0;
while($j<sizeof($providers))
{
mysql_query("INSERT IGNORE scraper.keywords(keyword) 
VALUES('".$keyword.' \"'.$cities[$i].'\" \"'.$providers[$j].'\"'."')");
$j=$j+1;
}
$i=$i+1;
}
header('Location: ./');
}
?>

<?php
$link = mysql_connect('localhost', 'root', 'simple');
mysql_select_db('colombus',$link);
$query=mysql_query("SELECT EMAIL_TXT FROM cb_emails WHERE 
FLAG=0 AND (EMAIL_TXT LIKE '%gmail.com%' OR EMAIL_TXT LIKE 
'%@hotmail.com%' OR EMAIL_TXT LIKE '%live.com%' OR EMAIL_TXT LIKE 
'%yahoo.com%') 
");

$query2=mysql_query("SELECT * FROM cb_gmail WHERE FLAG=0");
?>
<h4><?php echo mysql_num_rows($query)?> emails are in queue.</h4>

<h4><?php echo mysql_num_rows($query2)?> gmail accounts are still 
available.</h4>





<?php
$link = mysql_connect('localhost', 'root', 'simple');
mysql_select_db('scraper',$link);
$query=mysql_query("SELECT url FROM urls WHERE emailscraping=0");
?>
<h4><?php echo mysql_num_rows($query)?> pages are in queue.</h4>


<?php
$link = mysql_connect('localhost', 'root', 'simple');
mysql_select_db('colombus',$link);

$date=date('Y-m-d');


$query=mysql_query("SELECT *  FROM cb_emails WHERE FLAG = 1 AND 
TIMESTAMP LIKE '%".$date."%'");
?>
<h4><?php echo mysql_num_rows($query)?> emails has been sent today! 

<?php
$round=mysql_num_rows($query)*0.61/100;
?>


<?php echo round($round,0);?> users are expected to 
register.</h4>

<h3>Our news friends</h3>

<?php
$yesterday=date("Y-m-d", strtotime("yesterday"));

$link = mysql_connect('localhost', 'root', 'simple');
mysql_select_db('ezdia',$link);
$query=mysql_query("SELECT photo_thumbnail  FROM users WHERE 
creationDate LIKE '%".$yesterday."%' AND photo_thumbnail!=''");

while($results=mysql_fetch_array($query))
{
echo '<img src="http://www.ezdia.com'.$results[0].'" width="80" 
height="96">';
}


?>
