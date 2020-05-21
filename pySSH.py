import paramiko
import os
# For settings
import configparser
# For command line argumends
import argparse
# test
defualtHostsPath = os.path.join(os.path.curdir,"hosts","hosts.txt") 

class Hosts:
    items = []
    def ScanHostFile(self,optionalHostPath = None):
        global defualtHostsPath
        config = configparser.ConfigParser()
        fileName = optionalHostPath if optionalHostPath != None else defualtHostsPath
        
        if os.path.exists(fileName):
            try:
                fileHandle = open(fileName)
            except:
                raise
            else:
                config.read_file(fileHandle)
                for entry in config:
                    if entry != "DEFAULT":
                        self.items.append({\
                         "ip" : config[entry]["ip"],\
                         "port" : config[entry]["port"],\
                         "password" : config[entry]["password"]})
                fileHandle.close()
    def __init__(self,optionalHostPath = None):
        self.ScanHostFile(optionalHostPath)
        
        

class Utility:
    #opened shells
    openedShells = []
    #hosts
    hosts = None
    def readShellList(self,path = None):
        self.hosts = Hosts()
    #def __init__(self):

def execFromConsole():
    utility = Utility()
    utility.readShellList()

execFromConsole()
