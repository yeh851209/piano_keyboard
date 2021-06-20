import tkinter as tk
import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")



root = tk.Tk()
root.title('piano')
root.geometry('1098x76')


WhiteKeyWidth = 20
WhiteKeyHeight = 70
BlackKeyWidth = 17
BlackKeyHeight = 45

def whitekey():
	w1 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w2 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w3 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w4 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w5 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w6 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w7 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w8 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w9 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w10 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w11 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w12 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w13 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w14 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w15 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w16 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w17 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w18 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w19 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w20 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w21 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w22 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w23 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w24 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w25 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w26 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w27 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w28 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w29 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w30 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w31 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w32 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w33 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w34 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w35 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w36 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w37 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w38 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w39 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w40 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w41 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w42 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w43 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w44 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w45 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w46 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w47 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w48 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w49 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w50 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w51 =tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w52 = tk.Frame(root, width = WhiteKeyWidth, height =WhiteKeyHeight, bg = 'white', relief='raised',bd='1')
	w1.place(x=0,y=0)
	w2.place(x=20,y=0)
	w3.place(x=40,y=0)
	w4.place(x=60,y=0)
	w5.place(x=80,y=0)
	w6.place(x=100,y=0)
	w7.place(x=120,y=0)
	w8.place(x=140,y=0)
	w9.place(x=160,y=0)
	w10.place(x=180,y=0)
	w11.place(x=200,y=0)
	w12.place(x=220,y=0)
	w13.place(x=240,y=0)
	w14.place(x=260,y=0)
	w15.place(x=280,y=0)
	w16.place(x=300,y=0)
	w17.place(x=320,y=0)
	w18.place(x=340,y=0)
	w19.place(x=360,y=0)
	w20.place(x=380,y=0)
	w21.place(x=400,y=0)
	w22.place(x=420,y=0)
	w23.place(x=440,y=0)
	w24.place(x=460,y=0)
	w25.place(x=480,y=0)
	w26.place(x=500,y=0)
	w27.place(x=520,y=0)
	w28.place(x=540,y=0)
	w29.place(x=560,y=0)
	w30.place(x=580,y=0)
	w31.place(x=600,y=0)
	w32.place(x=620,y=0)
	w33.place(x=640,y=0)
	w34.place(x=660,y=0)
	w35.place(x=680,y=0)
	w36.place(x=700,y=0)
	w37.place(x=720,y=0)
	w38.place(x=740,y=0)
	w39.place(x=760,y=0)
	w40.place(x=780,y=0)
	w41.place(x=800,y=0)
	w42.place(x=820,y=0)
	w43.place(x=840,y=0)
	w44.place(x=860,y=0)
	w45.place(x=880,y=0)
	w46.place(x=900,y=0)
	w47.place(x=920,y=0)
	w48.place(x=940,y=0)
	w49.place(x=960,y=0)
	w50.place(x=980,y=0)
	w51.place(x=1000,y=0)
	w52.place(x=1020,y=0)
def blackkey():
	b1 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b2 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b3 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b4 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b5 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b6 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b7 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b8 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b9 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b10 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b11 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b12 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b13 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b14 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b15 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b16 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b17 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b18 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b19 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b20 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b21 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b22 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b23 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b24 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b25 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b26 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b27 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b28 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b29 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b30 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b31 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b32 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b33 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b34 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b35 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b36 =tk.Frame(root, width = BlackKeyWidth, height =BlackKeyHeight, bg = 'black')
	b1.place(x=10,y=0)
	b2.place(x=50,y=0)
	b3.place(x=70,y=0)
	b4.place(x=110,y=0)
	b5.place(x=130,y=0)
	b6.place(x=150,y=0)
	b7.place(x=190,y=0)
	b8.place(x=210,y=0)
	b9.place(x=250,y=0)
	b10.place(x=270,y=0)
	b11.place(x=290,y=0)
	b12.place(x=330,y=0)
	b13.place(x=350,y=0)
	b14.place(x=390,y=0)
	b15.place(x=410,y=0)
	b16.place(x=430,y=0)
	b17.place(x=470,y=0)
	b18.place(x=490,y=0)
	b19.place(x=530,y=0)
	b20.place(x=550,y=0)
	b21.place(x=570,y=0)
	b22.place(x=610,y=0)
	b23.place(x=630,y=0)
	b24.place(x=670,y=0)
	b25.place(x=690,y=0)
	b26.place(x=710,y=0)
	b27.place(x=750,y=0)
	b28.place(x=770,y=0)
	b29.place(x=810,y=0)
	b30.place(x=830,y=0)
	b31.place(x=850,y=0)
	b32.place(x=890,y=0)
	b33.place(x=910,y=0)
	b34.place(x=950,y=0)
	b35.place(x=970,y=0)
	b36.place(x=990,y=0)


whitekey()
blackkey()






root.mainloop()