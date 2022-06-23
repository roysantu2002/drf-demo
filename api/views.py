import datetime

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def login(request):
     person = {'name':'ABC', 'age':33}
     return Response(person)
    # now = datetime.datetime.now()
    # html = "<html><body>Login View %s.</body></html>" % now
    # return HttpResponse(html)
