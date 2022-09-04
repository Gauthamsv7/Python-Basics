#Decorators : we can add extra features to func

def div(a,b):
    print(a/b)

def smart(func):


    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div = smart(div)
div(2,4)
