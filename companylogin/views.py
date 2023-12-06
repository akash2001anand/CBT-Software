from email import message
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages
from rest_framework.renderers import JSONRenderer
from .serializers import *

from .models import *
from general_zone.models import *
from admin_zone.models import *
from centerlogin.models import *


def com_dashboard(request):
    try:
        if request.session['com_id']:
            user_id = request.session.get('com_id')
            Company_data = Company.objects.get(id = user_id)
            return render(request,'com_dashboard.html',{'Company_data':Company_data})
    except KeyError:
        pass
    return redirect('homepage')

def comLogout(request):
    try:
        if request.session['com_id']:
            request.session['com_id'] = None
    except KeyError:
        pass
    return  redirect('homepage')

def addExam(request):
    try:
        if request.session['com_id']:
            return render(request,'add_exam.html')
    except KeyError:
        pass
    return redirect('homepage') 
   
def saveExam(request):
    try:
        if request.session['com_id']:
            if request.method=='POST': 
                name = request.POST.get('exam_name') 
                no = request.POST.get('no_of_questions')  
                marks = request.POST.get('total_marks')  
                exam = Test(test_name = name,no_of_questions=no,total_marks=marks) 
                exam.save()    
                return redirect('com_dashboard')
    except KeyError:
        pass
    return redirect('homepage') 

def ongoing_tests(request):
    try:
        if request.session['com_id']:
            tests = Test.objects.all()
            return render(request,'ongoing_tests.html',{'tests':tests})
    except KeyError:
        pass
    return redirect('homepage') 
    
def completed_tests(request):
    try:
        if request.session['com_id']:
            tests = Test.objects.all()
            return render(request,'completed_tests.html',{'tests':tests})
    except KeyError:
        pass
    return redirect('homepage') 

def centers(request):
    try:
        if request.session['com_id']:
            centers = Center.objects.all()
            return render(request,'centers.html',{'centers':centers})
    except KeyError:
        pass
    return redirect('homepage') 
    
def addCenter(request):
    try:
        if request.session['com_id']:
            if request.method=='POST':
                center_name = request.POST.get('center_name')
                address = request.POST.get('address')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                profile_pic = request.POST.get('profile_pic')
                password = request.POST.get('password')
                center = Center(center_name=center_name,address=address,phone=phone,email=email,profile_pic=profile_pic,password=password)
                center.save()
            return redirect('centers')
    except KeyError:
        pass
    return redirect('homepage') 

def questions(request):
    try:
        if request.session['com_id']:
            questions = Question.objects.all()
            return render(request,'questions.html',{ 'questions':questions})
    except KeyError:
        pass
    return redirect('homepage') 
 
def addQuestion(request):
    try:
        if request.session['com_id']:
            if request.method=='POST':
                question = request.POST.get('question')
                option_1 = request.POST.get('option_1')
                option_2 = request.POST.get('option_2')
                option_3 = request.POST.get('option_3')
                option_4 = request.POST.get('option_4')
                correct_option = request.POST.get('correct_option')
                marks = request.POST.get('marks')
                question = Question(question=question,option_1=option_1,option_2=option_2,option_3=option_3,option_4=option_4,correct_option=correct_option,marks=marks)
                question.save()
            return redirect('questions')
    except KeyError:
        pass
    return redirect('homepage') 

def companyentry(request):
    try:
        if request.session['com_id']:
            return render(request,'com_entry.html')
    except KeyError:
        pass
    return redirect('homepage') 

def passcenter(request):
    try:
        if request.session['com_id']:
            return render(request,'pass_center.html')
    except KeyError:
        pass
    return redirect('homepage') 

def test_data(request,pk):
    test = Test.objects.get(id=pk)
    serializer = TestSerializer(test)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data)

def test_list(request):
    test = Test.objects.all()
    serializer = TestSerializer(test,many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data,safe=False)

