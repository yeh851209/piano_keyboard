
from __future__ import print_function

import logging
import sys
import rtmidi
import time

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

from rtmidi.midiutil import open_midiinput

#log = logging.getLogger('midiin_callback')
#logging.basicConfig(level=logging.DEBUG)
note_dic={21:'w1',22:'b1',23:'w2',24:'w3',25:'b2',26:'w4',27:'b3',28:'w5',
29:'w6',30:'b4',31:'w7',32:'b5',33:'w8',34:'b6',35:'w9',36:'w10',37:'b7',
38:'w11',39:'b8',40:'w12',41:'w13',42:'b9',43:'w14',44:'b10',45:'w15',46:'b11',
47:'w16',48:'w17',49:'b12',50:'w18',51:'b13',52:'w19',53:'w20',54:'b14',
55:'w21',56:'b15',57:'w22',58:'b16',59:'w23',60:'w24',61:'b17',62:'w25',
63:'b18',64:'w26',65:'w27',66:'b19',67:'w28',68:'b20',69:'w29',70:'b21',71:'w30',
72:'w31',73:'b22',74:'w32',75:'b23',76:'w33',77:'w34',78:'b24',
79:'w35',80:'b25',81:'w36',82:'b26',83:'w37',
84:'w38',85:'b27',86:'w39',87:'b28',88:'w40',89:'w41',90:'b29',
91:'w42',92:'b30',93:'w43',94:'b31',95:'w44'
96:'w45',97:'b32',98:'w46',99:'b33',100:'w47',101:'w48',102:'b34',
103:'w49',104:'b35',105:'w50',106:'b36',107:'w51',108:'w52'
}


class MidiInputHandler(object):
    def __init__(self, port,midiout):
        self.port = port
        self.midiout = midiout

    def __call__(self, event, data=None):
        message, deltatime = event
        self.midiout.send_message(message)
        #self._wallclock += deltatime
        on = message[0]
        note = message[1]
        strenth = message[2]
        print(note)
        #print(note_dic[note])


# Prompts user for MIDI input port, unless a valid port number or name
# is given as the first argument on the command line.
# API backend defaults to ALSA on Linux.
port = sys.argv[1] if len(sys.argv) > 1 else None

try:
    midiin, port_name = open_midiinput(port)
except (EOFError, KeyboardInterrupt):
    sys.exit()

print("Attaching MIDI input callback handler.")
midiin.set_callback(MidiInputHandler(port_name,midiout))

print("Entering main loop. Press Control-C to exit.")
try:
    # Just wait for keyboard interrupt,
    # everything else is handled via the input callback.
    while True:
        #time.sleep(2)

        continue
except KeyboardInterrupt:
    print('1')
finally:
    print("Exit.")
    midiin.close_port()
    del midiin
    del midiout
