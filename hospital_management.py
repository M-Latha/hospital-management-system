class HospitalManagement:
    def __init__(self):
        self.doctor_names = {
            "physician": "Dr.Pavan",
            "cardiologist": "Dr.Rakshita",
            "neurologist": "Dr.Zohara",
            "gynecologist": "Dr.Spoorthi",
            "dermatologist": "Dr.Yana",
            "oncologist": "Dr.Ram",
            "dentist": "Dr.Arijith",
            "orthopedic": "Dr.Anandhi"
        }

        self.consultation_fees = {
             "Dr.Pavan": 1000,
            "Dr.Rakshita": 1200,
            "Dr.Zohara": 1500,
            "Dr.Spoorthi": 1100,
            "Dr.Yana": 900,
            "Dr.Ram": 2000,
            "Dr.Arijith": 800,
            "Dr.Anandhi": 1000
        }

        self.consultation_time = {
             "Dr.Pavan": "9 AM to 11 AM",
            "Dr.Rakshita": "11 AM to 1 PM",
            "Dr.Zohara": "2 PM to 4 PM",
            "Dr.Spoorthi": "4 PM to 6 PM",
            "Dr.Yana": "10 AM to 12 PM",
            "Dr.Ram": "1 PM to 3 PM",
            "Dr.Arijith": "3 PM to 5 PM",
            "Dr.Anandhi": "5 PM to 7 PM"
        }

        self.bill_amount = {
            "fever": 300,
            "cold": 200,
            "flu": 400,
            "cancer": 5000,
            "skin-infections": 800,
            "brain-disorders": 2500,
            "nerve-disorders": 3000,
            "heart-disorders": 4000,
            "asthma": 600,
            "chest-pain": 1000,
            "tooth-ache": 700,
            "fractures": 2000,
            "pregnancy-checkup": 1500,
            "delivery": 8000
        }

        # Store patient details
        self.patients = {}
        self.current_patient = None

    def patient_registration(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        gender = input("Enter gender: ")
        mob = input("Enter mobile number: ")
        disease = input("Enter disease type: ")
        date = input("Enter consultancy date: ")
        self.patients[mob] = {
            "name": name, "age": age, "gender": gender,
            "disease": disease, "date": date
        }
        print("Registration Successful")

    def patient_login(self):
        name = input("Enter name: ")
        mob = input("Enter mobile number: ")
        if mob in self.patients and self.patients[mob]["name"].lower() == name.lower():
            self.current_patient = mob
            print("Login Successful")
        else:
            print("Invalid name or mobile number. Please register first.")

    def book_appointment(self):
        print("Available Specialists:")
        for sp in self.doctor_names:
            print(sp)
        choice = input("Enter specialist: ")
        if choice in self.doctor_names:
            doctor = self.doctor_names[choice]
            print(f"Doctor is {doctor}")
        else:
            print("Specialist not found.")

    def consultation(self):
        for d in self.consultation_fees:
            print(d)
        doc = input("Enter doctor name: ")
        if doc in self.consultation_fees:
            print(f"Fee is {self.consultation_fees[doc]}")
        else:
            print("Doctor not found.")

    def visiting_hours(self):
        for d in self.consultation_time:
            print(d)
        doc = input("Enter doctor name: ")
        if doc in self.consultation_time:
            print(f"Time is {self.consultation_time[doc]}")
        else:
            print("Doctor not found.")

    def pharmacy_billing(self):
        for d in self.bill_amount:
            print(d)
        disease = input("Enter disease name: ")
        if disease in self.bill_amount:
            print(f"Bill is {self.bill_amount[disease]}")
        else:
            print("Disease not found.")

    def total_bill(self):
        doc = input("Enter doctor name: ")
        disease = input("Enter disease name: ")
        if doc in self.consultation_fees and disease in self.bill_amount:
            total = self.consultation_fees[doc] + self.bill_amount[disease]
            print(f"Total bill is {total}")
        else:
            print("Invalid doctor or disease.")

    def cancel_appointment(self):
        mob = input("Enter mobile number: ")
        if mob in self.patients:
            del self.patients[mob]
            print("Appointment Cancelled ❌")
        else:
            print("No appointment found.")


obj = HospitalManagement()
while True:
    print("\nWELCOME TO HEALTH CARE HOSPITAL")
    print("1. Patient Registration")
    print("2. Patient Login")
    print("3. Book Appointment")
    print("4. Visiting Hours")
    print("5. Consultation Fees")
    print("6. Treatment Cost")
    print("7. Final Bill")
    print("8. Cancel Appointment")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        obj.patient_registration()
    elif choice == "2":
        obj.patient_login()
    elif choice == "3":
        obj.book_appointment()
    elif choice == "4":
        obj.visiting_hours()
    elif choice == "5":
        obj.consultation()
    elif choice == "6":
        obj.pharmacy_billing()
    elif choice == "7":
        obj.total_bill()
    elif choice == "8":
        obj.cancel_appointment()
    elif choice == "9":
        print("Thank you for visiting health Care Hospital 🙏")
        break
    else:
        print("Invalid option. Try again.")