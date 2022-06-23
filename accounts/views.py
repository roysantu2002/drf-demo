from rest_framework.response import Response

from rest_framework.decorators import api_view

@api_view(['GET'])
def getAccounts(request):
    person = {'name':'ABC', 'age':33}
    return Response(person)