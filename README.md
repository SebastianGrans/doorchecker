Doorchecker
===========

A website that, together with an Arduino and a magnetic reed switch, tells you if a door is open.

Installation 
------------
**The current code has not been tested, the follwing is the intended installation**
1. Upload the code in `doorchecker.ino` the the Arduino and assemble the Arduino and the magnetic reed switch according to the schematics. Then connect the Arduino, via USB to the computer on which the web server is running. Also mount the magnetic reed switch on the door/drawer/anything that can be open/closed.
2. Place the Python script, `doorchecker.py` somewhere on the server. Also edit the file and replace `/dev/ttyACM0` with the name of your Arduino and also specify the path of `index.html`. (When connecting the Arduino, type `dmesg` and it will probably be there somewhere.)
3. Start the Python script (Preferrebly using `screen` maybe?).  
4. Go to `somedomain.com/some_folder/index.html` and hopefully it will work. 

Issue and ideas
---------------
### A prettier face \[WIP\]
I'm not a web designer and currently I do not have the time to delve into it just to write a nice front-end for this. Instead I have reqruited [Erik Sjöström](https://github.com/metalgeek).
