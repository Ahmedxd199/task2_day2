from django.shortcuts import render
from .models import Register

# Create your views here.

def contact(request):
    return render(request, 'home/contact.html')
def home(request):
    return render(request, 'navbar.html')

def about(request):
    return render(request, 'home/aboutus.html')

def login(request):
    pass

def register(request):
    context = {}
    if (request.method == 'GET'):
        return render(request, 'home/register.html', context)
    else:

        # intsake reques.post
        print(request.POST)
        name = request.POST['name']
        pas= request.POST['pass']
        # save to db  intake table
        '''
        myintake=Intake()
        myintake.intakename=name
        myintake.startdate=sdate
        myintake.enddate=endate
        myintake.save()
        '''
        Register.objects.create(username=name, password=pas )
        intakes = Register.objects.all()
        context['intakes'] = intakes
        context['msg'] = 'intake inserted'
        return render(request, 'home/login.html', context)