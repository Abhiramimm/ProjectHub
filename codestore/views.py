from django.shortcuts import render,redirect

from codestore.forms import SignUpForm,SignInForm,ProjectForm

from django.views import View

from django.contrib.auth.models import User

from codestore.models import Project,Wishlist

from django.contrib.auth import authenticate,login,logout


# Create your views here.

class RegistrationView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignUpForm()

        return render(request,"register.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=SignUpForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            print("account created")

            return redirect("signin")
        
        return render(request,"register.html",{"form":form_instance})

class LoginView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignInForm()

        return render(request,"login.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=SignInForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_object=authenticate(request,username=uname,password=pwd)

            print(user_object)

            if user_object:

                login(request,user_object)

                print("session started")

                return redirect("project-list")
            
        print("failed to login")

        return render(request,"login.html",{"form":form_instance})

class ProjectCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=ProjectForm()

        return render(request,"project_add.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=ProjectForm(request.POST,request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("project-list")
        
        else:
            return render(request,"project_add.html",{"form":form_instance})

class ProjectListView(View):

    def get(self,request,*args,**kwargs):

        qs=Project.objects.all()

        return render(request,"project_list.html",{"data":qs})

class ProjectDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Project.objects.get(id=id)

        return render(request,"project_detail.html",{"data":qs})

class ProjectDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Project.objects.get(id=id).delete()

        return redirect("project-list")

class ProjectUpdateView(View):

     def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Project.objects.get(id=id)

        form_instance=ProjectForm(instance=qs)

        return render(request,"project_edit.html",{"form":form_instance})
    
     def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")

        qs=Project.objects.get(id=id)

        form_instance=ProjectForm(request.POST,instance=qs)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("project-list")
        
        else:

            return render(request,"project_edit.html",{"form":form_instance}) 

class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")


class UserHomeView(View):

    def get(self,request,*args,**kwargs):

        qs=Project.objects.all()

        return render(request,"userhome.html",{"data":qs})

class AddtoWishListView(View):

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Project.objects.get(id=id)

        wishlist_obj=Wishlist.objects.create(project_object=qs)

        wishlist_obj.save()

        print("item added")

        return redirect("wish-list")
    
class WishListView(View):

    def get(self,request,*args,**kwargs):

        qs=Wishlist.objects.all()

        return render(request,"wish_list.html",{"data":qs})

class RemoveWishlistItem(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Wishlist.objects.get(id=id).delete()

        return redirect("wish-list")

