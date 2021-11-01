### ok so I'm probs gonna need a if/elif/else splitter
# started by defining fizzbuzz as a singe function. added 'for' statement
# indexing variable 'i' from values 0 to 100.
# added three if evaluation statements
# I can't define variables using operator 'i' so I hope it will work if I
# switch it to a random other letter variable.
# ok apparently variable names have to be on the left side
# ok I'm gonna try to have the math operation actually in the
# function instead of having it reference a variable.
# BROOOOOO what if I define them as a function instead of a variable....
# ok scrapped everything because professor told me it's "too complicated"
# you know what nevermind unscrapping it because I want to.
# created eval functions to nest
# needed quotation marks around the "true" to pass the boolean check
# I'm gonna try to do this by changing the rate by which I'm counting
# gotta make it 0 to 101 because for somereason it counts inclusive for the
# first number but uninclusive of the second number
# okay after throwing a new function at the wall i have no idea what
# prof was on about I think I'm onto something
# sandwiching the native python bool() functioninto my if tree doesn't
# seem to work
# using my defined functions with a check of output "true" is printing
# "false" every other line


####Environmentxxxxx
# a / 3 = res3
# a / 5 = res5


###Function
#def fizzbuzz():
#    for i in range(0,100):
#        if evalfive({i}) == "true":
#            print("buzz")
#        elif evalthree({i}) == "true":
#            print("fizz")
#        else:
#            print(f"{i}")



def div5(n):
    res5 = n/5 == int
    bool(res5)

def div3(n):
    res3 = n/3 == int
    bool(res3)



def fizzbuzz():
    for i in range(0,101):
        if div3(i) is True:
            print("bro")
        elif div3(i) is False:
            print(i)
        else:
            print(i)



### restart kind-of

def fizzbuzz():
    for i in range(0,101):
        if i/3 == 2:
            print("bro")
        else:
            print(i)
## this successfully prints the text at number 6, so I know this sort of
# division clause can work in theory.

def fizzbuzz():
    for i in range(0,101):
        if type(i/3) == int:
            print("bro")
        else:
            print(i)
## https://www.codecademy.com/forum_questions/5187c9af569b6ae7ab004fae this
# link seemed to suggest that I could use a built in type() == function,
# yet doing so fails to print anything outside of the normal counting.
#okay, so functions don't like math as a single input, I guess?


def div5(n):
    return n / 5

# ok, this division function works on its own. let's try nesting it...

def fizzbuzz():
    def div5(n):
        return n / 5
    for i in range(0,101):
        if type(div5(i)) == "<class 'int'>":
            print("bro")
        else:
            print(i)
## returns normal counter...

def fizzbuzz():
    def div5(n):
        return n / 5
    for i in range(0,101):
        if type(div5(i)) == int:
            print("bro")
        else:
            print(i)
## trimmed some fat, yet still no bueno... I have another idea.

def fizzbuzz():
    for i in range(0,101):
        i /= 5
        print(f"{i}")

## wait a second (returning to previous function structure to see something)

def fizzbuzz():
    def div5(n):
        n /= 5
    for i in range(0,101):
        if type(div5(i)) == 2:
            print("bro")
        else:
            print(i)
# switched the return division function to division replacing variable with
# operation output. also ran a test defining number 2 instead of integer
# placeholder to see whether the issue was me calling integer check
# or in the function before...... it's the latter


def fizzbuzz():
    def div5(n):
        n /= 5
        print(f"{n}")
    for i in range(0,101):
        if div5(i) == 2:
            print("bro")
        else:
            print(i)
# tried trimming fat by dropping the type() function. also tried
# adding print at the end of the divison function. very weird result.
# oh wait....... it's because telling it to print will print it visibly


def fizzbuzz():
    def div5(n):
        n = n/5
        return(n)
    for i in range(0,101):
        if div5(i) == 2:
            print("bro")
        else:
            print(i)
#### YOOOOOOOOOOO return does the same as print but you can't see it
# this code works as is but it's only set up as testing the div5
# function so only partway there.

def fizzbuzz():
    def div5(n):
        n = n/5
        return(n)
    for i in range(0,101):
        if div5(i) == int:
            print("bro")
        else:
            print(i)
## ok, so == int doesn't work, I'm gonna try bringing back the type() funcs

def fizzbuzz():
    def div5(n):
        n = n/5
        return(n)
    for i in range(0,101):
        if type(f"{div5(i)}") == int:
            print("bro")
        else:
            print(i)
### ran some tests, and confirmed that "type() == int" is a valid
# boolean check in python. no idea why it's not working...
# tried formatting the output of division function as input
# of type() function to no avail.
# I tried establishing just the divison function in the environment
# and then ran "type(div5(2))" to see if it would work with that formatting.
# it did.


def fizzbuzz():
    def div5(n):
        n = n/5
        return(n)
    for i in range(0,101):
        if type(div5(i)) == int:
            print("bro")
        else:
            print(i)
## above code doesn't work yet seems like it should. the only issue I can
# think of that I haven't tested for is that maybe it's not interpreting
# the variable i the way a number input would be interpeted.
# I'm going to test it by defining a variable and running the same
# test as before.

# type(div5(a)) == int  successfully returns as false.

# https://www.programiz.com/python-programming/methods/built-in/isinstance
# I found this source that introduces the isinstance() function, which checks
# if x is an instane of y when listed as an ordered pair.

def fizzbuzz():
    def div5(n):
        n = n/5
        return(n)
    for i in range(0,101):
        if isinstance(div5(i), int):
            print("bro")
        else:
            print(i)
## still no bueno.


def fizzbuzz():
    def div5(n):
        n = n/5
        return(n)
    for i in range(0,101):
        if isinstance(div5(i), int) is True:
            print("bro")
        else:
            print(i)
# nope

def fizzbuzz():
    def div5(n):
        n = n/5
        return(n)
    for i in range(0,101):
        if isinstance(div5(i), int) == True:
            print("bro")
        else:
            print(i)
# still nope

def fizzbuzz():
    def div5(n):
        n = n/5
        return(n)
    for i in range(0,101):
        if isinstance(div5(i), int) == "true":
            print("bro")
        else:
            print(i)
#didn't think that would work but guess what it doesn't.

# totally different approach:

def fizzbuzz():
    for i in range(0,101,5):
        print(i)
        for d in range(0,101,3):
            print(d)
# this just loops, but maybe I'm onto something with this
# branch of nesting...

def fizzbuzz():
    def div5(n1):
        n2 = n1/5
        return(n2)
    def div3(n3):
        n4 = n3/3
        return(n4)
    i5 = div5(i)
    i3 = div3(i)
    for i in range(0,101):
        if i5 == int:
            print("bro")
        elif i3 == int:
            print("aye")
        else:
            print("yo")
# oh, I can't reference i prior to assignment

def fizzbuzz():
    def div5(n1):
        n2 = n1/5
        return(n2)
    def div3(n3):
        n4 = n3/3
        return(n4)
    for i in range(0,101):
        i5 = div5(i)
        i3 = div3(i)
        if isinstance(i5, int) == True:
            print("bro")
        elif i3 == int:
            print("aye")
        else:
            print(i)

# nada, still not working


# Okay, so here's the thing. It's 1AM and this thing is due
# tomorrow. I really wanted to challenge myself to figure
# the entire thing out on my own, but I need to submit something
# and I know I'm allowed to do research, so I'll surrender this
# time. However: I want to figure out the gap in my understanding
# instead of just getting the answer and mentally clocking out.


# after reading the entirety of an article tutorial, this
# is the result:

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
    elif i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else:
        print (str(i))


# I'm very satisfied in having looked up the answer,
# because to my delight I wasn't going about it
# entirely wrong. The structure of the function is
# the same as what I did, however it did not occur
# to me that I could use modulo as a way to efficiently
# divide and integer check all in one fell swoop.
# I'm not entirely sure why my division attempts didn't work,
# but I'm convinced that my understanding is solid because
# multiple times I tried to consider alternate methods
# of "division" and I just didn't put two and two together
# thus failing to realize that modulo was the way to go.

# source: https://k3no.medium.com/fizz-buzz-in-python-2edea331d715
# written by Keno Leon on his blog hosted on medium.com
