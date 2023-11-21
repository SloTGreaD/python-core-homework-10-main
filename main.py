from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):

    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)

    def validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Phone should be 10 symbols')
        return True



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []



    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    def add_phone(self,phone_number):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)
    def find_phone(self,phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            phone_obj.value = new_phone
        else:
            raise ValueError

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
        return phone


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    def find(self, name):
        key = name
        return self.data.get(key)
    def delete(self, name):
        key = name
        if key in self.data:
            del self.data[key]
