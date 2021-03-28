client_information = {1 : "Philip", 2: "Omega III", 3: "Ramya", 4: "Romesh", 5: "John"}
clients = ["Philip", "Omega III",  "Ramya", "Romesh", "John"]

details = {101: [['Sender',1],['Receiver',3],['Start Date','14-03-2020'],['Delivery Date','25-03-2020'],['Sender location','Area 1'],['Receiver Location','Area 6'],['Delivery Status','Delivered'],['Shipping cost',198]],
                    102: [['Sender',4],['Receiver',1],['Start Date','18-06-2020'],['Delivery Date','09-07-2020'],['Sender location','Area 2'],['Receiver Location','Area 4'],['Delivery Status','Delivered'],['Shipping cost',275]],
                    103: [['Sender',2],['Receiver',3],['Start Date','01-12-2020'],['Delivery Date','null'],['Sender location','Area 5'],['Receiver Location','Area 1'],['Delivery Status','In Transit'],['Shipping cost',200]],
                    104: [['Sender',1],['Receiver',5],['Start Date','23-06-2020'],['Delivery Date','25-06-2020'],['Sender location','Area 1'],['Receiver Location','Area 4'],['Delivery Status','Delivered'],['Shipping cost',314]],
                    105: [['Sender',3],['Receiver',4],['Start Date','29-08-2020'],['Delivery Date','10-09-2020'],['Sender location','Area 5'],['Receiver Location','Area 3'],['Delivery Status','Delivered'],['Shipping cost',275]],
                    106: [['Sender',5],['Receiver',2],['Start Date','28-06-2020'],['Delivery Date','null'],['Sender location','Area 3'],['Receiver Location','Area 1'],['Delivery Status','In Transit'],['Shipping cost',270]]   
}




new_details = {100+i: [clients[details[100+i][0][1]-1], clients[details[100+i][1][1]-1], details[100+i][2][1], details[100+i][3][1], details[100+i][4][1], details[100+i][5][1], details[100+i][6][1], details[100+i][7][1]] for i in range(1,len(details)+1)}


for j in range(1,len(new_details)):
    print(new_details[100+j])

i = 0

for i in range(1,len(new_details)+1):
    if new_details[100+i][0] == "Philip":
        print(new_details[100+i])

i = 0


print("Q7")

sent_dates = []
receive_dates = []
day_sent = []
month_sent = []
day_receive = []
month_receive = []

for i in range(1,len(new_details)+1):
    sent_dates.append(new_details[100+i][2])
    receive_dates.append(new_details[100+i][3])

i = 0

for i in range(len(sent_dates)):
    a = sent_dates[i].split("-")
    b = receive_dates[i].split("-") 
    day_sent.append(a[0])
    month_sent.append(a[1])
    if b[0] == "null":
        day_receive.append("31")
        month_receive.append("31")
    else:
        day_receive.append(b[0])
        month_receive.append(b[1])


i = 0
for i in range(len(day_sent)):
    diff = int(day_sent[i]) - int(day_receive[i])
    if diff < 0:
        diff = -diff
    else:
        diff = diff + 0
    if diff <= 7 and new_details[101+i][6] == "Delivered":
        print(101+i,new_details[101+i])


print("Q8")

for i in range(len(day_sent)):
    diff = int(day_sent[i]) - int(day_receive[i])
    if diff < 0:
        diff = -diff
    else:
        diff = diff + 0
    if diff >= 15 or new_details[101+i][6] == "In Transit" or int(month_receive[i]) - int(month_sent[i]) >= 1:
        print(101+i,":",new_details[101+i])
        


