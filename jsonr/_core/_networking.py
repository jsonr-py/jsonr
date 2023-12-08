import asyncio
import socket
import ssl
import select
import selectors
import signal
import mmap

class Networking:
    def __init__(self):
        self.asyncio: object = asyncio
        self.socket: object = socket
        self.ssl: object = ssl
        self.select: object = select
        self.selectors: object = selectors
        self.signal: object = signal
        self.mmap: object = mmap
