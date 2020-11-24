class House:

    def __init__(self, floors, address, elevator):
        self.floors = floors
        self.address = address
        self.elevator = elevator

    def give_to_rent(self):
        return "OK"

hryshevka = House(5, "Toktogula 175", False)

print(f"lift ? => {hryshevka.elevator}")
print(f"floors ? => {hryshevka.floors}")
print(f"address ? => {hryshevka.address}")