import os.path
import json
import sys
class configReader(object):
    data = " "
    """Use this to read the config.txt. If you decide to get rid of the other languages, change
        __filepath to os.path.abspath(os.path.join(__basepath,"config.txt"))"""
    basepath = os.path.dirname(__file__)
    jsonFile = os.path.abspath(os.path.join(basepath,"..","config.json"))
    ##f = open(__filepath,"r")
    @classmethod
    def twitterUserName(this):
        with open(this.jsonFile,"r") as configFile:
            data = json.load(configFile)
        return str(data["twitter"]["username"])
    @classmethod
    def twitterDisplayName(this):
        return str("@" + this.twitterUserName())
    
