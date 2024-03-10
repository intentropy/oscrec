# OSCRec
*A command line tool for audio recording using OSC for controls*

## Concept
The idea is to be able to use an arbitrary number of recording devices for network based multi track recording.
Say you have 3 small A/D interfaces and 3 Raspberry PIs.  You can then start recording on all 3 devices by sending a record
message over OSC.  Compine this with OSCWhispers, and you can have a phone send the OSC to record to Whispers, and have Whispers 
forward the record start on to each of the PIs.  This would then be able to record multiple tracks simultaniously, which could be useful
for a small band on a tight budget, where each band member has their own 2 in 2 out small A/D device.

Please note, this is experimental and very early in development at this stage.

## Dependancies
* From pypi
    * JACK-Client >= 0.5.4
    * pyliblo >= 0.10.0
    * pyyaml >= 6.0.1
    * scipy 1.12.0
    * numpy 1.26.4


## Notes:
SciPy has a method for writting an WAV file

https://stackoverflow.com/questions/10357992/how-to-generate-audio-from-a-numpy-array
```
import numpy as np
from scipy.io.wavfile import write

rate = 44100
data = np.random.uniform(-1, 1, rate) # 1 second worth of random samples between -1 and 1
scaled = np.int16(data / np.max(np.abs(data)) * 32767)
write('test.wav', rate, scaled)
```

inport.array may be the data you are looking for for recording from the interface