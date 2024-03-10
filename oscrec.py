#!/usr/bin/env python3
"""OSCRec"""

from jack   import Client

from time   import sleep

def test_hold():
    while True:
        sleep( 1 )

if __name__ == '__main__':
    # Create client
    _client_name = "OSCRec"
    with Client( _client_name ) as client:

        server_data = {
            "blocksize": client.blocksize,
            "frame_time": client.frame_time,
            "sample_rate": client.samplerate,
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

        print( outports , inports )        
        test_hold()