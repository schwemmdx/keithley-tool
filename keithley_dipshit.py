from time import sleep
NOTE_C =0
NOTE_CS= 1
NOTE_D =2
NOTE_DS =3
NOTE_E =4
NOTE_F =5
NOTE_FS= 6
NOTE_G =7
NOTE_GS= 8
NOTE_A =9
NOTE_AS =10
NOTE_B = 11

notes= [
	[ 33, 35, 37, 39, 41, 44, 46, 49, 52, 55, 58, 62 ],
	[ 65, 69, 73, 78, 82, 87, 92, 98, 104, 110, 117, 123 ],
	[ 131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247 ],
	[ 262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494 ],
	[ 523, 554, 587, 622, 659, 698, 740, 784, 831, 880, 932, 988 ],
	[ 1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976 ],
	[ 2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951 ],
	[ 4186, 4435, 4699, 4978, 5274, 5588, 5920, 6272, 6645, 7040, 7459, 7902 ]
]



def playNote( k2636,octave,note, duration):
    k2636.beep(duration,notes[octave][note])



def noteDoomBase(k2636,octave,speed):

	playNote(k2636,octave - 1, NOTE_E,speed/2)
	playNote(k2636,octave - 1, NOTE_E,speed/2)


def theme(k2636):
    octave = 3
    dur = 0.15
    
    playNote(k2636,2,NOTE_E,dur)
    playNote(k2636,2,NOTE_E,dur)
    playNote(k2636,3,NOTE_E,dur)
    playNote(k2636,2,NOTE_E,dur)
    playNote(k2636,2,NOTE_E,dur)
    playNote(k2636,3,NOTE_D,dur)
    playNote(k2636,2,NOTE_E,dur)
    playNote(k2636,2,NOTE_E,dur)
    playNote(k2636,3,NOTE_C,dur)
    playNote(k2636,2,NOTE_E,dur)
    playNote(k2636,2,NOTE_E,dur)
    playNote(k2636,2,NOTE_B,dur)
    playNote(k2636,2,NOTE_C,dur)
    playNote(k2636,2,NOTE_E,dur)


def finalCountdown(k):
    dur =  0.25
    playNote(k,3,NOTE_CS,dur)
    playNote(k,3,NOTE_B,dur)
    playNote(k,3,NOTE_CS,dur)
    playNote(k,3,NOTE_FS,dur)
    playNote(k,3,NOTE_D,dur)
    playNote(k,3,NOTE_CS,dur)
    playNote(k,3,NOTE_D,dur)
    playNote(k,3,NOTE_CS,dur)
    playNote(k,3,NOTE_B,dur)
