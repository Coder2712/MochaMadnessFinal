from django.shortcuts import render,redirect
from .models import User,Blogs,Contact
# Create your views here.
def Signup(request):
    if request.session.get('is_login'):
        return redirect('/home')
    if request.POST:
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['password']
        obj = User(uname=u, email=e, password=p)
        obj.save()
        return redirect('/Login')
    return render(request,"Signup.html")

def Login(request):
    if request.session.get('is_login'):
        return redirect('/home')
    if request.POST:
        e = request.POST['email']
        p = request.POST['password']
        count = User.objects.filter(email=e, password=p).count()
        if count > 0:
            request.session['is_login'] = True
            return redirect('/home')
    return render(request,"Login.html")

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name= request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        desc=request.POST.get('desc','')
        print(name, phone, email, desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"contact.html")

def Blog(request):
    data=Blogs.objects.all
    return render(request,"Blog.html",{"data":data})

def menu(request):
    return render(request,"menu.html")

def readmore(request,id):
    data=Blogs.objects.get(id=id)

    return render(request,"readmore.html",{"data":data})

def logout(request):
    del request.session['is_login']
    return redirect('/Login')