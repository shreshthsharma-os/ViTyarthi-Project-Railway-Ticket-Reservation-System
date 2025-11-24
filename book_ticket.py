import random

def perform_booking(trains_db, bookings_db):
    print("Book a Ticket")
    train_num=int(input("Enter Train Number: "))

    if train_num not in trains_db:
        print("Train not found")

    train_details = trains_db[train_num]
    print("Selected Train:", train_details['name'])
    print("Departure Time:", train_details['time'])
    print("Available Classes:")
    for cls in train_details['classes']:
        print(cls)


    travel_class=input("Enter Class Code: ").upper()
    
    if travel_class not in train_details["classes"]:
        print("Invalid class")

    class_data=train_details["classes"][travel_class]
    
    if class_data["seats"]>0:
        passenger_name=input("Enter Passenger Name: ")
        pnr=random.randint(1000000000, 9999999999)

        while pnr in bookings_db: 
            pnr=random.randint(1000000000, 9999999999)

        trains_db[train_num]["classes"][travel_class]["seats"]-=1
        
        bookings_db[pnr]={
            "name": passenger_name,
            "train_no": train_num,
            "train_name": train_details["name"],
            "route": train_details["route"],
            "time": train_details["time"],
            "class": travel_class,
            "price": class_data["price"]}

        print("Success! Ticket is Booked.")
        print("Your PNR is:", pnr)
    else:
        print("Sorry, no seats available.")