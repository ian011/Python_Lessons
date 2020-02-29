person = dict(Name="ian",Age=21,Status="single",Salary=100000)
print(person)
print(person["Name"])
person['Name']="Ian Akira"  #edits pre existing information
person["salary"]="80000"
person["insurance"]="not yet"
person["hudumanumber"]="6618"  #adds new key
del person["hudumanumber"]  #deletes any new key
print(person)