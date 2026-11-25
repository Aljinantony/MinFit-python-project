from rest_framework import serializers
from gym_app.models import MemberDb,MembershipDb,PaymentDb


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemberDb
        fields = "__all__"
        read_only_fields = ['Joining_date']
class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = MembershipDb
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentDb
        fields = "__all__"
        read_only_fields = ['payment_date']