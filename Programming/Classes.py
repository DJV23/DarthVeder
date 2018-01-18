# ClassesAddress.py
#
#
#
#

class Address():
    def __init__(self):
      self.unit_number = 0
      self.street_name = ""
      self.city = ""
      self.province_state = ""
      self.postal_code = ""
      self.country = ""

def mailingAddress(self):
  mailing_address = str(self.unit_number) + "" + self.street_name + "" + self.city + "" + self.province_state + "" + self.postal_code + "" + self.country




parents_address = Address()

parents_address.unit_number = 123
parents_address.street_name = "harness drive"
parents_address.city = "Loloci"
parents_address.province_state = "Rololia"
parents_address.postal_code = "V1A 8J5"
parents_address.country = "Ramboloia"

print(parents_address)
