import time,datetime


def Time2Timestamp(SecondStyles):

    if SecondStyles== "ms":
        # obtain the sys current time(ms_level)
        now_time = datetime.datetime.now()  
        return  now_time

    elif SecondStyles=="s":
        #obtain the sys current time(s_level)
        time_now = int(time.time())         
        #Convert the localtime 
        time_local = time.localtime(time_now)
        #transform  the localtime to format like (2017-09-16 11:28:54)
        dtime= time.strftime("%Y-%m-%d %H:%M:%S",time_local) 
        # transform the str time to  Arraytime styles
        timeArray = time.strptime(dtime, "%Y-%m-%d %H:%M:%S")
        # transform the arraytime to the timestamp
        timestamp = int(time.mktime(timeArray))
        return  timestamp

   
# tt=Time2Timestamp("s")
# print(tt)

# TC=[1,2,3,4]
# Now_Timestamp=Time2Timestamp("s")
# print(Now_Timestamp)
# for timecount in range(len(TC)-1,-1,-1):
#     print("Please Wait for the "+str(TC[timecount])+" Seconds")


# print("Input StartTime Like: 10-12")
# StartTime=input('Input the Time:')
# StartTimeTemp=StartTime.split('-')
# print(StartTimeTemp)
# StartTime='2018-12-17'+' '+str(StartTimeTemp[0])+':'+str(StartTimeTemp[1])+':'+'00'
# print(StartTime)
# timeArray=time.strptime(StartTime, "%Y-%m-%d %H:%M:%S")
# print(timeArray)
# tt=int(time.mktime(timeArray))
# print(tt)
