import argparse
import cmd
import ConfigParser
import logging

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
								Version 1.0    "

class CrispyCLI(cmd.Cmd):
    """ Available commands on crispy server. """

    def __init__(self, srv, config_file="crispy.conf"):
	cmd.Cmd.__init__(self)
	self.config = ConfigParser.ConfigParser()
	self.config.read(config_file)
	if self.config.getboolean("CMDLINE", "display_banner"):
	    self.intro = BANNER
	else:
	    self.intro = ""
	self.prompt="{0}:{1}>> ".format(srv.server_address[0], srv.server_address[1])
	self.srv = srv

    def cmdloop(self, intro=None):	
	try:
	    cmd.Cmd.cmdloop(self, intro)
	except KeyboardInterrupt as e:
	    do_exit
	    #self.stdout.write('\n')
	    #self.cmdloop(intro="")

    def do_exit(self, args):
	""" Quit Crispy shell. """
	logger.debug("do_exit() was called")
	sys.exit()

    def do_help(self, args):
	""" Help menu. """
	logger.debug("do_help() was called")
	cmd.Cmd.do_help(self, args)

    def emptyline(self):
	""" Do nothing when an emptyline is entered. """
	pass

    def do_sessions(self, args):
	""" List/interact with established sessions. """
	logger.debug("do_sessions() was called")
	print "implement me"
    
    def do_run(self, args):
	""" Run a module on one or multiple clients. """
	logger.debug("do_run() was called")
	print "implement me"
