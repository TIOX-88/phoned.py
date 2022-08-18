import pyfiglet
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

text = pyfiglet.figlet_format("TIOX VAU")
number=input("Enter Your NO. With Country Code +(: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")



print(text)
print(phone)
print(time)
print(car)
print(reg)
