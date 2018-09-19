# Loops and String Manipulation
\label{ch:loops}

## `while` loops
\label{sec:while}

Most of the examples of code we've seen so far have been fairly short -- a few
lines here and there.  Now we're going to start looking at programs that are a
bit longer.  Don't be too daunted by this.  If you practice, you'll gain comfort
with knowing how to break down programs section by section.  Let's go ahead and
practice doing this starting with this chapter.

Sometimes we'll want to repeat an action in code.  One example might be that we
repeatedly ask the user for input until we run out of that input.  Suppose we
write a program that calculates the amount of sales tax on different items at a
store.  We might write the code found in Listing~\ref{code:sales_tax}.

\begin{codelisting}
\label{code:sales_tax}
\codecaption{Code to compute total cost on items including sales tax}
```python, options: "linenos": true
tax = 0.07   # that is, 7 percent
print("Enter the amount of each item.")
print("Enter 'quit' to end the program.")
amount = input("Amount of item? ")
while amount != "quit":
    amount = float(amount)
    total = (amount * tax) + amount
    print("The total for that item will be %.2f." % total)
    amount = input("Amount of item? ")
print("Thank you for using this program.")
```
\end{codelisting}

To some readers, this program might look intimidating at first, but each section
contains ideas we've seen before.  We've just added one idea after the next.
So, what are these familiar code sections?  Well, we are getting input from the
user.  If the input is not the word "quit," we cast the amount to a float (line
6) and compute the total price of the item with tax included (line 7).

What is special about the above code is the keyword `while` in line 5.  `while`
works similar to `if` in many ways.  When we use `if`, we specify a Boolean
condition immediately after the word `if`, and if the condition is `True`,
Python executes the code that is indented beneath it.  `while` works the same
way, however, once we reach the end of the indented block, the code "loops" back
up to the condition again.  If the condition is again `True`, we reenter the
indented block of code.  Thus, we can make code repeat itself as long as a
condition is met.  A programming language "construct" that allows code to be
repeated is known as a *loop*.

We call `amount != "quit"` in Listing~\ref{code:sales_tax} the *loop condition*.
We call the indented block of statements that follows the loop condition the
*loop body*. We say that the statements in the indented block are *inside* the
loop body. The final `print` statement in line 10 of
Listing~\ref{code:sales_tax} is not indented and is therefore *outside* the loop
body.

Try out the code above if you haven't already.  Does it behave the way you
expect?

Now, notice that we ask for input twice in this program: once just before we try
to enter the loop (line 4), and once at the end of the indented block inside the
loop body (line 9).  Why?  The value returned by the initial `input` statement
gets us into the loop body, though it doesn't have to.  It is possible that the
user types "quit" right away, in which case the program bypasses the loop and
prints our "thank you" message.  At the end of the loop body, we need to ask the
user for the next input value, so that we have a new amount.  Otherwise, the
program would just continue to calculate the same total value over and over
again and the program would never have the chance to end.

To see this for yourself, delete the last line of the loop body in
Listing~\ref{code:sales_tax}, i.e., delete line 9. Instead of deleting it, you
could just comment it out by putting a `#` symbol at the start of that line.
Run your code and type an initial amount, say, `4.00`. Your code will endlessly
compute sales tax with no end in sight!  Press the "Control" and "C" keys
simultaneously to abort your program (we will write this `Ctrl+C` in the future
because that's how programmers write such things).

With this in mind, we will often see loops written using the pattern in
Figure~\ref{fig:while_tmpl}.

![A common \kode{while} loop
pattern\label{fig:while_tmpl}](images/ch3/while_tmpl.png)

We call each new time through the body of the loop an *iteration*.  We may refer
to the first iteration, second iteration, next iteration, final iteration, etc.,
when discussing the behavior of a loop.

To get a sense of the mechanics of how `while` loops work, beginning programmers
often consider "toy" examples that showcase a number of "gotchas" when it comes
to programming loops.  Consider Listing~\ref{code:while_ex1}.

\begin{codelisting}
\label{code:while_ex1}
\codecaption{"Toy" while loop example 1}
```python, options: "linenos": true
x = 1
while x <= 5:
    print(x)
    x = x + 1
print("Done.")
```
\end{codelisting}

Run it.  This prints the following.

```console
1
2
3
4
5
Done.
```

We don't always need to have a non-indented statement following a loop.  We are
only doing this in the examples so it is clear in the output that we left the
loop body.

In each iteration, we print the value of `x` and then increase `x` by `1`.
Adding `1` to a value is such a common thing in programming that it has a
special name: *increment*.  That is, we are *incrementing* `x` by adding `1` to
it.  When `x` eventually becomes `5`, we print the `5` and then add `1` more to
make `x` become `6`.  When we evaluate the expression `x <= 5`, we get `6 <= 5`,
which is `False`, so our code falls down to the non-indented section of code.

It is good to observe that, in this example, the last value we print is `5`, but
the value of `x` when we exit the loop is `6`.

Let's look at another "toy" example.  We will modify
Listing~\ref{code:while_ex1}, which was the following.

```python, options: "linenos": true, "hl_lines": [3,4]
x = 1
while x <= 5:
    print(x)
    x = x + 1
print("Done.")
```

Notice that we've highlighted the statements that form the loop body.  Let's
change the order of those loop body statements to see what, if any, effect it
has (Listing~\ref{code:while_ex2}).

\begin{codelisting}
\label{code:while_ex2}
\codecaption{"Toy" while loop example 2}
```python, options: "linenos": true, "hl_lines": [3,4]
x = 1
while x <= 5:
    x = x + 1
    print(x)
print("Done.")
```
\end{codelisting}

Run it.  Our output is different from the first example.

```console
2
3
4
5
6
Done.
```

Can you explain why this is?

In Listing~\ref{code:while_ex2}, we are incrementing `x` before we print it.
Thus, the first value we print is not `1` but `2`.  The order of statements
matters in programming, and it definitely matters in loops.

Consider another example (Listing~\ref{code:while_ex3}).

\begin{codelisting}
\label{code:while_ex3}
\codecaption{"Toy" while loop example 3}
```python, options: "linenos": true
x = 1
while x <= 5:
    print(x)
print("Done.")
```
\end{codelisting}

Here, we have removed the line that increments `x`.  You should be able to guess
what will happen when we run this program (hint: be ready to press `Ctrl+C`).

Since we have removed the line that increments `x`, `x` never changes, and so
the program just prints `1` over and over again.  Loops that are never-ending
are called *infinite loops*.  You will inadvertently create infinite loops every
now and then when you program.  It becomes very important to know how to debug
them.

Let's try another example (Listing~\ref{code:while_ex4}).

\begin{codelisting}
\label{code:while_ex4}
\codecaption{"Toy" while loop example 4}
```python, options: "linenos": true
x = 0
while x <= 4:
    print(x)
    x = x + 1
print("Done.")
```
\end{codelisting}

All we've done is changed the initial value of `x` and the value of `x` that
causes us to not reenter the loop.  The output is:

```console
0
1
2
3
4
Done.
```

Let's make a small change to Listing~\ref{code:while_ex4}. Suppose we change
line 2 so that the code appears as it does in Listing~\ref{code:while_ex5}.

\begin{codelisting}
\label{code:while_ex5}
\codecaption{"Toy" while loop example 5}
```python, options: "linenos": true, "hl_lines": [2]
x = 0
while x < 4:
    print(x)
    x = x + 1
print("Done.")
```
\end{codelisting}

Now instead of `<=`, we have `<`.  This makes the code end the loop one value of
`x` earlier.  The output is:

```console
0
1
2
3
Done.
```

Let's change the condition in line 2 again so that it uses `>` instead of `<`.
The code now reads as in Listing~\ref{code:while_ex6}.

\begin{codelisting}
\label{code:while_ex6}
\codecaption{"Toy" while loop example 6}
```python, options: "linenos": true, "hl_lines": [2]
x = 0
while x > 4:
    print(x)
    x = x + 1
print("Done.")
```
\end{codelisting}

What is the output?  Why?

The output will be, as you may or may not have expected, is:

```console
Done.
```

The variable `x` is set to zero initially.  In the next line, the expression `x >
4` becomes `0 > 4`, which is `False`.  Thus, the code bypasses the loop body
entirely.  There is no "rule" that says we have to do the loop body at least
once.  Computers are stupid.  They only do what you tell them to.  In this case,
because the condition is `False` initially, we never do the loop body and go
straight to the non-indented line of code past the loop body.

All of our "toy" examples thus far have involved incrementing a loop variable
`x`, that is, adding `1` to `x`.  However, we can change our variable however we
wish.  We could create the code in Listing~\ref{code:while_ex7}.

\begin{codelisting}
\label{code:while_ex7}
\codecaption{"Toy" while loop example 7}
```python, options: "linenos": true
x = 2
while x <= 8:
    print(x)
    x = x + 2
print("Who do we appreciate?")
```
\end{codelisting}

In this code, we add `2` to `x` each time.  The output of this code is:

```console
2
4
6
8
Who do we appreciate?
```

We've used the heck out of the variable name `x`.  Let's pick a different name
for a while just for the sake of using something different.  In
Listing~\ref{code:blastoff}, we will use the name `count` for our loop variable
name.

\begin{codelisting}
\label{code:blastoff}
\codecaption{Blastoff example}
```python, options: "linenos": true
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Blastoff!")
```
\end{codelisting}

In this code, we subtract `1` from `count` each time.  This is called
*decrementing* `count`. The output of this code is:

```console
5
4
3
2
1
Blastoff!
```

Toy examples are a great way to understand how loops work from a "mechanical"
perspective, but let's see how we can use them to solve real problems.  Recall
our very first example in this section, Listing~\ref{code:sales_tax}, which
dealt  with reporting the price of an item after sales tax.  Our next example is
also related to money.  Suppose we open a savings account, one that pays 5%
interest per year into the account as long as we don't withdraw any money that
we deposit.  Let's say we start the account by depositing $10,000.00.  How many
years will it take to double our investment?

Mathematicians would attempt to derive an equation to solve this problem, but
with computers we don't have to.  We can make the computer figure it out for us.
We just need to know how to write the code to tell the computer what to do.

The question "How many years will it take to double our investment?" tells us a
lot about the code we would need to write.  We would need to keep track of our
balance as it grows by 5% each year.  We would need to keep track of the number
of years that have elapsed so far in our code.  We would also need to check to
see if the balance has doubled.  If, in describing what our program is supposed
to do, we say we need to check something, we are often talking about a Boolean
condition found in an `if` statement or a `while` loop.

Try to program this example on your own first.  You can't learn to be a good
programmer if you don't try things regularly by starting with a blank screen or
a blank sheet of paper.  If you get really stuck, then (and only then) glance at
the answer below.

Okay, let's look at a solution found in Listing~\ref{code:investment1}
(Warning: Our initial solution will have flaws, as initial solutions often do).

\begin{codelisting}
\label{code:investment1}
\codecaption{Doubling investment example}
```python, options: "linenos": true
balance = float(input("Enter starting balance: "))
years = 0
while balance < 2*balance:
    balance = balance * 0.05 + balance
    years = years + 1
    print("The balance after %d years is $%.2f." %
            (years, balance))
print("It will take %d years to double your investment." % years)
```
\end{codelisting}

This is a good first attempt.  Here, we are letting the loop do the work of
adding to the balance year after year, each time checking to see if the balance
has doubled and if we can leave the loop.  However, our logic is flawed a bit.
Consider the loop condition `balance < 2*balance`.  A variable's value will never
be greater than twice itself (unless that value is negative, but let's steer
clear of negative values in bank accounts!).

The problem here is that we're trying to use the variable `balance` for two very
different purposes simultaneously.  On one hand, we are using `balance` to keep
track of the current balance as it changes year after year.  On the other hand,
we're pretending that it still holds the starting balance from our initial
investment.  We should really keep the starting balance in a separate variable,
which we will name `startbalance`.

With this in mind, we can modify the previous code as follows in
Listing~\ref{code:investment_final}.

\begin{codelisting}
\label{code:investment_final}
\codecaption{Doubling investment example - final version}
```python, options: "linenos": true, "hl_lines": [1,2,4]
startbalance = float(input("Enter starting balance: "))
balance = startbalance
years = 0
while balance < 2*startbalance:
    balance = balance * 0.05 + balance
    years = years + 1
    print("The balance after %d years is $%.2f." %
            (years, balance))
print("It will take %d years to double your investment." % years)
```
\end{codelisting}

## Manipulating and printing strings
\label{sec:str_manip}

Given our newly found exposure to loops, now is a good time to revisit strings.
It turns out, there is a fair amount of nifty stuff we can do with strings using
loops.  Suppose we create a new string variable named `s` in the following way.

```python
s = "abc def"
```

Programmers sometimes talk about different important parts of a string.  They
call these parts *substrings*.  There are a lot of different possible substrings
of `"abc def"` including `"a"`, `"ab"`, and `"def"`, just to name a few.  The
string `""` is also technically a substring of `s`.  Note that `""` is different
from `" "`.  The former is called the *empty string*; it is a string without any
characters.  The latter is a string with a single space in it.

Note that the string `s` contains a space between the substrings `"abc"` and
`"def"`.  That will become an important observation later.  Now, we can inspect
individual characters by using square brackets and character's position in the
string.  Consider the following example.

```python
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])
print(s[7])
```

If we run this code, we see the following output.

```console
a
b
c

d
e
f
Traceback (most recent call last):
  File "/Users/shep/cs1/code/ch3strings.py", line 9, in <module>
    print(s[7])
IndexError: string index out of range
```

The syntax for retrieving a single character from a string `s` is `s[index]`
where `index` is an integer representing the position of the character we wish
to retrieve.  The first character (in this case `"a"`) is at position `0` rather
than position `1`.  That may take a little getting used to. We will use the
words "index" and "position" interchangeably to describe the location of a
character in a string (also, note that the plural of "index" is "indices").
Let's re-list the code again in Listing~\ref{code:str_index}, this time with
comments to explain each line.

\begin{codelisting}
\label{code:str_index}
\codecaption{String indexing}
```python, options: "linenos": true
s = "abc def"
print(s[0]) # print "a"
print(s[1]) # print "b"
print(s[2]) # print "c"
print(s[3]) # print " " (which ends up as just a blank line)
print(s[4]) # print "d"
print(s[5]) # print "e"
print(s[6]) # print "f"
print(s[7]) # Kablooey! There is no character at index 7.
```
\end{codelisting}

Between the square brackets, you can place one index or you can give a range of
indices, as we see in Listing~\ref{code:str_slice}.

\begin{codelisting}
\label{code:str_slice}
\codecaption{String slicing}
```python, options: "linenos": true
s = "abc def"
print(s[0:2])
print(s[0:3])
print(s[3:6])
print(s[3:])
print(s[:4])
```
\end{codelisting}

This code yields the following output.

```console
ab
abc
 de
 def
abc
```

We can observe that the first print in line 2 of Listing~\ref{code:str_slice}
does not print characters at indices `0` through `2`.  Rather, it prints
characters at positions `0` and `1` but not `2`. We might conclude from this
that when we have two indices in square brackets following a string, the first
number is the first position *inclusive* and the second number is the last
position that will be selected up to, but not including, or *exclusive*. Note
that the indices are separated by a colon (`:`). In this situation, we will call
the colon the *slicing operator*.  

Lines 4 and 5 in Listing~\ref{code:str_slice} show us that the first and second
indices of the slicing operator are optional.  If one is omitted, Python assumes
that the we mean "go to the ends of the string."  When we use square brackets to
select one or more characters from a string, we say that we are obtaining a
substring of the original string.  Obtaining a substring from some original
string in this manner is called *string slicing*.

What appears to be indentation in lines 3 and 4 of the output is actually the
single space found at index `3` in the string `s`.  It is difficult to tell if there
is a space at the end of line `5`.  One way to tell is to append an additional
character to the output to see the space.  For example:

```python
print(s[:4] + "$")
```

The output is:

```console
abc $
```

Can you see the space in the output above?

There are quite a few things we can do with strings.  Another interesting
feature of strings is that they have their own set of special functions.
Consider Listing~\ref{code:cheese_shout}.

\begin{codelisting}
\label{code:cheese_shout}
\codecaption{}
```python, options: "linenos": true
t = "I like cheese."
shout = t.upper()
print(shout)
```
\end{codelisting}

Most of the functions we have seen thus far (like `print`, `input`, etc.) do not
have a period/dot in front of them.  Calling a function which operates
specifically on a value or a variable uses *dot-notation*, like `t.upper()`.

On the Internet, typing something in all capital letters is a convention that
indicates shouting.  In effect, the upper() function can be used on a string
value (which is often contained in a variable) to return an all-uppercase
version of that string.  The output of Listing~\ref{code:cheese_shout} is:

```console
I LIKE CHEESE.
```

It is very important to note that `upper()` does not change the contents of the
string variable `t`.  If I do this:

```python
t = "I like cheese."
shout = t.upper()
print(shout)
print(t)
```

I get this as output:

```console
I LIKE CHEESE.
I like cheese.
```

Functions like `upper()` are not restricted to being called on variables.  They
may be called on any string value, like this:

```python
shout = "I like cheese.".upper()
print(shout)
```

This works because Python transforms the first statement as shown in
Figure~\ref{fig:str_transform}.

![\label{fig:str_transform}](images/ch3/str_transform.png)

A common mistake is to omit the parentheses at the end of `upper()`.  Remember
that `upper` is just the name of the function; the parentheses are what calls
the function.  If we remove the parentheses, we get output that looks strange (Listing~\ref{code:func_missing_parens}).

\begin{codelisting}
\label{code:func_missing_parens}
\codecaption{Function call missing parentheses}
```python, options: "linenos": true, "hl_lines": [2]
t = "I like cheese."
print(t.upper)
```
\end{codelisting}

This produces something like:

```console
<built-in method upper of str object at 0x1019807e8>
```

This is Python's way of saying "yes, `upper` is the name of a function.  If you
want to actually use that function, put parentheses at the end."  Let's add the
parentheses to the end of the function call
(Listing~\ref{code:func_using_parens}).

\begin{codelisting}
\label{code:func_using_parens}
\codecaption{A fix for Listing~\ref{code:func_missing_parens}}
```python, options: "linenos": true, "hl_lines": [2]
t = "I like cheese."
print(t.upper())
```
\end{codelisting}

And now, it works.

Observe that when we "shout" by using `upper()`, the punctuation displayed is a
period.  Shouldn't we change that to an exclamation point (`!`)?  Consider the
following code in Listing~\ref{code:str_replace}.

\begin{codelisting}
\label{code:str_replace}
\codecaption{Using \kode{replace}}
```python, options: "linenos": true
t = "I like cheese."
shout = t.upper().replace(".", "!")
print(shout)
```
\end{codelisting}

The function `replace` is another string function.  It takes two arguments.  The
first is a pattern to find in the string, and the second is a string we wish to
insert instead.

Consider how Python executes line 2 of Listing~\ref{code:str_replace} (see Figure~\ref{fig:str_replace_transform}).

![\label{fig:str_replace_transform}](images/ch3/str_replace_transform.png)

This example works because `t` is a string, so calling `t.upper()` returns
another string.  And, because `t.upper()` is a string, we can call `replace` on
it to return yet another string.  Calling a series of functions in one line is
called *function chaining*.

Note that the original string value of `t` still hasn't changed.  `t` is still
`"I like cheese."`.  If we wanted to actually change `t`, we would need to use
an assignment statement as in Listing~\ref{code:replace_asgn}.

\begin{codelisting}
\label{code:replace_asgn}
\codecaption{Using assignment with \kode{replace}}
```python
t = t.upper().replace(".", "!")
```
\end{codelisting}

Now, `t` is changed to the newly returned string value.

We can even chain calls to `replace` (see Listing~\ref{code:replace_chain}):

\begin{codelisting}
\label{code:replace_chain}
\codecaption{Function chaining with \kode{replace}}
```python
t = t.upper().replace("LIKE","LOVE").replace(".", "!")
```
\end{codelisting}

As you might guess, and in the interest of completeness of our discussion, in
addition to `upper` there is a function named `lower` for returning all
lowercase versions of strings.

Now, let us explore the relationship between strings and loops.  Consider the
code in Listing~\ref{code:print_chars}.

\begin{codelisting}
\label{code:print_chars}
\codecaption{Using a loop to print characters in a string}
```python, options: "linenos": true
s = "abc def"
index = 0
while index < 7:
    print(s[index])
    index = index + 1
```
\end{codelisting}

Listing\ref{code:print_chars} produces the following output:

```console
a
b
c

d
e
f
```

Why?

The variable `index` starts at `0`.  Each time in the loop body, we print the
value of the expression `s[index]`, which in the first loop iteration is `s[0]`,
which has the value `"a"`.  The code adds `1` to `index`, so now index is `1`
(it was `0` previously).  The code loops back around to the beginning of the
loop. We print the value of `s[index]` again, which this time is `s[1]`, and
`s[1]` is `"b"`.  We continue in this fashion with each iteration of the loop
having a new value of `index`.  Eventually, `index` becomes `7`, at which point
we exit the loop.  

This is yet another "toy" example intended to get us to see the relationship
between loops and strings, which is a powerful relationship we will exploit very
shortly.

Let's make one change to Listing~\ref{code:print_chars}.  We will change only
the value of the string variable `s`.  Our new code is in
Listing~\ref{code:print_chars_hardcodelen}.

\begin{codelisting}
\label{code:print_chars_hardcodelen}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [1]
s = "protagonist"
index = 0
while index < 7:
    print(s[index])
    index = index + 1
```
\end{codelisting}

The output is now:

```console
p
r
o
t
a
g
o
```

Oh no!  Where is the rest of the string?  Why did it stop after `7` characters?
It stopped after `7` characters because we told it to!

Unfortunately, we have *hard-coded* the loop condition as `index < 7`.  We could
change the value of `s`, and we shouldn't assume the length of `s` will always
be `7` characters.  From a logic standpoint, the `7` is supposed to refer to the
length of the string, which is also `1` more than the last index in the string.
Recall from the previous example that the last index of `s` was `6` and the
number of characters (the length of the string) was `7`.  In
Listing~\ref{code:print_chars_hardcodelen}, the length of the string is `11`,
not `7`.

Any time we hard-code a value, like `7`, it makes our code brittle and less
resistant to change.  Let us replace this line:

```python
while index < 7:
```

with this line:

```python
while index < len(s):
```

The `len` function returns the number of characters in the string.  Our new code
is shown in Listing~\ref{code:print_chars_good}.

\begin{codelisting}
\label{code:print_chars_good}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [3]
s = "protagonist"
index = 0
while index < len(s):
    print(s[index])
    index = index + 1
```
\end{codelisting}

Alternatively, we could have done things a little differently.  See
Listing~\ref{code:print_chars_alt} and note the highlighted lines.

\begin{codelisting}
\label{code:print_chars_alt}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [3,4]
s = "protagonist"
index = 0
lastindex = len(s) - 1
while index <= lastindex:
    print(s[index])
    index = index + 1
```
\end{codelisting}

We have created a new variable named `lastindex`.  In the case of the string
`"protagonist"`, the value of `lastindex` will be `10` since `len(s)` is `11`.
It is very important to see the relationship between the last index and the
length of the string. Because indices start at `0`, not `1`, the last index is
always the length minus `1` (in this case, the value of the expression
`len(s)-1`).

Let's see how well this is all sinking in.  Can you write code to print the
characters of a string, one on each line, but in reverse order this time?  In
other words, if my string is `"abc"`, can you write code that prints:

```console
c
b
a
```

Give it a try.

Let's check your work.  With some experimentation, you might have been able to
get close to a solution that looks like the code in
Listing~\ref{code:reverse_print_str}.  (If not, keep trying and practicing.)

\begin{codelisting}
\label{code:reverse_print_str}
\codecaption{}
```python, options: "linenos": true
s = "abc"
index = len(s) - 1
while index >= 0:
    print(s[index])
    index = index - 1
```
\end{codelisting}

Note that we are setting the initial index variable to the last index of string
(again, length minus `1`), and in our loop body we are subtracting `1` rather
than adding `1`.

In Python, as it is in other programming languages, there is often more than one
way to write a program.  Another approach to printing a string in reverse could
take advantage of the fact that you can put *negative* indices in square
brackets to obtain characters in a string starting from the end rather than from
the beginning.  For example, suppose we have the following code.

```python
foo = "abc"
print(foo[-1])
print(foo[-2])
print(foo[-3])
```

This prints:

```console
c
b
a
```

With this in mind, we could write new code that produces the same output as Listing~\ref{code:reverse_print_str}, but in a different way.  Consider Listing~\ref{code:reverse_print_str_alt}

\begin{codelisting}
\label{code:reverse_print_str_alt}
\codecaption{}
```python, options: "linenos": true
foo = "abc"
index = -1
while index >= -len(foo):
    print(foo[index])
    index = index - 1
```
\end{codelisting}

Note the loop condition.  If `len(foo)` in this case is `3`, then `-len(foo)` is
`-3`.

(Why did we name our variable `foo`?  That's weird, right?  You're correct; it
is weird!  There's a historical reason why computer science books often name
variables `foo` and `bar`.  Search the Web for `foobar` and its original form
`FUBAR` so that you can learn where this nomenclature comes from.)

## `for` loops
\label{sec:for}

Loops of the form found in Listing~\ref{code:while_setup_for} are very common.
Suppose `n` is an integer variable defined earlier in a program.

\begin{codelisting}
\label{code:while_setup_for}
\codecaption{}
```python, options: "linenos": true
k = 0
while k < n:
    print(k)
    k = k + 1
```
\end{codelisting}

Loops of this form are so common, in fact, that there is a shorter version of
the loop known as a `for` loop.  Listing~\ref{code:while_setup_for} could be
re-written as a `for` loop as shown in Listing~\ref{code:for_ex1}.

\begin{codelisting}
\label{code:for_ex1}
\codecaption{}
```python, options: "linenos": true
for k in range(0, n):
    print(k)
```
\end{codelisting}

Gone is the explicit declaration of the variable `k`.  Gone also is the
increment statement `k = k + 1`.  The range expression gives `k` an initial
value of `0` in this example, and then it allows the loop to continue until `k ==
n`, at which point the computer leaves the loop.

Recall Listing~\ref{code:print_chars_good} in Section~\ref{sec:str_manip}, which
is shown below.  To print the characters of a string, each on a separate line,
using a `while` loop, we could write:

```python, options: "linenos": true
s = "protagonist"
index = 0
while index < len(s):
    print(s[index])
    index = index + 1
```

We can now re-write this code using the shorter, more succinct `for` loop (see Listing~\ref{code:for_print_chars}).

\begin{codelisting}
\label{code:for_print_chars}
\codecaption{}
```python, options: "linenos": true
s = "protagonist"
for index in range(0, len(s)):
    print(s[index])
```
\end{codelisting}

`for` loops can also countdown or count in multiples just as easy as `while`
loops can.  Suppose we want to print a string in reverse order like we did in
Listing~\ref{code:reverse_print_str}.  As a reminder, the code looked like this:

```python, options: "linenos": true
s = "abc"
index = len(s) - 1
while index >= 0:
    print(s[index])
    index = index - 1
```

Instead, we can add a third argument to `range` which specifies what we add to
the loop variable to change it prior to each iteration of the loop.  Thus, we
can do this (Listing~\ref{code:for_reverse_print_str}).

\begin{codelisting}
\label{code:for_reverse_print_str}
\codecaption{}
```python, options: "linenos": true
s = "cba"
for index in range(len(s)-1, -1, -1):
    print(s[index])
```
\end{codelisting}

That's a lot to mentally unpack.  Let's take it a piece at a time.  Let's take
the first emphasized expression in `range` below.

> \kode{for index in range(}\textbf{\emph{len(s)-1}}\kode{, -1, -1)}

This sets the last index in the string `len(s)-1` as the initial value of the
variable `index`.  The next expression/value we wish to emphasize in `range` is:

> \kode{for index in range(len(s)-1,}\textbf{\emph{-1}}\kode{, -1)}

This says that when `index` goes past `0` and reaches `-1`, we should exit the
loop.  Finally, we have:

> \kode{for index in range(len(s)-1, -1,}\textbf{\emph{-1}}\kode{)}

This `-1` specifies how `index` should be changed prior to each iteration.  This
means that `index` will have `1` subtracted from its value.

Let's see how we are doing here.  Suppose I have the code in
Listing~\ref{code:print_odds}.

\begin{codelisting}
\label{code:print_odds}
\codecaption{}
```python, options: "linenos": true
for i in range(1, 9, 2):
    print(i)
```
\end{codelisting}

What is the output of this code?

We would expect to see the following on-screen.

```console
1
3
5
7
```

Can you explain why?

The variable `i` gets the value `1` to start the loop.  In each iteration, the
value of `i` is printed.  Just before each iteration, we add `2` to `i`.
Therefore, `i` will have the values `1`, `3`, `5`, and `7` within the loop body.
When `i` reaches `9`, the `for` loop will end.

Let us try to use our knowledge of `for` loops to write a program that reverses
a string.  In other words, given user input, reverse the input and print it to
the user.  If the user enters `"abc def"`, then the program should output `"fed
cba"`.

Here is our attempt (Listing~\ref{code:for_rev_str} ).

\begin{codelisting}
\label{code:for_rev_str}
\codecaption{}
```python, options: "linenos": true
s = input("Enter a string: ")
rev = ""
for i in range(len(s)-1, -1, -1):
    rev = rev + s[i]
print("The reverse of the string is: %s." % rev)
```
\end{codelisting}

`s` is the input string variable and `rev` will be the string variable that
holds `s`'s reverse.  We take each character from `s` using a `for` loop and we
concatenate it onto the end of `rev`.

Consider how `rev` changes with each iteration of the loop, as shown in
Table~\ref{tbl:for_rev_str_trace}.

\begin{table}
\caption{Trace table for Listing~\ref{code:for_rev_str}\label{tbl:for_rev_str_trace}}
\begin{tabular}{|l|l|l|}
\hline
\kode{rev} & \kode{i} & \kode{s[i]} \\
\hline
\kode{"f"} & \kode{6} & \kode{"f"} \\
\kode{"fe"} & \kode{5} & \kode{"e"} \\
\kode{"fed"} & \kode{4} & \kode{"d"} \\
\kode{"fed "} & \kode{3} & \kode{" "} \\
\kode{"fed c"} & \kode{2} & \kode{"c"} \\
\kode{"fed cb"} & \kode{1} & \kode{"b"} \\
\kode{"fed cba"} & \kode{0} & \kode{"a"} \\
\hline
\end{tabular}
\end{table}

Table~\ref{tbl:for_rev_str_trace} is known a *trace table*.  It serves as a tool
for programmers to make sense of how values change from iteration to iteration
of a loop.

## `for` loops with strings, revisited
\label{sec:for_str}

We've barely scratched the surface of what `for` loops can do for us.  `for`
loops in Python have a nifty additional form that allows us to write even
simpler, more readable code.  We'll explore this alternate form now.  Let's set it up in the context of an example.  Suppose we wish to iterate through the characters of a string `s` with the intent of reversing it.  We might write the code found in Listing~\ref{code:for_rev_str2}.

\begin{codelisting}
\label{code:for_rev_str2}
\codecaption{}
```python, options: "linenos": true
s = input("Enter a string: ")
rev = ""
for index in range(0, len(s)):
    rev = s[index] + rev
print("The reverse of the string is: %s." % rev)
```
\end{codelisting}

Notice how we've changed the logic from what we did in
Listing~\ref{code:for_rev_str}, our previous attempt.  In the previous code, we
traversed the string starting at its last character and working towards its
first character, and for each character, we appended it to the end of the
reversed string `rev`.  In this code (Listing~\ref{code:for_rev_str2}), we are
doing the opposite.  We are traversing the string from first character (the
"front" of the string) to last character (the "back" of the string) and
prepending the character to the front of the reversed string `rev`.  Both
methods solve the same problem and produce the same output.

As it turns out, we don't even need to concern ourselves with having an `index`
variable.  Python has a version of the `for` loop syntax that operates
exclusively on strings.  Consider the following highlighted adjustments to
Listing~\ref{code:for_rev_str2} shown in Listing~\ref{code:for_in_rev_str}.

\begin{codelisting}
\label{code:for_in_rev_str}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [3,4]
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("The reverse of the string is: %s." % rev)
```
\end{codelisting}

In this form of the Python `for` loop, the loop variable `ch` is assigned a
different character from the string `s` each time the loop condition is checked.
Notice that there is no more `index` variable or `range` function.

## Loops for input validation and translation
\label{sec:loop_valid_and_translate}

We have been asking users for input in many of our previous examples.  We have
always assumed users will type the correct information, but what happens when
they do not.  Suppose we ask users to enter their age.  We have been doing this
as follows.

```python
age = int(input("Enter your age: "))
```

What if users' fingers slip and they enter `"1r"` instead of `"14"`?  The `int`
function will crash because `"1r"` cannot be cast to an integer.  This happens
because we have prematurely tried to cast the string to an integer without
checking the input first.  We need to wait to perform the `int` cast until we
know it is safe to do so.  Another way to say this is we need to postpone the
type conversion until we have *validated* the input.  The code in
Listing~\ref{code:isdigit} demonstrates how we might do input validation before
casting a string to an integer.

\begin{codelisting}
\label{code:isdigit}
\codecaption{}
```python, options: "linenos": true
age_str = input("Enter your age: ")
while not age_str.isdigit():
    print("That is not a valid age.")
    age_str = input("Enter your age: ")
age = int(age_str)
```
\end{codelisting}

`isdigit` (line 2 of Listing~\ref{code:isdigit}) is a function that we can
always use on a string value.  The "dot" (`.`) separates the word `isdigit` from
the string it refers to, in this case the value stored in the variable
`age_str`.  `age_str.isdigit()` returns `True` if every one of the characters in
`age_str` are numbers, otherwise it returns `False`.

(Note: What do you suppose would be the value of the expression `"".isdigit()`?
In other words, is the result of `isdigit` `True` or `False` when the string
contains no characters at all.  You may wish to try typing this statement into
the Python Shell for yourself to see what happens.)

Let us examine another example that uses loops to operate on strings.  Suppose we ask users for their full names using an `input` statement.

```python
fullname = input("Enter your full name: ")
```

The variable `fullname` could contain `"Javier Sanchez"`, `"Mary Johnson"`, or
just about anything, though in most cases, there will be a first name and a last
name separated by a space.  Let us try to extract the first name from the value
in `fullname`.  To do this, we'll need to use the slicing operator (`:`).
Depending on the length of the first name, the range of the string slice will be
a little different.

```python
# Suppose fullname == "Javier Sanchez"
#                      01234567...
firstname = fullname[0:6]

# Or, suppose fullname == "Mary Johnson"
#                          01234567...
firstname = fullname[0:4]
```

Since we can't possibly know the length of the first name ahead of time, we will
need to find the index of the space in order to slice the appropriate substring.
If we are able to put the index of the space into a variable named `space`, then
we can extract the first name as follows.

```python
firstname = fullname[0:space]
```

If `fullname` is `"Javier Sanchez"` then `space` would be `6`, if `fullname` is
`"Mary Johnson"` then `space` would be `4`, and so on.  Finding the index of the
space requires us to search the string character by character, which is
something we have already done, both with `while` loops and with `for` loops.

Here is our strategy.  We will use a loop to examine each character in
`fullname`, one at a time.  If we encounter the space, we will set the value of
`space` to the current index of the loop, and then we will jump out of the loop
using the command `break`.  After all, once we've found the space, our work is
done; there is no need to keep looping.

Thus, our code appears in Listing~\ref{code:find_space}.

\begin{codelisting}
\label{code:find_space}
\codecaption{Finding the index of a space in a string}
```python, options: "linenos": true
fullname = input("Enter your full name: ")
for index in range(0, len(fullname)):
    if fullname[index] == ' ':
        space = index
        break

firstname = fullname[0:space]
print("Your first name is %s." % firstname)
```
\end{codelisting}

Try out this code on several full names that you can think of.  Try to find
*edge cases* that may not work.  *Edge cases* are exceptional cases of program
input that could cause your code to fail.  One such edge case in this problem is
full names that do not have spaces, i.e., the names of individuals who only have
one name.  Consider celebrities' names such as Prince, Cher, Sting, Madonna,
etc.  Those names are their full names and first names simultaneously.  Try
typing "Prince" in as the input to your program.

```console
Enter your full name: Prince
Traceback (most recent call last):
  File "/Users/shep/cs1/code/ch3fullname.py", line 6, in <module>
    firstname = fullname[0:space]
NameError: name 'space' is not defined
```

Can you explain this error to yourself?  Why is `space` not defined in line `6`?
Where in the code do we create the `space` variable normally?

In this case, `space` is first created inside the loop.  This is generally bad
programming practice.  If the variable is used by code outside of a loop, the
variable should also be defined outside the loop.  So, let's define `space`
before we reach the loop, but what should be its initial value?  Let's choose a
value that doesn't look like a normal index.  Normal indices would be `0`, `1`,
`2`, `3`, etc., so let's choose `-1` as the initial value of `space`.  Our code
can now be written as in Listing~\ref{code:find_space2}.

\begin{codelisting}
\label{code:find_space2}
\codecaption{Finding the index of a space in a string, attempt 2}
```python, options: "linenos": true
fullname = input("Enter your full name: ")

space = -1
for index in range(0, len(fullname)):
    if fullname[index] == ' ':
        space = index
        break

if space == -1:
    firstname = fullname
else:
    firstname = fullname[0:space]

print("Your first name is %s." % firstname)
```
\end{codelisting}

Finding a character or a pattern in a string is such a common operation, Python
gives us a way to do it without writing a loop every time.  We can simplify the
code above using the `find` function as follows in Listing~\ref{code:find_space3}.

\begin{codelisting}
\label{code:find_space3}
\codecaption{Finding the index of a space in a string, attempt 3}
```python, options: "linenos": true
fullname = input("Enter your full name: ")

space = fullname.find(" ")

if space == -1:
    firstname = fullname
else:
    firstname = fullname[0:space]

print("Your first name is %s." % firstname)
```
\end{codelisting}

`find` (line 3 of Listing~\ref{code:find_space3}) is a function that we can
always use on a string value.  The "dot" (`.`) separates the word `find` from
the string it refers to, in this case the value stored in the variable
`fullname`.  The argument is the single character or multiple character pattern
to search for.  `find` returns the index where that pattern starts in the value
of `fullname`.

Here are some examples of using `find`.

```python
print("abcde".find("b"))     # prints 1
print("abcde".find("cd"))    # prints 2
print("abcde".find("cash"))  # prints -1, which indicates the
                             # pattern was not found
print("abcde".find("abcde")) # prints 0
```

Now that we know how to find a pattern (and specifically, a space) in a string,
consider what that allows us to do.  Suppose we have a sentence that we wish to
break into individual words.  How are words separated in the English language?
If you said "using spaces" then you are correct (for the most part).

Let's try to do something like this through an example.  If you spend time on
the Web, you might have learned that Internet citizens have tabbed September
19th as "International Talk Like a Pirate Day."  Imagined pirate-speak draws
from many sources in popular culture.  Fictional pirates might say "Ahoy!"
instead of "Hello!" or they might use the word "matey" to describe a friend.  If
we wanted to translate a single English word into its Pirate equivalent, we
might do something like Listing~\ref{code:pirate_one_word}.

\begin{codelisting}
\label{code:pirate_one_word}
\codecaption{}
```python, options: "linenos": true
english_word = input("Enter a word: ")
if english_word == "hello":
    pirate_word = "ahoy"
elif english_word == "friend":
    pirate_word = "matey"
else:
    # The word has no known pirate translation.
    # Leave it in English.
    pirate_word = english_word
print("%s in pirate is %s." % (english_word, pirate_word))
```
\end{codelisting}

What if we wanted to change an entire English sentence into Pirate instead of
just translating a single word?  How would we accomplish that?

Let's keep this as simple as possible, so for now let's ignore "edge cases" like
uppercase letters and punctuation.  Let's only worry about translating
all-lowercase words separated by spaces.

You might not have any idea how to accomplish this in code, but there are a
number of ways to get started.  One way is to realize that every computer
program tends to take input and transform it into output.  If we envision a
program as taking variables and changing their values in order to reach a goal,
we can write down how we want those variables to change, and then write down the
code to perform the changes.

Let's think about what variables we would want to have to make an
English-to-Pirate translator program work.  Suppose we have two variables, one
named `sentence` and the other named `word`.  `sentence` contains the English
sentence the user types, and `word` will store each word as we extract it from
`sentence`. Each time we extract an English word into `word`, the string in
`sentence` should shrink.

Again, if we are thinking about a program as something that makes changes to
input variables, we can envision a program looping to change `sentence` and
`word` repeatedly.  Here is an example.

```python
word: ""        sentence: "hi there my friend"
word: "hi"      sentence: "there my friend"
word: "there"   sentence: "my friend"
word: "my"      sentence: "friend"
word: "friend"  sentence: ""
```

Think of this process in a loop.  Each time through the loop, we find the index
of the space in `sentence` and put that index into a variable named `space`.  We
use the slicing operator to get the first word in the sentence from `0` to
`space`.  Then, we use the slicing operator again to "shrink" `sentence` so that
`sentence` only contains the remaining words.

This would allow us to translate each word, one at a time.  Let's write some
code.  Our first attempt is found in Listing~\ref{code:pirate_sent1}.

\begin{codelisting}
\label{code:pirate_sent1}
\codecaption{}
```python, options: "linenos": true
sentence = input("Enter an English sentence: ")
word = ""
print("word: \"%s\", sentence: \"%s\"" % (word, sentence))

space = sentence.find(" ")
while space != -1:
    word = sentence[0:space]
    sentence = sentence[space+1:]
    print("word: \"%s\", sentence: \"%s\"" % (word, sentence))
    space = sentence.find(" ")
```
\end{codelisting}

Let's try it out.

```python
Enter an English sentence: hello there my friend
word: "" sentence: "hello there my friend"
word: "hello" sentence: "there my friend"
word: "there" sentence: "my friend"
word: "my" sentence: "friend"
```

This is pretty good, but what about the final word in this example: "friend".  Since there is no space trailing the last word in the sentence, we will need to add some code after the loop to take care of the last word.  Consider Listing~\ref{code:pirate_sent2}.

\begin{codelisting}
\label{code:pirate_sent2}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [12,13,14,15]
sentence = input("Enter an English sentence: ")
word = ""
print("word: \"%s\", sentence: \"%s\"" % (word, sentence))

space = sentence.find(" ")
while space != -1:
    word = sentence[0:space]
    sentence = sentence[space+1:]
    print("word: \"%s\", sentence: \"%s\"" % (word, sentence))
    space = sentence.find(" ")

if sentence != "":
    word = sentence
    sentence = ""
    print("word: \"%s\", sentence: \"%s\"" % (word, sentence))
```
\end{codelisting}

The highlighted block of code in Listing~\ref{code:pirate_sent2} checks to see
if there's still text residing in `sentence`.

Now all that's left is to do the translating.  We will take each `word` and
append its translation to a new string which we'll call `pirate`.  We can get
rid of our `print` statements, too, since they were only there to aid our
understanding of what the code does.  Listing~\ref{code:pirate_sent3} is our
final code.

\begin{codelisting}
\label{code:pirate_sent3}
\codecaption{Final English-to-Pirate Translator}
```python, options: "linenos": true
sentence = input("Enter an English sentence: ")
word = ""
pirate = ""

space = sentence.find(" ")
while space != -1:
    word = sentence[0:space]
    sentence = sentence[space+1:]
    if word == "hello":
        pirate = pirate + "ahoy" + " "
    elif word == "friend":
        pirate = pirate + "matey" + " "
    else:
        pirate = pirate + word + " "
    space = sentence.find(" ")

if sentence != "":
    word = sentence
    sentence = ""
    if word == "hello":
        pirate = pirate + "ahoy" + " "
    elif word == "friend":
        pirate = pirate + "matey" + " "
    else:
        pirate = pirate + word + " "

print("Your sentence translated to pirate is:")
print(pirate)
```
\end{codelisting}

An example of a running program is:

```console
Enter an English sentence: hello there my friend
Your sentence translated to pirate is:
ahoy there my matey
```

We can add more translations by adding more `elif` conditions to the `if`-blocks
of statements, though we must add them both to the `while` loop code and the
`if`-block that follows the `while` loop.  Having to add this logic in two
different places makes the code more difficult to maintain, since we might add
an `elif` to the earlier part of the code but then forget to add it to the later
part of the code.  In Chapter~\ref{ch:funcs}, we will examine functions, which
will improve the maintainability of this code dramatically.

## Nested loops
\label{sec:nested_loops}

Some interesting and practical things happen when we use a loop as the body of
another loop.  Consider Listing~\ref{code:outer_inner}, and try to guess as to
its output.

\begin{codelisting}
\label{code:outer_inner}
\codecaption{}
```python, options: "linenos": true
for outer in range(0, 3):
    for inner in range(0, 3):
        print("outer = %d, inner = %d" % (outer, inner))
```
\end{codelisting}

Let's follow the code step-by-step as we would with any code.  The first
statement we encounter is `for outer in range(0, 3)`.  Since this is first time
we've encountered this statement, this code sets `outer` to `0` and we enter its
loop body.  The first statement of the loop body is, of course, another loop.
This loop statement is `for inner in range(0, 3)`.  So, this sets `inner` to `0`
and we enter its loop body.  This means that at this point in the code, we are
actually inside two loops: an inner one, which is inside an outer one.  The
first (and only) statement in the inner loop prints the values of `outer` and
`inner` so that we can see how the values change throughout the program.

We call a loop-inside-a-loop construct a set of *nested loops*.  That is, the
inner loop is nested inside the outer loop.

Before we continue discussing how these loops work, run the code to see the output.

```console
outer = 0, inner = 0
outer = 0, inner = 1
outer = 0, inner = 2
outer = 1, inner = 0
outer = 1, inner = 1
outer = 1, inner = 2
outer = 2, inner = 0
outer = 2, inner = 1
outer = 2, inner = 2
```

We can get a pretty good idea of how this works from looking at the output.
Once we enter the outer loop, we encounter the inner loop right away.  Python
will stay in the inner loop until it is completed, and then it will exit to the
outer loop.  The outer loop will increment `outer` by one, and since `outer` is
still within its range, it will enter the outer loop body, which, once again,
will reach the inner loop.  Since we left the inner loop once already, reaching
the inner loop this time is like reaching it for the first time.  The statement
`for inner in range(0, 3)` sets `inner` to `0` once again, and the process
repeats itself.

We often use nested loops to write programs in Python.  For one example, suppose
we wish to write a program that repeatedly asks for students' names and exam
scores.  The output should be students' names followed by their exam average.
Listing~\ref{code:student_avgs} shows how to do this using nested loops.

\begin{codelisting}
\label{code:student_avgs}
\codecaption{}
```python, options: "linenos": true
student = input("Student name? ('quit' to end) ")
while student != "quit":
    sum = 0.0
    count = 1
    score = input("Score %d? ('quit' to end)  " % count)
    while score != "quit":
        score = float(score)
        sum += score
        count += 1
        score = input("Score %d? ('quit' to end)  " % count)

    # count is one more than it should be since we
    # increment count before we quit.
    count -= 1  

    if count > 0:
        average = sum / count
        print("%s's average is %.2f" % (student, average))
    else:
        print("No grades entered for %s." % student)

    student = input("Student name? ('quit' to end) ")
```
\end{codelisting}

One thing to note about this code, besides the nested `while` loops, is the
shorthand assignment statements.  Instead of typing

```python
count = count + 1
```

we can type

```python
count += 1
```

This type of shorthand assignment construct works for most operators in Python.

Beyond that observation, we note that the outer `while` loop is responsible for
getting each student's name.  The inner `while` loop retrieves each score and
adds it to a sum.  Once we exit the inner loop, we can calculate the average
using the sum.  We must be careful to make sure that there are any scores at
all.  If `count` were `0` and we divided by `0` without checking, our program
would crash.

The output of this code might look something like the following depending on
what the user types.

```console
Student name? ('quit' to end) David Chan
Score 1? ('quit' to end)  95.5
Score 2? ('quit' to end)  80.5
Score 3? ('quit' to end)  87.0
Score 4? ('quit' to end)  quit
David Chan's average is 87.67
Student name? ('quit' to end) Sarah McDowell
Score 1? ('quit' to end)  quit
No grades entered for Sarah McDowell.
Student name? ('quit' to end) quit
```

## Exercises
\label{sec:loops_exercises}

1. Write a program that asks for a word, phrase, or sentence.  The program should then print whether the input is a palindrome.  (Do a Web search to see what a palindrome is.)

2. Write a program that repeatedly asks for a number until the user enters "quit."  The program should print the sum and average of all the numbers.

3. What is the output of the following program?

    <<(exercises/ch3/p3.3.py)

4. What is the output of the following program?

    <<(exercises/ch3/p3.4.py)


5. What is the output of the following program?

    <<(exercises/ch3/p3.5.py)

6. Write an English-to-Pirate translator like the one found in
Section~\ref{sec:loop_valid_and_translate}, only have your program repeatedly
ask for sentences until the user presses ENTER/RETURN without typing anything.
You can still ignore capitalization and punctuation.

7. Do the previous problem again, only this time properly handle capitalization
and punctuation.

8. Write a program that translates English sentences to Pig Latin.
    To form the Pig Latin equivalent of a word, remove the first consonant sound of the word and append it to the end preceded by a dash and followed by "ay".  Thus, "cat" becomes "at-cay" and "ship" becomes "ip-shay."   The latter example demonstrates that consonant sounds can be blended consonants.

    If an English word begins with a vowel, the word is simply restated with "-way" appended to it.  In other words, "apple" becomes "apple-way."  Your solution should handle capitalization and punctuation.

    Example of a working program:

    <<(exercises/ch3/p3.8.txt, lang: ruby)

9. Write a program that asks for a number and then prints that number of rows of 5 asterisks.  For example, if the user enters 4, the program would print the following.

    ```
    ***** \\
    ***** \\
    ***** \\
    *****
    ```

10. Write a program that asks for two numbers x and y.  The program should print a rectangle of asterisks consisting of x rows and y columns.  For example, if the user enters 3 and 8, respectively, the program would print the following.

    ```
    ******** \\
    ******** \\
    ********
    ```

11. Write a program that asks for a number and then prints a triangle of asterisks where the base has that number of asterisks.  For example, if the user enters 4, the program would print the following.

    ```
    * \\
    ** \\
    *** \\
    ****
    ```

12. Write a program that asks for a number and then prints an inverted triangle of asterisks where first row contains that number of asterisks.  For example, if the user enters 4, the program would print the following.

    ```
    **** \\
    *** \\
    ** \\
    *
    ```

13.	Python programs are capable of generating random numbers (well, "pseudo"-random numbers – more about that in the next chapter).  One example of how to do this is as follows.

    <<(exercises/ch3/p3.13.py)

    If you run this program over and over again you'll see the number change.  We can use random integers to simulate real-life occurrences, including games of chance and movement of animals.

    Consider one program that demonstrates the use of random numbers.  A drunkard stumbling around in a grid of streets picks one of four directions (north, south, east, or west) at each intersection, and then he moves to the next intersection.

    Write a program that simulates the drunkard's walk.  Represent each intersection location as (x,y) integer pairs and have the drunkard start at (0,0).  Have the drunkard walk 100 intersections and print the intersection location where he ends up.  Run this program many times.  Does the drunkard tend to stay close to (0,0) or does he end up moving far away?
