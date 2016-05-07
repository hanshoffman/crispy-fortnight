colors = {"red":"\033[0;31;40m", "green":"\033[0;32;40m", "yellow":"\033[0;33;40m", "gray":"\033[0;37;40m"}
color_stop = "\033[0m"

def error(msg):
    """ Return a formatted error line to stdout. """
    print "\n{}[!] {}{}".format(colors["red"], msg, color_stop)

def info(msg):
    """ Return a formatted info line to stdout. """
    print "\n{}[*] {}{}".format(colors["gray"], msg, color_stop)

def success(msg):
    """ Return a formatted success line to stdout. """
    print "\n{}[+] {}{}".format(colors["green"], msg, color_stop)

def warning(msg):
    """ Return a formatted warning line to stdout. """
    print "\n{}[-] {}{}".format(colors["yellow"], msg, color_stop)

def highlight(msg, color):
    """ Return a string in the given color. """
    print "{}{}{}".format(colors[color], msg, color_stop)
