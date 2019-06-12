from canard import can
from canard.hw import cantact

dev = cantact.CantactDev("/dev/ttyACM0") # Connect to CANable that enumerated as ttyACM0
dev.set_bitrate(500000) # Set the bitrate to a 0.5 Mb/s
dev.start() # Go on the bus
count = 0

while True:
    count += 1
    frame = dev.recv() # Receive a CAN frame
    print(str(count) + ": " + str(frame)) # Print out the received frame
