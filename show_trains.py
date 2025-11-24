def display_available_trains(trains_db):
    print("Available Trains")
    
    for train_no, details in trains_db.items():
        print("Train No:", train_no)
        print("Name:", details['name'])
        print("Route:", details['route'])
        print("Time:", details['time'])
        
        print("Classes:")
        for cls_name, cls_data in details['classes'].items():
            print(cls_name, "-", "Price:", cls_data['price'], "Seats:", cls_data['seats'])
        