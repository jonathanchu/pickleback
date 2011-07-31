from django.http import HttpResponse
from django.utils import simplejson as json
import xmlrpclib

def pypi(request):
    uri = 'http://pypi.python.org/pypi'
    server = xmlrpclib.Server(uri)
    if request.method == 'GET':
        query = request.GET.get('q', None)
        if query:
            res = server.search({'name': query})
            json_encoding = json.dumps(res, ensure_ascii=False, indent=2).strip()
            return HttpResponse(json_encoding, 
                                mimetype="application/json; charset=utf8")
    return HttpResponse(mimetype="application/json")
    
    
