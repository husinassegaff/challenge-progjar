import select
import socket
import sys
import threading

# A default function for Prime checking conditions


def PrimeChecker(a):
    # Checking that given number is more than 1
    if a > 1:
        # Iterating over the given number with for loop
        for j in range(2, int(a/2) + 1):
            # If the given number is divisible or not
            if (a % j) == 0:
                return('T')
                break
        # Else it is a prime number
        else:
            return('Y')
    # If the given number is 1
    else:
        return('T')


class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(5)

    def run(self):
        self.open_socket()
        input = [self.server]
        running = 1
        while running:
            inputready, outputready, exceptready = select.select(input, [], [])

            for s in inputready:
                if s == self.server:
                    # handle the server socket
                    client_socket, client_address = self.server.accept()
                    c = Client(client_socket, client_address)
                    c.start()
                    self.threads.append(c)
                elif s == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = 0

         # close all threads
        self.server.close()
        for c in self.threads:
            c.join()


class Client(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024

    def run(self):
        running = 1
        while running:
            data = self.client.recv(self.size)
            # print ('recv: ' + str(self.address) + str(data))
            if data:
                Hasil = PrimeChecker(int(data))
                self.client.send(Hasil.encode())
            else:
                self.client.close()
                running = 0


if __name__ == "__main__":
    s = Server()
    s.run()
