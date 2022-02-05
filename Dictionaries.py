customer = {
    "name": "David",
    "age": 25,
    "is_verified": True
}
customer["birthdate"] = "1995"
print(customer.get("name"))

#phone no.

phone = input("Phone: ")
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)