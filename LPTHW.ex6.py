# in this exercise we are going to create a bunch of variables with complex strings so we can see what they're for
# strings are what you want to display for export from your program
# use double quotes

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the side side of..."
e = "a string with a right side."

print(w + e)