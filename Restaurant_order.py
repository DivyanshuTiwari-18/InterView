print("               //////////////////////////////////////////////////")
print("               \\\                                              //")
print("               //        Welcome To Our Restaurant             \\\\")
print("               \\\                                              //")
print("               //////////////////////////////////////////////////")
menu=['Coffee','Tea','Cappuccino','Shake']
menu_price=['40','20','50','60']
print("\n                        Here is The Menu :\n")
for i in range(len(menu)):
	print("                            ",i+1,'->',menu[i],"   @ Rs. ",menu_price[i])
Ordered_List=[]
Ordered_List_Bill=[]
Total = 0
def Bill2():
	global Total
	for x in range(0, len(Ordered_List_Bill)):
		Total = Total + Ordered_List_Bill[x]
def take_order(order2):
	global Bill
	if order2 in menu:
		if order2 == menu[0]:
			Ordered_List.append(menu[0])
			order_confirm()
		elif order2 == menu[1]:
			Ordered_List.append(menu[1])
			order_confirm()
		elif order2 == menu[2]:
			Ordered_List.append(menu[2])
			order_confirm()
		elif order2 == menu[3]:
			Ordered_List.append(menu[3])
			order_confirm()
					
	else:
		print("\n                        Sorry, I don't Understand ")
		print("                        Only Menu options are Available ")
		order1()			
def order_confirm():
	confirmation = input("\n                        Want to add something Else (Y/N): ")
	if confirmation == 'Y':
		order1()
	elif confirmation == 'N':
		print("\n                        Your Order is: ")
		print("                        ***********************************")
		for i in range(len(Ordered_List)):
			print("                        *       ",i+1,".",Ordered_List[i])
		if len(Ordered_List)>=0:
			for i in range(len(Ordered_List)):
				if Ordered_List[i]=="Coffee":
					Ordered_List_Bill.append(40)
				if Ordered_List[i]=="Tea":
					Ordered_List_Bill.append(20)
				if Ordered_List[i]=="Cappuccino":
					Ordered_List_Bill.append(50)
				if Ordered_List[i]=="Shake":
					Ordered_List_Bill.append(60)
			Bill2()
			print("                        ***********************************")
			print("                               Total = Rs.",Total)
		print("               ######################################################")
		print("               #                                                    #")
		print("               #   Your Bill(With GST 2%) Rs.",Total+Total*2/100," = Rs.",round(Total+Total*2/100),"       #")
		print("               #                                                    #")
		print("               #           ----> Thank You <----                    #")
		print("               ######################################################")
def order1():
	global order2
	order2 = input("\n                   ---> What you want to order: ")
	take_order(order2)
Bill=0
order1()
