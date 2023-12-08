import msvcrt
import winreg
import winsound

class Windows:
    def __init__(self):
        self.msvcrt: object = msvcrt
        self.winreg: object = winreg
        self.winsound: object = winsound
