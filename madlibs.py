from argparse import Action
from time import time
from tokenize import String
from unicodedata import name


def main():
	# write your code here
	
	time = input("Please enter the time")
	item = input("Please enter the item")
	name = input("Please enter a name")
	scream = input("Please enter a sentence")
	action = input("please edter a verb")
	story = f"""It was {time} o'clock when I heard a knock at the door.
	I opened the door and there was a box full of {item} with a note saying From Mr. {name}.
	Just as I closed the door I heard a scream {scream}
	I froze in place and all I could do was {action}"""
	print(story)



if __name__ == '__main__':
	main()