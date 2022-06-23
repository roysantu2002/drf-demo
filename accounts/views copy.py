import datetime

from django.http import HttpResponse
from rest_framework.views import APIView


class Accounts(APIView):
    def get(self, request):
        now = datetime.datetime.now()
        html = "<html><body>Accounts View %s.</body></html>" % now
        return HttpResponse(html)
