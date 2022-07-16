from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from django.views.decorators.csrf import csrf_protect
def indexView(request):
    return render(request,'index.html')

def chatbot(request):
    return render(request,'chatbot.html')

@login_required
def homeView(request):
    allblog=Blog.objects.all()
    return render(request,'home.html',{'allblog':allblog})

@login_required
def aboutView(request):
    return render(request,'about.html')
@csrf_protect
def registerView(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def myblog(request,id):
    details=User.objects.filter(id=id)
    allblog=Blog.objects.filter(user_id=id)
    return render(request,'myblog.html',{'data':allblog,'details':details})

def show(request,bid):
    bcid=Blog.objects.get(bid=bid)
    showblog=Blog.objects.filter(bid=bid)
    showcomment=Comment.objects.filter(bcid=bid)
    if request.method=="GET":
        showblog=Blog.objects.filter(bid=bid)
        showcomment=Comment.objects.filter(bcid=bid)
        return render(request,"show.html",{'comm':bcid,'showblog':showblog,'showcomment':showcomment})
    elif request.method=="POST":    
        try:
            cbody=request.POST['cbody']
            Comment(cbody=cbody,bcid=bcid).save()
            messages.success(request,'Saved comment')
            bcid=Blog.objects.get(bid=bcid)
            return render(request,'show.html',{'comm':bcid})
        except Exception as e:
            messages.success(request,'')
    return render(request,'show.html',{'showblog':showblog,'showcomment':showcomment,'comm':bcid})

@login_required
def Insert(request,id):
    userid=User.objects.get(id=id)
    if request.method=="GET":
        return render(request,"insert.html",{'display':userid})
    elif request.method=="POST":
        try:
            aname=request.POST['aname']
            btitle=request.POST['btitle']
            desc=request.POST['desc']
            date=request.POST['date']
            Blog(aname=aname,btitle=btitle,desc=desc,date=date,user_id=id).save()
            messages.success(request,'Saved blog')
            userid=User.objects.get(id=id)
            return render(request,'insert.html',{'display':userid})
        except Exception as e:
            messages.success(request,'Failed to Insert')

@login_required
def delete(request,bid,id):
    details=User.objects.filter(id=id)
    allblog=Blog.objects.filter(user_id=id)
    delblog=Blog.objects.filter(bid=bid)
    context ={
        'data':allblog,
        'details':details,
        'delblog':delblog,
    }
    # fetch the object related to passed id
    obj1 = get_object_or_404(Blog, bid = bid)
    if request.method =="POST":
        # delete object
        obj1.delete()
        # after deleting redirect to
        return render(request,'myblog.html',{'data':allblog,'details':details})
    return render(request,'delete.html',context)

def search(request):
    query=request.GET['query']
    allblog=Blog.objects.filter(btitle__icontains=query)
    params={'allblog':allblog}
    return render(request,'search.html',params)

@login_required
def update(request,bid): 
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(Blog, bid = bid)
    # pass the object as instance in form
    form = Blogform(request.POST or None, instance = obj)
    # save the data from the form and
    if form.is_valid():
        form.save()
        #userid=User.objects.get(id=id) 
        messages.success(request,'Update blog')
        return redirect('update',bid)
    # add form dictionary to context
    context["form"] = form
    return render(request,'update.html',context)

@login_required
def Feedback(request):
    form = Feedbackform
    if request.method == 'POST':
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Saved Feedback')
            return redirect('Feedback') 
    context = {'form':form}
    return render(request, 'feedback.html', context)