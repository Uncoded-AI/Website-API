from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from docType import detect_class

class Article(APIView):
    def post(self, request, format=None):
        return Response({"catagory":detect_class(request.data['text'])})