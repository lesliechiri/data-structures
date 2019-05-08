def tens(list):
    a = []
    for x in list:
        y = x*10
        a.append(y)
    return a
    

def bee(list):
    s = [x*x for x in list] 

    return s

def sorted(a,b):
    c = a+b
    c.sort()
    return c

    

def range_sum(n):
    y = []
    
    for x in range(1,n+1):
        y.append(x)
        z = sum(y)
        
    return z


def largest(list):

    return max(list)


def smallest(list):

    return min(list)

def my_modulus():
    a = dict()
    
    
    for x in range(10,20):
        if x%3==0:
            a[x]=x%3
        else:
            a[x]=x%3  
        
    return a 


def data():
    student1 = {"name":"Irene","balance":1000}
    student2 = {"name":"Pauline","balance":2000}
    student3 = {"name":"Naima","balance":3000}
    student4 = {"name":"Rose","balance":1000}
    students = [student1,student2,student3,student4]

    for student in students:
        sms = "hello {},your balance is{}".format(student["name"],student["balance"])
        print(sms)              








