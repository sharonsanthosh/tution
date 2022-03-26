from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.db.models import Sum
from datetime import datetime,date

# Create your views here.
def login(request):
    des3 = designation.objects.get(designation='account')
    manag = designation.objects.get(designation="manager")
    Adm1 = designation.objects.get(designation="admin")

    
    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=manag.id).exists():     
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['m_id'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.branch_id
            request.session['m_id'] = member.id 
            mem=user_registration.objects.filter(id= member.id)
            Num = user_registration.objects.count()
            Num1 = project.objects.count()
            Trainer = designation.objects.get(designation='trainer')
            trcount=user_registration.objects.filter(designation=Trainer).count()
            return render(request,'MAN_profile.html',{'mem':mem,'num':Num,'Num1':Num1,'trcount':trcount})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Adm1.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['Adm_id'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.branch_id
            request.session['Adm_id'] = member.id 
            Adm=user_registration.objects.filter(id= member.id)
            Num = user_registration.objects.count()
            Num1 = project.objects.count()
            Trainer = designation.objects.get(designation='trainer')
            trcount=user_registration.objects.filter(designation=Trainer).count()
            return render(request,'BRadmin_index.html',{'num':Num,'Num1':Num1,'Adm':Adm,'trcount':trcount})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des3.id).exists():
            member = user_registration.objects.get(
            email=request.POST['email'], password=request.POST['password'])
            request.session['usernameacnt'] = member.designation_id
            request.session['usernameacnt1'] = member.fullname
            request.session['usernameacnt2'] = member.id
            return render(request, 'account_index.html', {'member': member})


        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
    return render(request,'login.html')


def MAN_index(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=m_id)
        return render(request,"MAN_index.html") 
    else:
        return redirect('/')

def MAN_profile(request):
        mem = user_registration.objects.all()
        Num = user_registration.objects.count()
        Man1 = designation.objects.get(designation='Manager')
        Man2 = user_registration.objects.filter(designation = Man1)
        return render(request,'MAN_profile.html',{'Man1':Man2,'num':Num,'mem':mem})  

def MAN_registration(request):
    return render(request,"MAN_registration.html") 
    
def MAN_registrationstaff(request):
    return render(request,"MAN_registrationstaff.html") 
     
def MAN_registrationstudent(request):
    return render(request,"MAN_registrationstudent.html") 

def MAN_currentstaff(request):
    des = designation.objects.get(designation = "staff")
    mem = user_registration.objects.filter(status ="Active" or "active", designation_id = des)
    pay = payment.objects.all()
    return render(request,"MAN_currentstaff.html",{'mem':mem,'pay':pay}) 

def MAN_resignedstaff(request):
    des = designation.objects.get(designation = "staff")
    mem = user_registration.objects.filter(status ="resigned" or "Resigned", designation_id = des)
    pay = payment.objects.all()
    return render(request,"MAN_currentstaff.html",{'mem':mem,'pay':pay})

def MAN_currentstudent(request):
    des = designation.objects.get(designation = "student")
    mem = user_registration.objects.filter(status ="Active" or "active", designation_id = des)
    pay = payment.objects.all()
    return render(request,"MAN_currentstudent.html",{'mem':mem,'pay':pay}) 

def MAN_resignedstudent(request):
    des = designation.objects.get(designation = "student")
    mem = user_registration.objects.filter(status ="resigned" or "Resigned", designation_id = des)
    pay = payment.objects.all()
    return render(request,"MAN_resignedstudent.html",{'mem':mem,'pay':pay})

def MAN_academics(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id) 
        return render(request,'MAN_academics.html',{'mem':mem})
    else:
        return redirect('/')

def MAN_batch(request):
    return render(request,"MAN_batch.html")

def MAN_addbatch(request):
    if request.method == "POST":
            mem = batch()
            mem.batchname = request.POST.get('batch')
            mem.desc = request.POST.get('desc')
            mem.save()
    return render(request,"MAN_addbatch.html")

###########account section##############

def account_index(request):
    return render(request,"account_index.html")


def account_leaverequest(request):
    return render(request,"account_leaverequest.html")

def account_applyleave(request):
    if 'usernameacnt' in request.session:
        if request.session.has_key('usernameacnt'):
            usernameacnt = request.session['usernameacnt']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=usernameacnt)
        if request.method == "POST":
            mem = leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user_id = request.POST.get('pr_id')
            mem.status = "pending"
            mem.save()
        return render(request, 'account_applyleave.html',{'pro':pro})  
    else:
        return redirect('/')
        
def account_requestedleave(request):
    if 'usernameacnt' in request.session:
        if request.session.has_key('usernameacnt'):
            usernameacnt = request.session['usernameacnt']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=usernameacnt)
        var = leave.objects.filter(user_id=usernameacnt).order_by("-id")
        return render(request, 'account_requestedleave.html',{'pro':pro,'var':var}) 
    else:
        return redirect('/')

def account_issues(request):
    return render(request,"account_issues.html")

def account_reportedissue(request):
    if 'usernameacnt' in request.session:
        if request.session.has_key('usernameacnt'):
            usernameacnt = request.session['usernameacnt']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=usernameacnt)
        design=designation.objects.get(designation="manager")
        var=reported_issue.objects.filter(reporter_id=usernameacnt,reported_to_id = design.id)
        return render(request,"account_reportedissue.html",{'var':var,'pro':pro})
    else:
        return redirect('/')
    
def account_issuereply(request,id):
    if 'usernameacnt' in request.session:
        if request.session.has_key('usernameacnt'):
            usernameacnt = request.session['usernameacnt']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=usernameacnt)
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        
        return render(request, 'account_issuereply.html',{'var':var,'pro':pro})
    else:
        return redirect('/')


def account_report_an_issue(request):
    if 'usernameacnt' in request.session:
        if request.session.has_key('usernameacnt'):
            usernameacnt = request.session['usernameacnt']
        else:
            variable="dummy"
        pro1 = user_registration.objects.get(id=usernameacnt)
        pro = user_registration.objects.filter(id=usernameacnt)
        design=designation.objects.get(designation="manager")
        man = user_registration.objects.get(branch_id=pro1.branch_id,designation_id=design.id)
        if request.method == 'POST':
            vars = reported_issue()
            vars.issue=request.POST.get('report')
            vars.reported_date=datetime.now()
            vars.reported_to_id=man.id
            vars.reporter_id=usernameacnt
            vars.status='pending'
            vars.save()
        return render(request,"account_report_an_issue.html",{'pro':pro})
    else:
        return redirect('/')

#########admin section#########

def BRadmin_index(request):
    return render(request,"BRadmin_index.html")



def Mnlogout(request):
    if 'm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def logout5(request):
    if 'usernameacnt' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def ADlogout(request):
    if 'Adm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')