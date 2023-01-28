import socket

class Client:
    def __init__(self, main_server_ip):
        self.main_server_ip = main_server_ip

    def run(self):
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the main server
        sock.connect((self.main_server_ip, 6969))
        print("Connected to main server")
        # Receive command from main server
        command = sock.recv(1024).decode()
        print("Received command: {}".format(command))

if __name__ == "__main__":
    client = Client("3.136.22.127")
    client.run()
