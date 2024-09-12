from rest_framework import serializers
from .models import Transaction
from expense import models


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            "title",
            "amount",
            "transaction_type",
        ]
