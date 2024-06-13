import socket
import time

SINGLE_TELLO_IP = "192.168.10.1"
COMMAND_PORT: int = 8889

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Send command")
s.sendto(b"command", (SINGLE_TELLO_IP, COMMAND_PORT))
# time.sleep(2.)

print("Send takeoff")
s.sendto(b"takeoff", (SINGLE_TELLO_IP, COMMAND_PORT))
# time.sleep(2.)

data = s.recv(1024)
print(f"Receive: {data}")

print("Send move forward")
s.sendto(b"forward 50", (SINGLE_TELLO_IP, COMMAND_PORT))
# time.sleep(2.)

data = s.recv(1024)
print(f"Receive: {data}")

print("Send land")
s.sendto(b"land", (SINGLE_TELLO_IP, COMMAND_PORT))
# time.sleep(2.)

data = s.recv(1024)
print(f"Receive: {data}")
