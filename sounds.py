import numpy as N
import wave

def get_signal_data(frequency=100, duration=1, volume=32768, samplerate=44100):
    """Outputs a numpy array of intensities"""
    samples = duration * samplerate
    period = samplerate / float(frequency)
    omega = N.pi * 2 / period
    t = N.arange(samples, dtype=N.float)
    y = volume * N.sin(t * omega)
    return y

def numpy2string(y):
    """Expects a numpy vector of numbers, outputs a string"""
    signal = "".join((wave.struct.pack('h', item) for item in y))
    # this formats data for wave library, 'h' means data are formatted
    # as short ints
    return signal

class SoundFile:
    def  __init__(self, signal, filename, duration=1, samplerate=44100):
        self.file = wave.open(filename, 'wb')
        self.signal = signal
        self.sr = samplerate
        self.duration = duration
  
    def write(self):
        self.file.setparams((1, 2, self.sr, self.sr*self.duration, 'NONE', 'noncompressed'))
        # setparams takes a tuple of:
        # nchannels, sampwidth, framerate, nframes, comptype, compname
        self.file.writeframes(self.signal)
        self.file.close()

if __name__ == '__main__':
    duration = 2
    myfilename = 'test.wav'
    data = get_signal_data(1000, duration)
    signal = numpy2string(data)
    f = SoundFile(signal, myfilename, duration)
    f.write()
    print 'file written'

#part a
#All of the sounds made sense. I compared the sounds from this program to an actual piano.
#While the piano was not the exact frequency it was a good refrence point to compare to.
#After the first 5 frequencies I was able to predict what the next sound would be.
#As I raised the frequecy the sound seemed to be getting louder even though I 
#did not increase the sound on my computer
#






