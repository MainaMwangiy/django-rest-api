from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''Test API View.'''

    def get(self, request, format=None):
        '''Returns a list of APIView features.'''

        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'It is similiar to a traditional Django views',
            'Gives you the most control over your logic',
            'It is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
