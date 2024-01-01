from src import v1


class TestTemplate(v1.TextTemplate):
    lengths = {"answer": "one integer spelled out"}
    template = "The answer is: <answer>"

class Getter(v1.TextTemplate):
    lengths = {"name": "A name, if no name found say anon", "age": "one integer, if 11 or above do the numerical, if below spell it out like ten.", "gender": "Either boy or girl, based on their name. If unclear write either"}
    template = "The user's name is <name> and their age is <age>. They are a <gender>."


template = Getter("Hi I'm Julie and I am fifteen years old.")

print(template.run()) # prints "The user's name is Julie and their age is 15. They are a girl"