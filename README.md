![Alt text](https://github.com/cathoderay/minifyme/raw/master/wiki/minifyme.png)


Welcome to our (because it's open source) funny js minification/compression project.
Now, depending on the structure of your code, this minifier can harm it. It's still a work in progress.


How to use
-------

Before running minifyme, I recommend using jslint and fix your errors for yourself.
Try https://github.com/reid/node-jslint

    $ ./minifyme.py file.js

    Statistics
    ==========    
        Original file size: 166 bytes  
        Minified file size: 90 bytes
    
        Removed bytes: 0.45% 
    
    File test.min.js written.


How it works
------------

The main idea is to apply a sequence of transformations to the input. These transformations are functions that receive a string (javascript code) and 
returns a string (javascript code) with the same behavior when interpreted (more on minification [here](http://en.wikipedia.org/wiki/Minification_(programming\))), though, hopefully, shorter.

For a while, transformations already working are:


  1. Removing leading and trailing whitespaces: '\r', '\t', ' '.;
  2. Removing // comments;
  3. Removing /**/ comments;


Performance
-----------

Not yet a requirement for this project. It's just for fun!


Next steps
---------
Parse js decently.

Remove unnecessary white spaces.
