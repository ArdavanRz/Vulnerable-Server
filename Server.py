# first of all import the socket library
import socket
import os
import platform
# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

#initialzing system info with uname that contains a limited amount of info
sysinfo = platform.uname()



# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    command = c.recv(1024).decode()
    if(command == "sys") :
        print("command accepted")
        c.send("accepted".encode())

        c.send(sysinfo.system.encode())
        c.send(sysinfo.node.encode())
        c.send(sysinfo.release.encode())
        c.send(sysinfo.version.encode())
        c.send(sysinfo.machine.encode())
        c.send(sysinfo.processor.encode())

        # Close the connection with the client

    if(command == "exit") :
        c.close()
        break



    # Breaking once connection closed


