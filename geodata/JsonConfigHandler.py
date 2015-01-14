__author__ = 'jmeline'

import json
import os
from collections import namedtuple


class JsonConfigHandler():
    def __init__(self):
        self.data = None
        self.extractedObject = None
        print("Current working directory: ", os.getcwd())
        self._extractJson()

    def _extractJson(self):
        f = None
        try:
            f = open(os.path.join(os.getcwd(), "geodata/config.json"))
        except:
            print ("Error, no Configuration was found")
            print(os.path.join(os.getcwd(), "config.json"))

        self.data = json.load(f)

        self.extractedObject = namedtuple('Config', self.data)(**self.data)






