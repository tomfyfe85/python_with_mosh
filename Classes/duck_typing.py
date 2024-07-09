class FileStream():
    def read(self):
        print("reading data from file")


class NetworkStream():
    def read(self):
        print("reading data from a network")


class MemoryStream():
    def read(self):
        print("mem stream")


def read(steam_type):
    for stream in steam_type:
        stream.read()


_file = FileStream()
network = NetworkStream()
memory = MemoryStream()

read([_file, network, memory])
