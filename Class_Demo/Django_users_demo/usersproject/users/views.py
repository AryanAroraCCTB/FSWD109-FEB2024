from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users
import json


# Create your views here.
def user_list(request):
    users = Users.objects.all()
    return JsonResponse({"users": [user.serialize() for user in users]})


def user_detail(request, id):
    user = Users.objects.get(id=id)
    return JsonResponse({"user": user.serialize()})


def user_create(request):
    data = json.loads(request.body)
    new_user = Users.objects.create(
        name=data["name"], email=data["email"], age=data["age"]
    )
    return JsonResponse({"user": new_user.serialize()})


def user_update(request, id):
    data = json.loads(request.body)
    user = Users.objects.get(id=id)
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.age = data.get("age", user.age)
    user.save()
    return JsonResponse({"user": user.serialize()})


def user_delete(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return JsonResponse({"user": user.serialize()})
