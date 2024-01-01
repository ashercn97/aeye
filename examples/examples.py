from src import v1


class TestTemplate(v1.TextTemplate):
    lengths = {"answer": "one integer spelled out"}
    template = "The answer is: <answer>"


template = TestTemplate("2+2")

print(template.run())