# import random module for selecting a response
import random
# import datetime module for getting a date for today
import datetime
# from collections import defaultdict
name = "UsydBot"
date = datetime.datetime.today().strftime("%d/%m/%Y")

# Use a dictionary to store a list of responses for each statement
responses = {'What is your name': ['My name is ' + name, 'People call me ' + name],
             'What is the date today': ['Today is ' + date, 'I am sure it is ' + date],
             'everything else': ['I am sorry I cannot understand', 'Sorry, I am not ready to answer that.']}
# responses=defaultdict(lambda: ['I am sorry I cannot understand','Sorry, I am not ready to answer that.'],responses)


# Write a function called respond which chooses a proper answer
def respond(message):
    """
    checks user input and replies
    :param message: question from user
    :return: answer string
    """
    # See if the given statement is in the responses
    if message in responses:
        # Use random.choice() to choose a proper response
        response = random.choice(responses[message])
    else:
        response = random.choice(responses['everything else'])
    return response


# respond('What is your name')
print(respond('What is your name'))
print(respond('What is the date today'))
print(respond('NLP is fun'))
