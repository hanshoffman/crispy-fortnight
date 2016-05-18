# crispy-fortnight
Custom, cross-platform Remote Access Terminal (RAT) coded in Python 2.7 built just for fun. The intent is to learn Python, understand the "inner-workings" of RAT's and improve detection of malicious behavior - not to create anything new. Features are added for purely educational learning, NOT for malicious activity! You are responsible for your own actions.

## Generate Server RSA keys
Place these self-signed keys in crispy/crypto
- openssl req -new -x509 -keyout key.pem -out cert.pem -days 365 -nodes -newkey rsa:2048

## How to run things
Run crispyd.py(local) and implant.py(remote) at the root of the project. Use "tail -f crispy.log" to follow the log file on the server.
- ie. "python crispyd.py --config crispy.conf"
- optional " --loglvl=DEBUG"

## Required Python libraries for crispyd server
Package manager install:
python-dev
python-pip
pip install:
rpyc
psutil

## Contributors
Shoutouts to people who have helped along the way either directly or indirectly.
- Thanks to @jchristman for all the bug fixes and commits!
- Thanks to @bts0 for the AES code.
- Thanks to @WesleyThurner for the help with various modules!
- Thanks to @n1nj4sec for rpyc, cmd.Cmd and a few other examples in his similar and far superior Python RAT. After numerous attempts of mine to avoid using RPC, I came across this code when trying to find good examples on the R
PyC library. I ended up modeling a large portion of my code after his. "good artists copy; great artists steal (Pablo Picasso)" https://github.com/n1nj4sec/pupy
- RPyC creator @tomerfiliba https://github.com/tomerfiliba/rpyc

## Implemented modules
| Done | Name | Lin | Mac | Win | description |
|:---:|:---:|:---:|:---:|:---:|---|
|   | apps | X | X |   | list all installed applications  |
|   | checkav | X | X | X | determine probability of which (if any) AV is installed |
|   | checkvm | X | X | X | determine id client is running on a virtual machine  |
| X | download | X | X | X | transfer a file from remote client to server |
| X | drives | X | X | X |  enumerate drives on client |
|   | execute | X | X | X | execute binary on client |
|   | kill  | X | X | X |  kill process on remote client |
|   | netstat | X | X |   | perform netstat on remote client  |
|   | persistence  |   |   |   | create persistence on remote client |
|   | printers  | X | X |   | enumerate printers |
|   | ps | X | X | X | process list of remote client |
|   | screenshot |   |   |   | take a screenshot of the remote client |
|   | search |   |   |   |   |
| X | upload | X | X | X | transfer a file to the remote client |
| X | users | X | X |   |  list all users |

## TODO
- [x] set up proper packaging
- [x] set up client/server communication
- [x] add logging to server for debuggin purposes
- [x] add upload/download functionality
- [x] modularize code
- [x] central session control
- [x] set up client/server authentication and stream encrytpion
- [ ] create implant binaries using pyinstaller
- [ ] add shell functionality
- [ ] add tab completion
- [ ] obfuscate implant binaries
- [ ] improve checkav module signatures
- [ ] improve checkvm module checks
