# crispy-fortnight
Custom, cross-platform Remote Access Terminal (RAT) coded in Python 2.7 built just for fun. The intent is to learn Python, understand the "inner-workings" of RAT's and improve detection of malicious behavior - not to create anything new. Features are added for purely educational learning, NOT for malicious activity! You are responsible for your own actions. 
 
## How to run things
Run crispyd.py(local) and implant.py(remote) at the root of the project. Use "tail -f crispy.log" to follow the log file on the server.
ie. "python crispyd.py --config crispy.conf"

## Contributors
Shoutouts to people who have helped along the way either directly or indirectly.
<br>-Thanks to @jchristman for all the bug fixes and commits!
<br>-Thanks to @bts0 for the AES code.
<br>-Thanks to @WesleyThurner for the apps module code with versioning on mac!
<br>-Thanks to @n1nj4sec for rpyc, cmd.Cmd and a few other examples in his similar and far superior Python RAT. After numerous attempts of mine to avoid using RPC, I came across this code when trying to find good examples on the R
PyC library. I ended up modeling a large portion of my code after his. "good artists copy; great artists steal (Pablo Picasso)" https://github.com/n1nj4sec/pupy
<br>-RPyC creator @tomerfiliba https://github.com/tomerfiliba/rpyc

## Implemented modules
<br>[x] upload - transfer a file to the remote client
<br>[x] download - transfer a file from remote client to server
<br>[ ] users - find all users
<br>[ ] apps - find all installed applications
<br>[ ] screenshot - take a screenshot of the remote client
<br>[ ] checkav - determine probability of which (if any) AV is installed
<br>[ ] checkvm - determine if client is running on a virtual instance

## TODO
<br>[x] set up proper packaging
<br>[x] set up client/server communication
<br>[x] add logging to server for debuggin purposes
<br>[x] add upload/download functionality
<br>[x] modularize code
<br>[x] central session control
<br>[ ] set up client/server authentication and stream encrytpion
<br>[ ] create implant binaries using pyinstaller
<br>[ ] add shell functionality
<br>[ ] add tab completion
<br>[ ] obfuscate implant binaries
