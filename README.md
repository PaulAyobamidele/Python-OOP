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

### IMPORTANT NOTES

# CLASSES AND OBJECTS

The class defines the shape and capabilities of an object. An object takes this generic frame and forms an actual instance of the class. An object has its own set of all the data defined in the instance variables of the class.

You create an object from a class through an assignment statement!

###### UNDERSTANDING SELF

Two Mental Models for Objects

1.  We can think of each object as a <self-contained> unit that contains all the data type, a set of instance variables defined in the class and a copy of all the methods defined in the original class.

2.  Here it explores the workings of objects at a more lower level.
    So for example. When you say......>>>>>>>>>>>>>>>>
    oDimmer1 = DimmerSwitch('Dimmer1')
    print(type(oDimmer1))
    print(oDimmer1)
    print()

    > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

        <class '__main__.DimmerSwitch'>

    <**main**.DimmerSwitch object at 0x7ffe503b32e0>

    Line one means this is a type class of DimmerSwitch.
    Line two means that the program stored this instance of the class (object) on the computer memory.

    What Self means basically is that.

    Self is the placeholder, that is set to represent the original object in the call.
