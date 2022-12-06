import sys

sys.path.insert(0, "../")
from utilities import success, get_input

packet = get_input(whole=True)

w = 4
for i in range(len(packet) - w):
    if len(set(packet[i:i+w])) == len(packet[i:i+w]):
        success(i+w)
