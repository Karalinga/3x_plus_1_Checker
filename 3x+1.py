# #3x+1 problem
# import timeit
# import _thread
# start = timeit.default_timer()
# start_number = 295147905179352825856
# #x = int(input("Enter your number: "))
# count  = 0
# x = int(848484848844/10000)
# ser_val = start_number+848484848844/10000
# def problemLoop(start_number,x):
# 	for i in range(start_number,start_number+x):
# 		print(i)
# 		while(x!=1):
# 			if(x%2==0):
# 				x = int(x/2)
# 			else:
# 				x = 3*x +1
# 			#count +=1

# 			#print(x)
# 		#print(count)
# 		#count = 0
# #problemLoop(start_number,int(x*1/3))
# #problemLoop(start_number,int(x*1/3))
# try:
# 	_thread.start_new_thread(problemLoop,(start_number,int(x*1/3),))
# 	_thread.start_new_thread(problemLoop,(int(x*1/3),int(x*2/3)))
# 	# _thread.start_new_thread(problemLoop,(x*2/3,x))
# except:
# 	print("Couldn't start thread.")
# stop = timeit.default_timer()

# print("Program finished after",count,"steps and took",stop-start,"time to complete.")
# #taking an incredibly long time at some point between start + 10 000 and 848484848844
# #thread.start_new_thread
# #_thread.start_new_thread(problemLoop,(start_number,ser_val*1/3))


#3x+1 problem
import timeit
import threading

start = timeit.default_timer()
start_number = 295147905179352825856
#x = int(input("Enter your number: "))
count  = 0
x = int(848484848844/10000)
ser_val = start_number+848484848844/10000
def problemLoop(start_number,x):
    for i in range(start_number,start_number+x):
        #print(i)
        while(x!=1):
            if(x%2==0):
                x = int(x/2)
            else:
                x = 3*x +1


threads = []
for i in range(3):
    if(i == 0):
        t = threading.Thread(target=problemLoop, args=(start_number, int(x/3), ))
    else:
        t = threading.Thread(target=problemLoop, args=(int(x*i/3), int((x*(i + 1))/3), ))
    threads.append(t)
    t.start()


stop = timeit.default_timer()

print("Program done after: ", stop-start)