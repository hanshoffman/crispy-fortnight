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
		 [   crispy-fortnight %s-%s   ]\n" %(__version__, __release_date__)

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
	if self.config.getboolean("CMDLINE", "use_color"):
	    self.use_color = True
	else:
	    self.use_color = False
	self.colors = {"red":"\033[0;31;40m", "green":"\033[0;32;40m", "yellow":"\033[0;33;40m", "gray":"\033[0;37;40m"}
	self.color_stop = "\033[0m"
	self.prompt = "{}@crispy>> ".format(getpass.getuser())
	self.doc_header = "Available commands:"
	self.srv = srv

    def format_error(self, msg):
        """ Return a formatted error line to stdout. """
	if self.use_color:
	    print "{}[!] {}\n{}".format(self.colors["red"], msg.rstrip(), self.color_stop)
	else:
	    print "[!] {}\n".format(msg.rstrip())

    def format_info(self, msg):
        """ Return a formatted info line to stdout. """
        if self.use_color:
	    print "{}[%] {}\n{}".format(self.colors["gray"], msg.rstrip(), self.color_stop)
	else:
	    print "[%] {}\n".format(msg.rstrip())

    def format_success(self, msg):
        """ Return a formatted success line to stdout. """
        if self.use_color:
	    print "{}[+] {}\n{}".format(self.colors["green"], msg.rstrip(), self.color_stop)
	else:
	    print "[+] {}\n".format(msg.rstrip())

    def format_warning(self, msg):
        """ Return a formatted warning line to stdout. """
        if self.use_color:
	    print "{}[*] {}\n{}".format(self.colors["yellow"], msg.rstrip(), self.color_stop)
	else:
	    print "[*] {}\n".format(msg.rstrip())
    
    def do_exit(self, args):
	""" Shutdown crispy daemon. All sessions will be lost. """
	sys.exit()

    do_quit = do_exit

    def do_help(self, args):
	""" Help menu. """
	logger.debug("do_help() was called")
	cmd.Cmd.do_help(self, args)

    def emptyline(self):
	""" Do nothing when an emptyline is entered instead of repeat last command. """
	pass

    def do_banner(self, args):
	""" Print crispy banner. """
        logger.debug("do_banner() was called")
	parser = CrispyArgumentParser(description=self.do_banner.__doc__, prog="banner")

        try:
            pargs = parser.parse_args(shlex.split(args))
	    if pargs:
                print "{}".format(BANNER)
        except MyParserException as e:
            print e	
   	
    def do_lcd(self, args): 
	""" Change the cli working directory. """
	logger.debug("do_lcd() was called")
	parser = CrispyArgumentParser(description=self.do_lcd.__doc__, prog="lcd")
        parser.add_argument("dir", metavar="<DIR>", help="directory to change to")

	try:
            pargs = parser.parse_args(shlex.split(args))
	    if pargs is None:
		return
	    else:
	        if os.path.isdir(pargs.dir):
                    os.chdir(pargs.dir)
                    self.format_success("Changed directory to {}".format(pargs.dir))
                else:
		    self.format_error("Unknown directory")
        except MyParserException as e:
            print e

    def do_lpwd(self, args):
	""" Print current working directory on the crispy daemon. """
	logger.debug("do_lpwd() was called")
	parser = CrispyArgumentParser(description=self.do_lpwd.__doc__, prog="lpwd")
	
	try:
	    pargs = parser.parse_args(shlex.split(args))
	    if pargs:
	        print "{}\n".format(os.getcwd())
	except MyParserException as e:
            print e
	
    def do_ls(self, args):
        """ Directory listing on daemon. """
        logger.debug("do_ls() was called")
        parser = CrispyArgumentParser(description=self.do_ls.__doc__, prog="ls")

        try:
            pargs = parser.parse_args(shlex.split(args))
            if pargs:
		for f in os.listdir(os.getcwd()):
                    print "{}".format(f)
                print ""
        except MyParserException as e:
            print e

    def do_modules(self, args):
	""" List available modules. """
	logger.debug("do_modules() was called")
        parser = CrispyArgumentParser(description=self.do_modules.__doc__, prog="modules")

        try:
            pargs = parser.parse_args(shlex.split(args))
            if pargs:
                print "\nAvailable modules:\n==================="
        	for mod in self.srv.get_modules():
            	    print "{}".format(mod)
        	print ""
        except MyParserException as e:
            print e

    def do_run(self, args):
        """ Run a module on one or multiple clients. """
        logger.debug("do_run() was called")
	parser = CrispyArgumentParser(description=self.do_run.__doc__, prog="run")
	parser.add_argument("module", metavar="<module>", help="module name")
	parser.add_argument("arguments", nargs=argparse.REMAINDER, metavar="<arguments>", help="module arguments")

	try:
	    pargs = parser.parse_args(shlex.split(args))
	except MyParserException as e:
            print e

	selected_clients = "*"
	#targets = self.srv.get_clients(selected_clients) #change srv code to include both a get_clients() & get_clients_list()
	#targets.run_module(pargs.module, pargs.arguments)
	
	try:
	    mod = self.srv.get_module(pargs.module)
	except Exception as e:
	    self.format_error("Error loading \"%s\" module: %s" %(pargs.module, e)) 

    def do_sessions(self, args):
	""" Active session manipulation and interaction. """
	logger.debug("do_sessions() was called")
	parser = CrispyArgumentParser(description=self.do_sessions.__doc__, prog="sessions")
	parser.add_argument("-i", dest="interact", help="interact with the selected session", metavar="<session_id>", type=int)
	#parser.add_argument("-f", "--filter", dest="filter", metavar="<client_filter>", help="clients to run module on (default: *)")
	parser.add_argument("-k", dest="kill_id", help="kill the selected session", metavar="<session_id>", type=int)
	parser.add_argument("-l", action="store_true", dest="list", help="list all active sessions")
	
	try:
	    pargs = parser.parse_args(shlex.split(args))
	    if pargs is None:
		return
	    else:
		if isinstance(pargs.interact, int):
		    self.format_info("Interacting w/ session %s..." %pargs.interact)
	        elif isinstance(pargs.kill_id, int):
		    self.srv.remove_client_id(pargs.kill_id)
		    self.format_success("Killed session %s..." %pargs.kill_id)
		elif pargs.list:
		    print "\nActive sessions:\n==================="
	            for client in self.srv.get_clients():
	                print "{}".format(client.short_name())
	                #print "{}".format(client) #long print
		    print ""
		else:
		    parser.print_help()
	except MyParserException as e:
	    print e
