from django.shortcuts import render,redirect
from reporting import forms
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from reporting.models import MyUser,Batch,Course
from django.urls import reverse_lazy

class AdminHome(TemplateView):
    # def get(self,request,*args,**kwargs):
    #     return render(request,"reporting/admin_home.html")
    template_name = "reporting/home.html"



class UserAdd(CreateView):
    model=MyUser
    form_class=forms.UserAddForm
    template_name="reporting/user_add.html"
    success_url = reverse_lazy("adduser")
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["users"]=MyUser.objects.all()
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
    model=Batch
    form_class = forms.BatchAddForm
    template_name = "reporting/batchadd.html"
    success_url = reverse_lazy("addbatch")
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["batches"]=Batch.objects.all()
        return context

# class ListBatch(ListView):
#         model = Batch
#         template_name = "reporting/listbatches.html"
#         context_object_name = "batches"




class EditBatch(UpdateView):
    model = Batch
    template_name = "reporting/editbatch.html"
    form_class = forms.BatchAddForm
    pk_url_kwarg = "id" #default id is "pk" changed to "id"
    # context_object_name = "batch"           #what is this?
    success_url = reverse_lazy("addbatch")




class Courseadd(CreateView):
    model=Course
    form_class = forms.CourseAddForm
    template_name = "reporting/courseadd.html"
    success_url = reverse_lazy("addcourse")
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["courses"]=Course.objects.all()
        return context


# class ListCourses(ListView):
#     model = Course
#     template_name = "reporting/listcourse.html"
#     context_object_name = "courses"

class Temp(TemplateView):
    template_name = "reporting/base.html"

