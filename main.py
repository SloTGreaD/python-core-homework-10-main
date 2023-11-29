from collections import UserDict
from datetime import datetime, timedelta
class Field:
    def __init__(self, value):
        self.value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value
    

class Name(Field):
    pass

class Phone(Field):
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value
    

    def validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Phone should be 10 symbols')
        return True

class Birthday(Field):
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value
    def validate_bithday(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Try to use this form YYYY-MM-DD')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            birthday_date = datetime(today.year, self.birthday.value.month, self.birhtday.value.day).date()
            if today > birthday_date:
                bithrday_date = datetime(today.year+1, self.birthday.value.month, self.birhtday.value.day).date()
            days_to_birthday = (birthday_date - today).days
            return days_to_birthday

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
    def iterator(self, iteam_number):
        counter = 0
        result = ''
        for item, record in self.date.items():
            result += f'{item}: {record}'
            counter += 1
            if counter >= iteam_number:
                yield result
                counter = 0
                result = ''
