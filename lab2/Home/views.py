from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Register,Intake
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin ,logout
from django.views import View
from .forms import AddUserForm,AddUserFormModel
from django.views.generic import ListView

# Create your views here.


class Intakelist(ListView):
    model = Intake



def contact(request):
    return render(request, 'Home/contact.html')
def home(request):
    return render(request, 'navbar.html')

def about(request):
    return render(request, 'Home/aboutus.html')

def insertIntake(request):
    if request.method == "GET" :
        return render(request, 'Home/Intake.html')
    else:
        intake = request.POST['intake'];
        intakes = Intake.objects.create(name = intake)
        return render(request, 'Home/Intake.html')


class insertForm1(View):
    def get(self, request):
        context = {}
        context['form'] = AddUserForm()
        return render(request, 'Home/SignForm1.html',context)
    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            choise=request.POST['IntakeF']
            print(choise)
            tractobj = Intake.objects.get(id=request.POST['IntakeF'])
            Register.objects.create(username=request.POST['name'], password=request.POST['password'], Intakeid=tractobj)
            #User.objects.create_user(username=request.POST['name'], password=request.POST['pass'], is_staff=True)

            return redirect(login)

class insertForm2Model(View):
    def get(self, request):
        context = {}
        context['form'] = AddUserFormModel()
        return render(request, 'Home/SignUpForm2Model.html',context)
    def post(self, request):
        form = AddUserFormModel(request.POST)
        if form.is_valid():
            form.save()
            context={}
            context['form'] = AddUserFormModel()
            context['msg']="Success Insert INTAKE"
            return render(request, 'Home/SignUpForm2Model.html',context)

def register(request):
    context = {}
    if (request.method == 'GET'):
        return render(request, 'Home/register.html', context)
    else:

        #print(request.POST)
        name = request.POST['name']
        pas= request.POST['pass']
        intake=request.POST['intake']
        print(intake)
        tractobj = Intake.objects.get(name=request.POST['intake'])
        Register.objects.create(username=name, password=pas, Intakeid=tractobj )
        User.objects.create_user(username=request.POST['name'], password=request.POST['pass'], is_staff=True)
        users = Register.objects.all()
        # context['users'] = users
        # request.session['users'] = users
        # context['msg'] = 'success register'
        #return render(request, 'Home/login.html', context)
        return redirect(login)

def login(request):

    context={}
    if ( request.method == 'GET' ):
        context['msg'] = ""
        return render(request, 'Home/login.html')
    else:
        user = Register.objects.filter(username=request.POST['name'] , password=request.POST['pass'])
        auth=authenticate(username=request.POST['name'], password=request.POST['pass'])
        #print(user[0].username)
        if(len(user)>0 and auth is not None):

            #context['username'] = user[0].username
            authlogin(request , auth)
            request.session['username'] = request.POST['name']

            return HttpResponseRedirect('userlogin')
        else:
            name=request.POST['name']
            context['msg'] = f"{name} is invalid"
            return redirect(login)


def userlogin(request):
    context={}
    users = Register.objects.all()
    context['users'] = users
    return render(request, 'userlogin.html', context)


def my_logout(request):
    request.session.clear()
    logout(request)
    return redirect(home)




def updateV(request,id):
     context={}
     if request.method == "GET":
         return render(request, 'users/updateView.html')
     else:
         username = request.POST.get('name')
         user = Register.objects.get(id=id)
         print(user)
         if user:
             user.username = username
             user.save()
             users = Register.objects.all()
             context['users'] = users
             return render(request, 'userlogin.html', context)
         else:
             context['msg'] = "did not find this user"
             return render(request, 'users/updateView.html', context)


def deleteuser(request,id):
    context={}
    Register.objects.filter(id=id).delete()
    users = Register.objects.all()
    context['users'] = users
    return render(request, 'userlogin.html', context)


# def updateuser(request,id):
#     context={}
#     user = Register.objects.filter(id=id);
#     print(user.username)
#     if(len(user)==0):
#         context['msg']="did not find this user"
#         return render(request, 'userlogin.html', context)
#     else:
#         username = request.POST.get('name')
#         user.username = username
#         user.save()
#         users = Register.objects.all()
#         context['users'] = users
#         return render(request, 'userlogin.html', context)


# def updateuser(request,id):
#     context={}
#     if request.method == 'POST':
#         username= request.POST.get('name')
#         user= Register.objects.filter(id=id)
#         if user:
#             user.username = username
#             user.save()
#             users = Register.objects.all()
#             context['users'] = users
#             return render(request, 'userlogin.html', context)
#         else:
#             context['msg'] = "did not find this user"
#             return render(request, 'users/updateView.html', context)
#
#
#
# def view(request):
#     if request.method == "GET":
#         render(request,"updateView.html")
#         print("1")
#     else:
#         return redirect(userlogin)
