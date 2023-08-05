from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from base.models import Tailor, Work, Style
from base.serializer import TailorSerializer, WorkSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTailor(request):
    user = request.user.profile
    tailor = Tailor.objects.get(profile=user)
    serializer = TailorSerializer(tailor, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allAvailableWork(request):
    user = request.user.profile
    tailor = Tailor.objects.get(profile=user)
    #works = user.work_set.all().order_by('-createdAt')
    works = Work.objects.filter(tailor=tailor)
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllJobDone(request):
    user = request.user.profile
    tailor = Tailor.objects.get(profile=user)
    works = Work.objects.filter(tailor=tailor, isCompleted=True).order_by('-createdAt')
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllPendingJob(request):
    user = request.user.profile
    tailor = Tailor.objects.get(profile=user)
    works = Work.objects.filter(tailor=tailor, isCompleted=False).order_by('-createdAt')
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editWork(request, pk):
    work = Work.objects.get(_id=pk)
    data = request.data
    style_id = data.get('style')
    work.style = Style.objects.get(_id=style_id)
    work.measurement = data['measurement']
    work.isCompleted = data["isCompleted"]
    work.save()
    serializer = WorkSerializer(work, many=False)
    return Response("Work updated successfully")
