# Loops and String Manipulation
\label{cha:loops}

## `while` loops
\label{sec:while}

Most of the examples of code we've seen so far have been fairly short -- a few
lines here and there.  Now we're going to start looking at programs that are a
bit longer.  Don't be too daunted by this.  If you practice, you'll gain comfort
with knowing how to break down programs section by section.  Let's go ahead and
practice doing this starting with this chapter.

Sometimes we’ll want to repeat an action in code.  One example might be that we
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
    print("The total for that item will be %.2f." % amount)
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
way, however, once we reach the end of the indented block, the code “loops” back
up to the condition again.  If the condition is again `True`, we reenter the
indented block of code.  Thus, we can make code repeat itself as long as a
condition is met.  A programming language “construct” that allows code to be
repeated is known as a *loop*.

We call `amount != "quit"` in Listing~\ref{code:sales_tax} the *loop condition*.
We call the indented block of statements that follows the loop condition the
*loop body*. We say that the statements in the indented block are *inside* the
loop body. The final `print` statement in line 10 of
Listing~\ref{code:sales_tax} is not indented and is therefore *outside* the loop
body.

Try out the code above if you haven’t already.  Does it behave the way you
expect?

Now, notice that we ask for input twice in this program: once just before we try
to enter the loop (line 4), and once at the end of the indented block inside the
loop body (line 9).  Why?  The value returned by the initial `input` statement
gets us into the loop body, though it doesn’t have to.  It is possible that the
user types “quit” right away, in which case the program bypasses the loop and
prints our “thank you” message.  At the end of the loop body, we need to ask the
user for the next input value, so that we have a new amount.  Otherwise, the
program would just continue to calculate the same total value over and over
again and the program would never have the chance to end.

To see this for yourself, delete the last line of the loop body in
Listing~\ref{code:sales_tax}, i.e., delete line 9. Instead of deleting it, you
could just comment it out by putting a `#` symbol at the start of that line.
Run your code and type an initial amount, say, `4.00`. Your code will endlessly
compute sales tax with no end in sight!  Press the “Control” and “C” keys
simultaneously to abort your program (we will write this `Ctrl+C` in the future
because that’s how programmers write such things).

With this in mind, we will often see loops written using the pattern in
Figure~\ref{fig:while_tmpl}.

![A common \kode{while} loop
pattern\label{fig:while_tmpl}](images/ch3/while_tmpl.png)

We call each new time through the body of the loop an *iteration*.  We may refer
to the first iteration, second iteration, next iteration, final iteration, etc.,
when discussing the behavior of a loop.

To get a sense of the mechanics of how `while` loops work, beginning programmers
often consider “toy” examples that showcase a number of “gotchas” when it comes
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

We don’t always need to have a non-indented statement following a loop.  We are
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

Let’s look at another “toy” example.  We will modify
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

Let’s try another example (Listing~\ref{code:while_ex4}).

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

All we’ve done is changed the initial value of `x` and the value of `x` that
causes us to not reenter the loop.  The output is:

```console
0
1
2
3
4
Done.
```

Let’s make a small change to Listing~\ref{code:while_ex4}. Suppose we change
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
entirely.  There is no “rule” that says we have to do the loop body at least
once.  Computers are stupid.  They only do what you tell them to.  In this case,
because the condition is `False` initially, we never do the loop body and go
straight to the non-indented line of code past the loop body.

All of our “toy” examples thus far have involved incrementing a loop variable
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

Toy examples are a great way to understand how loops work from a “mechanical”
perspective, but let’s see how we can use them to solve real problems.  Recall
our very first example in this section, Listing~\ref{code:sales_tax}, which
dealt  with reporting the price of an item after sales tax.  Our next example is
also related to money.  Suppose we open a savings account, one that pays 5%
interest per year into the account as long as we don’t withdraw any money that
we deposit.  Let’s say we start the account by depositing $10,000.00.  How many
years will it take to double our investment?

Mathematicians would attempt to derive an equation to solve this problem, but
with computers we don't have to.  We can make the computer figure it out for us.
We just need to know how to write the code to tell the computer what to do.

The question “How many years will it take to double our investment?” tells us a
lot about the code we would need to write.  We would need to keep track of our
balance as it grows by 5% each year.  We would need to keep track of the number
of years that have elapsed so far in our code.  We would also need to check to
see if the balance has doubled.  If, in describing what our program is supposed
to do, we say we need to check something, we are often talking about a Boolean
condition found in an `if` statement or a `while` loop.

Try to program this example on your own first.  You can’t learn to be a good
programmer if you don’t try things regularly by starting with a blank screen or
a blank sheet of paper.  If you get really stuck, then (and only then) glance at
the answer below.

Okay, let’s look at a solution found in Listing~\ref{code:investment1}
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
Consider the loop condition `balance < 2*balance`.  A variable’s value will never
be greater than twice itself (unless that value is negative, but let’s steer
clear of negative values in bank accounts!).

The problem here is that we’re trying to use the variable `balance` for two very
different purposes simultaneously.  On one hand, we are using `balance` to keep
track of the current balance as it changes year after year.  On the other hand,
we’re pretending that it still holds the starting balance from our initial
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
\label{sec:string_manip}

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
individual characters by using square brackets and character’s position in the
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
Let’s re-list the code again in Listing~\ref{code:str_index}, this time with
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
that the we mean “go to the ends of the string.”  When we use square brackets to
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

This is Python’s way of saying “yes, `upper` is the name of a function.  If you
want to actually use that function, put parentheses at the end.”  Let’s add the
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

Observe that when we “shout” by using `upper()`, the punctuation displayed is a
period.  Shouldn’t we change that to an exclamation point (`!`)?  Consider the
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

Note that the original string value of `t` still hasn’t changed.  `t` is still
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

This is yet another “toy” example intended to get us to see the relationship
between loops and strings, which is a powerful relationship we will exploit very
shortly.

Let’s make one change to Listing~\ref{code:print_chars}.  We will change only
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

Let’s see how well this is all sinking in.  Can you write code to print the
characters of a string, one on each line, but in reverse order this time?  In
other words, if my string is `"abc"`, can you write code that prints:

```console
c
b
a
```

Give it a try.

Let’s check your work.  With some experimentation, you might have been able to
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
