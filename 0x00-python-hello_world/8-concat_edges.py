#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
will = str[str.index("object"):str.index("programming") + len("programming")]+" "+ "with python"
print(will)
