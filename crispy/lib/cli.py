import argparse
import cmd
import ConfigParser
import getpass
import logging
import sys

from . myparser import *
from crispy import __version__

logger = logging.getLogger(__name__)

BANNER = "                                                                     \n \
     ___           ___                       ___           ___                 \n \
    /  /\         /  /\        ___          /  /\         /  /\         ___    \n \
   /  /:/        /  /::\      /  /\        /  /:/_       /  /::\      /__/|    \n \
  /  /:/        /  /:/\:\    /  /:/       /  /:/ /\     /  /:/\:\    |  |:|    \n \
 /  /:/  ___   /  /:/~/:/   /__/::\      /  /:/ /::\   /  /:/~/:/    |  |:|    \n \
/__/:/  /  /\ /__/:/ /:/___ \__\/\:\__  /__/:/ /:/\:\ /__/:/ /:/   __|__|:|    \n \
\  \:\ /  /:/ \  \:\/:::::/    \  \:\/\ \  \:\/:/~/:/ \  \:\/:/   /__/::::\    \n \
 \  \:\  /:/   \  \::/~~~~      \__\::/  \  \::/ /:/   \  \::/       ~\~~\:\   \n \
  \  \:\/:/     \  \:\          /__/:/    \__\/ /:/     \  \:\         \  \:\  \n \
   \  \::/       \  \:\         \__\/       /__/:/       \  \:\         \__\/  \n \
    \__\/         \__\/                     \__\/         \__\/                \n \
								       %s" %(__version__)

class CrispyCLI(cmd.Cmd):
    """ Available commands for crispy cli. """

    def __init__(self, srv, config_file="crispy.conf"):
	cmd.Cmd.__init__(self)
	self.config = ConfigParser.ConfigParser()
	self.config.read(config_file)
	if self.config.getboolean("CMDLINE", "display_banner"):
	    self.intro = BANNER
	else:
	    self.intro = ""
	self.prompt="{0}@crispy>> ".format(getpass.getuser())
	self.doc_header = "Available commands:"
	self.srv = srv

    @staticmethod
    def format_error(msg):
        """ Return a formatted error log line. """
        print "[!] " + msg.rstrip() + "\n"

    @staticmethod
    def format_info(msg):
        """ Return a formatted info log line. """
        print "[%] " + msg.rstrip() + "\n"

    @staticmethod
    def format_success(msg):
        """ Return a formatted success log line. """
        print "[+] " +  msg.rstrip() + "\n"

    @staticmethod
    def format_warning(msg):
        """ Return a formatted warning log line. """
        print "[*] " + msg.rstrip() + "\n"
    
    def do_exit(self, args):
	""" Shutdown crispy daemon. All sessions will be lost. """
	raise KeyboardInterrupt

    do_quit = do_exit

    def do_help(self, args):
	""" Help menu. """
	logger.debug("do_help() was called")
	cmd.Cmd.do_help(self, args)

    def emptyline(self):
	""" Do nothing when an emptyline is entered instead of repeat last command. """
	pass

    def do_modules(self, args):
	""" List available modules. """
        self.format_error("implement me")

    def do_run(self, args):
        """ Run a module on one or multiple clients. """
        logger.debug("do_run() was called")
        self.format_error("implement me")

    def do_sessions(self, args):
	""" List/interact with established sessions. """
	logger.debug("do_sessions() was called")
	
	parser = CrispyArgumentParser(description=self.do_sessions.__doc__,
                                       prog="sessions")
	#parser.add_argument("-i",
        #                dest="interact",
	#		help="interact with the selected session",
	#		metavar="<session_id>",
	#		type=int)
	#parser.add_argument("-k",
        #                dest="kill",
        #                help="kill the selected session",
        #                metavar="<session_id>",
        #                type=int)
	parser.add_argument("-l",
			action="store_true",
			dest="list",
                        help="list all active sessions")

	try:
	    pargs = parser.parse_args()
	    print "*" + pargs 
	    if pargs.list:
		print "great success!"
	        #for session in self.srv.get_sessions_list():
	        #    print "{}".format(session.__str__)
	except MyParserException:
	    pass
