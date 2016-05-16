from _socket import gethostname
#if you are running both server and client on same computer then don't change anything
hostname=gethostname() #'server IPaddress here'
#if you have different computers for server and client then make sure that both computer must connect to same network
# comment the above value of hostname and find out the ipaddress of the server by typing 'ipconfig' in cmd of the server
#the look out for ipaddress and change the value of hostname from gethostname() to server ipaddress and put it in single quotes 
