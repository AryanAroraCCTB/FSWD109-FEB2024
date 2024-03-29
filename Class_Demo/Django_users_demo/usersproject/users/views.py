from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users
import json
from .forms import UserForm


# Create your views here.
def user_list(request):
    page_number = request.GET.get('page_number')
    page_size = request.GET.get('page_size')
    if page_number and page_size:
        # return some users
        start = (page_number - 1) * page_size
        end = start + page_size
        users = Users.objects.all()[start:end]
    else:
        # return all users
    	users = Users.objects.all()
    return JsonResponse({"users": [user.serialize() for user in users]})





















def user_detail(request, id):
    user = Users.objects.get(id=id)
    return JsonResponse({"user": user.serialize()})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(f'{form.is_valid()} {form.cleaned_data}')
        data = form.cleaned_data
        new_user = Users.objects.create(name=data["name"], email=data["email"], age=data["age"])
        return JsonResponse({"user": new_user.serialize()})
    else:
        form = UserForm()
        return render(request, 'user_form.html', {'form': form})
         

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
