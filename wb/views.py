from django.shortcuts import render
import traceback
from django.http      import HttpResponse
#Models
from .models import (
user_info,
user_info_update,
user_account
)

import urllib
from urllib import request
#import urllib2
#import cookielib
import http.cookiejar
from .lzzy3x import lzzy
from bs4 import BeautifulSoup

# Create your views here.

'''
def signup(request):

	if(not request.method=='POST'):
		return render(request,'index.html')

	try:
		userid_ = request.POST.get("userid")
		name_   = request.POST.get("name")
		phone_  = request.POST.get("phone")
		id_card_= request.POST.get("id_card")
		bank_card_ = request.POST.get("bank_card")
		user_info.objects.create(   student_id=userid_,  #学号
                                    name=name_,         #姓名
                                    phone=phone_,       #手机号
                                    idCard=id_card_,   #身份证号
                                    bankCard=bank_card_#银行卡号
)
		return HttpResponse("登记成功！")
	except Exception:
		return HttpResponse("登记错误！请重新返回链接登记！\n错误信息："+traceback.format_exc())
'''


def login(request):

	return render(request,'login.html')


post_data={
                        "__VIEWSTATE":"/wEPDwUJOTYxNDY3OTc0D2QWAgIBD2QWAgIHDxBkDxYBAgEWAQUJ6L6F5a+85ZGYZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFDUJ1dHRvbl/nmbvpmYY5+nSLBhHqz30JO3nWw0VfDqWktA==",
                        "__EVENTVALIDATION":"/wEWCQLeuKaSDQLep8vjCAKu8uE5AvKm2soEAvLJzeAMAvWZ8TkC6fHPnw8CwsjN4QICyKiipgEA9oXb2ioPAMKqh7by35bI/EDoHg==",
                        "txt_卡学号":"",
                        "txt_密码":"",
                        "Button_登陆.x":"72",
                        "Button_登陆.y":"35",
                        "Rad_角色":"学生"
                }
loginUrl = 'http://jw.lzzy.net/st/login.aspx'
def signup(request):

	if(not request.method=='POST'):
		return render(request,'login.html')

	try:
		student_id=request.POST.get("st_id")
		student_pwd=request.POST.get("st_pwd")
		post_data["txt_卡学号"]=student_id
		post_data["txt_密码"]=student_pwd
		name = Auth(student_id,student_pwd)

		if(name!=None):
			if(user_account.objects.filter(student_id=student_id).count() == 0):
				user_account.objects.create(student_id=student_id,student_pwd=student_pwd)
			request.session['st_id']=student_id
			return render(request,'index.html',{"name":name["name"]})#-------------------------------------------
		else:
			return render(request,'login.html',{'script':"alert",'wrong':'账号密码误'})
	except:
		return render(request,'login.html',{'script':'alert','wrong':'账号密码错误'})#HttpResponse('Ex:'+traceback.format_exc())


def Auth(account,password):
        cookie_filename = account
        cookie_path = '/home/admin/student/StudentManage/login/'
        gradeUrl = 'http://jw.lzzy.net/st/student/st_edit.aspx'
        lz = lzzy(cookie_path+cookie_filename,account,password)
        ht = lz.get_connect_url(gradeUrl,'UTF8')
        try:
            soup = BeautifulSoup(ht,"html5lib")
            st_data={}
            st_data["name"]= soup.find("input",{'id':'txt_姓名'}).get('value')#.get_text()#.encode('UTF8')#
            return st_data
        except:
            return None


def auth(request):

	if(request.method == 'POST'):
		try:
			st_id = request.session.get('st_id')
			home_c  = request.POST["home_addr_City"]
			home_q	= request.POST["home_addr_Qu"]
			home_x	= request.POST["home_addr_xx"]
			home=home_c+home_q+home_x
			fphone= request.POST["fphone"]
			mphone= request.POST["mphone"]
			user_info_update.objects.create(student_id=st_id,home_addr=home,father_phone=fphone,mother_phone=mphone)
			return HttpResponse("登记成功!")
		except:
			 return HttpResponse('你已经登记过信息啦~')

	else:
		return render(request,'login.html')
