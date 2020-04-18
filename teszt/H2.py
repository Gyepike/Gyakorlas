import  datetime
mynow = datetime.datetime.now()
#print(mynow)

x = 10
y = "10"

sum1 = x + x
sum2 = y + y

print(sum1)
print(sum2)

student_grades = list(range(0,10,1))

#student_grades = range(0,10,1)
#print(list(student_grades))
print(student_grades)
#print(dir(student_grades))
alma = [1,4,5]
print("Alma list {}".format(alma))

alma.reverse()
print("Alma list {}".format(alma))
#print(dir(alma))
#print(dir(int))
#print(int.__abs__(-2))
#print(help(int.__abs__))
#print(help(str.upper))
print("hello".title())
#print(dir(dic))
print(sum(student_grades))
print(student_grades.count(2)) # count 2 number
#print(dir(__builtins__ ))
ki = "AAA".lower()
print(dir())

Munyi = "Munyoka"
kiiratas = "Az en nevem %s " %Munyi
print(kiiratas)
print("Az en neve {}".format(Munyi))
print(f"Az en neve {Munyi}")

name = "Mate"
name2 = "Tamas"

ki = "A  %s es %s barato2" %(name,name2)
print(ki)
ki = f"A  {name} es {name2}  baratok"
#print(ki)


def nagybetu(neve):
    return "Neve nagybetuvel_ : %s" %neve.title()

#print(nagybetu("alfonz"))

list = [3,6,8,11]
tanar = "tanar ur"

for i in list:
    # print(f" {i} Tanar ur")
    print("Az szamok  %s  " %i)
    #print("Az en nevem  %s  %s" %(i, tanar))

