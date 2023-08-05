from rest_framework.decorators import api_view, permission_classes, parser_classes,APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status

from django.contrib.auth.models import User
from datetime import date, datetime
from base.serializer import *


"""
todo:
-create work
-edit work
-delete work
-add tailor
-delete tailor
-edit tailor
-payment-history
-list all tailor
-delete tailor
-update tailor
-list all work
-list order
"""

#work functions start here
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def createWork(request):
    user = request.user.profile
    print(user.role)
    if user.role == 'company':
        company = FashionCompany.objects.get(profile=user)
        print(company)
        data = request.data
        style_id=data.get('styleId')
        print(style_id)
        style = Style.objects.get(_id=style_id)
        print(style)
        customer_id = data.get('customerId')
        customer = Customer.objects.get(_id=customer_id)
        tailor_id = data.get('tailorId')
        tailor = Tailor.objects.get(_id=tailor_id)

        work = Work.objects.create(
            company = company,
            style = style,
            tailor = tailor,
            customer = customer,
            style_description = style.description,
            tailor_name = tailor.name,
            custormer_name = customer.name,
            company_name=company.name,
            measurement = data['measurement'],
            price = data['price'],
     

        )

        serializer = WorkSerializer(work,many=False)
        return Response(serializer.data)
    else:
        message = {'details': 'UNAUTHORISED'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


        
        
@api_view(['PUT'])  
#@permission_classes([IsAuthenticated])
def updateWork(request,pk):
    #user = request.user.profile
    #console.log(user)
    #if user.role == 'company':
    work = Work.objects.get(_id=pk)
    data = request.data
    #work.company = FashionCompany.objects.get(profile=user)
    style_id=data.get('style')
    work.style = Style.objects.get(_id=style_id)
    work.style_description = work.style.description
    tailor_id = data.get('tailor')
    work.tailor = Tailor.objects.get(_id=tailor_id)
    work.tailor_name=work.tailor.name
    work.measurement=data['mearsurement']
    work.price = data['price']
    work.isCompleted=data["isCompleted"]
    work.save()
    serializer =WorkSerializer(work, many=False)
    return Response(serializer.data)
    #else:
      #  message = {'details': 'UNAUTHORISED'}
       # return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])  
@permission_classes([IsAuthenticated])    
def DeleteWork(request, pk):
    user = request.user.profile
    if user.role == "company":
        work = Work.objects.get(_id=pk)
        work.delete()
        return Response("work deleted")
    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['GET'])  
@permission_classes([IsAuthenticated])    
def getWorkById(request,pk):
    work = Work.objects.get(_id=pk)
    serializer =WorkSerializer(work,many=False)
    return Response(serializer.data)

@api_view(['GET'])  
@permission_classes([IsAuthenticated])    
def getAllWOrk(request):
    user = request.user.profile
    if user.role  == "company":
        company = FashionCompany.objects.get(profile=user)
        works = Work.objects.filter(company=company).order_by('-createdAt')
        serializer = WorkSerializer(works,many=True)
        return Response(serializer.data)
    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)




#tailor function start here
@api_view(['POST'])  
@permission_classes([IsAuthenticated])    
def AddTailor(request):
    company_profile = request.user.profile
    company = FashionCompany.objects.get(profile=company_profile)
    data = request.data
    try:
        tailor = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        
        Profile.objects.get(user=tailor)
      
        Profile.role="tailor"
        Profile.save

        Tailor.objects.create(
            profile = tailor.profile,
            company=company,
            name=tailor.username,
            email=tailor.email
        )

    #return Response('Tailor added')

    

        serializer = UserSerializerWithToken(tailor, many=False)
        return Response(serializer.data)


    except:
        message = {'details': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
        





@api_view(['DELETE'])  
@permission_classes([IsAuthenticated])    
def deleteTailor(request,pk):
    tailor = Tailor.objects.get(_id=pk)
    profile = Profile.objects.get(_id=tailor.profile._id)
    print(profile)
    user = User.objects.get(id=profile.user.id)
    print(user)
    profile.delete()
    user.delete()
    tailor.delete()
    return Response("Tailor deleted")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTailorByid(request,pk):
    tailor = Tailor.objects.get(_id=pk)
    serializer=TailorSerializer(tailor,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTailors(request):
    user = request.user.profile
    company = FashionCompany.objects.get(profile=user)
    tailor = Tailor.objects.filter(company=company).order_by('-createdAt')
    serializer=TailorSerializer(tailor,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def updateTailor(request,pk):
    user = request.user.profile
    company = FashionCompany.objects.get(profile=user)
    if company.role == 'company':
        tailor =Tailor.objects.get(_id=pk)
        tailor_profile = tailor.profile
        console.log(tailor_profile.user)
        user=User.objects.get(_id=tailor_profile.user)
        user.first_name = data['name']
        user.username = data['email']
        user.email = data['email']
        user.save()

        tailor.name= user.first_name
        tailor.email=user.email
        tailor.save()
        return Response('tailor Updated')

    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)









@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def Transfer(request):
    user = request.user.profile
    data=requet.data
    company = FashionCompany.objects.get(profile=user)
    tailor_id=data['tailor_id']
    amount = data['amount']
    tailor = Tailor.objects.get(_id=tailor_id)
    tailor.wallet += amount
    company.wallet -= amount
    tailor.save()
    company.save() 

    return Response("transaction succcesful")

#styles functions
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getStyles(request):
    user = request.user.profile
    if user.role  == "company":
        company = FashionCompany.objects.get(profile=user)
        styles = Style.objects.filter(company=company)
        serializer = StyleSerializer(styles,many=True)
        return Response(serializer.data)
    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getStyle(request,pk):
    user = request.user.profile
    if user.role  == "company":
        style=Style.objects.get(_id=pk)
        serializer = StyleSerializer(style, many=False)
        return Response(serializer.data)
    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadStyle(request):
    user = request.user.profile
    if user.role  == "company":
        company = FashionCompany.objects.get(profile=user)
        style =Style.Objects.create(
            company=company,
            image=request.Files['image'],
            description=data['description'],
            gender=data['gender']
        )

    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


class AddStyleView(APIView):
    parser_classess = (MultiPartParser, FormParser)
    permission_classes = ([IsAuthenticated])

    def post(self,request, *args, **kwargs):
        user = request.user.profile
        data = request.data
        if user.role == "company":
            company = FashionCompany.objects.get(profile=user)

            image = data['image']
            print(image)
            style= Style.objects.create(
                company=company,
                image=image,
                description=data['description'],
                gender=data['gender']
            )

            serializer = StyleSerializer(style,many=False)
            return Response(serializer.data)

        else:
            message={'details':'you are not authorised'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk, *args, **kwargs):
        user = request.user.profile
        data = request.data
        if user.role == "company":
           
            style  = Style.objects.get(_id=pk)
            style.image = data['image']
            style.gender = data['gender']
            style.description = data['description']

            style.save()


        else:
            message={'details':'you are not authorised'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)







@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateStyle(request,pk):
    user = request.user.profile
    data = request.data
    if user.role  == "company":
        #company = FashionCompany.objects.get(profile=user)
        style = Style.Objects.get(_id=pk)
        style.image = data.Files['image']
        style.description = data['description']
        style.gender = data['gender']
        style.save()

    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteStyle(request,pk):
    user = request.user.profile
    if user.role  == "company":
        style = Style.objects.get(_id=pk)
        style.delete()
        return Response("style deleted")
    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


#customer functions
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCustomers(request):
    user = request.user.profile
    if user.role  == "company":
        company = FashionCompany.objects.get(profile=user)
        customers = Customer.objects.filter(company=company)
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)
    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCustomer(request,pk):
    user = request.user.profile
    if user.role  == "company":
        customer = Customer.objects.get(_id=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCustomer(request,pk):
    user = request.user.profile
    if user.role  == "company":
        customer = Customer.objects.get(_id=pk)
        customer.delete()
        return Response("customer deleted")
    else:
        message={'details':'you are not authorised'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])  
@permission_classes([IsAuthenticated])    
def AddCustomer(request):
    company_profile = request.user.profile
    company = FashionCompany.objects.get(profile=company_profile)
    data = request.data
    try:
        customer = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        
        Profile.objects.get(user=customer)
      
        Profile.role="customer"
        Profile.save

        Customer.objects.create(
            profile = customer.profile,
            company=company,
            name=customer.username,
            email=customer.email,
            phone= data['phone'],
            address = data['address']
        )

    #return Response('customer added')

    

        serializer = UserSerializerWithToken(customer, many=False)
        return Response(serializer.data)


    except:
        message = {'details': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
      


