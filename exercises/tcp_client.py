# Source: Black Hat Python - Python Programming for Hackers and Pentesters
import socket


def connect_tcp_with(target, port):
    target_host = target
    target_port = port
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the client
    client.connect((target_host, target_port))
    # send some data
    client.send(str.encode("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"))
    # receive some data
    return bytes.decode(client.recv(4096))
