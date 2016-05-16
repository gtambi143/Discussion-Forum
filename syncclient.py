import socket               # Import socket module
import time
#s = socket.socket()         # Create a socket object
                # Reserve a port for your service.

#s.connect((host, port))
#s.send("Hello server!")
f = open('sync1.txt','rb')
print 'syncronising...'
l = f.read(1024)
while(1):
    s = socket.socket()
    host = socket.gethostname() # Get local machine name
    port = 12345 
    s.connect((host,port))
    while (l):
        print 'Syncronising...'
        s.send(l)
        l = f.read(1024)
    f.close()
    print "Done Syncronising"
    f = open('sync1.txt','rb')
    l = f.read(1024)
    s.shutdown(socket.SHUT_WR)
    print s.recv(1024)
    s.close()
    time.sleep(10)
