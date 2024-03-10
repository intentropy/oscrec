#!/usr/bin/env python3
"""OSCRec

Description:
    This is a simple wrapper for jack_capture, that created an Open Sound Control server to control the
    JACK transport while jack_capture is running.

    It will also rsync files to a destination after recording

    The only arg it takes is it's configuration file, written in yaml.
"""

from os     import system
from sys    import argv
from yaml   import safe_load

if __name__ == '__main__':
    # Load config from arg 1
    if len( argv ) != 2:
        exit(1)
    config_file = argv[ 1 ]
    with open( config_file ) as file:
        config = safe_load( file.read() )

    print( config )
