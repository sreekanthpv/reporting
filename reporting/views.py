from django.shortcuts import render, redirect


from reporting import forms
from django.views.generic import TemplateView, CreateView, ListView, UpdateView,DeleteView
from reporting.models import MyUser, Batch, Course, TimeSheet
from django.urls import reverse_lazy
<<<<<<< HEAD
from django.contrib.auth import authenticate, login, logout
from reporting.filters import TimeSheetFilter
from django_filters.views import FilterView

from django.utils.decorators import method_decorator
from reporting.decorators import signin_required



=======
from django.contrib.auth import authenticate,login,logout
>>>>>>> 1c63d94d68bfd45fd4bbeaf578cc1d4350b7512b
class AdminHome(TemplateView):
    # def get(self,request,*args,**kwargs):
    #     return render(request,"reporting/admin_home.html")
    template_name = "reporting/home.html"

@method_decorator(signin_required,name='dispatch')
class UserHome(TemplateView):
    template_name = "reporting/userhome.html"


class UserAdd(CreateView):
    model = MyUser
    form_class = forms.UserAddForm
    template_name = "reporting/user_add.html"
    success_url = reverse_lazy("adduser")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = MyUser.objects.all()
        return context
    # context={}
    # def get(self,request,*args,**kwargs):
    #     form=self.form_class()
    #     self.context['form']=form
    #     return render(request,self.template_name,self.context)
    # def post(self,request):
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('admin_home')
    #


class Edituser(UpdateView):
    model = MyUser
    form_class = forms.UserAddForm
    template_name = "reporting/edituser.html"
    success_url = reverse_lazy("adduser")
    pk_url_kwarg = "id"


class BatchAdd(CreateView):
    model = Batch
    form_class = forms.BatchAddForm
    template_name = "reporting/batchadd.html"
    success_url = reverse_lazy("addbatch")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["batches"] = Batch.objects.all()
        return context


# class ListBatch(ListView):
#         model = Batch
#         template_name = "reporting/listbatches.html"
#         context_object_name = "batches"


class EditBatch(UpdateView):
    model = Batch
    template_name = "reporting/editbatch.html"
    form_class = forms.BatchAddForm
    pk_url_kwarg = "id"  # default id is "pk" changed to "id"
    # context_object_name = "batch"           #what is this?
    success_url = reverse_lazy("addbatch")


class Courseadd(CreateView):
    model = Course
    form_class = forms.CourseAddForm
    template_name = "reporting/courseadd.html"
    success_url = reverse_lazy("addcourse")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        return context


#
# class ListCourses(ListView):
#     model = Course
#     template_name = "reporting/listcourse.html"
#     context_object_name = "courses"
#


class UserSignInView(TemplateView):
    template_name = "reporting/usersignin.html"
    form_class = forms.UserLoginForm
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                if not request.user.is_admin:
                    return redirect("userhome")
                else:
                    return redirect("adminhome")
            else:
                return redirect("signin")

@method_decorator(signin_required,name='dispatch')
class UserSignOutView(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("usersignin")



@method_decorator(signin_required,name='dispatch')
class AddTimesheetview(CreateView):
    model = TimeSheet
    form_class = forms.AddTimeSheetForm
    template_name = "reporting/addtimesheet.html"

    def get(self, request, *args, **kwargs):
        form=self.form_class(request.user)
        return render(request,self.template_name,{"form":form})


    def post(self, request, *args, **kwargs):
        form = forms.AddTimeSheetForm(request.user,request.POST)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.user = request.user
            timesheet.save()
            return redirect("addtimesheet")
        else:
            return render(request,self.template_name,{"form":form})



@method_decorator(signin_required,name='dispatch')
class Timesheets(ListView):
    model = TimeSheet
    template_name = "reporting/viewtimesheets.html"
    context_object_name = "timesheets"

    def get_queryset(self):
        queryset = TimeSheet.objects.filter(user=self.request.user)  # verified=False  (custom)
        return queryset
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context["timesheets"]=TimeSheet.objects.filter(user=self.request.user)
    #     return context




@method_decorator(signin_required,name='dispatch')
class EditTimesheet(UpdateView):
    model = TimeSheet
    form_class = forms.AddTimeSheetForm
    template_name = "reporting/edittimesheet.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listtimesheet")


class AdminTimeSheets(ListView):
    model = TimeSheet
    template_name = "reporting/adminviewtimesheets.html"
    context_object_name = "timesheets"

    def get_queryset(self):
        queryset = TimeSheet.objects.all()
        return queryset


class Verify(TemplateView):
    model = TimeSheet
    pk_url_kwarg = "id"

    # template_name = "reporting/adminviewtimesheets.html"
    def get(self, request, *args, **kwargs):
        instance = self.model.objects.get(id=kwargs["id"])
        instance.verified = True
        instance.save()
        return redirect("admintimesheet")


#
# def search(request):
#     filters = TimeSheetFilter(request.GET,queryset=TimeSheet.objects.all())
#     return render(request,"reporting/searchtimesheet.html",{"filter":filters})


@method_decorator(signin_required,name='dispatch')
class TimeSheetSearch(FilterView):
    model = TimeSheet
    filterset_class = TimeSheetFilter
    template_name = "reporting/searchtimesheet.html"
    context_object_name = "filter"

    def get_queryset(self):
        if self.request.user.is_admin:
            queryset = TimeSheet.objects.all()
            return queryset
        else:
            queryset = TimeSheet.objects.filter(user=self.request.user)
            return queryset

class RemoveTimeSheet(DeleteView):
    model = TimeSheet
    pk_url_kwarg = "id"
    template_name = "reporting/deletetimesheet.html"
    success_url = reverse_lazy("listtimesheet")


    # def post(self, request, *args, **kwargs):
    #      print(kwargs["id"])
    #      timesheet=TimeSheet.objects.get(id=kwargs["id"])
    #      timesheet.delete()
    #      timesheet.save()
    #      return redirect("listtimesheet")




<<<<<<< HEAD
# def delete(request,id):
#     timesheet=TimeSheet.objects.get(id=id)
#     # print(timesheet)
#     timesheet.delete()
#     # timesheet.save()
#     return redirect("listtimesheet")
=======

class SignInView(TemplateView):
    template_name = "reporting/user_login.html"
    form_class=forms.SigninForm



    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["form"]=self.form_class()
        return context

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                print("success")

                return redirect("userhome")

class UserHome(TemplateView):
    template_name = "reporting/user_home.html"

class SignOut(TemplateView):


    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")
>>>>>>> 1c63d94d68bfd45fd4bbeaf578cc1d4350b7512b
