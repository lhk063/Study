""" 
print("Hello world!")

a = 2
b = 3
c = a + b
print(c)
"""

""" 
name = "Ashe"
age = 29
dead = True  # boolean

print("Hello my name is", name)
print("and I'm", age, "years old")

print("Hello my name is " + name)
print("and I'm " + str(age) + " years old")
"""

""" 
def say_hello():
    print("Hello how r u?")

def say_bye():
    print("bye bye")

say_hello()
say_hello()
say_bye()
"""

""" 
def say_hello(name): # parameter
    print("Hello", name, "how are you?")


say_hello("Ashe") # argument
say_hello("Nico")
say_hello("Delta")
 """

""" 
def say_hello(name, age):
    print("hello", name)
    print("you are", age, "years old")


def tax(money):

    print(money * 0.35)


tax(200)
tax(20000)

 """

""" 
def say_hello(name="lee"):
    print("hello", name)


say_hello("ashe")
say_hello()


def tax(money):
    return money * 0.11


def pay_tax(tax):
    print("thank you for paying", tax)


to_pay = tax(1000)
pay_tax(to_pay)
 """


""" name = "ashe"
age = "29"
color = "blue"

print(
    f"hello i'm {name}, i have {age}years in the earth, {color}is my eyes color")


def make_juice(fruit):
    return f"{fruit}+juice"


def add_ice(juice):
    return f"{juice}+ice"


def add_sugar(iced_juice):
    return f"{iced_juice}+sugar"


juice = make_juice("apple")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)
 """

""" if 10 < 5:
    print("Correct!")
elif 10 > 5:
    print("Correct!")
else:
    print("Nothing")
 """

age = int(input("how old are you?"))

if age < 20:
    print("you can't")
elif age >= 20:
    print("you can")
else:
    print("Go ahead")
