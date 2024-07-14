import random
good_days_count= 0
print("Shelly's happy days are:")
days_of_the_week=["Sunday","Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday"]
temperatures = []
for i in range(7):
	temperatures.append(random.randint(26,41))
	if (temperatures[i]%2==0):
		good_days_count=good_days_count+1
		print(days_of_the_week[i])






highest_temp= max(temperatures)

highest_temp_day=days_of_the_week[temperatures.index(highest_temp)] 

lowest_temp= min(temperatures)

lowest_temp_day=days_of_the_week[temperatures.index(lowest_temp)] 

alltemp=0
for i in temperatures:
	alltemp= alltemp+ i

avg= alltemp/7
above_avg = []
for i in temperatures:
	if i>avg:
		above_avg.append(i)

print("Temperatures for the week:" , temperatures)
print("The highest temperatures and their respective days" ,highest_temp)
print(highest_temp_day)
print("The lowest temperatures and their respective days." ,lowest_temp)
print(lowest_temp_day)
print("Days with temperatures above the average.", above_avg)
print("the average is: ", avg)







