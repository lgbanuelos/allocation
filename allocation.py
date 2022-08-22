from datetime import date, time, datetime
import array as arr

class Allocation:
	def __init__(self, customer, price, check_in_day, check_out_day):
		self.customer = customer
		self.price = price
		self.check_in_day = check_in_day
		self.check_out_day = check_out_day
	def __str__(self) -> str:
		return f"customer: {self.customer}, price: {self.price}, check in: {self.check_in_day}, check_out: {self.check_out_day}"

listAllocations=[]
firstRequest=Allocation("Pedro",1350.50,date(2022,3,10),date(2022,3,20))
SecondRequest=Allocation("Luis",1400.50,date(2022,3,15),date(2022,3,22))
ThirdRequest=Allocation("Juan",1350,date(2022,3,21),date(2022,3,24))
FourthRequest=Allocation("Carlos",1350,date(2022,3,26),date(2022,3,31))
FifthRequest=Allocation("Cesar",1600,date(2022,3,27),date(2022,4,2))
sixthRequest=Allocation("Martha",1350,date(2022,3,31),date(2022,4,5))
listAllocations.append(firstRequest)
listAllocations.append(SecondRequest)
listAllocations.append(ThirdRequest)
listAllocations.append(FourthRequest)
listAllocations.append(FifthRequest)
listAllocations.append(sixthRequest)
listAllocations.append(Allocation("X", 10000,date(2022,3,11),date(2022,4,5)))

listAllocations = sorted(listAllocations, key= lambda x: x.check_in_day)

for a in listAllocations:
	print(a)


def BestRequest(Allocations):
	limit=len(Allocations)
	counter=0
	bestDeal=[]
	blackList=[]
	while counter < (limit-1):
		print("===============================")
		for item in blackList:
			print(item)
			if  Allocations[counter] == item:
				counter +=1
				continue
		print("--------------------------------")
		counter2=counter
		overlapping=False
		while counter2< (limit-1):
			diffRequest=Allocations[counter].check_out_day - Allocations[counter2+1].check_in_day
			if (diffRequest.days<=0):
				counter2 += 1
				continue
			else:
				diffRequestA= Allocations[counter].check_out_day - Allocations[counter].check_in_day
				diffRequestB= Allocations[counter+1].check_out_day - Allocations[counter+1].check_in_day
				TotalPaidA = (diffRequestA.days*Allocations[counter].price)
				TotalPaidB =(diffRequestB.days*Allocations[counter2+1].price)
				if (TotalPaidA > TotalPaidB):
					found=False
					for item in blackList:
						if Allocations[counter+1] == item:
							found=True
							break
						else:
							found=False
					if found == False:
						blackList.append(Allocations[counter+1])
					counter2 += 1
					continue
				else:
					found=False
					for item in blackList:
						if Allocations[counter+1] == item:
							found=True
							break
						else:
							found=False
					if found == False:
						blackList.append(Allocations[counter])
					break
			counter2 += 1
		counter += 1
	bestDeal = list(set(Allocations) - set(blackList))
	return bestDeal

AcceptRequests=BestRequest(listAllocations)


print("These are the names of the customers that you should accept")
for obj in AcceptRequests:
	print(obj.customer)
