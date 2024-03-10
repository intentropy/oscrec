#!/usr/bin/env python3
"""OSCRec

Description:
    This is a simple wrapper for jack_capture, that created an Open Sound Control server to control the
    JACK transport while jack_capture is running.

    It will also rsync files to a destination after recording

    The only arg it takes is it's configuration file, written in yaml.

Notes:
    Make methods to run outside of with
"""

from os     import system
from sys    import argv
from yaml   import safe_load
from liblo  import ServerThread
from jack   import Client

class OSCRec( ServerThread , Client ):
    def __init__( self , listen_port ):
        super().init( listen_port )
        self.jack_client = jack_client
        """NOTE:
            Any message to the path should be fine"""
        # Start jack transport and record
        self.add_method( "oscrec/start" , None , self.start )
        # Stop jack transport, then export recordings
        self.add_method( "oscrec/stop" , None , self.stop )
        # Shut everything down
        self.add_method( "oscrec/exit" , None , self.exit )

    def __enter__( self ):
        """Start the liblo server, and thread a jack_capture per system outport"""
        # Start liblo server
        self.start()

        # Start jack captures
        self.outports = {}
        for outport in self.get_ports():
            if outport.is_output:
                self.outports.update( { outport.name , outport } )
        

    def __exit__( self , *exc ):
        """Terminate the threaded jack captures and shutdown liblo server"""
        # Stop jack captures

        # Stop liblo server
        self.stop()
        self.free()


    def start( self , *args , **kwargs):
        """Start jack transport"""
        pass

    def stop( self , *args , **kwargs ):
        """Stop jack transport"""
        pass




if __name__ == '__main__':
    # Load config from arg 1
    if len( argv ) != 2:
        exit(1)
    config_file = argv[ 1 ]
    with open( config_file ) as file:
        config = safe_load( file.read() )

    liblo_port = config.get( "liblo" , {} ).get( "port" , 9000 )

    with OSCRec( liblo_port ) as oscrec:
        while True:
            sleep( 1 )