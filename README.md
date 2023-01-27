# Quizzler-App---OOP-Python
A quiz app that generates 10 questions from various categories depending on the Trivia opendtb using API calls.

It is a simple Python-GUI app that generates 10 different questions from the Trivia open-database using API call from different categories and has a right
    and a wrong button and a scoreboard to follow up with the score.
    
It consists of 5 modules :
    >> ui module : contains the UI design of the program, screen, buttons, labels ...etc.
    >> quiz-brain module : responsible for following up with the question number, answer checking, moving to next question, and detecting the end of quizz.
    >> data module : containing the API call for fetching the questions from the Trivia open-database database.
    >> question-model : consists of a class that contains the question-text and the question-answer as its attributes to ease manipulating questions.
    >> main module : to start the quiz, control the flow of the questions and execution of the app in general.
    
