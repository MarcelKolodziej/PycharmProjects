from survey import AnonymousSurvey
# Define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)

    # Show the survey result.
    print("\nThank you to everyone who participated in the survey!")
    my_survey.show_results()