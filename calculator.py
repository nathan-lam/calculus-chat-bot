import base_calculator as cr

test = 'You: What is 1 + (2 -3)*( 4 /5)'


#print(math.result)





bot_name = "Sam"
print("Let's chat! (type 'quit' to exit)")
while True:
    sentence = input("You: ")
    if sentence == "quit":
        break

    if cr.valid_expression(sentence):
        print('Bot:', cr.get_answer(sentence))
    else:
        print('Sam: Sorry, I dont understand')
