class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
    def __repr__(self):
        return f"{self.name} (Age: {self.age}, Disease: {self.disease})"
class Hospital:
    def __init__(self):
        self.patients = []
    def add_patient(self, name, age, disease):
        self.patients.append(Patient(name, age, disease))
        print(f"Patient {name} added")
    def search_by_disease(self, disease):
        result = [p.name for p in self.patients if p.disease.lower() == disease.lower()]
        if result:
            print(f"Patients with {disease}: {result}")
        else:
            print(f"No patients found with {disease}")
hospital = Hospital()
n = int(input("Enter number of patients: "))
for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    disease = input("Enter disease: ")
    hospital.add_patient(name, age, disease)

search_disease = input("\nEnter disease to search: ")
hospital.search_by_disease(search_disease)
