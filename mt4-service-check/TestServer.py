
import  requests
import time




mt4array=[2065203906,2065203924,2065203894,2065203899,2065204018,2065204025,2065204025,2065203994,2065204036,2065204088,
          2065204056,2065204039,2065204174,2065204393,2065203931,2065203964,2065203975]
# mt4array=[2065203906]
print
print
print  " Begin API server Test ..."
print
print

def GetInfoUrl(mt4array):
    success = 0
    failed = 0
    totalTime=0
    JsonData=None
    for i in range(len(mt4array)):
        print ""
        print "==========MT4:%d" % mt4array[i]+"=========="
        beginTime=time.time()
        result=""
        url = "http://localhost/marginlevel?isReal=true&account=%d" % mt4array[i]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        }
        data = None

        try:
            HomeReq = requests.get(url, data=data, headers=headers)
            HomeData = HomeReq.content
            HomeData=HomeData.replace("\\", "").replace("\"{", "{").replace("}\"", "}")
            #get margin data from json
            #marginLevel=json.dumps(JsonData['marginLevel'],ensure_ascii=False)
            #print marginLevel
            #margin=int(marginLevel['Margin'])
            #print  margin
            #print  margin

            if str(mt4array[i]) in HomeData:
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

    averageTime= totalTime/len(mt4array)


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






