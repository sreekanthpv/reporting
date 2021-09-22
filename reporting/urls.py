from django.urls import path
from reporting import views
urlpatterns=[
  path('home',views.AdminHome.as_view(),name='adminhome'),
  path('users/add',views.UserAdd.as_view(),name="adduser"),
  path('users/change', views.Edituser.as_view(), name="edituser"),
  path('user/update/<int:id>',views.Edituser.as_view(),name="edituser"),
  path('batches/add', views.BatchAdd.as_view(), name="addbatch"),
  path('courses/add', views.Courseadd.as_view(), name="addcourse"),
  # path('courses/view', views.ListCourses.as_view(), name="listcourses"),
  # path('batches/view', views.ListBatch.as_view(), name="listbatches"),
  path('batch/update/<int:id>', views.EditBatch.as_view(), name="editbatch"),
  path('temp',views.Temp.as_view(),name="temp"),

]