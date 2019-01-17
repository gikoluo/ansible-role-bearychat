#!/usr/bin/python

import sys, getopt, logging
from bearychat import incoming

####
#bearychat.py -t "text" -c "channels" -m -n "Notification"
####

helpInfo = """
bearychat[.py] -t <text> -c <channels> -m
"""

team = "{{ team }}"
hook_key = "{{ hook_key }}"

def main(argv):
    text = ''
    channels = ""
    markdown = False
    notification = ''
    try:
        opts, args = getopt.getopt(argv,"hmt:c:n:",["test=", "channels=", "notification="])
    except getopt.GetoptError:
        print( helpInfo )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( helpInfo )
            sys.exit()
        elif opt == "-m":
            markdown = True
        elif opt in ("-t", "--text"):
            text = arg
        elif opt in ("-c", "--channels"):
            channels = arg
        elif opt in ("-n", "--notification"):
            notification = arg
    logging.debug('Send message to %s: %s / %s' % ( channels, text, notification))

    if text == '' or channels == '':
        print( helpInfo )
        sys.exit(2)

    arr_channels = channels.split(",")

    for c in arr_channels:
        data = {
            "text": text,
            "markdown": markdown,
            "notification": notification,
            "channel": c
        }
        logging.debug( data )
        resp = incoming.send(
            "https://hook.bearychat.com/%s/incoming/%s" % (team, hook_key),
            data)

        logging.debug(resp.status_code)
        logging.debug(resp.text)

        print( 'ok. sent.' )

if __name__ == "__main__":
   main(sys.argv[1:])