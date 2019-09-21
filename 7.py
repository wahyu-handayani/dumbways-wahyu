from pymongo import MongoClient
democlient=MongoClient()
myclient=MongoClient('localhost',27017)
mydb=myclient["PUNYA_WAHYU"]
mycoll=mydb["users"]
mycoll2=mydb["posts"]
mycoll3=mydb["comments"]

mylist=[{"id":1,"username":"Bulan","id_work":1,"id_salary":1},
        {"id":2,"username":"Bintang","id_work":2,"id_salary":2}]
mycoll.insert_many(mylist)

mylist2=[{"id":1,"title":"Tugas 1","content":"IT","createdBy":1},
         {"id":2,"title":"Tugas 2","content":"Keuangan","createdBy":2}]
mycoll2.insert_many(mylist2)

mylist3=[{"id":1,"comment":"semangat selalu","postId":1},
         {"id":2,"comment":"hidup itu indah","postId":2}]
mycoll3.insert_many(mylist3)

def get_multiple_data():
    """
    get document data by document ID
    :return:
    """
    mylist = mycoll.find()
    return list(mylist)
x=get_multiple_data()
print(x)