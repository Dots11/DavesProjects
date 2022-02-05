def greet_user(name, last_name):
    print(f"Hello {name} {last_name}!")
    print("Welcome aboard!")


print("Start")
greet_user("John", "Smith")
greet_user("Mary", "Smith")
print("Finish")

#keyword argument - position does not matter
#most part use positional arguments, if numerical use keyword to improve readability
def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
    print("Welcome aboard!")


print("Start")
greet_user(first_name="John", last_name ="Smith")

print("Finish")