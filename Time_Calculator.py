hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

a = ( mins + dura ) % 60 
b = ( mins + dura ) // 60

c = hour + b 

print (c, ":", a )
