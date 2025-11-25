def train_info():
    #all the information about trains is described below
    return {
        101: {"name": "Shatabdi Express","route": "Delhi-Agra","time": "06:00 AM",
            "classes": {"CC": {"seats": 50, "price": 800},"EC": {"seats": 20, "price": 1500}}},
        102: {"name": "Rajdhani Express","route": "Mumbai-Delhi","time": "04:30 PM",
            "classes": {"3A": {"seats": 50, "price": 2000},"2A": {"seats": 30, "price": 3000},"1A": {"seats": 10, "price": 5000}}},
        103: {"name": "Gatimaan Express","route": "Delhi-Jhansi","time": "08:10 AM",
            "classes": {"CC": {"seats": 60, "price": 1200},"EC": {"seats": 15, "price": 2200}}},
        104: {"name": "Vande Bharat","route": "Chennai-Mysore","time": "05:50 AM",
            "classes": {"CC": {"seats": 45, "price": 1500},"EC": {"seats": 25, "price": 2800}}}}

def empty_dict_for_bookings():
    #An empty dictionary to store booking details for passengers
    return {}