#Multi-Threading
#For threading we have to use function name as run bcs it is an inbuild function and instead of calling run have to use start.


# from threading import *
# from time import *
#
# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)
#
# t1 = Hello()
# t2 = Hi()
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()
#
# print("Bye")

#
#
# import time
# import threading
# def calc_squre(numbers):
#     print("Cal the square ")
#     for n in numbers:
#         time.sleep(0.2)
#         print("Square : ",n*n)
# def calc_cube(numbers):
#     print("Cal the cube ")
#     for n in numbers:
#         time.sleep(0.2)
#         print("Cube : ",n*n*n)
# arr = [2,3,4,6]
# t = time.time()
# t1 = threading.Thread(target=calc_squre,args=(arr,))
# t2 = threading.Thread(target=calc_cube,args=(arr,))
#
# t1.start()
#
# t2.start()
#
# t1.join()
# t2.join()
# print("Done in : ",time.time()-t)
#


#New Example

import threading
import time
# start = time.perf_counter()
# def do_something():
#     print("Sleep 1 second")
#     time.sleep(1)
#     print("Done sleeping \n")

#Method 1 :
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

#Method 2 : #Threading in loop
# threads = []
# for _ in range(10): #using _ in the loop is basically to throw away variable
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)
# for thread in threads:
#     thread.join()
#
# finish = time.perf_counter()
#
# print(f"Finish in {round(finish - start,2)} second
#


#New Example
#
# import threading
# import time
# start = time.perf_counter()
# def do_something(seconds):
#     print(f"Sleep {seconds} second(s)")
#     time.sleep(seconds)
#     print("Done sleeping \n")
#
#
# #Method 1 : #Threading in loop
# threads = []
# for _ in range(10): #using _ in the loop is basically to throw away variable
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
# for thread in threads:
#     thread.join()
#
# finish = time.perf_counter()
#
# print(f"Finish in {round(finish - start,2)} seconds(s)")



#New method

# import concurrent.futures
# import time
#
# start = time.perf_counter()
#
# def do_something(seconds):
#     print(f"Sleeping {seconds} second(s)")
#     time.sleep(seconds)
#     return f"Done Sleeping .....{seconds}"
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5,4,3,2,1]
#     result = [executor.submit(do_something,sec) for sec in secs]
#     for f in concurrent.futures.as_completed(result):
#         print(f.result())
# finish = time.perf_counter()
# print(f"Finish in {round(finish - start,2)} second(s)")


#New Method

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)")
    time.sleep(seconds)
    return f"Done Sleeping .....{seconds}"
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

finish = time.perf_counter()
print(f"Finish in {round(finish - start,2)} second(s)")
