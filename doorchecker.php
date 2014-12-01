<html>
    <head>
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
	<title>Är skamvrån öppen?</title>
        <!-- <meta http-equiv="refresh" content="5" /> -->
    </head>
    <body>
	<?php
		/* Change to where the script is placed.
		Also make sure that www-data can both execute and 
		read the file. */ 
		$command = escapeshellcmd('/var/www/doorchecker.py');
		$doorstatus = shell_exec($command);
		echo $doorstatus;
	?>
    </body>
</html>
