from abc import ABC, abstractmethod


class InvaildOperationsError(Exception):
    pass


class Stream(ABC):

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("mem stream")


def read(steam_type):
    for stream in steam_type:
        stream.read()


_file = FileStream()
network = NetworkStream()
memory = MemoryStream()

read([_file, network, memory])
