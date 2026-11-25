from rest_framework.views import APIView
from rest_framework.response import Response

from gym_app.models import MemberDb,MembershipDb,PaymentDb
from gym_app.serializers import MemberSerializer,MembershipSerializer,PaymentSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q


class MemberCreateListView(APIView):

    def get(self, request):
        members = MemberDb.objects.all()
        serializer_instance = MemberSerializer(members, many=True)

        return Response(serializer_instance.data, status=200)

    def post(self, request):
        form_data = request.data
        serializer_instance = MemberSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response({
                "message": "Member added successfully",
                "Member Details": serializer_instance.data
            }, status=201)

        return Response(serializer_instance.errors, status=400)
class MemberDetailView(APIView):

    def get(self, request, id):
        member = get_object_or_404(MemberDb, id=id)
        serializer_instance = MemberSerializer(member)

        return Response(serializer_instance.data, status=200)

    def put(self, request, id):
        member = get_object_or_404(MemberDb, id=id)

        serializer_instance = MemberSerializer(
            member,
            data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response({
                "message": "Member updated successfully",
                "Member Details": serializer_instance.data
            }, status=200)

        return Response(serializer_instance.errors, status=400)

    def delete(self, request, id):
        member = get_object_or_404(MemberDb, id=id)
        member.delete()

        return Response({
            "message": "Member deleted successfully"
        }, status=200)

class MemberDetailView(APIView):

    def get(self, request, id):
        member = get_object_or_404(MemberDb, id=id)
        serializer_instance = MemberSerializer(member)

        return Response(serializer_instance.data, status=200)

    def put(self, request, id):
        member = get_object_or_404(MemberDb, id=id)

        serializer_instance = MemberSerializer(
            member,
            data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response({
                "message": "Member updated successfully",
                "data": serializer_instance.data
            }, status=200)

        return Response(serializer_instance.errors, status=400)

    def delete(self, request, id):
        member = get_object_or_404(MemberDb, id=id)
        member.delete()

        return Response({
            "message": "Member deleted successfully"
        }, status=200)
class MemberSearchView(APIView):

    def get(self, request):
        search_query = request.query_params.get('search')

        if not search_query:
            return Response(
                {"message": "Please enter a name or phone number"},
                status=400
            )

        members = MemberDb.objects.filter(
            Q(name__icontains=search_query) |
            Q(phone__icontains=search_query)
        )

        serializer_instance = MemberSerializer(members, many=True)

        return Response(serializer_instance.data, status=200)

class MembershipCreateListView(APIView):

    def get(self, request):
        memberships = MembershipDb.objects.all()
        serializer_instance = MembershipSerializer(memberships, many=True)
        return Response(serializer_instance.data, status=200)

    def post(self, request):
        serializer_instance = MembershipSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({
                "message": "Membership added successfully",
                "data": serializer_instance.data
            }, status=201)

        return Response(serializer_instance.errors, status=400)

class MembershipDetailView(APIView):

    def get(self, request, id):
        membership = get_object_or_404(MembershipDb, id=id)
        serializer_instance = MembershipSerializer(membership)
        return Response(serializer_instance.data, status=200)

    def put(self, request, id):
        membership = get_object_or_404(MembershipDb, id=id)
        serializer_instance = MembershipSerializer(
            membership, data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({
                "message": "Membership updated successfully",
                "data": serializer_instance.data
            }, status=200)

        return Response(serializer_instance.errors, status=400)

    def delete(self, request, id):
        membership = get_object_or_404(MembershipDb, id=id)
        membership.delete()

        return Response({
            "message": "Membership deleted successfully"
        }, status=200)

class PaymentCreateListView(APIView):

    def get(self, request):
        payments = PaymentDb.objects.all()
        serializer_instance = PaymentSerializer(payments, many=True)
        return Response(serializer_instance.data, status=200)

    def post(self, request):
        serializer_instance = PaymentSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response({
                "message": "Payment added successfully",
                "data": serializer_instance.data
            }, status=201)

        return Response(serializer_instance.errors, status=400)

class PaymentDetailView(APIView):

    def get(self, request, id):
        payment = get_object_or_404(PaymentDb, id=id)
        serializer_instance = PaymentSerializer(payment)
        return Response(serializer_instance.data, status=200)

    def put(self, request, id):
        payment = get_object_or_404(PaymentDb, id=id)

        serializer_instance = PaymentSerializer(
            payment, data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()

            return Response({
                "message": "Payment updated successfully",
                "data": serializer_instance.data
            }, status=200)

        return Response(serializer_instance.errors, status=400)

    def delete(self, request, id):
        payment = get_object_or_404(PaymentDb, id=id)
        payment.delete()

        return Response({
            "message": "Payment deleted successfully"
        }, status=200)

class DashboardView(APIView):

    def get(self, request):

        total_members = MemberDb.objects.count()

        active_members = MembershipDb.objects.filter(
            status='Active'
        ).count()

        expired_memberships = MembershipDb.objects.filter(
            status='Expired'
        ).count()

        total_payments = PaymentDb.objects.count()

        return Response({
            "total_members": total_members,
            "active_members": active_members,
            "expired_memberships": expired_memberships,
            "total_payments": total_payments
        }, status=200)