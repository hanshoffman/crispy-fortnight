import argparse
import cmd
import ConfigParser
import fprint
import getpass
import logging
import os
import shlex
import subprocess
import sys

from crispy import __release_date__
from crispy import __version__
from .. modules import *
from . myparser import *

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
	self.prompt = "{}@crispy>> ".format(getpass.getuser())
	self.doc_header = "Available commands:"
	self.srv = srv

    def do_clear(self, args):
        """ Clear the screen. """
        subprocess.call(['clear'])    

    def do_exit(self, args):
	""" Shutdown crispy daemon. All sessions will be lost. """
        self.srv.shutdown()
	sys.exit()

    do_quit = do_exit

    def do_help(self, args):
	""" Help menu. """
	logger.debug("do_help() was called")
	cmd.Cmd.do_help(self, args)

    def emptyline(self):
	""" Do nothing when an emptyline is entered instead of repeat last command. """
	pass

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
                    fprint.success("Changed directory to {}".format(pargs.dir))
                else:
		    fprint.error("Unknown directory")
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
                print "\nDirectory listing:\n==================="
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
	parser.add_argument("session_id", metavar="<session id>", help="session to run on")
	parser.add_argument("arguments", nargs=argparse.REMAINDER, metavar="<arguments>", help="module arguments")

	try:
	    pargs = parser.parse_args(shlex.split(args))
	except MyParserException as e:
            print e
	    return

        try:
            target = self.srv.get_client(int(pargs.session_id))
        except:
            fprint.error("Improper session id.")
            return
	
        try:
	    mod =  self.srv.get_module(pargs.module, target) 
	except Exception as me:
	    fprint.error("Error loading \"{}\" module: {}".format(pargs.module, me))
            return
	
        args = "" if not pargs.arguments else pargs.arguments
    
        if not mod.check_args(args):
            return

        try:
	    target.run_module(mod, args) 
        except Exception as e:
            fprint.error(e)

    def do_sessions(self, args):
	""" Active session manipulation and interaction. """
	logger.debug("do_sessions() was called")
	parser = CrispyArgumentParser(description=self.do_sessions.__doc__, prog="sessions")
	parser.add_argument("-i", dest="interact", help="pop a shell on the given session", metavar="<session_id>", type=int)
	parser.add_argument("-k", dest="kill_id", help="kill the selected session", metavar="<session_id>", type=int)
	parser.add_argument("-K", action="store_true", dest="kill_all", help="kill all connected sessions")
	parser.add_argument("-l", action="store_true", dest="list", help="list all active sessions")
	
	try:
	    pargs = parser.parse_args(shlex.split(args))
	    if pargs is None:
		return
	    else:
		if isinstance(pargs.interact, int):
		    fprint.error("Not implemented yet")
		    #fprint.info("Interacting w/ session %s..." %pargs.interact)
	        elif isinstance(pargs.kill_id, int):
		    self.srv.remove_client(self.srv.get_client(int(pargs.kill_id)).get_session())
		    fprint.success("Killed session %s..." %pargs.kill_id)
                elif pargs.kill_all:
                    self.srv.remove_all()
                    fprint.success("All sessions killed.")
		elif pargs.list:
		    print "\nActive sessions:\n==================="
	            for client in self.srv.get_client_list():
	                print "{}".format(client.short_name())
		    print ""
		else:
		    parser.print_help()
	except MyParserException as e:
	    print e
