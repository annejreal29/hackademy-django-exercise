from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import UserSerializer #GroupSerializer
from django.shortcuts import get_object_or_404


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

@api_view(['GET', 'POST'])
def getUser(request):
    users = User.objects.all()
    if request.method == 'POST':
        serializer_class = UserSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
    else:
        serializer_class = UserSerializer(users, many=True)
    return Response(serializer_class.data)

@api_view(['GET', 'PUT', 'DELETE'])
def getUserById(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'GET':
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data)
    elif request.method == 'PUT':
        serializer_class = UserSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

