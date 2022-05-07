# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4 = add_numbers_print(4, 5)
# print(sum4)
# print(type(sum4))

# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print("Will i reach here?")
#     return number_sum
# sum6 = add_numbers_more(100, 20)

def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print("Will I be able to print? :-(")
    return food
print("But I'm not sure will print? :'(")
print(menu("monday"))