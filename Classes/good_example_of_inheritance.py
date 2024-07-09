from abc import ABC, abstractmethod


class InvaildOperationsError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvaildOperationsError("Stream is open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvaildOperationsError("Stream is already closed")
        self.opened = False

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


# MAKE STREAM CLASS AN ABSTRACT BASE CLASS

stream = MemoryStream()
stream.open()
stream.open()
