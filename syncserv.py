import socket               # Import socket module
import time
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
#f = open('sync.txt','wb')
s.listen(5)                 # Now wait for client connection.
while True:
    while(1):
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        print "syncronising..."
   
        f = open('sync.txt','wb')
        l = c.recv(1024)
        while (l):
            print "syncronising..."
            f.write(l)
            l = c.recv(1024)
        f.close()
        print 'i m out'
        #a=raw_input("do u want to continue syncronising? y/n")
        #if(a=='n'):
        #    break
        c.send('y')
        #time.sleep(3)
        
f.close()
print "Done syncronising"
c.send('Thank you for connecting')
c.close()  
