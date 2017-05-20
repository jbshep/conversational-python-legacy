# Functions
\label{ch:funcs}

## Introduction to Functions
\label{sec:func_intro}

Consider Listing~\ref{code:one_prog}.

\begin{codelisting}
\label{code:one_prog}
\codecaption{}
```python, options: "linenos": true
print("This is program one.")
x = input("Enter a string: ")
if x[0].lower() in "aeiou":
    print("That string starts with a vowel.")
else:
    print("That string does not start with a vowel.")

print("This is program two.")
x = input("Enter a string: ")
if x.isalnum():
    print("That string only contains only a-z's and 0-9's.")
else:
    print("That string contains some \"weird\" characters.")
```
\end{codelisting}

Each of these two sections of code are supposed to be their own separate
programs.  If I type this code into one code file and run it, of course, both
programs will be executed, one after the other.  This is, after all, how
programs work.  Python executes each statement, one after another, and since
"program one" comes before "program two," all of program one's statements will
be executed and then all of program two's statements will be executed.

In program one, we are checking the first character of `x` using the expression
`x[0]` (see line 3 of Listing~\ref{code:one_prog}).  We change it to lowercase,
and then we use the `in` operator to see if that single character is a vowel.
Without the `in` operator, we would need to write an `if` statement that looks
something like this.

```python
if x[0].lower() == "a" or x[0].lower() == "e" or \
   x[0].lower() == "i" or x[0].lower() == "o" or \
   x[0].lower() == "u":
```

Yuck.

Let’s try something new.  Let's construct Listing~\ref{code:two_progs1} by
modifying Listing~\ref{code:one_prog} using a new language construct.

\begin{codelisting}
\label{code:two_progs1}
\codecaption{}
```python, options: "linenos": true
def one():
    print("This is program one.")
    x = input("Enter a string: ")
    if x[0].lower() in "aeiou":
        print("That string starts with a vowel.")
    else:
        print("That string does not start with a vowel.")

def two():
    print("This is program two.")
    x = input("Enter a string: ")
    if x.isalnum():
        print("That string only contains only a-z’s and 0-9’s.")
    else:
        print("That string contains some \"weird\" characters.")
```
\end{codelisting}

Now run this code.  What happens?  Yes, nothing!  There is absolutely no output,
which suggests that none of our statements ran.  Oh dear.  Well, let’s add a bit
more code (see the highlighted lines in Listing~\ref{code:two_progs2}).  

\begin{codelisting}
\label{code:two_progs2}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [18,19]
def one():
    print("This is program one.")
    x = input("Enter a string: ")
    if x[0].lower() in "aeiou":
        print("That string starts with a vowel.")
    else:
        print("That string does not start with a vowel.")


def two():
    print("This is program two.")
    x = input("Enter a string: ")
    if x.isalnum():
        print("That string only contains only a-z’s and 0-9’s.")
    else:
        print("That string contains some \"weird\" characters.")

# Add the following line.
one()
```
\end{codelisting}

Try again.  Aha!  Only the statements of code listed underneath `def one():` are
executed.  Now, try changing `one()` to `two()` in
Listing~\ref{code:two_progs2}.  Run it.  Now only the statements under `def
two():` are executed.

What’s happening here?  Any code that is not indented at all is considered part
of the *main* program.  Code that is indented beneath a line that starts with
`def` is like a little mini-program.  `def` stands for "define."  In this case,
we are defining a mini-program and giving it a name.  Mini-programs are better
known as... (\*drum roll please\*)... *functions*!

So, in Listing~\ref{code:two_progs2}, the main program is simply on lines 18 and
19 (though line 18 is just a comment).  Let's change the main program to see
what happens.  See Listing~\ref{code:two_progs3} (specifically lines 18 - 20).

\begin{codelisting}
\label{code:two_progs3}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [18,19,20]
def one():
    print("This is program one.")
    x = input("Enter a string: ")
    if x[0].lower() in "aeiou":
        print("That string starts with a vowel.")
    else:
        print("That string does not start with a vowel.")


def two():
    print("This is program two.")
    x = input("Enter a string: ")
    if x.isalnum():
        print("That string only contains only a-z’s and 0-9’s.")
    else:
        print("That string contains some \"weird\" characters.")

print("Main: calling a function.")
two()
print("Main: end of program.")
```
\end{codelisting}

Run this, and notice what happens.  The code starts in the main non-indented
section by printing `"Main: calling a function."` Then, the expression `two()`
calls the function, which makes the program "jump" up to the definition of the
function, which starts with `def two():`.  Each of the statements indented under
`def two():` are executed, one by one, and then once those statements are
finished, we jump back down to where `two()` was called in the first place.
Finally, the main program resumes and we print `"Main: end of program."`

In a sense, functions are like "tangents."  We can momentarily leave the main
program to execute some pre-prepared code.  We have been *calling* functions
throughout the entire book already.  We have used functions like `print`,
`input`, and `int`.  Now we have a sense of how to *define* our own new
functions.

## Parameters
\label{sec:params}

Let’s look at another example of how we can define our own functions that we can
call later.  Suppose, at a certain fictitious university named Higher Ed
University, students are given email addresses that follow a naming convention.
To form the email address, we take the first four characters of a student’s last
name, then the first three characters of a student’s first name, and then append
"@heu.edu" to it.  We could write a function to determine and print out such an
email address.

\begin{codelisting}
\label{code:print_email}
\codecaption{Defining \kode{print\_email}}
```python, options: "linenos": true
def print_email(first, last):
    username = last.lower()[0:4]
    username = username + first.lower()[0:3]
    print("%s@heu.edu" % username)
```
\end{codelisting}

Notice that the `print_email` function is defined differently than `one` or
`two` in Listing~\ref{code:two_progs3} in Section~\ref{sec:func_intro}.  In our
previous example, when we defined those functions, their definitions had empty
parentheses after the function name.  Now, we have two things that look a lot
like variables inside the parentheses.  In fact, they are variables, and their
values are used inside the function’s body.  Variables that are given inside the
parentheses in a function definition are called the function’s *parameters*.

Let us call this function.  We might type this.

```python
print_email("Jack", "Jackson")
```

This would print:

```console
jackjac@heu.edu
```

Or, if we typed this:

```python
print_email("Shania", "Carrington")
```

It would print:

```console
carrsha@heu.edu
```

How does this work?  When we call a function, we must provide the correct number
of values to the function.  The correct number of values is based on how many
parameters the function has.  In this case, the function `print_email` has two
parameters, `first` and `last`.  The *values* we pass to the definition of a
function are called the *arguments*.  When a function is called, the arguments’
values become the parameters’ values.  Thus, `first` gets the value `"Shania"`
and `last` gets the value `"Carrington"`.

Clever readers might suspect that this function has a bug.  It looks like if the
last name is fewer than four characters long or the first name is fewer than
three characters long, the program would crash.  Surprisingly, in Python the
string range operator is very forgiving.  If you were to type the expression
"abc"[0:20], the substring returned will still be "abc".  We can read this
substring operation aloud as “Start at index 0 and return any characters up to
index 20, if it exists.”  Therefore, there is no bug, but skeptical thinking
like this will help us as we program in the future.

What happens when you switch the order of the arguments?

```python
print_email("Carrington", "Shania")
```

What happens if you do not have the correct number of arguments?

```python
print_email("Shania")
```

Try these things on your own to see what happens.  Try to guess what they do
before you actually run the code.  If they produce errors, make a mental note of
what the error looks like.  That way, if you encounter that error again in the
future, you'll know what caused it and how to fix it.

Let's move on to a different example.  Let us write code that defines a new function, and then let's write some code to call that new function (see Listing~\ref{code:print_money}).

\begin{codelisting}
\label{code:print_money}
\codecaption{Defining and calling \kode{print\_money}}
```python, options: "linenos": true
def print_money(amount):
    print("$%.2f" % amount)

my_money = 50.25
print_money(my_money)
```
\end{codelisting}

This code will print:

```console
$50.25
```

It does not matter when we give an argument to a function call if we provide a
value or an expression that returns a value (in this case, the name of a
variable).

Now, let’s make one more change to the code (see
Listing~\ref{code:print_money_change_var}).


\begin{codelisting}
\label{code:print_money_change_var}
\codecaption{Defining and calling \kode{print\_money}, attempt 2}
```python, options: "linenos": true, "hl_lines": [3,7]
def print_money(amount):
    print("$%.2f" % amount)
    amount = amount + 10.00

my_money = 50.25
print_money(my_money)
print_money(my_money)
```
\end{codelisting}

In this example, we are doing something new.  We are taking the parameter
`amount` and actually changing its value in the last statement of the function’s
body.  Where does `amount`’s value come from?  It is passed the value of
`my_money` down in the main program.  One thing we should look out for is “side
effects.”  Does changing the value of `amount` have any effect on the value of
`my_money`?  In other words, does changing `amount` also change `my_money`?  If
it did, we would expect the second call to `print_money` to print a different
value than the first.

As it turns out, when we run the code, we see this:

```console
$50.25
$50.25
```

Changing `amount` does not change `my_money`.  This is because arguments are
passed to parameters in Python using their value alone.  This is called *pass by
value*.  If changing the parameter had actually changed the argument, then we
would have said Python practices *pass by reference*, where a reference to the
original variable would have been given to the function rather than just the
value.  Remember that Python uses pass by value when you are writing function
definitions.

It is generally bad programming practice to change the values of parameter
variables in the body of a function -- again, generally speaking -- but there are
exceptions.  For the most part, a programmer should be able to consult the
parameters at any point in the function’s body to see what the “input” to the
function was.  There is one situation, however, where it is desirable to modify
the parameter values passed to a function.  We will discuss this situation in
Chapter~\ref{ch:lists}.

## Return values
\label{sec:ret_vals}

If we think of functions in terms of them being like mini-programs, we might
observe that programs tend to ask for input, they doing something with the
input, and then finally they produce output.  In a sense, parameters give
programmers the ability to pass “input” to a function.  What then might we do to
allow functions to provide “output” back to the main program?

As you might recall, we have already seen functions that do this -- functions that
Python already has defined for us.  For example:

```python
ssn = input("Enter your social security number: ")
```

`input` is a function.  It allows the programmer to provide an argument, which
is the string to use for prompting the user.  We can imagine that somewhere,
some programmer has written a function definition for `input` that looks
something like this:

```python
def input(prompt):
    # Code that makes input work goes here.
```

Notice that the `input` function returns a value, which we then assign to a
variable.  In a function’s body, we can tell Python what value to return using
the `return` statement.  Let's start with an overly simple example so that we
understand the mechanics of the `return` keyword.  Suppose we define the
function shown in Listing~\ref{code:forty_two}.

\begin{codelisting}
\label{code:forty_two}
\codecaption{}
```python, options: "linenos": true
def favorite_number():
    return 42

number = favorite_number()
print(number)
```
\end{codelisting}

Whenever a `return` statement is encountered in a function’s body, the function
stops immediately and returns to where the function was called.  The value that
is returned from the function is whatever value was listed in the `return`
statement.  In Listing~\ref{code:forty_two}, there is only one statement in the
body of the `favorite_number` function: the return statement itself.

To interpret the code in Listing~\ref{code:forty_two}, we start at line 4, which
is the first line of the main program.  The `favorite_number` function is
called, so the program "jumps" up to `favorite_number`'s definition.  The
program enters the function's body and encounters the `return` statement.  The
`42` listed in the `return` statement causes the function to end, and the value
`42` is sent back to line 4.  Finally, line 4 can finish as the `42` is assigned
to the variable `number`.

Now, let's see how a function might take a parameter value and then return
something based on the parameter value.  To experiment with this, we will define
a function named `next_int` that takes an integer as a parameter.  Whatever
integer is given, the function will return the "next" integer.  If we give
`next_int` the value `3`, it will return `4`.  Said another way, `next_int(3) ==
4`.  If we give `next_int` the value `-2`, it will return `-1`.  Said another
way, `next_int(-2) == -1`.  We define `next_int` in Listing~\ref{code:next_int}.

\begin{codelisting}
\label{code:next_int}
\codecaption{}
```python, options: "linenos": true
def next_int(int_value):
    next_value = int_value + 1
    return next_value
```
\end{codelisting}

Now, let's call our function and print its resulting value:

```python
print(next_int(3))
print(next_int(-2))
```

which produces the following output:

```console
4
-1
```

Notice in `next_int`'s function body how we create a new variable named
`next_value`.  `next_value` holds the value we will return from our function.
There is no rule that says we must return the value of a variable.  Any
expression that produces a value can follow the `return` keyword.  In other
words, we could have simply returned `int_value + 1`, as shown in
Listing~\ref{code:next_int2}.

\begin{codelisting}
\label{code:next_int2}
\codecaption{}
```python, options: "linenos": true
def next_int(int_value):
    return int_value + 1
```
\end{codelisting}

Time to move on and look at a different example function.  Consider
Listing~\ref{pig_latin_word}.

\begin{codelisting}
\label{code:pig_latin_word}
\codecaption{}
```python, options: "linenos": true
def piglatin(english):
    if english[0] in "aeiou":
        return english + "-way"
    else:
        return english[1:] + "-" + english[0] + "ay"
```
\end{codelisting}

Whenever a `return` statement is encountered in a function’s body, the function
stops immediately and returns to where the function was called.  The value that
is returned from the function is whatever value is given to the return
statement.  Maybe you already understand this, but it bears repeating because it
is very important to understand this concept if you are going to be able to
understand functions.

In Listing~\ref{code:pig_latin_word}, we have a function named `piglatin`.  This
example comes from the exercises in Section~\ref{sec:loops_exercises} from
Chapter~\ref{ch:loops}.  We can pass to `piglatin` an English word, and for
simplicity’s sake, suppose the word always consists solely of lowercase letters.
We are only handling two cases for now: 1.) the word starts with a vowel, or 2.)
the word starts with a single consonant letter.

A function may have zero, one, or many return statements, but as soon as the
program encounters a return statement, the function ends and the value is
returned immediately.

How might we call this function?  There are several ways we could do it.

```python
engword = "apple"
pigword = piglatin(engword)
print("The pig latin of apple is %s." % pigword)

print("The pig latin of catalog is %s." % piglatin("catalog"))
```

Since `piglatin` returns a string, we can call `piglatin` anywhere we would
normally put a string.

It's hard for new programmers to learn to write their own functions.  It takes
practice.  It's helpful to see how to define a lot of example functions, and
it's also helpful to try writing your own functions and seeing what problems you
run into.  Let's take a look at a bunch of example functions, and at some point,
you should go back and try to define these functions on your own without looking
at the code.

Listing~\ref{code:get_area} is a function definition that, given the radius of a
circle, will return the area of the circle.

\begin{codelisting}
\label{code:get_area}
\codecaption{}
```python, options: "linenos": true
import math

def get_area(radius):
    return math.pi * radius * radius
```
\end{codelisting}

Listing~\ref{code:roll} is a function definition that simulates rolling a
6-sided die.

\begin{codelisting}
\label{code:roll}
\codecaption{}
```python, options: "linenos": true
import random

def roll():
    return random.randint(1, 6)
```
\end{codelisting}

Listing~\ref{code:posintsum} defines a function named `posintsum` that prints
the sum of the first `n` positive integers.  The listing also shows how you
might call this function.  For example, `posintsum(3)` would calculate the
result of `1+2+3+4` as `10`.  As another example, `posintsum(10)` would
calculate the result of `1+2+3+4+5+6+7+8+9+10` as `55`.  Note how we use a `for`
loop and a variable named `total` to accomplish this before returning the result
in `total`.

\begin{codelisting}
\label{code:posintsum}
\codecaption{Function definition and sample function calls for \kode{posintsum}}
```python, options: "linenos": true
def posintsum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print("1+2+3+4 = %d" % posintsum(4))
print("1+2+3+4+5+6+7+8+9+10 = %d" % posintsum(10))
```
\end{codelisting}

What if we had forgotten the return statement at the end of the function?  In
other words, what if our function definition looked like
Listing~\ref{code:posintsum_missing_return}?

\begin{codelisting}
\label{code:posintsum_missing_return}
\codecaption{Forgotten \kode{return} statement in \kode{posintsum}}
```python, options: "linenos": true, "hl_lines": [5]
def posintsum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    # Oh no! I need to remember to actually return total.
```
\end{codelisting}

As it turns out, all functions in Python return something no matter what.  If a
function does not have a `return` statement, the function will return a special
value known as `None`.  The type of the value `None` is `NoneType`.  You may
have already seen `None` if you got confused on the difference between `print`
and `input`, as many new programmers do.  Suppose we did the following.

```python
x = print("Enter a number: ")
# Oops.  x == None
```

Clearly, we meant to use `input` rather than `print`.  `print` returns `None`.

## Modularizing Code with Functions
\label{sec:func_mod}

Now that we can make “mini-programs” using functions, we can begin composing
full programs made out of mini-programs.  We will use functions to help organize
our code so that our code is easier to read and easier to maintain.  This will
also make it easier to cope with errors, particularly user error, as we will see
in the following example.  Let’s take an idea from the previous section and
suppose that we want to write a simple program that asks the user for a positive
integer `n`.  Our program should print out the sum of all positive integers up
through that `n`.  We will also want to only accept valid input, so we will need
to re-ask for input if what the user types is incorrect.  Examples of bad input
might be `23r5` (since there is a `r` in the number) or `-2` (since `-2` is
negative).

It is often difficult for novice programmers to know where to begin in writing a
program.  One very effective approach is to start by writing comments in English
that describe, step-by-step, what our program needs to do.  So, we might do
this.

```python
# Ask for a positive whole number 'n' (i.e., a positive integer).

# Compute the sum of 1 + 2 + ... + n and print it.
```

That’s a good start.  Now, let’s become "lazy" programmers.  Laziness is a good
thing in some situations, and this is one of those situations.  In fact, a
famous programmer named Larry Wall once stated that laziness is one of three
“virtues” that programmers should seek (look it up on the Web).

In order to be "lazy," we should pretend that someone has already defined
functions for us, and by calling these functions, our program will be done!

```python
# Ask for a positive whole number 'n' (i.e., a positive integer).
n = getposint()

# Compute the sum of 1 + 2 + ... + n and print it.
total = getsum(n)

print("The sum of the first %d positive whole numbers is %d."
       % (n, total))
```

Hooray!  We’ve written our program in three lines of actual code!  Well, we
haven’t really, but now we can focus on the “pieces” of the program by defining
the functions that will actually make this program work.  Let’s define
`getposint` first (see Listing~\ref{code:getposint}).

\begin{codelisting}
\label{code:getposint}
\codecaption{Function definition for \kode{getposint}}
```python, options: "linenos": true
def getposint():
    s = input("Enter a positive whole number: ")
    while not s.isdigit() and s != "0":
        print("Sorry, that does not look like a positive whole
               number.  Please try again.")
        s = input("Enter a positive whole number: ")
    return int(s)
```
\end{codelisting}

Now, let’s try to define `getsum` in Listing~\ref{code:getsum}.  Keep in mind
that `getsum` has a single argument, so it needs a single parameter, too.

\begin{codelisting}
\label{code:getsum}
\codecaption{Function definition for \kode{getsum}}
```python, options: "linenos": true
def getsum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
```
\end{codelisting}

Note that in line 3 of Listing~\ref{code:getsum} the second expression in
`range` is `n+1`.  Since we want to add up all the values from `1` to `n`, the
value that will make us leave the look is one more than `n`, that is, `n+1`.

Writing functions takes practice.  The more you try, the better you will get at
it.  A program with everything defined is shown in
Listing~\ref{code:compute_posintsum}.

\begin{codelisting}
\label{code:compute_posintsum}
\codecaption{Code composed with functions}
```python, options: "linenos": true
def getposint():
    s = input("Enter a positive whole number: ")
    while not s.isdigit() and s != "0":
        print("Sorry, that does not look like a positive whole
               number.  Please try again.")
        s = input("Enter a positive whole number: ")
    return int(s)

def getsum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


# Ask for a positive whole number 'n' (i.e., a positive integer).
n = getposint()

# Compute the sum of 1 + 2 + ... + n and print it.
total = getsum(n)

print("The sum of the first %d positive whole numbers is %d."
       % (n, total))
```
\end{codelisting}

Sometimes, programmers even like to put their main program code into its own
function.  That way, all of the code exists in some function.
Listing~\ref{code:compute_posintsum_final} shows how we would do this.

\begin{codelisting}
\label{code:compute_posintsum_final}
\codecaption{Code composed with functions, using \kode{main}}
```python, options: "linenos": true
def getposint():
    s = input("Enter a positive whole number: ")
    while not s.isdigit() and s != "0":
        print("Sorry, that does not look like a positive whole
               number.  Please try again.")
        s = input("Enter a positive whole number: ")
    return int(s)

def getsum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def main():
    # Ask for a positive whole number 'n' (i.e., a positive integer).
    n = getposint()

    # Compute the sum of 1 + 2 + ... + n and print it.
    total = getsum(n)

    print("The sum of the first %d positive whole numbers is %d."
           % (n, total))

# Run the program by calling main().
main()
```
\end{codelisting}

Some other programming languages like C++ and Java actually require programs to
start by calling a function named `main`.  If we always put our main program
code into a function named `main`, it will ease our transition from Python to
other languages.

## Variable Scope
\label{sec:var_scope}

## Exercises
\label{sec:funcs_exercises}
