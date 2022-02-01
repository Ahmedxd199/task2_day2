from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin ,logout
# Create your views here.

def contact(request):
    return render(request, 'home/contact.html')
def home(request):
    return render(request, 'navbar.html')

def about(request):
    return render(request, 'home/aboutus.html')


def register(request):
    context = {}
    if (request.method == 'GET'):
        return render(request, 'home/register.html', context)
    else:

        #print(request.POST)
        name = request.POST['name']
        pas= request.POST['pass']

        Register.objects.create(username=name, password=pas )
        User.objects.create_user(username=request.POST['name'], password=request.POST['pass'], is_staff=True)
        users = Register.objects.all()
        # context['users'] = users
        # request.session['users'] = users
        # context['msg'] = 'success register'
        #return render(request, 'home/login.html', context)
        return redirect(login)

def login(request):

    context={}
    if ( request.method == 'GET' ):
        context['msg'] = ""
        return render(request, 'home/login.html')
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
