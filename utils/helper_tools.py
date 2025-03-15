import json
import random
import string
from faker import Faker

class HelperTools:

    def __init__(self, filename = "test_data.json"):
        self.fake = Faker()
        self.filename = filename


    def register_user_data_generator(self):
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        email = self.fake.email()
        telephone = self.fake.phone_number()
        fax = self.fake.phone_number()
        company = self.fake.company()
        address = self.fake.address()
        city = self.fake.city()
        zipcode = self.fake.zipcode()
        login_name = first_name.lower() + str(random.randint(100, 999))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        # Return as a dictionary
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "telephone": telephone,
            "fax": fax,
            "company": company,
            "address": address,
            "city": city,
            "zipcode": zipcode,
            "login_name": login_name,
            "password": password
        }

    def save_test_data_to_json(self, data):
        try:
            # Load existing data if file exists
            with open(self.filename, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        data_entry = {
            "index": len(existing_data) + 1,  # Unique index
            "data": data
        }

        existing_data.append(data_entry)

        with open(self.filename, 'w') as file:
            json.dump(existing_data, file, indent=4)