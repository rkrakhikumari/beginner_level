from question import question

question.prompt =[
    "what is the color of apple ?\n(a) red/green\n(b) purple\n(c) black\n\n",
    "what is the color of banana ?\n(a) teal\n(b) yellow\n(c) purple\n\n",
    "what is the color of strawberry ?\n(a) yellow\n(b) purple\n(c) red\n\n"

]
questions =[
    question(question.prompt[0],"a"),
    question(question.prompt[1],"b"),
    question(question.prompt[2],"c"),

]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got"+ str(score) + " / " + str(len(questions))+ "correct")

run_test(questions)