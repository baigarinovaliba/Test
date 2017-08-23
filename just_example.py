import pyodbc

myServername = 'ALIBEK-PC'
myDatabase = 'North'
myUsername = 'sa'
myPassword = '1q2w3e4r5t'



myConnection = pyodbc.connect(' Driver={SQL Server};'
                              ' Server='+myServername+';'
                              ' Database='+myDatabase+';'
                              ' uid='+myUsername+';'
                              ' pwd='+myPassword+';' )

cursor=myConnection.cursor()



mySQLQuery = ("""
SELECT FirstName, LastName
FROM dbo.Employees
Where country = 'USA'
""" )




cursor.execute(mySQLQuery)
results = cursor.fetchall()

for row in results:
    Name=row[0]
    Surname=row[1]
  #  print("Name: "+Name+" Surname: "+Surname)
    with open('qwert.txt','a+') as f:
        f.write("Name: "+Name+" Surname: "+Surname+" ")
myConnection.close()
f.close()

f = open('qwert.txt','r')
res = f.read()
print(res)
f.close()