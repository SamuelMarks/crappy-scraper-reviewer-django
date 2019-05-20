# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django_review_app.apps.review.models import Review
from django_review_app.apps.review.seralizers import ReviewSerializer


@csrf_exempt
def review_list(request):
    """
    List all reviews, or create a new review.
    """
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def review_detail(request, pk):
    """
    Retrieve, update or delete a code Review.
    """
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        review.delete()
        return HttpResponse(status=204)
