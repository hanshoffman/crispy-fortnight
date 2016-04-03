import argparse
import cmd
import ConfigParser
import getpass
import logging
import os
import shlex
import sys

from . myparser import *
from crispy import __version__
from crispy import __release_date__

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
									       \n \
		 [   crispy-fortnight %s-%s   ]" %(__version__, __release_date__)

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
	self.prompt="{}@crispy>> ".format(getpass.getuser())
	self.doc_header = "Available commands:"
	self.srv = srv

    @staticmethod
    def format_error(msg):
        """ Return a formatted error log line. """
        print "[!] {}\n".format(msg.rstrip())

    @staticmethod
    def format_info(msg):
        """ Return a formatted info log line. """
        print "[%] {}\n".format(msg.rstrip())

    @staticmethod
    def format_success(msg):
        """ Return a formatted success log line. """
        print "[+] {}\n".format(msg.rstrip())

    @staticmethod
    def format_warning(msg):
        """ Return a formatted warning log line. """
        print "[*] {}\n".format(msg.rstrip())
    
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

    def do_banner(self, args):
	""" Print banner. """
	print "{}".format(BANNER)
    
    def do_lcd(self, args):
	""" Change directory on daemon. """
	logger.debug("do_lcd() was called")
	self.format_error("implement me")

    def do_lpwd(self, args):
	""" Print current working directory on daemon. """
	logger.debug("do_lpwd() was called")
	print "{}".format(os.getcwd())

    def do_ls(self, args):
        """ Directory listing on daemon. """
        logger.debug("do_ls() was called")
	for f in os.listdir(os.getcwd()):
	    print "{}".format(f)

    def do_modules(self, args):
	""" List available modules. """
	logger.debug("do_modules() was called")
	print "\nAvailable modules:"
	print "==================="
	for mod in self.srv.iter_modules():
	    print "{}".format(mod)
	print ""

    def do_run(self, args):
        """ Run a module on one or multiple clients. """
        logger.debug("do_run() was called")
        self.format_error("implement me")

    def do_sessions(self, args):
	""" Active session manipulation and interaction. """
	logger.debug("do_sessions() was called")
	
	parser = CrispyArgumentParser(description=self.do_sessions.__doc__, prog="sessions")
	parser.add_argument("-i", "--interact",
                        dest="interact",
			help="interact with the selected session",
			metavar="<session_id>",
			type=int)
	parser.add_argument("-k", "--kill",
                        dest="kill",
                        help="kill the selected session",
                        metavar="<session_id>",
                        type=int)
	parser.add_argument("-l", "--list",
			action="store_true",
			dest="list",
                        help="list all active sessions")
	try:
	    pargs = parser.parse_args(shlex.split(args))
	    if pargs.interact:
		pass
	    elif pargs.kill:
		pass
	    elif pargs.list:
		print "\nActive sessions:"
        	print "==================="
	        for session in self.srv.get_sessions_list():
	            print "{}".format(session.__str__)
		#Id  Description    Tunnel
 		#--  -----------    ------
	except MyParserException as e:
	    print e
