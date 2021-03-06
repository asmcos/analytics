# AIDatas api interface

import requests


serverurl="http://www.zhanluejia.net.cn:8080"
serverurl="http://127.0.0.1:1337"

class AIDatas:
    
    def __init__(self,url=serverurl):
        self.url = url
 
    def getrequest(self,offset="0",pagesize="10"):
        return requests.get(self.url+"/requests?_start="+offset+"&_limit="+pagesize+"&_sort=id:DESC").json() 

    def getmap(self,offset="0",pagesize="1000"):
        return requests.get(self.url+"/maps?_start="+offset+"&_limit="+pagesize+"&_sort=id:DESC").json() 



