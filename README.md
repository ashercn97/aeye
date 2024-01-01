# aeye
a _truly_ intelligent type system.

When using aeye, types aren't simple. They are not strings, floats, or integers. They are not even composite types like a user where their username is a string and their age is an integer. Instead, they work similarly to "types" in real life.

For example, a "type" in aeye could be "an integer spelled out" or "A name" (basically a step above composite types). It utilises the OpenAI API currently. 

## Useage

Right now, there is one main class that is used. It is called ```TextTemplate```. ```TextTemplate``` gets subclasses and then when initialized takes a prompt. In the subclass class, you will add the following attributes:

lengths: a dictionary of a keyword and then the "type" that it is supposed to be. For example, ```lengths = {"name": "the name found in the users introduction"}```
template: a template of how the response should look, keywords put between <>. For example ```template = "The user's name is <name>"```

Then, you will initialize it with the prompt, so if we had the class:

```
class TextMath(v1.TextTemplate):
  lengths = {"answer": "an integer but written out"}
  template = "The answer to the equation is <answer>"
```

we would use it by doing

```
template = TextMath("2+2")
print(template.run())
```

Which would print 
```
"The answer to the equation is four"
```

## Future

I want to add way for only type checking without the prompting. There is already a system and user prompt for them in the oai_functions file, but I am planning on making it better.




