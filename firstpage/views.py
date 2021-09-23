from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np


import mysql.connector
from mysql.connector.constants import ClientFlag
mydb = mysql.connector.connect(host="localhost", user="root", passwd="rahara2004", database="employee")
mycursor = mydb.cursor()



def index(request):
    context={'a':'Hello user'}
    return render(request, 'index.html',context)
    #return HttpResponse({'a':1})



def emp_id(request):
    #print (request)
    if request.method == 'POST':
         temp={}
         temp['emp_no']=request.POST.get('emp_no')
         temp['gender']=request.POST.get('gender')
         temp['hiredate']=request.POST.get('hiredate')

    x=int(temp['emp_no'])
    mycursor.execute("select * from employee where emp_no={}".format(x))
    
    result=mycursor.fetchall()

     
    context={}
    context['gender']=result[0][4]
    context['firstname']=result[0][2]
    return render(request, 'abc.html',context)

def emp_fromdate(request2):
    #print (request)
    if request2.method == 'POST':
         temp={}
         #temp['emp_no']=request2.POST.get('emp_no')
         temp['gender']=request2.POST.get('gender')
         temp['hiredate']=request2.POST.get('hiredate')
         temp['filter']=request2.POST.get('filter')
    global y, z, k 
    y=temp['gender']
    z=temp['hiredate']
    k=temp['filter']
    mycursor.execute("select * from employee where gender='{}' and hire_date{}'{}'".format(y,k,z))
    
    result2=mycursor.fetchall()

    mycursor.execute("select count(*) from employee where gender='{}' and hire_date{}'{}'".format(y,k,z))
    global result3
    result3=mycursor.fetchall()

    first_name = []
    emp_id = []
    hire_date=[]

    for a_tuple in result2:
        first_name.append(a_tuple[2])
    context2={}
    
    for a_tuple in result2:
        emp_id.append(a_tuple[0])

    for a_tuple in result2:
        hire_date.append(a_tuple[5])

    mylist = zip(first_name, emp_id, hire_date)
    #DEFINING DICTIONARY TO RENDER IN HTML
    context2 = {
            'mylist': mylist,
            'count':result3,
        }
    return render(request2, 'date.html',context2)


def order(request3):
    if request3.method == 'POST':
         temp={}
         temp['order']=request3.POST.get('hire_date')
    h=temp['order']
    mycursor.execute("select * from employee where gender='{}' and hire_date{}'{}' order by {}".format(y,k,z,h))
    result4=mycursor.fetchall()
    first_name = []
    emp_id = []
    hire_date=[]

    for a_tuple in result4:
        first_name.append(a_tuple[2])
    context2={}
    
    for a_tuple in result4:
        emp_id.append(a_tuple[0])

    for a_tuple in result4:
        hire_date.append(a_tuple[5])

    mylist = zip(first_name, emp_id, hire_date)
    context3 = {
            'mylist': mylist,
            'count': result3
        }
    
    return render(request3, 'date.html',context3)

