# OSCRec
*A command line tool for audio recording using OSC for controls*

## Concept
The idea is to be able to use an arbitrary number of recording devices for network based multi track recording.
Say you have 3 small A/D interfaces and 3 Raspberry PIs.  You can then start recording on all 3 devices by sending a record
message over OSC.  Compine this with OSCWhispers, and you can have a phone send the OSC to record to Whispers, and have Whispers 
forward the record start on to each of the PIs.  This would then be able to record multiple tracks simultaniously, which could be useful
for a small band on a tight budget, where each band member has their own 2 in 2 out small A/D device.

Please note, this is experimental and very early in development at this stage.