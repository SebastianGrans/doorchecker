Doorchecker
===========

A website that, together with an Arduino and a magnetic reed switch, tells you if a door is open.

News
----
Latest commit is a "big" update. I bought a Arduino Nano clone which did not cooperate with everything written for the Arduino Uno. In OS X the Arduino Nano did reset on Serial connection (just as the Uno), but on linux it did not. Which resulted in the Python code not working. Also I changed the schematics a bit.

Also: I built an enclosure for the whole package.
![Image](enclosure.jpg?raw=true)


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

### Logging and configurability
I plan on implementing logging functionality which leads to need of being able to configure the program. Eg. check frequency, file name, you name it. Therefore I should rewrite the program with configurability in mind.



