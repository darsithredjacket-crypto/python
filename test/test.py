mydict={
    "student1":{"name":"tony","score":57, "ttl marks":100},
    "student2":{"name":"yasmine","score":79, "ttl marks":100},
    "student3":{"name":"priya","score":86, "ttl marks":100},
    "student4":{"name":"nikil","score":90, "ttl marks":100},
    "student5":{"name":"alwin","score":78, "ttl marks":100},
}

total=0
for i in mydict:
    total= total + mydict[i]["score"]

avg= total/5
print(avg)

print(mydict.get("student2"))


