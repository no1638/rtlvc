from pyo import *
import pyo
print(pyo.__file__)


menu = f'''
Real Time Voice Changer
-----------------------

1. L's Voice Changer
2. Spyglass

> '''



    







# Define s as a Pyo Server object, set the input device to microphone array and output to vb audio cable
s = Server()
devin = s.setInputDevice(1)
devout = s.setOutputDevice(6)
s.setBufferSize(128) 
s.boot()


# splitting the mic into 3 separate variables to allow me to edit 3 different audio streams separately, allowing me to 'layer' the edited audio
mic1 = Input().play()
mic2 = Input().play()
mic3 = Input().play()

# im not familiar enough with pyo to tell you what this means ;w;
env = WinTable(8)

###############
#  LOW PITCH  #
###############

wsize = .1
trans = -4

ratio = pow(2., trans/12.)
rate = -(ratio-1) / wsize

ind = Harmonizer(mic1, transpo=trans)
win = Pointer(table=env, index=ind, mul=1)

snd = Delay(ind, delay=0.02)

################################################

################
#  HIGH PITCH  #
################


wsize1 = .1
trans1 = 2

ratio1 = pow(2., trans1/12.)
rate1 = -(ratio1-1) / wsize1

ind1 = Harmonizer(mic2, transpo=trans1)
win1 = Pointer(table=env, index=ind1, mul=1)

snd1 = Delay(mic2, delay=ind1*wsize1, mul=win)

################################################

################
#  MED PITCH   #
################


wsize2 = .1
trans2 = 0

ratio2 = pow(2., trans2/12.)
rate2 = -(ratio2-1) / wsize2

ind2 = Harmonizer(mic3, transpo=trans2)
win2 = Pointer(table=env, index=ind2, mul=1)

snd2 = Delay(ind2, delay=0.01)

################################################


# snd.out()
# snd2.out()
# snd1.out()
snd.out()
ind1.out()
ind2.out()

ind.ctrl(title="Low End Pitch Control")
ind2.ctrl(title="Mid Range Pitch Control")
ind1.ctrl(title="High End Pitch Control")



# all this does is load the GUI window that pops up when you run the script
s.gui(locals())