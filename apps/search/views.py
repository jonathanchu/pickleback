from django.http import HttpResponse
from django.utils import simplejson as json
import xmlrpclib

def pypi_search(request):
    uri = 'http://pypi.python.org/pypi'
    server = xmlrpclib.Server(uri)
    if request.method == 'GET':
        query = request.GET.get('q', None)
        if query:
            res = server.search({'name': query})
            return HttpResponse(json.dumps(res), mimetype="application/json")
    return HttpResponse(mimetype="application/json")
    
    
