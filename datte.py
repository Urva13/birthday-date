date = int(input())
month= int(input())
ys = input()
year=int(ys)
lyd=ys[2:]
lyd=int(lyd)

yc=(lyd+int(lyd/4))%7

t=(0,3,3,6,1,4,6,2,5,0,3,5)


mc=t[month-1]

c=(2,2,0,6)


cc=c[(int((year-1700)/100)%4)]

day=("sunday","monday","tuesday","wednesday","thuresday","friday","saturday")

lc=int(not(year%4))

print(yc,mc,cc,date,lc)
if(month<3):
    dc=int(yc+mc+cc+date-lc)%7
else:
    dc=int(yc+mc+cc+date)%7
print(day[dc])

