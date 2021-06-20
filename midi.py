import time
import rtmidi as midi

midiin = midi.MidiIn()
midiout = midi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

#with midiout:
    # channel 1, middle C, velocity 112
#    note_on = [0x90, 70, 112]
#    note_off = [0x80, 70, 0]
#    midiout.send_message(note_on)
#    time.sleep(0.6)
 #   midiout.send_message(note_off)
#    time.sleep(0.1)

print(midiin.get_ports())
midiin.set_callback()

del midiout