#
# the analytics main framework
# author:asmcos
# date: 2021.3.35
#
import AIDatas
import urlMap

API = AIDatas.AIDatas()


for req in API.getrequest(pagesize="100"):
    urlMap.handlerRequest(req)

