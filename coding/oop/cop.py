import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "omambia",
    "Joshua",
    datetime.date(1994, 4, 17), # year, month, day
    "No. 12 Rongai, ",
    "555 456 0987",
    "kid@edu.com"
)

print(person.name)
print(person.email)
print(person.age())