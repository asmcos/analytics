#
# RequestURI map
# header 
# form

import re
import urllib
from urllib.parse import urlparse


#urllib.parse.parse_qs(query)
#urlparse.urlparse

maplist = [
    {"rule":'^/$',"name":'首页'},
    {"rule":'^/zlj/index.html$',"name":'首页'},
    {"rule":'^/zlj/question.html$',"name":'提问'},
    {"rule":'^/zlj/listquestion',"name":'问题列表'},
]


def getmapregex():
    return []#AIDatas.getmap()

def handlerRequest(request):
    p = urlparse(request['RequestURI'])
    matchMap(p.path)

    query = urllib.parse.parse_qs(p.query)
    print("     path:",p.path)
    if len(query):
        print("     ",query)

def initmap ():
    global maplist
    ml = getmapregex()

def matchMap(path):
    for m in maplist:
        if re.search(m["rule"],path):
            print(m["name"],path)
