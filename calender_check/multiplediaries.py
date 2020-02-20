

def check_availability(duration, *args):
    index=0
    listlist=[]
    boundslist=[]
    
    for arg in args:
        if args.index(arg) % 2 == 0:
            print(arg)
            listlist.append(arg)
        else:
            boundslist.append(arg)
    for cal in listlist:
                cal[:] = [item.replace(":","") for s in cal for item in s]
                cal[:]= [int(s) for s in cal ]
    print("list list...."+str(listlist))
    for bound in boundslist:
        bound[:] = [s.replace(":","") for s in bound]
    print("boundslist"+str(boundslist))
    cal3=[]
    for cal in listlist:
        cal3+=cal
    print(cal3)
    arr=[]
    list2=[]
    i=0
    for item in cal3:   #convert items in cal3 to PAIRS so can sort/compare them
                            if i>=1:   
                                arr.append(item)
                                list2.append(arr)
                                arr=[]

                                i=0

                            else:
                                arr.append(item)
                                i+=1
    print(list2)
    list2.sort() #now can sort (it realises want to compare FIRST item of each pair)
    print(list2)

    currentlow=2359
    currenthigh=0
  
    for bound in boundslist:
        
                           print("bound - " + bound[0])
                           if int(bound[0]) < currentlow :
                               currentlow=int(bound[0])
                           if int(bound[1]) > currenthigh:
                                  currenthigh=int(bound[1])
                                 
    print(str(currentlow) + "low")
    print(str(currenthigh) + "high")
    available_slots=[]
    for item in list2:
                
                        ind=list2.index(item)
                        print(ind)
                        if ind<len(list2)-1:
                            time1=list2[ind][1]
                            print(time1)
                            time2=list2[ind+1][0]
                            print(time2)
                            hour1=int(str(time1)[:-2]) # extracts the hour (as mins are already "in mins") by splitting FROM last two digits (are guarunteed to be mins)
                            print(hour1)
                            hour1=hour1*60 #times hour by sixty then add this to the mins to get total mins
                            hour2=int(str(time2)[:-2])
                            hour2=hour2*60
                            min1=int(str(time1)[-2:])
                            min2=int(str(time2)[-2:])
                            total1=hour1+min1
                            print(str(total1)+"<total1")
                            
                            total2=hour2+min2
                            print(str(total2)+"total2")
                            
                            difference = total2 - total1
                            print("diff >" +str(difference))
                            
                            if int(time1)>int(currentlow) and int(time2)<int(currenthigh) and difference > 0 and difference >(duration+5):   # a negative difference means that the first time is LATER than the second - i.e there IS NO GAP between them (as first runs over second) so cannot book, therefore discard these
                                            print(str(time1)+str(time2) + "is a free slot!")
                                            available_slots.append([time1,time2])                #giving a five min leeway
                            else:
                                 pass
    difference = time2 - time1
    hours = difference // 100
    minutes = difference % 100
    return available_slots
    
   
result=check_availability(30,[["08:10","08:20"],["11:30","15:30"],["16:22","17:00"],["13:30","15:45"]], ["09:00","14:00"],[["08:00","09:00"],["8:45","8:50"],["12:00","13:45"]],["07:00","18:00"],[["02:00","05:00"]],["24:00","08:00"])
print(result)
availableslots2=check_availability(10,[["09:00","10:00"],["15:00","16:30"]],["10:00","18:00"],[["10:30","11:45"],["16:50","16:55"],["17:00","17:35"]],["13:00","20:00"],[["11:00","11:30"]],["09:00","17:00"] )
print("|available")
print(availableslots2)

