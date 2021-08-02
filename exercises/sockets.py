import socket

class ClientTCP:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_message(self, message):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        client.send(message)
        print( bytes.decode(client.recv(4096)) )

    @staticmethod
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


class ClientUDP:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_message(self, message):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(str.encode(message), (self.host, self.port))
        data, addr = bytes.decode(client.recvfrom(4096))
        print(data)

    @staticmethod
    def connect_udp_with():
        target_host = "127.0.0.1"
        target_port = 80
        # create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # send some data
        client.sendto(str.encode("AAABBBCCC"), (target_host, target_port))
        # receive some data
        data, addr = client.recvfrom(4096)
        print(data)


class ServerTCP:
    def __init__(self, bind_ip, port):
        self.bind_ip = bind_ip
        self.port = port

    def listen(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.bind_ip, self.port))
        server.listen(5)
        print(f"[*] Listening on {self.bind_ip}{self.port}")
        flag = str(input())
        while flag.lowercase != "c":
            client, addr = server.accept()
            print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
            #server.send("Server Message")
            print(bytes.decode(client.recv(4096)))

