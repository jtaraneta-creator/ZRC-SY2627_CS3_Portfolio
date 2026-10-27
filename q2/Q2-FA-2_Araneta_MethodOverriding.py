class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        return super().calculate_bill() * 0.80
        

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.85

PhilHealthPatient1 = PhilHealthPatient("Pedro Penduko", 1000)
PhilHealthPatient1.calculate_bill()
PhilHealthPatient1.__bill_amount = 1000

Patient1 = Patient("Juan Dela Cruz", 1000)
Patient1.calculate_bill()
Patient1.__bill_amount = 1000

SeniorPatient1 = SeniorPatient("Maria Santos", 1000)
SeniorPatient1.calculate_bill()
SeniorPatient1.__bill_amount = 1000

print("Hospital Billing System")
print("-----------------------")

for patient in [Patient1, SeniorPatient1, PhilHealthPatient1]:

    print(f"Patient Name: {patient.get_name()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
    print()

