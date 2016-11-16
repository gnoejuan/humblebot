import os.path
import json
import sys
class configReader(object):
    ##data = " "
    """Use this to read the config.txt. If you decide to get rid of the other languages, change
        filepath to os.path.abspath(os.path.join(basepath,"config.txt"))"""
    basepath = os.path.dirname(__file__)
    jsonFile = os.path.abspath(os.path.join(basepath,"..","config.json"))
    ##thanks /u/novel_yet_trivial
    with open(jsonFile, "r") as configFile:
        data = json.load(configFile)
    @classmethod
    def twitterUserName(cls):
        return this.data["twitter"]["username"]
    @classmethod
    def twitterDisplayName(cls):
        return str("@" + this.twitterUserName())
    @classmethod
    @classmethod
    @classmethod
    @classmethod
    @classmethod
    @classmethod
