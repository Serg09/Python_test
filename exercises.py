def square_number(my_number):
	return my_number ** 2 # two ** means number is squared
	# print(my_number)

def test_square_number():
	assert square_number(2) == 4
	assert square_number(8) == 64
	assert square_number(10) == 100
	print("Your code is correct!")

test_square_number()
print("")

# check if number is even -----------------------------

def is_even(any_number):
	return any_number % 2 == 0
	# if any_number % 2 == 0:
	# 	return True
	# else:
	# 	return False

def test_is_event():
	assert is_even(2) == True 
	assert is_even(3) == False 
	assert is_even(8) == True 
	assert is_even(100) == True 
	assert is_even(101) == False 
	print("Your code (even) is correct!")

test_is_event()

# ------

# check if number is odd -----------------------------

def is_odd(odd_number):
	return odd_number % 2 != 0

def test_is_odd():
	assert is_odd(2) == False 
	assert is_odd(3) == True 
	assert is_odd(8) == False 
	assert is_odd(100) == False 
	assert is_odd(101) == True 
	print("Your code (odd) is correct!")

test_is_odd()
print("")

# ------ FIND LENGTH OF THE STRING

def string_length(my_string):
	count = 0
	for letter in my_string:
		count += 1
	return count

print(string_length('hello'))

def test_string_length():
	assert string_length('hello!') == 6
	assert string_length('banana') == 6
	assert string_length('8') == 1
	assert string_length('Violetta') == 8 
	assert string_length('101') == 3 
	print("Your code (string_lenth) is correct!")

test_string_length()

print("")

# ------- LAST LETTER OF THE STRING
def last_letter(my_string):
	return my_string[-1]

def test_last_letter():
  assert last_letter('hello!') == '!'
  assert last_letter('banana') == 'a'
  assert last_letter('8') == '8'
  assert last_letter('funnyguys') == 's'
  assert last_letter('101') == '1'
  print("YOUR CODE (last letter) IS CORRECT!")
  
test_last_letter()
print("")

# ----- WHO IS BIGGER GUY? _------



# def bigger_guy(num1, num2):
#   if num1 > num2:
#     return num1
#   else:
#     return num2


def biggest_guy(num1, num2, num3):
	  # find bigger guy between num1 and num2
  # find biggest guy between bigger guy and num3
 #  if bigger_guy > num3:
	#   biggest_guy = bigger_guy
 #  else:
	# biggest_guy = num3
 #  return biggest_guy

	# return bigger_guy(bigger_guy(num1, num2), num3)

	# Best way is to use MAX function
	return max(num1, num2, num3)


# Do not remove lines below here,
# this is designed to test your code.

def test_biggest_guy():
  # try:
  	# print("----------RUNING TEST---------")
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('a', 'c', 'b') == 'c'  # 'b' is greater than 'a'
    print("SuCCESS!")
    print("YOUR CODE (biggest_guy) IS CORRECT!")
  
  # except (AssertionError) as e:
  #   print(e)
  #   import wrong
  #   return
  
  # import success
  
# test your code by un-commenting the line(s) below
test_biggest_guy()

print("")
print("")


# ----------------
# Usian Bolt Races You and Qazi

def choice_to_number(choice):
  return {'Usain': 1, 'Me': 2, 'Qazi': 3}[choice]
  
def number_to_choice(number):
  return {1: 'Usain', 2: 'Me', 3: 'Qazi'}[number]



# DO NOT remove lines below here,
# this is designed to test your code.

def test_choice_to_number():
  assert choice_to_number('Usain') == 1
  assert choice_to_number('Me') == 2
  assert choice_to_number('Qazi') == 3
  print("YOUR CODE (choice_to_number) IS CORRECT!")
  
def test_number_to_choice():
  assert number_to_choice(1) == 'Usain'
  assert number_to_choice(2) == 'Me'
  assert number_to_choice(3) == 'Qazi'
  print("YOUR CODE (number_to_choice) IS CORRECT!")
  
# def test_all():
#   try:
#     test_choice_to_number()
#     test_number_to_choice()
  
#   except AssertionError:
#     import wrong
  
#   else:
#     import success
  
# test your code by un-commenting the line(s) below
# test_all()
test_choice_to_number()
test_number_to_choice()
