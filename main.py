import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("x" * 80)

entered_num = input("please enter a phone number: ")

# create PhoneNumbers object
phone_num = phonenumbers.parse(entered_num, None)
# phone_num = phonenumbers.parse(entered_num, "MA")

print(phone_num)

# you might to get some information about the location that corresponds to a phone number.
print(geocoder.description_for_number(phone_num, "en"))

# for mobile numbers in some countries,
# you can also find out information about which carrier originally owned a phone number.
print(carrier.name_for_number(phone_num, "en"))


# you might also be able to retrieve a list of time zone names that the number potentially belongs to.
print(timezone.time_zones_for_geographical_number(phone_num))
