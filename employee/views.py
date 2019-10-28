from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from employee.models import *
from employee.froms import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

def register(request):
    if request.method == "POST":
        form = Registrationform(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            gender = request.POST.get('gender')
            city = request.POST.get('city')
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            user = Profile.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,phone=phone,gender=gender,city=city,password=password)
            user.save()
            print(form.errors)
            return render(request, 'auth/created.html', {'form':form})
        else:
            print(form.errors)

            return render(request, 'auth/signup.html', {'form': form})
    else:
        form = Registrationform()
    return render(request, 'auth/signup.html', {'form': form})

# def user_login(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         # username = Profile.objects.get(email=email).username
#         if email.isdigit():
#             user = Profile.objects.get(phone=email)
#         else:
#             user = Profile.objects.get(email=email)
#         if user:
#             auser = authenticate(username=email, password=password)
#             print(auser)
#             if auser:
#                 login(request, auser)
#                 return render(request, 'employee/details.html',{'user':auser})
#             else:
#                 messages.error(request, "Provide Valid Credentials")
#                 return render(request, 'auth/login.html',{'user':auser})
#         else:
#             messages.error(request, "Provide Valid Credentials")
#             return render(request, 'auth/login.html',{'user':user})
#     else:
#         return render(request, 'auth/login.html')



def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (Profile.objects.filter(username = username).exists()):
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                # return HttpResponseRedirect(request.GET['next'])
                # return HttpResponseRedirect(reverse('employee_list'))
                return render(request, 'employee/details.html',{'user':user})
            else:
                return render(request, "auth/login.html")
        else:
            # context["error"]= "Provide valid credentials !!"
            messages.error(request,"Provide valid credentials !!")
            return render(request, "auth/login.html")
    else:
        return render(request, "auth/login.html")


def community(request):
    # posts = Post.objects.order_by('-time')
    return render(request, 'employee/community_page.html')


def post_form(request):
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            catagory = request.POST.get('catagory')
            # catagory1 = Post_Catagory.objects.get(id=catagory)
            description = request.POST.get('description')
            Post.objects.create(title=title,catagory=catagory,description=description)
            posts = Post.objects.order_by('-time')
            return render(request, 'employee/community_page.html', {'post': posts})
        else:
            return render(request, 'employee/post_form.html',{'form': form})
    form = Post_Form()
    catagory = Post_Catagory.objects.all()
    context = {'form':form,'catagory':catagory}
    return render(request, 'employee/post_form.html', context)

def Post_details(request, id):
    post = Post.objects.get(pk=id)
    replies = Post_Reply.objects.filter(post_id=post.id, parent_id=0)
    reply_reply = Post_Reply.objects.filter(parent_id=0, post_id=post.id)
    context = {'post':post, 'replies':replies, 'reply_reply':reply_reply}
    return render(request, 'employee/post_details.html')


@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)

@login_required(login_url="/login/")
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

# @login_required(login_url="/login/")
# def employee_list(request):
#     context = {}
#     context['users'] = Profile.objects.all()
#     context['title'] = 'Employees'
#     return render(request, 'employee/index.html', context)


@login_required(login_url="/login/")
def employee_details(request, id=None):
    context = {}
    context['title'] = 'Employees'
    context['user'] = get_object_or_404(Profile, id=id)
    return render(request, 'employee/details.html', context)


# @login_required(login_url="/login/")
def employee_add(request):
    if request.method == 'POST':
        user_form = Registrationform(request.POST)
        if user_form.is_valid():
            u = user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/add.html', {"user_form": user_form})
    else:
        user_form = Registrationform()
        return render(request, 'employee/add.html', {"user_form": user_form})


# @login_required(login_url="/login/")
def employee_edit(request, id=None):
    user = get_object_or_404(Profile, id=id)
    if request.method == 'POST':
        # user_form = Registrationform(request.POST, instance=user)
        # if user_form.is_valid():
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.city=request.POST.get('city')
        print("raja")
        user.save()
            # return HttpResponseRedirect(reverse('employee_details'))
        return render(request, 'employee/details.html', {"user": user})
        # else:
        #     messages.error(request, "Form is not valid")
        #     return render(request, 'employee/edit.html', {"user": user})
    else:
        user_form = Registrationform(instance=user)
        return render(request, 'employee/edit.html', {"user_form": user_form})



# @login_required(login_url="/login/")
def employee_delete(request, id=None):
    user = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        user.delete()
        return HttpResponseRedirect(reverse('employee_details'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'employee/delete.html', context)



@login_required(login_url="/login/")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'employee/details.html', {'form': form})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
