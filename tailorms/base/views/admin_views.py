from rest_framework.decorators import api_view, permission_classes, parser_classes,APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from rest_framework import status

from django.contrib.auth.models import User
from datetime import date, datetime
from base.serializer import *

@api_view(['GET'])
def getFashionsCompany(request):
    companies = FashionCompany.objects.all()
    serializer = FashionCompanySerializer(companies,many=True)
    return Response(serializer.data)



class FashionCompanyApi(APIView ):
   # parser_classess = (MultiPartParser, FormParser)
    permission_classes = ([IsAdminUser])
    #get all fashion company
    def get(self,request, *args, **kwargs):
        
        companies = FashionCompany.objects.all()
        serializer = FashionCompanySerializer(companies,many=True)
        return Response(serializer.data)

    #get fashion company by id
    def get(self,pk, request,*args, **kwargs):
        company = FashionCompany.objects.get(_id=pk)
        serializer = FashionCompanySerializer(company,many=False)
        return Response(serializer.data) 

    #register new fashion company
    def post(request,*args, **kwargs):

        data = request.data
        try:
            user = User.objects.create(
                first_name=data['name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )

            Profile.objects.get(user=user)
            profile.role="company"
            profile.save

            FashionCompany.objects.create(
                profile = user.profile,
                name=user.username,
                email=user.email,
                address=data['address']

            )

            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data)
        except:
            message = {'details': 'User with this email already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def delete(request,pk,*args, **kwargs):
        company = FashionCompany.objects.get(_id=pk)
        company.delete()
        return Response("deleted")

    def patch(request,pk,*args,**kwargs):
        company=FashionCompany.objects.get(_id=pk)

        company.name = data['name']
        company.email=data['email']
        company.address = data['address']
        company.logo = data['image']
        company.save()

        serializer = FashionCompanySerializer(company,many=False)
        return Response(serializer.data)


class TailorApi(APIView ):
   # parser_classess = (MultiPartParser, FormParser)
    permission_classes = ([IsAdminUser])

    def get(request,self,*args,**kwargs):
        tailors = Tailor.objects.all()
        serializer = tailors(company,many=True)
        return Response(serializer.data)



"""
assumimg we have model called Tialor in my django models.py 
with the following fields

class Tailor(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    company = models.ForeignKey(FashionCompany, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    wallet = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True, default=0.0)
    total_work=models.IntegerField(default=0)
    total_pending_work=models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self):
        return self.name

generate the django drf code to archive the following functions using best practices also not only isAdmin user should allow to make the request,
- get all Tailor objects
- get tailor by id
- add new tailor
- delete tailor
- update tailor

"""
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_tailors(request):
    tailors = Tailor.objects.all()
    serializer = TailorSerializer(tailors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tailor_by_id(request, pk):
    try:
        tailor = Tailor.objects.get(pk=pk)
        serializer = TailorSerializer(tailor)
        return Response(serializer.data)
    except Tailor.DoesNotExist:
        message = {'detail': 'Tailor not found'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_tailor(request):
    data = request.data
    serializer = TailorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_tailor(request, pk):
    try:
        tailor = Tailor.objects.get(pk=pk)
        tailor.delete()
        return Response("Tailor deleted")
    except Tailor.DoesNotExist:
        message = {'detail': 'Tailor not found'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_tailor(request, pk):
    try:
        tailor = Tailor.objects.get(pk=pk)
        data = request.data
        serializer = TailorSerializer(instance=tailor, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Tailor.DoesNotExist:
        message = {'detail': 'Tailor not found'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)



#Customer_addmin functions
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customer_by_id(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    except Customer.DoesNotExist:
        message = {'detail': 'Customer n not found'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response("Customer deleted")
    except Customer.DoesNotExist:
        message = {'detail': 'Customer not found'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        data = request.data
        serializer = TailorSerializer(instance=customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Customer.DoesNotExist:
        message = {'detail': 'Tailor not found'}
        return Response(message, status=status.HTTP_404_NOT_FOUND)
    


