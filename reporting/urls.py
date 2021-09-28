from django.urls import path
from reporting import views
urlpatterns=[
  path('home',views.AdminHome.as_view(),name='adminhome'),
  path('users/userhome', views.UserHome.as_view(), name='userhome'),

  path('users/add',views.UserAdd.as_view(),name="adduser"),
  path('users/change', views.Edituser.as_view(), name="edituser"),
  path('users/update/<int:id>',views.Edituser.as_view(),name="edituser"),
  path('users/signin',views.UserSignInView.as_view(),name="usersignin"),
  path('users/signout', views.UserSignOutView.as_view(), name="usersignout"),

  path('batches/add', views.BatchAdd.as_view(), name="addbatch"),
  path('courses/add', views.Courseadd.as_view(), name="addcourse"),
  # path('courses/view', views.ListCourses.as_view(), name="listcourses"),
  # path('batches/view', views.ListBatch.as_view(), name="listbatches"),
  path('batch/update/<int:id>', views.EditBatch.as_view(), name="editbatch"),
  path('users/timesheet/add', views.AddTimesheetview.as_view(), name="addtimesheet"),
  path('users/timesheet/view', views.Timesheets.as_view(), name="listtimesheet"),
  path('timesheet/change/<int:id>',views.EditTimesheet.as_view(),name='edittimesheet'),
  path('admin/timesheet/view', views.AdminTimeSheets.as_view(), name="admintimesheet"),
  path('admin/timesheet/verify/<int:id>', views.Verify.as_view(), name="verify"),
  path('timesheet/search',views.TimeSheetSearch.as_view(),name="search"),
  path('timesheet/remove/<int:id>', views.RemoveTimeSheet.as_view(), name="deletetimesheet"),

]