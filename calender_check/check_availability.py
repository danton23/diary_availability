def check_availability(cal1,bound1,cal2,bound2,duration):    #allows user to enter TWO calenders plus earliest and latest for both and desired meeting duration and see if there are any avaiable times for them BOTH to have a meeting with each other
            print(str(cal1)+"<cal1")
            print(bound1)
            print(cal2)
            print(bound2)
            print(duration)
            cal1[:] = [item.replace(":","") for s in cal1 for item in s]
            cal1[:]= [int(s) for s in cal1 ]
            bound1[:] = [s.replace(":","") for s in bound1]
            cal2[:] = [item.replace(":","") for s in cal2 for item in s]
            cal2[:]= [int(s) for s in cal2 ]
            bound2[:] = [s.replace(":","") for s in bound2]
            cal3=cal2+cal1
            i=0
            arr=[]
            list2=[]
            for item in cal3:
                            if i>=1:   
                                arr.append(item)
                                list2.append(arr)
                                arr=[]

                                i=0

                            else:
                                arr.append(item)
                                i+=1
            print("cal 3>" +str(cal3))
            list2.sort()
            print(list2)
            
            if int(bound1[0])> int(bound2[0]):
                       earliest=bound2[0]
            else:
                earliest=bound1[0]
            if int(bound1[1])<int(bound2[1]):
                       latest=bound1[1]
            else:
                latest=bound2[1]
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
                            
                            if int(time1)>int(earliest) and int(time2)<int(latest) and difference > 0 and difference >(duration+5):   # a negative difference means that the first time is LATER than the second - i.e there IS NO GAP between them (as first runs over second) so cannot book, therefore discard these
                                            print(str(time1)+str(time2) + "is a free slot!")
                                            available_slots.append([time1,time2])                #giving a five min leeway
                            else:
                                 pass
                          
            
            print(str("earliest="+earliest))
            print(str("latest="+latest))
            difference = time2 - time1
            hours = difference // 100
            minutes = difference % 100
            return available_slots


availableslots=check_availability([["08:10","08:20"],["11:30","15:30"],["16:22","17:00"],["13:30","15:45"]], ["09:00","14:00"],[["08:00","09:00"],["8:45","8:50"],["12:00","13:45"]],["07:00","18:00"],30)
print(availableslots)
