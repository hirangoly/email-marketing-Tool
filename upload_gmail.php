<form method="post" enctype="multipart/form-data">
<table width="350" border="0" cellpadding="1" cellspacing="1" 
class="box">
<tr> 
<td width="246">
<input type="hidden" name="MAX_FILE_SIZE" value="800000000">
<input name="userfile" type="file" id="userfile"> 
</td>
<td width="80"><input name="upload" type="submit" class="box" 
id="upload" value=" Upload "></td>
</tr>
</table>
</form>

<?php
if(isset($_POST['upload']) && $_FILES['userfile']['size'] > 0)
{
$fileName = $_FILES['userfile']['name'];
$tmpName  = $_FILES['userfile']['tmp_name'];
$fileSize = $_FILES['userfile']['size'];
$fileType = $_FILES['userfile']['type'];

$fp      = fopen($tmpName, 'r');
$content = fread($fp, filesize($tmpName));
$lines = explode("\n", $content);

$link = mysql_connect('localhost', 'root', 'simple');
mysql_select_db('colombus',$link);

$i=0;
while($i<sizeof($lines))
{

$insertion=explode("\t", $lines[$i]);

mysql_query("INSERT IGNORE 
colombus.cb_gmail(USERNAME,PASSWORD,FULLNAME_TXT,PROFILE_URL_TXT) 
VALUES('".addslashes(substr($insertion[0], 0, 
-1))."','".addslashes(substr($insertion[1], 0, 
-1))."','Mabel','http://www.ezdia.com/profile/mabel')");
$i=$i+1;
}
fclose($fp);

echo "<br>File $fileName uploaded<br>";
} 
?>
