# -*- coding: utf-8 -*-
import random

import  requests
import time



#
# mt4array=[2065203571,2065204790,2065207694,2065204407,2065204147,1065208780,2065203970,2065204413,2065205263,2065206810,
#           2065206951,1065432205,2065208093,2065205708,2065203836,1065181360,2065204178,1065211811,2065204116,1065213000]



mt4array=[2065204407]
print
print
print  " Begin API server Test ..."
print
print

def GetInfoUrl(mt4array):
    foreachNum=100
    success = 0
    failed = 0
    totalTime=0
    JsonData=None
    for i in range(foreachNum):

        time.sleep(0.01)
        randNum=random.randint(0, len(mt4array)-1)



        print ""
        print "==========MT4:%d,order : %d" % (mt4array[randNum],randNum)+"=========="
        beginTime=time.time()
        result=""
        url = "http://localhost/marginlevel?isReal=true&account=%d" % mt4array[randNum]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        }
        data = None

        try:
            HomeReq = requests.get(url, data=data, headers=headers)
            HomeData = HomeReq.content
         #   HomeData=HomeData.replace("\\", "").replace("\"{", "{").replace("}\"", "}")
            #get margin data from json
            #marginLevel=json.dumps(JsonData['marginLevel'],ensure_ascii=False)
            #print marginLevel
            #margin=int(marginLevel['Margin'])
            #print  margin
            #print  margin

            if str(mt4array[randNum]) in HomeData:

                if str("\"Balance\":0.0") in HomeData:
                    failed += 1
                    print ">>>" + HomeData
                    result = "Failed:balance can not be null , request url : %s" % ("!!!!!!!!!!!!!!!!!!!!!!!Money error", url)
                else:
                    success+=1
                    result = "Success:"
                print ">>>"+HomeData
            else:
                failed+=1
                print ">>>" + HomeData
                result = "Failed:error info:%s , request url : %s" % ("Json formate error", url)





        except Exception, e:
            failed+=1
            result="Failed:error info:%s , request url : %s"  %(e.message,url)
            print str(JsonData)
        endTime = time.time()
        usedTime=endTime-beginTime
        totalTime+=usedTime
        #sigle result
        print  "%s , time used : %d . [begin:%d,end:%d]" %(result,usedTime,beginTime,endTime)

    averageTime= totalTime/foreachNum


    print
    print
    print "Stop API server Test ..."
    print
    print
    print " Here is the report :"
    print " %d success , %d faild , " %(success,failed)
    print " totaltime:%d" %totalTime
    print " averageTime:%d" %averageTime








GetInfoUrl(mt4array)






