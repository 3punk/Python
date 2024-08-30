import time

rest = 2
delay = 3

questions = ("1. How many planets in solar system?: ",
             "2. What is the longest river in the world?: ",
             "3. What is the easiest programming language to learn?: ",
             "4. What is programming language that used to styling in websites?: ",
             "5. What Tkinter used for?: ",
             "6. Who is the first person landed on the moon?: ",
             "7. Who is the person that have King of Pop title?: ",
             "8. Who is the inventor of Tesla Coil?: ",
             "9. Who is the inventor of Theory of Relativity?: ",
             "10. When is Indonesian's Indepence Day?: ",
             "11. What is our galaxy called?: ",
             "12. What's phobia of ocean called?: ",
             "13. Who's God of Thunder?: ",
             "14. Who's God of Sun based on Japanese Mythology?: ",
             "15. Who leads NAZI in Germany?: ",
             "16. Who is the famous dictator in Russia?: ",
             "17. Which is the correct statement below?: ",
             "18. 10 + 10 : (2 x 5) - 10: ",
             "19. (5 x 5) - 20 + 20 : 5 x 5: ",
             "20. What happen if you throw items to cactus?(Minecraft Quiz): ")

options = (("A. 5", "B. 6", "C. 7", "D. 8"), 
           ("A. Kapuas river", "B. Nile river", "C. Amazon river", "D. Yangtze river"), 
           ("A. Python", "B. JavaScript", "C. C++", "D. C#"), 
           ("A. HTML", "B. PHP", "C. CSS", "D. Node.Js"), 
           ("A. Make website", "B. Make GUI", "C. Make menu", "D. Make Donald Trump"),
           ("A. Buzz Lightyear", "B. The Rock", "C. John Cena", "D. Neil Armstrong"),
           ("A. Michael Jackson", "B. John Mayer", "C. Meghan Trainor", "D. Haley Reinhart"),
           ("A. Isaac Newton", "B. Albert Einstein", "C. Nikola Tesla", "D. Charles Darwin"),
           ("A. Galileo Galilei", "B. James Watt", "C. Al-Khawarizmi", "D. Albert Einstein"),
           ("A. 28th October", "B. 17th August", "C. 30th September", "D. 25th December"),
           ("A. Milky Way", "B. Large Magellanic Cloud", "C. Small Magellanic Cloud", "D. Andromeda"),
           ("A. Aerophobia", "B. Trypanophobia", "C. Thalassophobia", "D. Agliophobia"),
           ("A. Poseidon", "B. Uranus", "C. Aphrodite", "D. Zeus"),
           ("A. Amaterasu Oomikami", "B. Inari Ookami", "C. Izanagi no Mikoto", "D. Kaguya Otsutsuki"),
           ("A. Vladimir Lenin", "B. Adolf Hitler", "C. Joseph Stalin", "D. Mao Zhedong"),
           ("A. Soekarno", "B. Van Den Bosch", "C. Joseph Stalin", "D. Vladimit Putin"),
           ("A. Bats is the only mammals that can fly", "B. Tyrannosaurus is the biggest dinosaur", "C. Chicken can fly", "D. Donald Trump is the smartest being in the whole universe"),
           ("A. 10", "B. 5", "C. 40", "D. 1"),
           ("A. 5", "B. 20", "C. 25", "D. 10"),
           ("A. The items HP restored", "B. Die", "C. Spawn mob", "D. Items destroyed/disappeared"))

answers = ("D", "B", "A", "C", "B", "D", "A", "C", "D", "B", "A", "C", "D", "A", "B", "C", "A", "D", "C", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------")
    print(question)
for option in options[question_num]:
    print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        time.sleep(rest)
        print("Correct answer")
        time.sleep(delay)
    else:
        print("Incorrect asnwer")
        time.sleep(rest)
        print(f"{answers[question_num]} is the correct answer")
        time.sleep(delay)

    question_num += 1

print("--------------------------")
print("         Results          ")
print("--------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
