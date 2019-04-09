from django.shortcuts import render
from django.http import HttpResponse
from usersApp.models import User

# Create your views here.
def index(request):
    return render(request, 'usersApp/index.html')

def users(request):
    name_list = User.objects.order_by('first')
    namedict = {'users':name_list}
    return render(request, 'usersApp/users.html',namedict)
