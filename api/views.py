from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer, ProfileSerializer
from home.models import Transaction, Profile

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/transaction-list',
		'Detail View' : '/transaction-detail/<str:pk>/',
		'Create':'/transaction-create/',
		'Update':'/transaction-update/<str:pk>/',
		'Delete':'/transaction-delete/<str:pk>/',
	}
	return Response(api_urls)



@api_view(['GET'])
def transactionList(request):
	transactions = Transaction.objects.all()
	serializer = TransactionSerializer(transactions, many=True)

	return Response(serializer.data)

	
@api_view(['GET'])
def transactionDetial(request, pk):
	transactions = Transaction.objects.get(id=pk)
	serializer = TransactionSerializer(transactions, many=False)

	return Response(serializer.data)





@api_view(['GET'])
def profileList(request):
	profiles = Profile.objects.all()
	serializer = ProfileSerializer(profiles, many=True)

	return Response(serializer.data)

	
@api_view(['GET'])
def profileDetail(request, pk):
	profile = Profile.objects.get(id=pk)
	serializer = ProfileSerializer(profile, many=False)

	return Response(serializer.data)



@api_view(['POST'])
def profileCreate(request):
	serializer = ProfileSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)



@api_view(['POST'])
def profileUpdate(request, pk):
	profile = Profile.objects.get(id=pk)
	serializer = ProfileSerializer(instance=profile, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)



@api_view(['DELETE'])
def profileDelete(request, pk):
	profile = Profile.objects.get(id=pk)
	profile.delete()

	return Response("Profile successfully Deleted")