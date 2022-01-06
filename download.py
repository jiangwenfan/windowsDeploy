import os 
import json 
import request
import threading

class Download():
    #class init
    def __init__(self):
        pass 
        
    appList = [] #
    #appList = [{'QQ':'https://down.qq.com/qqweb/PCQQ/PCQQ_EXE/PCQQ2021.exe'},{'微信':'https://dldir1.qq.com/weixin/Windows/WeChatSetup.exe'}]
    
    #read profile
    def readAllocation(self,fileName)
        self.fileName = fileName #profile name. eg:xxx.json yyy.xml
        suffix = fileName.split(".")[1]
        
        #read json profile 
        def readJson():
            pass 
        
        #read xml profile 
        def readXml():
            pass 
        
        #when file not exists,return message! 
        if(not os.path.exists(fileName)):
            return "profile not exists!"
            
        if(suffix == "json")
            readAllocation
        elif(suffix == "xml")
            readJson
        else:
            return "file type error!"
        
    #thread number depend on app number,and download 
    def download(self):
    
        #real download
        def downloadPackage(appName,appPath):
            binResponse = requests.get(url=appPath)
            with open(appName,'wb') as f:
                f.write(binResponse)
            
        #depend on app number set thread number.
        for i in range(len(appList)):
            appName = list(appList[i].keys())[0]+".exe"
            appPath = list(appList[i].values())[0]
            t = threading.Thread(target=downloadPackage,func=(appName,appPath))
            t.start()
        
        
    