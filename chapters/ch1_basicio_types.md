# Basic I/O, Statements, Expressions, Variables, and Types
\label{ch:basicio_types}

## Getting set up to program
\label{sec:getting_started}

Computers consist of hardware and software.  Hardware is the physical stuff you
can hold in your hands, like memory, disks, keyboards, etc.  Software tells the
hardware what to do.  In this book, we're going to learn how to create software.
Creating software is called *programming* or *coding*.  When coding, we give the
computer  instructions for it to do.

Typically, hardware consists of a bunch of electrical circuits.  Instructions
for controlling the circuits is called *machine code* (which is basically a
bunch of 1's and 0's that tell the computer which electrical circuits to turn on
and off... beep beep boop boop).  However, we will not need to learn machine
code or worry about electrical circuits.  We will write code that looks
something more like normal human language, and then we will use another software
program called a *compiler* or an *interpreter* to translate our nice, readable
code into machine code that will control the hardware.  Nice, eh?

The code we write will be written in a high-level programming language named
*Python*.  Although programming languages might look technical, they are more
human reader-friendly than the hardware's machine code language.
Figure~\ref{fig:interp} shows the relationship between Python language code, the
interpreter, and the hardware.

![Code translated by an interpreter to hardware
language\label{fig:interp}](images/ch1/interp.jpg)

To get started programming in Python, we will need to install two software
programs on our computer.  These programs will help us to write our own
programs.  One is the Python interpreter. The other is named *Thonny*.  Thonny
will give us a window in which to type our code, and then Thonny will hand our
code to the Python interpreter so that we can run our program.

FIXME installation of Python and Thonny will go here.  Be sure to help readers
navigate Thonny, and don't forget to have them type commands directly into the
shell (even though they don't know any Python yet).

## The `print` statement
\label{sec:print}

You are now ready to start typing *statements* into the file `hello.py`.  These
statements will make up a program.  Each statement gives the computer an
instruction.  A statement might tell the computer to put something on the screen
(which is called "printing"), it might prompt the user to type something, or it
might tell the computer to remember some information so that we can recall it
and use it later in the program, etc.

Any time from here forward that you click the play button in Thonny, Thonny will
hand your statements to the Python interpreter.  The Python interpreter will
take each statement, one at a time, and change the statement into machine code
(again, 1's and 0's... beep beep boop boop).  If any of your statements put
words or numbers on the screen, those will show up in the Python Shell window.

Let's try to write a program that makes some text show up in the Shell
window.

So, let's type the following into your new **hello.py** file.

```python
print("Hello")
```

Run your program by pressing the play button.

What do you see?  You should see in your Python Shell window the word `Hello`
on a separate line.  If you don't, ask your friendly neighborhood programmer for
help.

Cool.  Why does this work, and can we break it and learn something in the
process?  The `print` statement allows us to put words and numbers on the
screen, that is, in the Python Shell window.  You type print, and then in
parentheses, you put what you want to appear on-screen.  What are those double
quotes doing there?  Let's get rid of them and then run the program to see what
happens.  Replace your code with this:

```python
print(Hello)
```

Notice the double quotes are gone.  Run your program using play button again.

Oh no!  We've broken our computer!  Well, not really.  The word `print` means
something to Python--it's part of the language--but `Hello` doesn't mean
anything to Python.  The double quotes tell Python to actually print the text
"Hello" onto the screen.

Let's delete the one line we have in our file, and replace it with the following
three lines.

```python
print("Hello")
print("How are you?")
print("Goodbye.")
```

Run your code again and you will see these three lines appear on-screen in
order.

What if you change the order of the statements?

```python
print("Hello")
print("Goodbye.")
print("How are you?")
```

Notice we switched the order of the last two statements.  Python will only
execute your statements in the order you give them.  Consider the following
analogy: programs are to computers as recipes are to cooking.  The order of the
statements matter just like the order of steps in a recipe matter.

## The `input` statement
\label{sec:input}

Okay, change our code again.  Delete the three lines you have so far and then
add one new one.

```python
print("Hello, Steve.")
```

This code attempts to make our program more personalized, but it makes the bold
(and unfortunate) assumption that the user's name will always be Steve.  What if
we wanted to ask users what their names are, and then greet the user by name?
How many statements would we need?  We would need two: 1.) to ask for the name,
and 2.) to greet the person using that name.  Here's a good first attempt.

```python
print("What is your name? ")
print("Hello, name.")
```

What do you see?  The code does ask for the user's name (that's good), but it
does not give the user the ability to type anything in (that's bad).

Let's introduce a new type of statement called `input`.  All programs take
*input* from the user (possibly from the keyboard, a mouse, or something else)
and produce *output* (usually information is *printed* to the screen, but the
information could be placed elsewhere, too, like placed in a file or sent over
the Internet to a Web site or something).  The `input` statement will allow the
user to type something in.

Let's try this.  Change the first `print` statement to an `input` statement.

```python
input("What is your name? ")
print("Hello, name.")
```

Run this code.  What happens?

Cool!  The user (you) can now type in your name.  But, then the program fails to
address the person (you, again) using that name.  Bummer.

We need to make the program remember the person's name in the first statement so
that it can be used later in the second statement.

Let's change the first statement from this

```python
input("What is your name? ")
```

to this

```python
firstname = input("What is your name? ")
```

See the difference?  We've put `firstname =` in front of the input command.

Here's how it works. The `input` command retrieves the text the user types in
from the keyboard.  Then, we must *store* it somewhere so that we can use it
later in the program.  The word `firstname` is a *variable*.  Variables are kind
of like Post-It notes for the computer to help it remember numbers and text that
are important to us.  *Variables* store *values*.

We can choose to name the variable almost whatever we want.  There are some
rules for what you can and can't name a variable.  Variables must start with a
letter or an underscore (\_).  After that, they can include any letters,
numbers, or underscores, but no other symbols.  Variables cannot have spaces in
their name.  You also cannot name a variable one of the *reserved words* in
Python.  That is, there are commands that mean something to Python, like `if` or
`while`.  Always name the variable so that you'll remember its name.  Instead of

```python
firstname = input("What is your name? ")
```

We could have typed

```python
dudename = input("What is your name? ")
```

or

```python
awesomename = input("What is your name? ")
```

but for now we'll stick with

```python
firstname = input("What is your name? ")
```

Now, what about the second line?  It's still

```python
print("Hello, name.")
```

We need to use the variable `firstname` to retrieve the value we stored.  Change
the print line to this

```python
print("Hello,", firstname)
```

Run it.  Voila!  It works!

Now, instead of putting one thing inside the parentheses after the word `print`,
we're listing two things, separated by a comma.  The first is a text string
`"Hello,"`.  The second is the variable that stores the name.  Print will print
both of those things, separated by a space.

What if we don't want spaces between the things we print?  We'll get to that
later, too.

Awesome.  Try some stuff.  Try to break your code.  Don't worry, you can always
change your code back.  Our code so far should look like the code in
Listing~\ref{code:input1}.

\begin{codelisting}
\label{code:input1}
\codecaption{}
```python, options: "linenos": true
firstname = input("What is your name? ")
print("Hello,", firstname)
```
\end{codelisting}

Sometimes in this book we will show code snippets like we had been previously.
Other times, if we want to show a series of statements in context, we will use a
listing like we did above.  The listings will typically have line numbers before
each code statement so that we can draw attention to individual statements if we
wish.

Let's learn by breaking things.  In Listing~\ref{code:input1}, change the second
line by removing `first` from the variable name.  The code should now read

```python
firstname = input("What is your name? ")
print("Hello,", name)
```

Run this code.  What happens?  Why do you think this happens?

Once you create a variable named `firstname`, it's called `firstname` for the
duration of the program.  In the first line, we're creating `firstname`.  Then,
in the second line, we try to use a variable called `name`, but there is no such
variable called `name`.  Python rightly vomits red text all over the screen.

It would be like if your name was Jorge and I tried to get your attention by
yelling "Hey, Betty!"  You wouldn't know I was trying to get your attention.

Let's try one more thing.  Let's go back to our original code in
Listing~\ref{code:input1}.

Change the variable `firstname` in the second line by capitalizing the first letter.  In other words, change `firstname` to `Firstname`, like this.

```python
firstname = input("What is your name? ")
print("Hello,", Firstname)
```

Now run it and see what happens.  You get an error, don't you?  `Firstname` and
`firstname` are different variables.  Python is a *case-sensitive* language.  So
we don't make mistakes with mixing uppercase and lowercase in Python, we
typically stick to lowercase.

Remember how I said variable names can't have spaces in them?  Let's try it
anyway.  What if we changed `firstname` to `first name`?

```python
first name = input("What is your name? ")
print("Hello,", first name)
```

Run it and watch our program crash and burn.  It's a good things computers don't
have feelings because ours would probably be feeling rather abused right now.

Notice that each time we tried to "break" our code, we ended up with different
program errors. Pay attention to what the errors say.  At first, the errors look
like "tech-ese" but eventually you'll learn to make sense of them, and it will
help you in correcting your programs.

One cool thing about programming is it will give you a keener eye, and you'll
notice details and mistakes a lot better in other avenues of your life.  Well,
we'll hope so anyway.

## Assignment statements
\label{sec:asgn_stmts}

As it turns out, we now know a lot about Python even though we likely don't
realize it.  We know three kinds of statements.

1.	`print` statements
2.	`input` statements
3.	*assignment* statements

An assignment statement is a statement that creates or updates the value of a
variable.  Our input statement in the previous example was also an assignment
statement because it created the variable named `firstname`.

Let's look at more examples of assignment statements.  Consider the following.
I live on an acreage, and we have a barn where cats tend to gather.  We didn't
have to buy any cats; they just show up.  It's good they are around because they
eat mice and we don't like mice.

Suppose we want to store the number of cats we have in our barn at any given
time, and suppose we currently have six cats.  To store this information in a
Python variable, we would type the following.

```python
cats = 6
```

To experiment with what's happening here, let's add two more lines so that your
code now looks like Listing~\ref{code:cats}.

\begin{codelisting}
\label{code:cats}
\codecaption{}
```python, options: "linenos": true
cats = 6
print(cats)
print("cats")
```
\end{codelisting}

Can you guess what will happen when you run this code?  It is very important to
be able to read code line by line to figure out in your mind what will happen.
Later on, when you're programming and something doesn't work right, you'll need
to look at your code line by line to make sure that it makes logical sense.
This code will print

```console
6
cats
```

There are two print statements in Listing~\ref{code:cats}.  Since there are two
print statements, we can reasonably assume there will be two lines that appear
on the screen.  The first statement makes a new variable named `cats` and
assigns it the value `6`.  The second statement prints the value stored in cats.
The third statement prints the text string "cats" since there are double quotes
around it.

If we hadn't created the variable `cats` before printing the value of `cats`,
Python would have puked red text again saying that it doesn't know what `cats`
is.

It's worth noting that the first statement line `cats = 6` does not print
anything to the screen.  It's just an assignment statement.  It's only job is to
*define* a new variable.  It does not print anything.  Only `print` statements
actually print anything on the Python Shell window.

Okay, let's try to break things again!  What happens if we switch the order of
`cats` and the number `6` in the first line of Listing~\ref{code:cats}, like
this.

```python
6 = cats
```

Run it.  Kablooey!  Now we've learned a rule about assignment statements.  Think
of the = sign as being more like a left arrow \( \leftarrow \).  When we write
`cats = 6`, we can think of it like `cats` \( \leftarrow \) `6` in that the
value `6` is being assigned to the new variable `cats`.  You cannot change the
order of `cats` and `6`.

See?  Computers are picky.

So, on the left-hand side of the equals sign in an assignment statement, we can
give the name of a variable.  If the variable doesn't exist, it is created brand
new.  If the variable does already exist, the value of the variable is updated
(or, overwritten – update and overwrite are synonymous).  So what can we put on
the right-hand side of the equals?

On the right-hand side, we can put any *expression* that produces a value.  Here
are some examples of expressions.

* `6`
* `2 + 4`
* `6 * 1`
* `8 - 2`
* `12 / 2`
* `12 – (3 * 2)`

The asterisk (`*`) or star does multiplication.  The forward slash (`/`)
performs division.  The double forward slash (`//`) performs whole number
division by dropping the remainder.  For example, `5 // 2` produces the value
`2`.  The percent (`%`) gives us the remainder.  This operation is also known as
the modulus, or simply mod.  For example, `5 % 2` produces the value `1`.

The  `+`, `-`, `*`, `/`, `//`, and `%` are known as *operators*.  Operators take
two expressions (which produce values) and produces a new value.  Parentheses
can be used to group expressions much like we do in mathematics.  Also as in
mathematics, operators have precedence.  Expressions produce a value by
evaluating the expression left-to-right while performing parenthetical
expressions first, then multiplication and division, and finally addition and
subtraction.

Just for the heck of it, we could re-write the assignment statement `cats = 6`
as

```python
cats = 12 - (3 * 2)
```

To recap, the left-hand side (abbreviated *LHS*) of an assignment statement is
the name of a variable.  The variable will either be created (that is, defined)
if it doesn't already exist or updated (that is, overwritten) depending on
whether the variable existed previously.  The right-hand side (abbreviated
*RHS*) is an expression that, when evaluated by Python, produces a value.

With all this in mind, let's try something.  What happens when you change our
code so that it looks like Listing~\ref{code:cats_plus1}.

\begin{codelisting}
\label{code:cats_plus1}
\codecaption{}
```python, options: "linenos": true
cats = 6
cats = cats + 1
print("You have", cats, "cats.")
```
\end{codelisting}

Remember how assignment statements work.  They work in two steps.

1. We determine the value produced on the RHS.
2. That value is assigned to the variable on the LHS.

What is the value on the RHS of `cats = cats + 1`?  When we reach this
statement, `cats` is `6`.  Thus, `cats + 1` is the same as `6 + 1`, which is
`7`.  Therefore, the assignment statement `cats = cats + 1` is essentially the
same as saying `cats = 7`.

We can visualize how this assignment statement is *evaluated* in
Figure~\ref{fig:cats_eval}.

![Evaluating an assignment
statement\label{fig:cats_eval}](images/ch1/cats_eval.png)

Remember, the equals sign performs assignment of the value produced by the RHS
to the variable on the LHS.  Therefore, the equals sign is more like a left
arrow that the mathematical equals sign that says "the thing on the LHS and the
thing on the RHS have the same value."  The fact that you can type `x = x + 1`
in Python looks yucky to mathematicians.  Poor, poor mathematicians...

We will say more about the relationship between values, expressions, and
statements in the next section.

## Values, types, expressions, and statements

Let's modify the code example from the previous section.  It is, after all,
silly because you start with a fixed number of cats when, in fact, we could
start with any number of cats.  Let's ask users for how many cats they have in
their barn.  Then, our program should calculate the number of cats they'll have
in the barn in a month's time.  For the sake of argument, let's suppose the
number of cats will increase by 4.

A running program that solves this problem would look like this on the Python
Shell window.

```console
How many cats do you have? 10
In a month's time, you will have 14 cats!
```

The 10 at the end of the first line is typed in by the user, as an example. Can
you write this program?  Give it a try.  You know how to write code to get input
from the user.  You know how to produce output.  You know how to create
variables and perform calculations using expressions.  Try to write this
program.

(One attempt at a solution follows, but try to shield your eyes and don't look
at it right away.  You won't learn very well if you don't try and fail every now
and then.)

Listing~\ref{code:cats_typeerror} shows an attempt that you might have made.

\begin{codelisting}
\label{code:cats_typeerror}
\codecaption{}
```python, options: "linenos": true
cats = input("How many cats do you have? ")
cats = cats + 4
print("In a month's time, you will have", cats, "cats.")
```
\end{codelisting}

This seems reasonable and logical, but it doesn't work!  You end up with an
error.  Let's take a very close look at the error.  It's very important to
understand how to read error messages.  If you know how, they often tell you
exactly what's wrong.

```console
Traceback (most recent call last):
  File "/Users/shep/cs1/code/cats.py", line 2, in <module>
    cats = cats + 4
TypeError: Can't convert 'int' object to str implicitly
```

The error states that the problem is on line 2 of your code.  That's helpful,
but keep in mind line 2 is only where the error was detected.  It's possible
that what caused the error occurred earlier in the code than line 2.

Note what the error message says: "Can't convert 'int' object to str
implicitly."  What does this mean?  In order to understand what it means, we
need to revisit some of the concepts we touched on in Section~\ref{sec:asgn_stmts}.

A *statement* can consist of one or more expressions.  An *expression* is a
piece of code that produces a *value*.  Every value has a *type*.  Consider the
following example.

```python
carrots = (7 + 3) * 2
```

This is one assignment statement whose right-hand side (RHS) consists of two
expressions.  The first expression is

```python
7 + 3
```

`7` and `3` are values known as *integers*, which is just a fancy word for
"whole number."  In Python, an integer is called an `int`, for short.  `7` is a
value and its type is `int`.  `3` is value and its type is `int`.  Since `7` is
an `int` and `3` is an `int`, adding them together gives us the value `10`,
which is also an `int`.  Thus, the following table describes what we know about
this expression.

|Expression|Value|Type|
|---------------------|
|`7+3`|`10`|int|

Remember, an expression is a piece of code that produces a value.  Every value
has a type.

Say it again: an expression produces a value, and every value has a type.

If you're not sure what the type of an expression is, you can find out by typing
the expression into the Python Shell.  If I entered `7 + 3`, the Python Shell
would output `10`.  If I entered `type(7 + 3)`, the Python Shell would output
`"<class 'int'>"`.  Try out the type command to see what different expressions and
different values have as their type.  Try `type(7)`, `type(7.52)`, and
`type("Hello")`.

The next expression for us to consider in our current example is `(7 + 3) * 2`.
We can see from this expression that expressions can consist of other
expressions.  We already know that `7 + 3` is an expression whose value is `10`
and whose type is `int`.  Thus, we can determine the following about this
expression.

|Expression|Value|Type|
|---------------------|
|`(7+3)*2`|`20`|int|

From this, we can determine that the variable `carrots` will have as its value
`20` and its type will be `int`.

There is another number type named `float`.  Floats are used to represent
numbers that have a fractional part.  The value `5.2` is an example of a float.
Float values can be expressed in scientific notation as well.  The value `3e2`
is equivalent to $$3 \times 10^2$$, which is $$300$$, for example.  The value
after the `e` is the power of ten to which we multiply the first number.

Any time we type a specific value like `5` or `5.25` in a program, we call that
value a *literal*.  That is, `5.25` is a float literal because it is "literally"
the value `5.25`.  It's important to have the word "literal" in your programmer
vocabulary.

Now let us consider a different example, shown in Listing~\ref{code:firstlast}.

\begin{codelisting}
\label{code:firstlast}
\codecaption{}
```python, options: "linenos": true
firstname = "Kanye"
lastname = "West"
fullname = firstname + " " + lastname
```
\end{codelisting}

These three statements all involve text values.  Text values have a special type
called *string*.  In Python, a string is called a `str` for short.  If, in the
Python Shell, I were to enter `type("Kanye")`, I would see the output `<class
'str'>`.  If I entered the first statement `firstname = "Kanye"` and then
afterwards entered `type(firstname)`, I would see the output `<class 'str'>`.

There are four expressions in these three statements.  They are shown in the
following table.

|Expression|Value|Type|
|---------------------|
|`"Kanye"`|`"Kanye"`|`str`|
|`"West"`|`"West"`|`str`|
|`firstname + " "`|`"Kanye "`|`str`|
|`firstname + " " + lastname`|`"Kanye West"`|`str`|

Some operators can work on strings, too.  When we use the plus (+) on two string
values, it "smashes" the two strings together to form a new string.  Here, we
are taking the first name and putting a space on the end of it.  Then, we are
appending the last name onto that new string that consists of the first name and
trailing space.  There is a geeky name for "smashing" two strings together to
make a new string, and that name is *concatenation*.  We would say that the plus (+)
*concatenates* two strings.

Remember, an expression is a piece of code that produces a value.  Every value
has a type.  Every variable has a value and a type.

When we write a string literal, we always put quotes around it. The quotes are
not part of the string value, however.  In other words, if I write `"abc"`, I
know `"abc"` is a string literal, and I know the quotes are not a part of the
string's value.  Also, we can use either double quotes (`"`) or single quotes (`'`)
as long as they match one another.  That is, we can write `"cheese"` or
`'cheese'` but not `'cheese"`.

Types and values are tremendously important in Python, and this is illustrated
by our problematic code from earlier in this section.  Recall
Listing~\ref{code:cats_typeerror}, which is shown again below:

```python, options: "linenos": true
cats = input("How many cats do you have? ")
cats = cats + 4
print("In a month's time, you will have", cats, "cats.")
```

When we ran this code, we got an error on line 2 that told us
"\coloredtext{red}{Can't convert 'int' object to str implicitly.}"  When line 2
tries to do the plus operation, it gets confused because `4` is an `int` and it
thinks that `cats` is a `str` rather than an `int`. Think about it.  Can you
guess why?  Look back at line 2.  Look back at line 1.

The `input` command in line 1 retrieves characters entered from the keyboard.
These characters could be letters, symbols, and/or numbers.  Since the value
placed into `cats` by `input` could be any of these things, the type of the
value `input` gives us is `str`.  Suppose the user typed a `5` at the prompt
"How many cats do you have?"  The initial value of the variable cats will be the
`str` value `"5"` rather than the `int` value `5`.

It doesn't make sense to Python to add a string and an integer.  After all, what
is reasonable to assume about the type and value of an expression like `"Hello" +
32`?  In the above example, we need to convert `cats` from a string to an
integer so that we can treat `cats` as an integer.  Let us add a new line of
code after the `input` statement in Listing~\ref{code:cats_cast} at line 2.

\begin{codelisting}
\label{code:cats_cast}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [2]
cats = input("How many cats do you have? ")
cats = int(cats)
cats = cats + 4			
print("In a month's time, you will have", cats, "cats.")
```
\end{codelisting}

The `int` command converts the string value stored in `cats` to an integer, and
then it overwrites the value of `cats` to this new `int` value.  Converting a
value from one type to another is called *casting*.

When we write code, it is bound to have errors we need to correct.  Sometimes,
those errors make the program crash and we see an actual error message in
\coloredtext{red}{red text} on the screen.  Other times, however, we don't get a
nice error message.  Instead, the program appears to behave erroneously.
Erroneous code is called a *bug*, and it is up to us to "debug" the program.

FIXME At some point, we'll have a nice detour in this box about the origin of
the term "debug."  It's an amusing historical tale.  For now, read this:
http://www.wired.com/2013/12/googles-doodle-honors-grace-hopper-and-entomology/

Let's practice detecting and fixing bugs.  We'll again use
Listing~\ref{code:cats_typeerror} as our starting point, only this time instead
of adding `4` to the number of cats, we will double the number of cats by
multiplying by `2`.  After all, when it comes to feral barn cats, this is a more
accurate representation of what happens to cat populations.  Consider our new
Listing~\ref{code:cats_mult}.

\begin{codelisting}
\label{code:cats_mult}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [2]
cats = input("How many cats do you have? ")
cats = cats * 2		
print("In a month's time, you will have", cats, "cats.")
```
\end{codelisting}

Note that we forgot to cast `cats` to be an `int`.  We might expect this
program to have a `TypeError` since it doesn't make sense to multiply a string
and an integer.  In fact, this is not what happens.  Type `3` for the number of
cats.  What happens?

`33` cats?!  Good grief!  As it turns out, Python allows string values to be
repeated using the asterisk/star (`*`) operator.  Instead of performing `3 * 2`,
the expression we've inadvertently performed is `"3" * 2`, which is the same as
`"3" + "3"`, which is the same as `"33"`.  If we properly cast `cats` to an
`int` before multiplying, we get the proper result and we have "debugged" the
program.

It is important to understand what operators are available to us.
Tables~\ref{tbl:arith_ops} and \ref{tbl:str_ops} provide a more comprehensive
list of these operators and their function.

\begin{table}
\caption{Arithmetic operators\label{tbl:arith_ops}}
\begin{tabular}{|r|l|}
\hline
Operator & Usage \\
\hline
\kode{+} & Addition \\
\kode{-} & Subtraction \\
\kode{*} & Multiplication \\
\kode{/} & Division \\
\kode{//} & \pbox{9cm}{Integer division - Returns the whole number result only from division.  Example: \kode{5 // 2} gives us \kode 2 rather than \kode{2.5}.} \\
\kode{\%} & \pbox{9cm}{Modulus, or mod - Returns the remainder from division. Example: \kode{5 \% 2} gives us \kode{1} since \kode{5} divided by \kode{2} is \kode{2} remainder \kode{1}} \\
\kode{**} & \pbox{9cm}{Exponentiation - Returns the result of raising a number to a power.
Example: \kode{2 ** 3} gives us \kode{8} \\
\hline
\end{tabular}
\end{table}



\begin{table}
\caption{String operators\label{tbl:str_ops}}
\begin{tabular}{|r|l|}
\hline
Operator & Usage \\
\hline
\kode{+} & Concatenation \\
      & \pbox{9cm}{\texttt{Example}: \kode{"ab" + "cd"} gives us \kode{"abcd"}} \\
\kode{*} & Repetition \\
      & \pbox{9cm}{\texttt{Example}: \kode{"-" * 5} gives us \kode{"-{}-{}-{}-{}-"}} \\ %* fix syn hilite
\kode{\%} & Formatting \\
      & The string format operator allows us to insert one string value into the middle of another string, which is known as the format string.  The format string can contain any number of format specifiers, which are placeholders for the values to be inserted.  See Table~\ref{tbl:str_fmts} for a list of format specifier examples. \\

      & \texttt{Example 1}: \\
      & Suppose we have a variable \kode{forks} that contains the integer value \kode{5}. \\

      & \kode{"There are \%d forks on the table." \% forks} \\
      & would produce the string \kode{"There are 5 forks on the table."} \\

      & \texttt{Example 2}: \\
      & Suppose we have two variables \kode{first} and \kode{last} that contain string values \kode{"Bob"} and \kode{"Barker"}. \\

      & \kode{"Hi, \%s \%s." \% (first, last)} \\
      & would produce the string \kode{"Hi, Bob Barker."}  Note that if we have multiple values to be inserted into the format string, we enclose them in parentheses and separate them with commas. \\

      & \texttt{Example 3}: \\
      & Suppose we have a variable \kode{ch} that contains a single character \kode{‘!'} \\

      & \kode{"OMG\%c\%c\%c" \% (ch, ch, ch)} \\
      & would produce the string \kode{"OMG!!!"}. \\
\hline
\end{tabular}
\end{table}

\begin{table}
\caption{String format specifiers\label{tbl:str_fmts}}
\begin{tabular}{|r|l|}
\hline
Specifier & Description \\
\hline
\kode{\%d} & the value to be inserted is an integer \\
\kode{\%5d} & the value is aligned to the right across a 5-character column \\
\kode{\%-5d} & the value is aligned to the left across a 5-character column \\
\kode{\%f} & the value to be inserted is a float \\
\kode{\%10.2f} & the value to be inserted is a float aligned to the right across a 10-character column, and we should use two decimal places after the decimal point only \\
\kode{\%s} & the value to be inserted is a string \\
\kode{\%10s} & the value is aligned to the right across a 10-character column \\
\kode{\%-10s} & the value is aligned to the left across a 10-character column \\
\kode{\%c} & the value to be inserted is a single character \\
\hline
\end{tabular}
\end{table}

## Calling functions
\label{sec:call_funcs}

In Section~\ref{sec:asgn_stmts}, we identified the three types of statements
that we knew at that point.

1. `print` statements
2. `input` statements
3. *assignment* statements

We have since learned about other statements.  For example, we can use `type` to
determine the type of an expression or `int` to cast a `str` to an `int`.  We
have also been using the word *command* to refer to words like `print`, `input`,
and `type` that seem to have important meaning to Python.  In fact, these
commands are actually called *functions*.  It's important to learn to speak like
a programmer when you are writing code, so we will call them functions from here
forward.

You'll note that in this book, we try to steer clear of technical terms until we
reach an appropriate time to introduce them.  This seems to be a better approach
than throwing every possible technical term at you right away and then expect
you to memorize them without any context whatsoever.

So, let's practice speaking like programmers.

|Instead of...|Programmers would say...|
|--------------------------------------|
|*use* a function|*call* a function|
|function *produces* a value|function *returns* a value|

Consider the following code.

```python
answer = input("Do you wish to continue (y/n)? ")
```

Programmers would say they are *calling* the input function, and the input
function will *return* a string value.

All functions return a value, even something like `print`.  Just for fun
(wheee!), type the following into the Python Shell window.

```python
var = print("Hello.")
```

Now, type `var` in the Shell window and press ENTER.  Hmm, normally when we type
the name of a variable or we type an expression into the Python Shell window, it
tells us its value.  We get nothing.  Type the expression `type(var)` into the
Shell.  Aha!  The variable `var` has a special type called `NoneType`.  Every
function call is an expression that returns some value, even if at least that
value belongs to `NoneType`.

Okay, it makes sense to have `int`, `float`, and `str` because it's easy to
think of whole and fractional numbers and text values, but why does `NoneType`
exist?  We're really not ready for the answer yet, but rest assured we'll cover
it eventually.  The short answer is that seasoned Python programmers can use
`NoneType` to make their code really easy to read in some circumstances.  Stay
tuned.

We can now simplify the list of statements we know about to these.

1. function call statements
2. assignment statements

From now on, we will refer to things like `print`, `input`, and `type` as
functions rather than as commands.  Note that assignment statements can have
function calls in them, like `name = input("What is your name? ")`.  This
statement is an assignment statement, and the RHS is a function call.

The expressions that are placed between the parentheses after the function's
name are called *arguments*.  Some functions take no arguments, some functions
take one argument, and some other functions can take several arguments.
Arguments are separated with commas.  Arguments tell the function how to do its
job.  The code in Listing~\ref{code:age_inc} shows different examples of how to
call functions with differing numbers of arguments.

\begin{codelisting}
\label{code:age_inc}
\codecaption{}
```python, options: "linenos": true
age = input("What is your age? ")
age = int(age)
age = age + 1
print("In one year, you will be", age, "years old.")
```
\end{codelisting}

Lines 1 and 2 demonstrate calling a function with one argument.  Line 4 has
three arguments.  The first is a string value, the second is a string variable,
and the third is another string value.

Because functions return values, we can call one function and immediately give
its return value to another function.  Look at lines 1 and 2 in
Listing~\ref{code:age_inc} again.  Since casting can be performed on any
expression, we could do both the `input` and the `int` cast on one line, like
this.

```python
age = int(input("What is your age? "))
```

The `input` function is called first, and the result returned by `input` is then given to `int`, which casts the result from a string to an integer.  Students are often puzzled by what appears to be "double right parentheses" at the end of the above statement.  Note that the last right parenthesis matches the left parenthesis for `int`, and the next to last right parenthesis matches the left parenthesis for `input`.  This is shown visually in Figure~\ref{fig:match_parens}.

![Use of arrows to showing matching parentheses\label{fig:match_parens}](images/ch1/match_parens.png)

If the user were to type `18`, the code above would be executed and "transformed" through the steps shown in Figure~\ref{fig:stmt_exec}.

![Statement execution\label{fig:stmt_exec}](images/ch1/stmt_exec.png)

Just for fun (again: whee!!), let's change line 4 of Listing~\ref{code:age_inc} and try out the string formatting operator (`%`).  Instead of this,

```python
print("In one year, you will be", age, "years old.")
```

We could do this:

```python
print("In one year, you will be %d years old." % age)
```

Here, the value of `age` gets inserted into the format string in place of the
`%d`.  There is no advantage to one way or the other, per se.  There will be
lots of ways to write code, though you should try to write code so that is
*readable*.  If you write code that is easy to read, it will be easier to
change.  Some programmers like the second way because it is easy to see the
format of what the output will be, and it can be easier to control where the
spaces go in the output.

There is another way to do string formatting in Python that is newer and is now
preferred as of Python 3.5.  We will introduce it later in the book.  However,
we show this method for string formatting since this is an introductory computer
science textbook, and this "style" of string formatting is one you'd encounter
in other programming languages (e.g., C, Java, etc.).

To review, we started with four lines of code.

```python
age = input("What is your age? ")
age = int(age)
age = age + 1
print("In one year, you will be", age, "years old.")
```

Then, we "tweaked" the code so that, ultimately, it looked like this.

```python
age = int(input("What is your age? "))
age = age + 1
print("In one year, you will be %d years old." % age)
```

As you program, you will develop your own coding style.  You will want to decide
which of the two blocks of code (or a combination of them) looks the most
readable to you.

## Handy functions
\label{sec:handy_funcs}

The purpose of this book is to teach novice programmers how to program.  The
purpose is not to have you learn every single thing about the Python programming
language.  To that point, this book is not intended to be a desk reference for
all things Python.  If you want to find information about a particular language
feature or a list of available functions, the best way to look is to use a Web
search (like Google) or go straight to the [Python
Documentation](https://docs.python.org/) online.

That said, there are a number of handy functions that come "pre-packaged" with
Python and ready for you to use.  We will list a few of them here in the
subsections that follow, since we're highly confident you'll use them very soon.
We'll introduce more functions throughout the book.  Eventually, you'll learn
how to create your own functions.  That will happen in Chapter~\ref{ch:funcs}.
Creating your own functions is pretty cool.

Some functions can be called just by stating their name.  For example, we can
use the `print` function just by typing something like `print("Hello")`.  Other
functions are part of what we call *libraries*.  One example is the `math`
library.  In order to use functions in the `math` library, we must do two
things.  First, we must type the statement `import math`.  Then, `math` library
functions start with the prefix `math.` (read aloud as "math-dot"), so when we
call them we must use the `math.` prefix.  Here is an example of using a
function from a library (see Listing~\ref{code:import_math}).

\begin{codelisting}
\label{code:import_math}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [1,4]
import math

number = float(input("Enter a number: "))
squared = math.pow(number, 2)
print("Your number squared is %f." % squared)
```
\end{codelisting}

In Listing~\ref{code:import_math} line 4, the function named `pow` is contained
in the library `math`.  Because of this, we must type `math.pow` for the
function name in order to call it.  As you may be able to guess, `pow` raises a
number to a power.  In this case, we are raising whatever number the user types
to the second power, which is called squaring the number.

### Math functions
\label{subsec:math_funcs}

Suppose `i` is an `int` variable and `f` and `g` are both `float` variables.
Said another way, `type(i) == int`, `type(f) == float`, and `type(g) == float`.
Some of the functions in Table~\ref{tbl:math_funcs} belong to the `math` library
and some do not.  If we want to use these functions, we need to first type the
statement `import math`.  If we don't write `import math`, we will get a
`NameError` that tells us `math` is not defined.

Here is how to read Table~\ref{tbl:math_funcs}.  If the function is shown as `i =
math.ceil(f)`, that means the function expects us to pass it a `float` (hence
the `f` in parentheses), and the function will return an `int` (hence the `i` on
the LHS of the equals).

There are many more functions found in `math`, but these are the ones you're
most likely to use in the near future.  Again, consult the online [Python
Documentation](https://docs.python.org/) if there's something specific you're
looking for that's not mentioned in this subsection.

\begin{table}
\caption{Math functions\label{tbl:math_funcs}}
\begin{tabular}{|l|l|}
\hline
Function & Returns \\
\hline
\kode{i = round(f)} & The integer resulting from rounding \kode{f}. \\
  & Examples: \\
  & \kode{round(5.2) == 5} \\
  & \kode{round(5.78) == 6} \\
  & \kode{round(6) == 6} \\
  & \kode{round(-1.2) == -1} \\
\kode{i = math.ceil(f)} & The smallest integer \(\geq\) \kode{f}. \\
  & Examples: \\
  & \kode{math.ceil(5.2) == 6} \\
  & \kode{math.ceil(5.78) == 6} \\
  & \kode{math.ceil(6) == 6} \\
  & \kode{math.ceil(-1.2) == -1} \\
\kode{i = math.floor(f)} & The largest integer \(\leq\) \kode{f}. \\
  & Examples: \\
  & \kode{math.floor(5.2) == 5} \\
  & \kode{math.floor(5.78) == 5} \\
  & \kode{math.floor(6) == 6} \\
  & \kode{math.floor(-1.2) == -2} \\
\kode{g = abs(f)} & The absolute value of \kode{f}. \\
  & Examples: \\
  & \kode{abs(23.2) == 23.2} \\
  & \kode{abs(-23.2) == 23.2} \\
\hline
\end{tabular}
\end{table}

Let's consider an example of how we might use some of these functions.

Suppose we want to buy a whole bunch of fidget spinners in bulk and then re-sell
them to make a profit.  If we buy them in bulk, then we can get a good deal
because they'll be cheaper per fidget spinner.  Let's have users enter the
number of fidget spinners they want and the number of spinners that come in a
case.  The program should tell them how many cases they'll need to buy to get at
least that many number of fidget spinners.

To write this program, we'll need to ask for two inputs: the number of spinners
and the number of spinners per case.  Then, we'll need to calculate the number
of cases needed and then output that number.  Listing~\ref{code:spinner_cases}
shows how to do this in Python code.

\begin{codelisting}
\label{code:spinner_cases}
\codecaption{}
```python, options: "linenos": true
spinners = int(input("How many spinners do you need? "))
spinners_per_case = int(input("How many spinners come in a case? "))

cases = math.ceil(spinners / spinners_per_case)

print("You need to order %d cases." % cases)
```
\end{codelisting}

In line 4 of Listing~\ref{code:spinner_cases}, we divide `spinners` by
`spinners_per_case` to get how many cases we'll need.  But this gives us a
fractional number potentially.  For example, if we wanted `18` spinners and `12`
come in a case, that would be `1.5` cases, but we can't order one case and then
another half of a case.  We actually need `2` cases.  This is where `mail.ceil`
comes in.  We take the "fractional" number of cases needed and find the
*ceiling* of it.  This makes `cases` an integer that is greater than or equal to
the number of fractional cases.

### Random functions
\label{subsec:rand_funcs}

The library `random` has functions that help us generate random numbers.  This
is useful for writing programs that involve random chance, for example, rolling
dice, flipping coins, etc.  There are several useful functions in `random`, but
the two we'll focus on right now are `random` and `randint`.

Suppose `i`, `start`, and `end` are `int` variables and `f` is a `float` variable.

\begin{table}
\caption{Math functions\label{tbl:rand_funcs}}
\begin{tabular}{|l|l|}
\hline
Function & Returns \\
\hline
\kode{f = random.random()} & A float value between \kode{0} and \kode{1} inclusive. \\
\kode{i = random.randint(start, end)} & An integer value between \kode{start} and \kode{end} inclusive. \\
\hline
\end{tabular}
\end{table}

Listing~\ref{code:rand_ex} shows an example of how one might use a `random`
library function.

\begin{codelisting}
\label{code:rand_ex}
\codecaption{}
```python, options: "linenos": true
import random

print("Rolling a six-sided die......")
die_roll = random.randint(1, 6)
print("You rolled a %d." % die_roll)
```
\end{codelisting}

The code in Listing~\ref{code:rand_ex} may produce a different die roll every
time you run the program.

## Comments
\label{sec:comments}

As we go forward in learning Python, our programs will get longer and more
intricate.  It may be helpful to annotate our code with short comments to remind
us what our code does.  Listing~\ref{code:age_w_comments} shows a (somewhat
silly) example.

\begin{codelisting}
\label{code:age_w_comments}
\codecaption{}
```python, options: "linenos": true
# Get the user's age.
age = input("What is your age? ")
age = int(age)

# Tell the user his or her age one year from now.
age = age + 1
print("In one year, you will be", age, "years old.")
```
\end{codelisting}

The lines that start with a `#` symbol are called comments.  Any line that
starts with `#` will be ignored by the Python interpreter.  Those lines are only
for the programmer to read.  Again, this is a somewhat silly example because our
code is relatively simple and probably does not require comments.


Programmers will also use comments at the beginning of a code file to document
what the program does.  Here is an example (see Listing~\ref{code:comment_hdr}).

\begin{codelisting}
\label{code:comment_hdr}
\codecaption{A header comment at the top of a code file}
```python
# Program: tictactoe.py
# Programmer: Susan McConnell
# Description:
#   This program allows users to play Tic Tac Toe against
#   a computer opponent.  Users choose the row and column
#   to place their ‘X' or ‘O' on the game grid in each turn.
```
\end{codelisting}

Because placing a `#` symbol at the start of a line hides the code from Python,
another use of comments is to hide old code.  Sometimes, we want to save old
code without deleting it.  This can occur when we're not sure if new code we're
trying out is going to work, and so we may not want to lose our old code in case
we need to go back to it later.  Listing~\ref{code:comment_out} demonstrates
this concept.

\begin{codelisting}
\label{code:comment_out}
\codecaption{Commenting out code}
```python, options: "linenos": true, "hl_lines": [1,2]
#age = input("What is your age? ")
#age = int(age)

age = int(input("What is your age? "))
```
\end{codelisting}

Python will not execute lines 1 and 2 because they are "commented out."
It will, however, execute line 4.

Another use for comments is to help us program.  As human beings, we do not
naturally think in code.  Even experienced programmers struggle to think purely
in terms of programming language code.  One good way to program is to write
comments first in plain English to help us organize our logic and thoughts, and
then we write Python code beneath the comments.  For example, we might start
with:

```python
# Get the user's age.

# Print how old they'll be in a year.
```

Then, we can fill in the details.

```python
# Get the user's age.
age = input("What is your age? ")
age = int(age)

# Print how old they'll be in a year.
age = age + 1
print("In one year, you will be", age, "years old.")
```

Comments end up being very important later on in the book when we start creating
our own functions (yes, we get to make our own functions eventually).  Practice
writing comments when you write your own code.

## Exercises
\label{sec:basicio_types_exercises}

1. Write a program that creates as its output a face on the screen by arranging different symbols, letters, and/or numbers.  Here is an example.

    \begin{verbatim}
    \\///
     0 0
      v
     ---
    \end{verbatim}

2. What is the output of the following program?

    <<(exercises/ch1/p1.2.py)

3. What is the output of the following program?

    <<(exercises/ch1/p1.3.py)

4. What is the output of the following program?

    <<(exercises/ch1/p1.4.py)

5. What is the output of the following program if the user enters a `2` at the first prompt and a `3` at the second prompt?

    <<(exercises/ch1/p1.5.py)

    Be careful.  Try to type this program into the Python Shell and see what you get.

6. Write a program that asks users for two whole numbers.  It should then add them and print the result.  Here is an example of what the output should look like.

    <<(exercises/ch1/p1.6.txt, lang: python)

7. What is the output of the following program?

    <<(exercises/ch1/p1.7.py)

8. What is the output of the following program?

    <<(exercises/ch1/p1.8.py)

9. What is the output of the following program?

    <<(exercises/ch1/p1.9.py)

10. What is the output of the following program?

    <<(exercises/ch1/p1.10.py)

11. What is the output of the following program?  Write down the answer exactly how it would appear on-screen.

    <<(exercises/ch1/p1.11.py)

12. What is the output of the following program?  Write down the answer exactly how it would appear on-screen.

    <<(exercises/ch1/p1.12.py)

13. What is the output of the following program?  Write down the answer exactly how it would appear on-screen.

    <<(exercises/ch1/p1.13.py)

14. What is the output of the following program?  Write down the answer exactly how it would appear on-screen.

    <<(exercises/ch1/p1.14.py)

15. Write a program that asks the user for a single character.  The program should then greet them in block letters "HI" consisting solely of that character.  Here is an example of a running program.

    <<(exercises/ch1/p1.15.1.txt, lang: python)

    Here is another example of a running program if the user were to type a different character.

    <<(exercises/ch1/p1.15.2.txt, lang: python)
