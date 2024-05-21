#
#question_class


class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "Which mammal is known to have the longest lifespan?\n(a) Blue Whale\n(b) Elephant\n(c) Human\n(d) Bowhead Whale\n\n"
    "What is a group of lions called?\n(a) A pack\n(b) A herd\n (c) A pride\n (d) A flock\n\n"
    "Which bird is often associated with delivering babies in stories?\n(a) Stork\n(b) Eagle\n(c) Sparrow\n(d) Penguin\n\n"
    "Which sea creature has three hearts?\n(a) Dolphin\n(b) Shark\n (c) Octopus\n (d) Whale\n\n"
    "What is the name given to the nose of elephants?\n(a) Snout\n(b) Trunk\n(c) Tusk\n(d) Nostril\n\n"
    "Which three colours are on the flag of Italy?\n(a) Red, White and Blue\n(b) Green, White and Red\n(c) Black, Red and Yellow\n(d) Blue, White and Red\n\n"
    "How many strings does a ukulele have?\n(a) 4\n(b) 5\n(c) 6\n(d) 7\n\n"
    "What is the highest mountain on Earth?\n(a) K2\n(b) Kangchenjunga\n(c) Mount Everest\n(d) Lhotse\n\n" #7
    "Which country is Alaska part of?\n(a) USA\n(b) UK\n(c) Canada\n(d) Russia\n\n"
    "What is the name of the narrow arm of the Atlantic Ocean between England and France?\n(a) The Strait of Gibraltar\n(b) The English Channel\n(c) The North Sea\n(d) The Irish Sea\n\n"
    "Who was the first woman to win a Nobel Prize?\n(a) Marie Curie\n(b) Rosalind Franklin\n(c) Ada Lovelace\n(d) Dorothy Hodgkin\n\n"
    "Which volcano covered the Roman city of Pompeii under ashes?\n(a) Mount Etna\n(b) Mount Vesuvius\n(c) Mount Olympus\n(d) Mount Kilimanjaro\n\n"
    "How often are leap years?\n(a) Every Year\n(b) Every 2 Years\n(c) Every 4 Years\n(d) Every 10 Years\n\n"
    "Who invented the telephone?\n(a) Alexander Graham Bell\n(b) Thomas Edison\n(c) Benjamin Franklin\n(d) Nikola Tesla\n\n" #13
    "What is the only food that cannot go bad?\n(a) Dark Chocolate\n(b) Peanut Butter\n(c) Canned Tuna\n(d) Honey\n\n"
    "What is the name of Hagrids pet spider?\n(a) Nigini\n(b) Crookshanks\n(c) Aragog\n(d) Mosag\n\n"
    "What is the heaviest organ in the human body?\n(a) Brain\n(b) Liver\n(c) Skin\n(d) Heart\n\n"
    "Which of these EU countries does not use the euro as its currency?\n(a) Poland\n(b) Denmark\n(c) Sweden\n(d) All of the above\n\n"
    "What type of food holds the world record for being the most stolen around the globe?\n(a) Wagyu Beef\n(b) Cheese\n(c) Coffee\n(d) Chocolate\n\n"
    "What element does the chemical symbol Au stand for?\n(a) Silver\n(b) Magnesium\n(c) Salt\n(d) Gold\n\n"
    "What is the highest-grossing Broadway show of all time?\n(a) The Lion King\n(b) Wicked\n(c) Kinky Boots\n(d) Hamilton\n\n" #20
    "On average, how many seeds are located on the outside of a strawberry?\n(a) 100\n(b) 200\n(c) 400\n(d) 500\n\n"
    "Which fast food restaurant has the largest number of retail locations in the world?\n(a) Burger King\n(b) Taco Bell\n(c) Subway\n(d) Mcdonalds\n\n"
    "What is the oldest soft drink in the United States?\n(a) Coca Cola\n(b) Pepsi\n(c) Dr Pepper\n(d) Ginger Ale\n\n"
    "In what country do more than half of people believe in elves?\n(a) Norway\n(b) Russia\n(c) Poland\n(d) Iceland\n\n"
    "What is the highest-grossing video game franchise to date?\n(a) Mario\n(b) Pokemon\n(c) Call of Duty\n(d) Street Fighter\n\n" #25
    "Which countrys national animal is a unicorn?\n(a) Scotland\n(b) Denmark\n(c) New Zealand\n(d) France\n\n"
    "What is the main ingredient in a falafel?\n(a) Lentil\n(b) Chickpea\n(c) Broccoli\n(d) Split Pea\n\n"
    "What color dresses do Chinese women traditionally wear on their wedding day?\n(a) Blue\n(b) Gold\n(c) White\n(d) Red\n\n"
    "What is the capital of South Korea?\n(a) incheon\n(b) Seoul\n(c) Busan\n(d) Gangnam\n\n"
    "Mycology is the scientific study of what?\n(a) Cancer\n(b) Flowers\n(c) Fungi\n(d) Blood\n\n"
]

questions = [
    question(question_prompts[0], "d"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "a"),
    question(question_prompts[3], "c"),
    question(question_prompts[4], "b"),
    question(question_prompts[5], "b"),
    question(question_prompts[6], "a"),
    question(question_prompts[7], "c"),
    question(question_prompts[8], "a"),
    question(question_prompts[9], "b"),
    question(question_prompts[10], "a"),
    question(question_prompts[11], "b"),
    question(question_prompts[12], "c"),
    question(question_prompts[13], "a"), 
    question(question_prompts[14], "d"),
    question(question_prompts[15], "c"), #
    question(question_prompts[16], "b"), #
    question(question_prompts[17], "d"),
    question(question_prompts[18], "b"),
    question(question_prompts[19], "d"),
    question(question_prompts[20], "a"),
    question(question_prompts[21], "b"),
    question(question_prompts[22], "c"), #
    question(question_prompts[23], "c"),
    question(question_prompts[24], "d"),
    question(question_prompts[25], "b"),
    question(question_prompts[26], "a"), 
    question(question_prompts[27], "b"), 
    question(question_prompts[28], "d"),
    question(question_prompts[29], "b"), 
    question(question_prompts[30], "c"),
]


def runner(questions_list):
    score = 0
    for question in questions_list:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1 #adding one to the score
        print("You got " + str(score) + "/" + str(len(questions_list)) + " correct") #you got 2/3 correct






