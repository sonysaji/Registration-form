from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import registration

# Create your views here.
def index(request):
    return render(request,'home.html')

@require_http_methods(["GET", "POST"])
def manage_user(request):
    if request.method=='POST':
        data= dict(request.POST) 
        obj = registration.objects.create(first_name=data['first_name'][0],last_name=data['last_name'][0],
        mobile=data['mobile'][0],email=data['email'][0],gender=data['gender'][0],password=data['password'][0]
        ) 
        print(dict(request.POST))

        return HttpResponse("Sucess")
    if request.method=='GET':
        queryset= registration.objects.all()
        print(type(queryset))
        return render (request,'data.html',{'users':queryset})
