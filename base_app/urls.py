from .import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.login, name='login'),
    re_path(r'^ADlogout/$', views.ADlogout, name='ADlogout'),
    re_path(r'^logout5/$', views.logout5, name='logout5'),
    re_path(r'^Mnlogout/$', views.Mnlogout, name='Mnlogout'),

    ########## MAN section###########
    re_path(r'^MAN_index$',views.MAN_index, name="MAN_index"),
    re_path(r'^MAN_profile/$',views.MAN_profile, name="MAN_profile"),
    re_path(r'^MAN_registration/$',views.MAN_registration, name="MAN_registration"),
    re_path(r'^MAN_registrationstaff/$',views.MAN_registrationstaff, name="MAN_registrationstaff"),
    re_path(r'^MAN_registrationstudent/$',views.MAN_registrationstudent, name="MAN_registrationstudent"),
    re_path(r'^MAN_currentstaff/$',views.MAN_currentstaff, name="MAN_currentstaff"),
    re_path(r'^MAN_resignedstaff/$',views.MAN_resignedstaff, name="MAN_resignedstaff"),
    re_path(r'^MAN_currentstudent/$',views.MAN_currentstudent, name="MAN_currentstudent"),
    re_path(r'^MAN_resignedstudent/$',views.MAN_resignedstudent, name="MAN_resignedstudent"),
    re_path(r'^MAN_academics/$',views.MAN_academics, name="MAN_academics"),
    re_path(r'^MAN_batch/$',views.MAN_batch, name="MAN_batch"),
    re_path(r'^MAN_addbatch/$',views.MAN_addbatch, name="MAN_addbatch"),

    ############ account section###########
    re_path(r'^account_index/$',views.account_index, name="account_index"),
    re_path(r'^account_leaverequest/$',views.account_leaverequest, name="account_leaverequest"),
    re_path(r'^account_applyleave/$',views.account_applyleave, name="account_applyleave"),
    re_path(r'^account_requestedleave/$',views.account_requestedleave, name="account_requestedleave"),
    re_path(r'^account_issues/$',views.account_issues, name="account_issues"),
    re_path(r'^account_reportedissue/$',views.account_reportedissue, name="account_reportedissue"),
    re_path(r'^account_report_an_issue/$',views.account_report_an_issue, name="account_report_an_issue"),
    re_path(r'^account_issuereply/(?P<id>\d+)/$',views.account_issuereply, name="account_issuereply"),

    ##########admin section############

    re_path(r'^BRadmin_index/$',views.BRadmin_index, name="BRadmin_index"),
   
]