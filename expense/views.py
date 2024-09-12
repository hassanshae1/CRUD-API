from django.shortcuts import render
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from expense import serializers

@api_view()
def get_transaction(request):
    queryset = Transaction.objects.all().order_by('-pk')
    serializer = TransactionSerializer(queryset, many = True)
    return Response({
        "data" : serializer.data
    })

class TransactionAPI(APIView):
    def get(self, request):
        queryset = Transaction.objects.all().order_by('-pk')
        serializer = TransactionSerializer(queryset, many = True)
        return Response({
        "data" : serializer.data
    })

    
    def post(self, request):
        data = request.data
        serializer = TransactionSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                "message" : "data not saved",
                "errors" : serializer.errors,
            })
        serializer.save()
        return Response({
            "message" : "data saved",
            "data" : serializer.data

        })
    
    def put(self, request):
        return Response({
            "message" : "This is a PUT Method"
        })
    
    # Other methods (get, post, etc.)...

    def patch(self, request):
        data = request.data

        # Check if 'id' is provided in the request
        if not data.get('id'):
            return Response({
                "message": "data not updated",
                "errors": "id is required",
            }, status=400)

        # Try to get the Transaction object by id
        try:
            transaction = Transaction.objects.get(id=data.get('id'))
        except Transaction.DoesNotExist:
            return Response({
                "message": "data not updated",
                "errors": "Transaction with this id does not exist",
            }, status=404)

        # Serialize the data (partial update)
        serializer = TransactionSerializer(transaction, data=data, partial=True)

        # Check if the data is valid
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors,
            }, status=400)

        # Save the changes
        serializer.save()
        return Response({
            "message": "data saved",
            "data": serializer.data
        })

    
