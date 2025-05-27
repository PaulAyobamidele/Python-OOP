"# Python-OOP"

### METHOD CALLING

To make any call to a method of an Object, the syntax in Python is as follows

<object>.<method>(<any arguments>)

Why then does it seem as if in Classes, when we called a method, the self arguments is not specified. We only pass in the arguments to fill the placeholders of the other arguments in the Objects.

This boils down to how Python reads this command!

When we call the command
<object>.<method>(<any arguments>)

Python reads

<method of object>(<object>, <any arguments>)

images\python_object_calling.png

Python rearranges the arguments for us when the call is made. It puts the Object name in place of the self arguments and subsequent arguments follows.

### MULTIPLE INSTANCES

oTV1 = TV()
oTV2= TV()
