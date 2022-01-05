from django.http import HttpResponse
from django.shortcuts import render
from Q.dbconn import cus, A

def create(request):
    cus.execute('create table student(id int primary key, name varchar(50), email varchar(30))')
    A.commit()
    A.close()
    return HttpResponse("TABLE IS CREATED SUCCESSFULLY")
if __name__ == "__main__" :
    create()

def insert(request,id,name,email):
    query = f"INSERT INTO STUDENT (id,name,email) VALUES ('{id}', '{name}', '{email}')"
    cus.execute(query)
    A.commit()
    A.close()
    return HttpResponse({cus.rowcount},"RECORD INSERTED SUCCESSFULLY")
if __name__ == "__main__" :
    create()

def select(request):
    cus.execute('select * from student')
    a = cus.fetchall()
    print(a)
    A.commit()
    return render(request,'select.html',{'a':a})
if __name__ == "__main__" :
    select()

def update(request,id,name,email):
    u = [name,email,int(id)]
    cus.execute('update set name=%s,email=%s where id=%s', u)
    A.commit()
    return HttpResponse('RECORD UPDATED SUCCESSFULLY')
if __name__ == "__main__" :
    update()

def delete(request,id):
    d = [int(id)]
    cus.execute('delete from student where id=%s', d)
    A.commit()
    return HttpResponse('RECORD DELETED SUCCESSFULLY')
if __name__ == "__main__" :
    delete()