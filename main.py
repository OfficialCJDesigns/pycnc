import socket

class Server:
    def __init__(self):
        self.servers = []

    def run(self):
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to a specific address and port
        sock.bind(("0.0.0.0", 6969))
        # Start listening for incoming connections
        sock.listen(5)

        while True:
            # Accept incoming connections
            (client, (ip, port)) = sock.accept()
            # Add the connected server to the list
            self.servers.append((client, ip, port))
            print("Connected to server at {}:{}".format(ip, port))
            print("Number of servers connected: {}".format(len(self.servers)))
            # Send command to connected server
            client.send("run command".encode())

if __name__ == "__main__":
    server = Server()
    server.run()
