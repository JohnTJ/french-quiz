import argparse


# Whatever was typed in after "python quiz.py", this will decide whether to run quiz or add
def act(choice):
	if choice == "quiz":
		quiz()
	elif choice == "add":
		add()

def quiz():
	myFile = open("quiz.txt","r")			# Opens English file for reading
	quiz = myFile.readlines()				# Creates list of english words
	myFile.close()

	myKey = open("key.txt","r")				# Opens French file for reading
	key = myKey.readlines()					# Creates list of French words
	myKey.close()

	english = []
	french = []


	# Creates new lists for English and French words without newlines
	for i in range(len(quiz)):
		english.append(quiz[i].rstrip('\n'))
	for i in range(len(key)):
		french.append(key[i].rstrip('\n'))

	print("Type the French Word in quotes")

	# Quiz: prompts User to enter answer, compares it to French translation
	# Note: Answers must be in quotations

	right = 0								# Correct answer counter
	wrong = 0								# Wrong answer counter
	for num in range(len(english)):
		print(english[num])
		answer = input()					# User's answer

		# Checks if User's answer was correct
		if answer == french[num]:
			print("correct")
			right += 1
			continue
		else:
			print("wrong\ncorrect answer: " + str(french[num]))
			wrong += 1

	total = float(len(english))
	score = (float(right) / total) * 100


	# Results
	print("You translated " + str(right) + " word(s) correctly and " + str(wrong) + " word(s) incorrectly")
	print("Score:" + str(score) + "%")


def add():
	print("This is where you can add more words to your study set")
	print("How many words would you like to add?")

	ammount = input()

	try:
		ammount = int(ammount)
	except:
		print("You must type in a number")

	for num in range(ammount):
		myFile = open("quiz.txt", "a")
		print("Type in english word or phrase")
		engl = input()
		myFile.write(engl + "\n")
		myFile.close()

		myKey = open("key.txt", "a")
		print("Now type in the French translation")
		fren = input()
		myKey.write(fren + "\n")
		myKey.close()

	print(str(ammount) + " word(s) have been added to the study set")




# Using argparse. Here I can type in quiz or add to take the quiz or add words to my set
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("choice", help="begins testing")

	args = parser.parse_args()
	act(args.choice)

if __name__ == "__main__":
	main()
