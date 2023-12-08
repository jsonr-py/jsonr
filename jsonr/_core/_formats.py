import cv2
import configparser
import tomllib
import netrc
import plistlib

class FileFormats:
    def __init__(self):
        self.cv2: object = cv2
        self.configparser: object = configparser
        self.tomllib: object = tomllib
        self.netrc: object = netrc
        self.plistlib: object = plistlib
