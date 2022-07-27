from urllib import request
from django.shortcuts import render
from django.http import  HttpResponseBadRequest
from django.template import loader

def show_login(rquest):
    dict = {
        "author_name" : "أحمد عمار الزرعد" ,
        "discripshin" : "صفحة تسجيل الدخول" ,
        "page_title" : "صفحة تسجيل الدخول" ,
    }
    return render(rquest , "mainsite/log_in_page.html" , dict )


def show_logup(request):
    dict = {
        "author_name" : "أحمد عمار الزرعد" ,
        "discripshin" : "صفحة انشاء حساب جديد" ,
        "page_title" : "صفحة انشاء حساب جديد" ,
    }
    return render(request , "mainsite/log_up_page.html" , dict )