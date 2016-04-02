*Writing Python test cases is very similar to Java

*Python TCP communication when reading files isn't always the same behavior.
 Reading in blocks vs...[finish me later]
 
*You shouldn't run Python modules directly. Eclipse automatically appends to path
 so files run properly but they don't work if you call the from the command line.

*File structure matters. You can do relative and absolute imports
 
*Python does allow for polymorphism

*Argparse library decides on how to handle errors for you (usually by exiting) making 
 it difficult to do what I want it to :( This forced me to write my own custom Argparser
 class to prevent the undesired sys.exit() call

*Cmd library steals focus from SocketServer srv.serve_forever() which forced me to 
 use threading in a unconventional way. Then I had to raise a KeyboardException to 
 have a "clean" exit from the cmdloop. 

*@staticmethod decorator does not pass class instance (self) to method. 
