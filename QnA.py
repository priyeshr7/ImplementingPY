
questions=[["question 1","A","B","C","D",1],
        ["question 2","A","B","C","D",1],
        ["question 3","A","B","C","D",3],
        ["question 4","A","B","C","D",3],
        ["question 5","A","B","C","D",3]]

def quiz():
    score=0
    for i in range(0, len(questions)):
        question = questions[i]
        print(f"{[i]} Question : question{[i]}")
        print(f" a. {question[1]}     b. {question[2]}")
        print(f" c. {question[3]}     d. {question[4]}")
        answer = int(input("Enter your answer(1-4): "))
        if (answer == question[-1]):
            score += 1
            print("Correct Answer! Your score is: ", score)
        else:
            print("Incorrect Answer Please restart.")
            break
        
quiz()
try:
    print("Do you want to restart? \n 1.Yes   2.No \n")
    opt= int(input("Enter your option: "))
    if opt == 1:
        quiz()
    else : 
        print("Thank you for playing!")
except ValueError:
    print("Invalid input. Please enter a number.")
    

    