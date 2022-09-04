#Here in the below code we are doing squaring of nums and sharing of the memory is also done
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method

import time
import multiprocessing

t = time.time()
result=[]
def calc_square(numbers):

    for idx, n in enumerate(numbers): #idx,n denotes the index and n=number that uses enumerate method which is more like iteration
        result[idx] = n*n
        print("Inside Result : " + str(result))

def calc_cube(numbers):
    for n in numbers:
    print("Cube :"+str(n*n*n))


if __name__ == "__main__":
    arr = [2,3,4,6]
    result = multiprocessing.Array("i",3) #Here i denotes the integer and 3 show the values taken
    p1 = multiprocessing.Process(target=calc_square,args=(arr,result))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Done")
    print("Outside Result : "+ result[:])

    print("Done in : ", time.time() - t)