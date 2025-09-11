import  json
with open('questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["questionText"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1,"-",alternative)
    user_answer = int(input("Enter your answer: "))
    question["user_choice"] = user_answer

score = 0
for index, question in enumerate(data):
    if int(question["user_choice"]) == int(question["correctAnswer"]):
        score += 1
        result  = "Correct!"
    else:
        result = "Incorrect!"

    message =f"{index +1} {result} - Your answer is {question['user_choice']}! Correct Answer: {question['correctAnswer']}"
    print(message)
print("Your score is:", score / len(data))





