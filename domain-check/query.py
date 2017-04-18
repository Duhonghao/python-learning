# -*- coding: utf-8 -*-




'''
接口采用HTTP，POST，GET协议：
调用URL：http://panda.www.net.cn/cgi-bin/check.cgi
参数名称：area_domain 值为标准域名，例：hichina.com
调用举例：
http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=teapic.com



返回XML：
<?xml version="1.0" encoding="gb2312"?>
<property>
<returncode>200</returncode>
<key>teapic.com</key>
<original>211 : Domain name is not available</original>
</property>



返回 XML 结果说明：
returncode=200 表示接口返回成功
key=***.com表示当前check的域名
original=210 : Domain name is available     表示域名可以注册
original=211 : Domain name is not available 表示域名已经注册
original=212 : Domain name is invalid   表示域名参数传输错误
original=213 : Time out 查询超时
'''


import  requests
import  time


def getDomainStatus(domain_name):
    url = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=%s" % domain_name
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    }
    data = None

    home_req = requests.get(url, data=data, headers=headers)
    xml_data =home_req.content #获取结果xml

    if str("<original>210") in xml_data:
        print "恭喜 : %s 可以注册." % domain_name
    else:
        print "%s 不可注册." % domain_name




def genDomainGroup(domain,type):
    word_array=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    num_array=["0","1","2","3","4","5","6","7","8","9"]
    full_path_list = 'logs/%d_list.txt' % int(time.time())
    full_path_report = 'logs/%d_report.txt' % int(time.time())
    file = open(full_path_list, 'w')
    file = open(full_path_report, 'w')
    file.write(domain)
    char_list=list(domain)
    print char_list
    for  char in  char_list:
        print  char
    file.close()





    print('Done')


def main():
    user_prefix="domain"
    user_suffix=".com"
    domain="domain.com"
    user_number=0 #域名默认格式为全选
    print "Welcome to use python domain query ."
    user_prefix=raw_input("请输入域名前缀[支持*通配符,如ba*du]:")
    user_suffix=raw_input("请输入域名后缀[.com/.cn/.org ...]:")
    domain = user_prefix + user_suffix
    if str("*") in domain:
        user_number = raw_input("请选择域名格式[0:字母+数字(暂不支持) 1:纯字母 2:纯数字(暂不支持)] :")
        print "正在生成组合..."
        genDomainGroup(domain,user_number)
    else:
        getDomainStatus(domain)


if __name__=="__main__":
    # main()
    genDomainGroup("a*cd*e.com",1)
