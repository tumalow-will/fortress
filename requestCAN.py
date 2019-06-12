"""Connect to CANable; print and echo any received frames"""
from canard import can
from canard.hw import cantact
import time

dev = cantact.CantactDev("/dev/ttyACM1") # Connect to CANable on this /dev/ttyACM#
dev.set_bitrate(500000) # Set the bitrate to a 0.5Mb/s
dev.start() # Go on the bus
count = 0
dev_id = 0x1871

while True:
    count += 1
    frame = can.Frame(dev_id, dlc=8, data = [0x00]*8, is_extended_id=True)
    dev.send(frame) # Echo the CAN frame back out on the bus
    print(str(frame))
    time.sleep(1)
