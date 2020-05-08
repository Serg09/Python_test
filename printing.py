print("Hello")
print("Monkeys eat nababas all the time")
print(54552.94595345*5674532.4982579)

print("")
print("")
print("")

import turtle

my_turtle = turtle.Turtle()

def square(length, angle):
	my_turtle.forward(length)
	my_turtle.left(angle)
	my_turtle.forward(length)
	my_turtle.left(angle)
	my_turtle.forward(length)
	my_turtle.left(angle)
	my_turtle.forward(length)
	my_turtle.left(angle)


# for i in range(10):
# 	square(100, 90)
# 	square(100, 100)
# 	# square(30, 45)



# import turtle

# my_turtle = turtle.Turtle()

# def square(length, angle):
# 	for i in range(4):
# 		my_turtle.forward(length)
# 		my_turtle.left(angle)

# for i in range(200):
# 	square(100, 90)
# 	my_turtle.left(11)
# 	# square(100, 100)


hello = "Hello"
print (hello[0:0])
print (hello[0:1])
print (hello[0:2])
print (hello[0:3])
print (hello[0:4])
print (hello[0:5])
print (hello[0:-1])
print (hello[0:-2]) 
print()

print("")
print("")
print("")


collection = ['hey', 5, 'd']
for x in collection:
    print(x)

print("")

string = "Hello World"
for x in string:
    print(string[:string.index("l")])

print("")
print("")
print("")

# Print until "W"
string = "Hello World"
for x in string:
    print(string[:string.index("W")])

print("")
print("")
print("")

# # [START : STOP : STEP]
greeting = "Hi, how are you doing? It is nice to meet you!"
print(greeting)
print(greeting[0:-1:1])
print(greeting[0:-1:2]) # print every second symbol
print(greeting[::-1]) # reverce 1
print(greeting[-1::-1]) # reverce 2 - print(greeting[stringlength::-1]) 
print("")
print("")
print("")

# list(range(10))
# my_turtle.forward(100)
# square(80, 70)
# my_turtle.forward(100)
# square(60, 130)
# my_turtle.forward(100)
# square(120, 200)
# my_turtle.forward(100)


# ---------------------------------------------------


data = "XBOX 360 | 150 | New"
product, price, condition = data.split("|")
print(product)
print(price)
print(condition)

print("")

numbers = [1,2,3,4,5,6]
print(numbers)
numbers.append(9)
numbers.append(10)
numbers.append(15)
print(numbers)
print(list(range(5)))
print(list(range(8,21)))


for number in range(8,21):
	numbers.append(number)
print(numbers)
print(numbers[::-1])
print(numbers[::2])


print("")
print("")
print("")

data = "XBOX 360 | 150 | New"
print(data)
print(data.find("|")) # pipe = 9
print(data.find("|", 10)) # second pipe = 15
print(data[data.find("|"):data.find("|", 10)]) # find list between to pipes. To remove first pipe run:
print(data[data.find("|")+1:data.find("|", 10)]) # +1 symbol to remove first pipe
print(data.split("|"))
print(data.split("|")[2])
details = data.split("|")
print(details)
print(details[1])
condition = details[2]
print(condition)

print("")

groceries = ["apple", "banana", 5, 6, "oranges"]
print(groceries)
print(groceries[0])
print(groceries[4])


print("")


split_text = "What-is-going-on"
print(split_text)
print(split_text.split())
print(split_text.split("-"))
print(split_text.split("-")[0])
print(split_text.split("-")[1])
print(split_text.split("-")[2])
print(split_text.split("-")[3])
print(split_text.split("-")[:4])
print(split_text.split("-")[0:-1])
print(split_text.split("-")[0::-1])
print(split_text.split("-")[0::2]) # every second word
print(split_text.split("-")[::-1]) # reverse


print("")



# -----------------------------------------------

# DICTIONARIES




phone_book2 = ["720-219-0867", "723-432-3634"]
print(phone_book2)
print(phone_book2[0])
print(phone_book2[1])
# DICT[key] --> value
# { key1: value1. key2: value2, ....}
phone_book = {
	"Sergey": ["720-219-0867", "sskumatov@gmail.com"], 
	"Violetta": ["324-342-6423", "V_skumatova@aol.com"], 
	"Diana": "234-234-2135"
	}

print(phone_book)
print(phone_book["Sergey"])
print(phone_book["Sergey"][0])
print(phone_book["Sergey"][1])
print(phone_book["Violetta"][0])
print(phone_book["Violetta"][1])
print(phone_book["Diana"])






# TURTLE

import turtle
tina = turtle.Turtle()
tina.shape('turtle')

number_list = [1,2,3,4,5,6,7,8,9,10] 

tina.color("green") 
for number in number_list: 
    tina.forward(number*10) 
    tina.left(60)

tina.forward(20)
tina.color("green")
tina.write("What color am I now?")



