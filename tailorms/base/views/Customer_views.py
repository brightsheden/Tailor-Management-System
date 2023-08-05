from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from rest_framework import status

from django.contrib.auth.models import User
from datetime import date, datetime
from base.serializer import *


@api_view(['GET'])
@permission_classes([isAuthenticated])
def getCustomer(request):
    user = request.user.profile
    customer = Customer.objects.get(profile=user)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)

def getCustomerWorks(request):
    user = request.user.profile
    customer = Customer.objects.get(profile=user)
    works = customer.work_set.all().order_by('-createdAt')
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)