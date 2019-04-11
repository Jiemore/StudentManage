#lzzy3x 支持Python3.x的校园访问模块
import urllib
from urllib import request
import http.cookiejar

class lzzy():
    def __init__(self,filename,account,password):
        #储存Cookie
        cookie = http.cookiejar.MozillaCookieJar(filename)
        self.opener = urllib.request.build_opener(request.HTTPCookieProcessor(cookie))
        #设置请求头，模拟浏览器访问
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')]
        self.get_connect_login(account,password)
        cookie.save(ignore_discard=True, ignore_expires=True)

    def get_connect_login(self,account,password):
        loginUrl = 'http://jw.lzzy.net/st/login.aspx'
        post_data = {
                        "__VIEWSTATE":"/wEPDwUJOTYxNDY3OTc0D2QWAgIBD2QWAgIHDxBkDxYBAgEWAQUJ6L6F5a+85ZGYZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFDUJ1dHRvbl/nmbvpmYY5+nSLBhHqz30JO3nWw0VfDqWktA==",
                        "__EVENTVALIDATION":"/wEWCQLeuKaSDQLep8vjCAKu8uE5AvKm2soEAvLJzeAMAvWZ8TkC6fHPnw8CwsjN4QICyKiipgEA9oXb2ioPAMKqh7by35bI/EDoHg==",
                        "txt_卡学号":"",
                        "txt_密码":"",
                        "Button_登陆.x":"72",
                        "Button_登陆.y":"35",
                        "Rad_角色":"学生"
                }
        post_data["txt_卡学号"] = account
        post_data["txt_密码"] = password
        self.opener.open(loginUrl,urllib.parse.urlencode(post_data).encode(encoding='UTF8'))

    def get_connect_url(self,gradeUrl,fcode):
        result = self.opener.open(gradeUrl)
        return result.read().decode(fcode)