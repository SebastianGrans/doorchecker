Doorchecker
===========

A website that, together with an Arduino and a magnetic reed switch, tells you if a door is open.

Installation
------------
1. Upload the code in `doorchecker.ino` the the Arduino and assemble the Arduino and the magnetic reed switch according to the schematics. Then connect the Arduino, via USB to the computer on which the web server is running. Also mount the magnetic reed switch on the door/drawer/anything that can be open/closed.
2. Place the Python script, `doorchecker.py` somewhere on the server. Ensure that the group `www-data` can read and execute the file. Also edit the file and replace `/dev/ttyACM0` with the name of your Arduino. (When connecting the Arduino, type `dmesg` and it will probably be there somewhere.)
3. Place `doorchecker.php` on the directory of the website (eg. `/var/www/). Then edit the file and specify where the script is placed.
4. Go to `somedomain.com/some_folder/doorchecker.php` and hopefully you will get a `1` if the door is open or a `0` if it is not. 

Issue and ideas
---------------

### 1 second delay
Due to the fact that the Arduino resets on new connection, there is a ~1 second delay on the website. This can be solved by two ways:

1. Remove the reset function
2. Rethink the server side

Number 1 is rather simple, either cut the RESET-EN trace on the Arduino, or connect a 110 Ohm resistor between reset and ground.
 
Number 2 is also simple and does not require me to find a 110 Ohm resistor. The solution would be to rewrite the Python script to connect to the Arduino every minute and save the status to a file which, without delay, could be read by php.

### A prettier face
I'm not a web designer and currently I do not have the time to delve into it just to write a nice front-end for this. Instead I intend to recruit someone with a better skill set.


