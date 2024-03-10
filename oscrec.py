#!/usr/bin/env python3
"""OSCRec"""

from jack   import Client
from yaml   import safe_dump
from time   import sleep
from scipy.io.wavfile   import write
from numpy              import (
    append, ndarray,
    int16,  int32,
    )

def test_hold():
    while True:
        sleep( 1 )

def print_inport_stream( inports , samplerate ):
    """This is a test function to print out the array per frame from inports"""
    while True:
        for name , inport in inports.items():
            if "1" in name:
                print( type( inport.get_array() ) )
        exit()
        sleep( 100000/ samplerate )
              
def test_rec( inports , samplerate ):
    """Test record and save foo.wav"""
    _array_data = ndarray( [] )
    for x in range( int( samplerate /10 ) ):
        for name , inport in inports.items():
            if "1" in name:
                #print( x / samplerate )
                _array_data = append( _array_data , inport.get_array() )
    write( "foobar.wav" , samplerate , _array_data )
    




if __name__ == '__main__':
    # Create client
    _client_name = "OSCRec"
    with Client( _client_name ) as client:

        client_data = {
            "blocksize": client.blocksize,
            "sample_rate": client.samplerate,
            "uuid":  client.uuid,
            }

        # Get all interface recording inputs (out ports)
        outports = {}
        for port in client.get_ports():
            if port.is_output:
                if "system" in port.name:
                    outports.update( {port.name: port} )

        # Create input (in port) for each outport.
        inports = {}
        for outport_name , outport  in outports.items():
            _inport_name = f"inport_for_{outport.name}"
            inports.update( 
                { _inport_name: client.inports.register( _inport_name ) }
                )

        # Connect system outport into client inport 
        for inport_name , inport in inports.items():
            for outport_name , outport in outports.items():
                print( inport_name , outport_name )
                if inport_name.endswith( outport_name ):
                    client.connect( outport , inport )

        print( safe_dump( client_data ) )
        print( outports )
        print( inports )
        #test_hold()
        #print_inport_stream( inports=inports , samplerate = client.samplerate )
        test_rec( inports=inports , samplerate = client.samplerate )