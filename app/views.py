from django.shortcuts import render

# Create your views here.

def if_else(request):
    d={'a':100,'b':200}
    return render(request,'if_else.html',d)

def if_elif(request):
    d={'a':1000,'b':200,'c':400}
    return render(request,'if_elif.html',d)

def nested_if(request):
    d={'a':100,'b':2000,'c':4000}
    return render(request,'nested_if.html',d)

def for_loop(request):
    d={'name':'Arun'}
    return render(request,'for_loop.html',d)


#def for_loop(request):
    l=[77,11,22,33,44,55,66,77,88]
    for num in l:
        if [num] > [num+1]:
            [num]
    print(num)
    d={'l':num}

    return render(request,'for_loop.html',d)