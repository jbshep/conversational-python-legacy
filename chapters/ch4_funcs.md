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
