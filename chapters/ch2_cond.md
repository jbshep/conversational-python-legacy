# Conditional Statements
\label{ch:cond}

## The `if` statement and the Boolean type
\label{sec:if}

Do you remember our sample program involving cats in Chapter 1?  Let's re-write
it here (Listing~\ref{code:barn_cats}).

\begin{codelisting}
\label{code:barn_cats}
\codecaption{}
```python, options: "linenos": true
cats = int(input("How many barn cats do you own? "))
cats = cats * 2
print("In a six-months, you will have %d cats!" % cats)
```
\end{codelisting}

Feral barn cats can multiply rapidly if not spayed or neutered, so this is not
that ridiculous of an example.  Suppose we want our program to make the
observation "That's a lot of cats!" if the barn owner ends up with more than 20
cats.  Our first attempt at this, based on what we know so far, might look like
this.

```python, options: "linenos": true, "hl_lines": [4]
cats = int(input("How many barn cats do you own? "))
cats = cats * 2
print("In a six-months, you will have %d cats!" % cats)
print("That's a lot of cats!")
```

Python programs always execute in sequence.  That is, first Python executes line
1, then line 2, line 3, and finally line 4.  With that in mind, line 4 will
always execute no matter what.  This is absurd given what we are trying to
accomplish, and even more absurd if the user types 0 for the number of cats
initially.

What we need is a way to say "only print if the number of cats is 20 or more."
Python allows us to do this by using something called an `if` statement.  Let's
modify our code as follows (Listing~\ref{code:if_cats}).

\begin{codelisting}
\label{code:if_cats}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [4,5]
cats = int(input("How many barn cats do you own? "))
cats = cats * 2
print("In a six-months, you will have %d cats!" % cats)
if cats > 19:
    print("That's a lot of cats!")
```
\end{codelisting}

Notice how we've added a line just before our final print statement.  Note also
how our print statement in line 5 is now tabbed over one tab-stop.  Now try out
your program using several different inputs for cats.  It works!

To understand more about why it works and how if statements work in general,
let's add one more line of code (for now).

```python, options: "linenos": true, "hl_lines": [6]
cats = int(input("How many barn cats do you own? "))
cats = cats * 2
print("In a six-months, you will have %d cats!" % cats)
if cats > 19:
    print("That's a lot of cats!")
print("Thank you for using our program.")
```

Try out your program using several different inputs for cats again.  Notice how
no matter how many cats you enter, the program always prints "Thank you for
using our program."  Now, let's tab the last line over one tab-stop so that it
lines up with the previous print statement.

```python, options: "linenos": true, "hl_lines": [6]
cats = int(input("How many barn cats do you own? "))
cats = cats * 2
print("In a six-months, you will have %d cats!" % cats)
if cats > 19:
    print("That's a lot of cats!")
    print("Thank you for using our program.")
```

Try out your program again.

Notice how now the program only prints "Thank you for using our program." if the
value of `cats` is greater than `19`.  This tells us something about how `if`
statements work.  When the expression `cats > 19` is true, any statements that
are indented beneath the `if` statement are executed, but they are only executed
if the expression `cats > 19`  is true.  A sequence of statements separated
together by indentation (i.e., tabs) is called a *block* of statements.

Let's try one more thing to understand how tabs/indentation work.  What happens
if we de-indent line 5, i.e., the first line under the `if`?

```python, options: "linenos": true, "hl_lines": [5]
cats = int(input("How many barn cats do you own? "))
cats = cats * 2
print("In a six-months, you will have %d cats!" % cats)
if cats > 19:
print("That's a lot of cats!")
    print("Thank you for using our program.")
```

Run your code.  Kablooey!  The error indicates that whenever Python sees an
`if`, there should be at least one indented section of code beneath it.

Earlier, we referred to `cats > 19` as an expression.  If it is an expression,
then it must produce a value and must have a type, right?  Let's go to our
Python Shell window and type the following: `type(cats > 19)`.  The result we
are given is something called a `bool`.  The word "bool" stands for Boolean.
The word Boolean refers to George Boole, an English mathematician who formalized
mathematical logic.  Valid Boolean values are either `True` or `False`.

Whenever the value of the Boolean expression given to an `if` statement is
`True`, the indented block of code beneath it will be executed.  If it is
`False`, the block will be skipped.

Based on what we know about variables having types, we might conclude that we
can create Boolean variables, too, and we'd be right!  Consider the
code in Listing~\ref{code:cats_bool_var}.

\begin{codelisting}
\label{code:cats_bool_var}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [5,6]
cats = int(input("How many barn cats do you own? "))
cats = cats * 2
print("In a six-months, you will have %d cats!" % cats)

too_many = cats > 19
if too_many:
    print("That's a lot of cats!")

print("Thank you for using our program.")
```
\end{codelisting}

Now, suppose we want to say "You should get more cats" if the barn owner does
not yet have 20 cats.  That is, we want to say this message if the Boolean
expression is `False`.  We can adjust our code by changing this:

```python
if cats > 19:
    print("That's a lot of cats!")
```

to this
```python
if cats > 19:
    print("That's a lot of cats!")
else:
    print("You should get more cats.")
```

Any `if` block can have an `else` block to handle situations where the `if`
condition is `False`, but having an `else` block is optional.

Boolean expressions can be formed using *logical operators*.  We've already seen
greater-than (`>`).  Table~\ref{tbl:logic_ops} shows the rest of the logical operators in
Python.  Note that, for example, `>=` denotes greater-than-or-equal-to,
presumably because the symbol \( \geq \)  does not exist on your computer keyboard.
Also, note that comparing two values for equality uses the `==` double-equals
symbol.  We already use the equals (`=`) symbol for assignment statements so `==`
is used to compare two values as part of a Boolean expression.

\begin{table}
\caption{Logical operators\label{tbl:logic_ops}}
\begin{tabular}{|r|l|}
\hline
Operator & Description \\
\hline
\kode{==} & equals \\
\kode{!=} & not equals \\
\kode{>} & greater than \\
\kode{>=} & greater than or equal to \\
\kode{<} & less than \\
\kode{<=} & less than or equal to \\
\hline
\end{tabular}
\end{table}

## `elif` and Boolean Operators
\label{sec:elif_bool_ops}

Different states in the U.S. have different rules for when one is allowed to
obtain a license to drive an automobile.  One common practice is to allow
individuals who are 16 or older to get a license.  Suppose we wished to write a
Python program that tells people if they are eligible to obtain a driver's
license in their state.  We might prompt users for their respective ages, and
then we could respond appropriately.  Let's use the code in
Listing~\ref{code:driver_start} as our starting point.

\begin{codelisting}
\label{code:driver_start}
\codecaption{}
```python, options: "linenos": true
age = int(input("What is your age? "))
if age >= 16:
    print("You are old enough to take your license exam.")
else:
    print("Perhaps you should ride a bike for now.")
```
\end{codelisting}

The situation in some states is more involved than this.  In fact, let us
suppose that if users are 14 or older, they can obtain a learner's permit where
they are able to drive if accompanied by an adult.  If they are 16 and they also
have had a driver's education class, then they can take the license exam.  Got
it?  Let's ignore driver's education for right now to simplify things, and let's
try to re-write our program using what we know so far.

```python
age = int(input("What is your age? "))
if age >= 14:
    print("You may obtain a learner's permit.")
else:
    if age >= 16:
        print("You are old enough to take your license exam.")
    else:
        print("Perhaps you should ride a bike for now.")
```

That's a lot of indentation!  Fortunately, the indentation makes the logic of
our code a bit easier to follow, which is a nice feature of Python code.  When
we reach the first `else`, our code beneath the `else` starts at a new indentation
level.

Try running this code using a variety of inputs.  Do you notice a problem?

It appears that no matter what age we enter, we can never get it to tell us
we're old enough to take the license exam.  Our Boolean conditions are not in
the correct order.  Even if we type that we are 17 years old, for example, the
first condition is `True`, so it prints "You may obtain a learner's permit."
Let's fix the order of our code to place the most restrictive Boolean expression
first.

```python
age = int(input("What is your age? "))
if age >= 16:
    print("You are old enough to take your license exam. ")
else:
    if age >= 14:
        print("You may obtain a learner's permit.")
    else:
        print("Perhaps you should ride a bike for now.")
```

This is much better.

You might imagine that if you have a lot of different conditions you wish to
handle in your program, your code many eventually look like a very long series
of stair steps.  This would make our code a bit difficult to read and maintain,
so Python provides us with a statement for making a series of else-if
conditions.  This statement is called `elif`, for short.  We can re-write the
code above as follows.

```python
age = int(input("What is your age? "))
if age >= 16:
    print("You are old enough to take your license exam. ")
elif age >= 14:
    print("You may obtain a learner's permit.")
else:
    print("Perhaps you should ride a bike for now.")
print("Done.")
```

Note that we've also added a statement that prints "Done" for illustrative
purposes.

Having `elif`'s work the same way as having an `else` block followed by an `if`
block.  If the first condition is `True`, we print that we are old enough to
take the exam.  Then, none of the other conditions are checked.  Instead, Python
drops down to the "Done" `print` statement.  If the first condition is `False`,
then, and only then, is the next condition checked.  If that condition is
`True`, we print that they can obtain a learner's permit and we drop down to the
"Done" `print` statement.  If that condition was `False`, our code descends to
the `else` block.

`else` blocks are always optional, as are `elif` blocks.  You can have any
number of `elif` blocks, but `if`/`elif`/`else` blocks must always come in that
order: first an `if` statement, then any `elif`'s, and finally an `else`.

Now let's consider driver's education in our example.  Individuals must be 16
years old and have had a driver's education class to take the license exam.  So,
we'll need to ask them if they've taken the exam by using another `input`
statement.

\begin{codelisting}
\label{code:drivers_ed_start}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [2]
age = int(input("What is your age? "))
drivers_ed = input("Have you passed driver's education? (y/n) ")
if age >= 16:
    print("You are old enough to take your license exam. ")
elif age >= 14:
    print("You may obtain a learner's permit.")
else:
    print("Perhaps you should ride a bike for now.")
print("Done.")
```
\end{codelisting}

Notice how we are prompting users to enter either `"y"` or `"n"` for their
answer to the driver's education question.  Also notice that we do not need to
cast the value returned from the `input` function to another type like we did in
the previous `input` statement (the one that asks for the age).  The variable
`drivers_ed` can remain a string, because `"y"` or `"n"` are string values.

Now, let's adjust our logic.  We'll only show the part of the code that deals
with taking the license exam for now.  This code:

```python
if age >= 16:
    print("You are old enough to take your license exam. ")
```

can become this code:

```python
if age >= 16:
    if drivers_ed == "y":
        print("You are old enough to take your license exam. ")
```

This new code says that in order to print `"You are old enough to take your
license exam"` first `age >= 16` must be `True`, and then `drivers_ed == "y"`
must be `True`, too.

There is another way to do this that you might like better.  We can use
something called a *Boolean operator*.  Instead of this:

```python
if age >= 16:
    if drivers_ed == "y":
        print("You are old enough to take your license exam. ")
```

we can say this:

```python
if age >= 16 and drivers_ed == "y":
    print("You are old enough to take your license exam. ")
```

The `and` keyword is the Boolean operator.  We can now modify Listing~\ref{code:drivers_ed_start} as follows in Listing~\ref{code:drivers_ed_and}.

\begin{codelisting}
\label{code:drivers_ed_and}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [2]
age = int(input("What is your age? "))
drivers_ed = input("Have you passed driver's education? (y/n) ")
if age >= 16 and drivers_ed == "y":
    print("You are old enough to take your license exam. ")
elif age >= 14:
    print("You may obtain a learner's permit.")
else:
    print("Perhaps you should ride a bike for now.")
print("Done.")
```
\end{codelisting}

When we join two separate Boolean expressions together with the keyword `and`,
the resulting expression is `True` only if both of the expressions are each
`True`.  If either `age >= 16` is `False` or `drivers_ed == "y"` is `False`,
then the whole Boolean expression `age >= 16` and `drivers_ed == "y"` is
`False`.

There are three Boolean operators in Python, which are given in Table~\ref{tbl:bool_ops}.

\begin{table}
\caption{Logical operators\label{tbl:bool_ops}}
\begin{tabular}{|r|l|}
\hline
Operator & Description \\
\hline
\kode{and} & Suppose \kode{a} and \kode{b} are Boolean expressions. \\
  & \\
  & If \kode{a == True} and \kode{b == True}, then \kode{a and b == True}. \\
  & If \kode{a == True} and \kode{b == False}, then \kode{a and b == False}. \\
  & If \kode{a == False} and \kode{b == True}, then \kode{a and b == False}. \\
  & If \kode{a == False} and \kode{b == False}, then \kode{a and b == False}. \\
  & \\
  & In other words, the expression \kode{a and b} is only \kode{True} if both \kode{a} and \kode{b} are individually \kode{True}. \\
\kode{or} & Suppose \kode{a} and \kode{b} are Boolean expressions. \\
  & \\
  & If \kode{a == True} and \kode{b == True}, then \kode{a or b == True}. \\
  & If \kode{a == True} and \kode{b == False}, then \kode{a or b == True}. \\
  & If \kode{a == False} and \kode{b == True}, then \kode{a or b == True}. \\
  & If \kode{a == False} and \kode{b == False}, then \kode{a or b == False}. \\
  & \\
  & In other words, the expression \kode{a or b} is \kode{True} whenever either \kode{a} or \kode{b} is individually \kode{True}, or both of them are \kode{True}. \\
\kode{not} & Suppose \kode{a} is a Boolean expression. \\
  & \\
  & If \kode{a == True}, then \kode{not a} is \kode{False}. \\
  & If \kode{a == False}, then \kode{not a} is \kode{True}. \\
\hline
\end{tabular}
\end{table}

Let us look at another example where these Boolean operators become useful.
Suppose we want to write a program that tells people if they have an increased
risk for heart disease.  There are a number of known risk factors, but for now
we'll only consider three.  Without Boolean operators, we might write the
program in Listing~\ref{code:heart_disease1}.

\begin{codelisting}
\label{code:heart_disease1}
\codecaption{}
```python, options: "linenos": true
bp = input("Do you have high blood pressure (y/n)? ")
smoke = input("Do you smoke (y/n)? ")
hist = input("Do you have a family history of heart disease (y/n)? ")

if bp == "y":
    print("You have an increased risk of heart disease.")
elif smoke == "y":
    print("You have an increased risk of heart disease.")
elif hist == "y":
    print("You have an increased risk of heart disease.")
else:
    print("You do not have an increased risk for heart disease.")
```
\end{codelisting}

Note that each of the statements that follow the `if`/`elif` conditions all
print the same message.  Instead, we can use the Boolean operator `or` to
simplify the code resulting in Listing~\ref{code:heart_disease2}.

\begin{codelisting}
\label{code:heart_disease2}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [5]
bp = input("Do you have high blood pressure (y/n)? ")
smoke = input("Do you smoke (y/n)? ")
hist = input("Do you have a family history of heart disease (y/n)? ")

if bp == "y" or smoke == "y" or hist == "y":
    print("You have an increased risk of heart disease.")
else:
    print("You do not have an increased risk for heart disease.")
```
\end{codelisting}

Lastly, we can use the `not` operator to improve the readability of code.
Recall how, in our driver's license example
(Listing~\ref{code:drivers_ed_and}), we asked if the user had taken a driver's
education course.  With this scenario in mind, consider the following (Listing~\ref{code:drivers_ed_bool_expr}).

\begin{codelisting}
\label{code:drivers_ed_bool_expr}
\codecaption{}
```python, options: "linenos": true
age = int(input("What is your age? "))
drivers_ed = input("Have you taken driver's ed (y/n)? ") == "y"
if 14 <= age and age <= 16 and not drivers_ed:
    print("You should consider taking a driver's ed course.")
```
\end{codelisting}

This example includes a few interesting code constructions.  Line 2 of
Listing~\ref{code:drivers_ed_bool_expr} is different from what you've seen
before.  Previously in Listing~\ref{code:drivers_ed_and}, we let `drivers_ed` be a string
variable whose value should be `"y"` or `"n"`. In this code, `drivers_ed` is a
Boolean variable.  Why?

Notice that the `input` part of the statement is followed by a logical operator,
the double-equals (`==`).  Thus, we are comparing what the user types to the
string `"y"`.  If the user typed `"y"`, then the RHS of the assignment statement
is `True`, so `drivers_ed` gets the value `True`.  If the user types anything
else, `drivers_ed` becomes `False`.

Next, we have code that checks to see if the user age's is still typically in
the range that students take a driver's education class.  If so, and they've not
had driver's education, they are advised to do so via a `print` statement.  The
only way the `print` statement will happen is if the age is between `14` and
`16`, and they've not had driver's education.

Keep in mind that the programming practice in line 2 of
Listing~\ref{code:drivers_ed_bool_expr} might not be a good idea.  Your author
has only written code this way to show you that it can be done.   The latter
part of the expression (`== "y"`) might be hard to notice, and because it is
hard to notice, it may make the code more difficult to read and therefore
maintain.  In the future, we may want to check what the user typed in to make
sure it's what we expect (i.e., a `"y"` or a `"n"`).  Checking inputs is
something we'll discuss in Chapter~\ref{ch:loops}.

## Nuances of Boolean operators
\label{sec:bool_nuances}

Students will sometimes write code like this.

```python
age = int(input("What is your age? "))
if age == 14 or 15:
    print("You can get a learner's permit.")
```

Run this code and type `18`.  Uh oh.  Why does it print "You can get a learner's
permit"?

Remember than anything on the LHS and RHS of a Boolean operator must be itself a
Boolean expression.  In other words, the LHS and RHS must both be `True` or
`False`.  In the above example, there is an expression on either side of the
double-equals.  One is

```python
age == 14
```

and the other is

```python
15
```

The expression `age == 14` is `False`.  The expression `15` is `True`.
**Anything non-zero in Python is treated as `True`.**  Therefore, the Boolean
expression is transformed as in Figure~\ref{fig:bool_op_nuance}.

![Evaluating a Boolean \kode{or}
expression\label{fig:bool_op_nuance}](images/ch2/bool_op_nuance.png)

Instead of

```python
age == 14 or 15
```

a programmer should write

```python
age == 14 or age == 15
```

Bottom line: be very careful when using and/or.

## Exercises
\label{sec:cond_exercises}

1. Suppose `x` is an integer variable.  What is the difference between the
expression `x = 2` and the expression `x == 2`?

2. Given the following code:

    <<(exercises/ch2/p2.2.1.py)

    What is the type and value of each of the following expressions?

    <<(exercises/ch2/p2.2.2.py)

3. Identify the error in the following code.

    <<(exercises/ch2/p2.3.py)

4. Identify the error in the following code.

    <<(exercises/ch2/p2.4.py)

5. What is the output of the following code?

    <<(exercises/ch2/p2.5.py)

6. Consider the following code.

    <<(exercises/ch2/p2.6.1.py)

    What is the output of the program if \kode{a} and \kode{b} were given the following values prior to the start of the code?

    <<(exercises/ch2/p2.6.2.py)

7. What is the output of the following code?

    <<(exercises/ch2/p2.7.py)

8. Write code that rounds a float number up or down *without* using the \kode{round} function introduced in Section~\ref{sec:handy_funcs}.  That is, write code that asks for a number, and then it takes that number and rounds it up or down appropriately without using \kode{round}.  For example, if the user types `3.6`, the program should output a `4` since the fractional part `.6` is greater than `.5`.  The user were to type `3.2`, the program should output a `3` since the fractional part `.2` is less than `.5`.

    It may help to know that if you use the `int` function to cast a float to an integer, the fractional part disappears.  This is called *truncation*.  For example, in the following code

    <<(exercises/ch2/p2.8.py)

    the value of \kode{i} ends up being `3`.
