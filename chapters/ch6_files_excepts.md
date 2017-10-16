# Files and Exceptions
\label{ch:files}

## Opening and Reading files
\label{sec:read_files}

Of the time people spend using computers, a very large proportion of the time is
spent on managing files.  People take photos, organize them, and sometimes edit
them on their laptops.  People open Word documents, edit them, and save their
changes.  People may make copies of files or move files from one folder to
another.  In some cases, people manage files directly.  In other situations,
people may be blissfully unaware that programs are managing files on their
behalf.  Suppose you are playing a video game.  When you, the user, save your
game, the game program most likely stores the level you were on in a file.  The
game would then open and read information from this file when you start the game
again so that you can start where you left off.  In this chapter, we will learn
how to create files, read from files, and write to files using Python.

As we often do in this book, we will begin with an example.  In Thonny, create a
new code file named `show-menu.py`.  Do not type anything into it just yet, but
leave the new code file open.  Now create a second file and name it `menu.txt`.
Take note that this file ends in `.txt` rather than `.py`.  Be sure to save the
file `menu.txt` in the same folder as you save the file `show-menu.py`.  This
`menu.txt` file will not contain Python code.  Instead, it should contain the
following lines.  Go ahead and type them into the file and save it.

```console
roast duck
ribeye steak
wood-fired pizza
plank-seared salmon
caesar salad
```

Now, return to the window for `show-menu.py`.  Still, do not type anything into
it, but go ahead and run the empty code file.  This should shift the focus back
to the Python Shell window.  In the Python Shell window type the following.

```python
open("menu.txt", "r")
```

What appears when you type this?  Now, type this:

```python
f = open("menu.txt", "r")
type(f)
```

Even though the type of `f` is reported as having the type `_io.TextIOWrapper`,
in general we will refer to `f` as a `file` type variable.  When we use the
`open` function, we pass it the name of the file we wish to open, and we also
tell it what we intend to do with the file.  In this case, the `"r"` indicates
that we wish to "read" from the file.

Now try this in the Python Shell window:

```python
f.readlines()
```

Interesting.  This function returns a list that looks like `['roast
duck\textbackslash n', 'ribeye steak\textbackslash n', 'wood-fired
pizza\textbackslash n', 'plank-seared salmon\textbackslash n', 'caesar
salad\textbackslash n']`.  Each item in the list is a single line in the file.
The `"\textbackslash n"` is the newline character.  A newline can be found at
the end of every line.

Try reading the lines again by typing:

```python
f.readlines()
```

Oh no!  Where did the lines go?  Has our file been deleted?  Is the file still
there but its contents have been deleted?

The good news is the file is still there and none of the lines have been harmed
in the process.  For evidence, try the following.

```python
f.seek(0)
f.readlines()
```

Hey, they're back!  What do you think `f.seek(0)` does?  (We'll explain exactly
what it does in a bit.)

Okay, now let's try these lines in the Python Shell window.

```python
f.seek(0)
f.readline()
f.readline()
f.seek(0)
f.readline()
f.readline()
```

The singular `f.readline()` works differently than the plural `f.readlines()`.
`readline` simply returns a single line as a string.  `readlines` returns all of
the lines as a `list` of strings.

We can also do this:

```python
f.seek(0)
f.read()
```

The function call `f.read()` returns the entire file as a single string.

Finally, we can do this.

```python
f.close()
```

This closes the file we opened earlier.  If we try to `seek` or `readline`, the
program will encounter an error.  We can check to see whether a file is closed
by typing:

```python
f.closed    # type is bool
```

Let's make sense of how this all works.  When we open a new file, imagine that
we are setting up a “pipe” in front of our file.  Through the pipe, we can pull
lines out of a file and into our Python program, line by line.  At any point,
the end of the pipe is pointing at the next line to be retrieved.

Suppose we type the following into the Python Shell window.

```python
line = ""
f = open("menu.txt", "r")
line = f.readline()
print(line)
line = f.readline()
print(line)
```

With each call to `readline()`, the next line will be read through the file's
pipe, and then the pipe will be moved to the location in the file to be read
next.  To help visualize this process, the first and second `readline` calls are
shown in Figure~\ref{fig:read1} and Figure~\ref{fig:read2}, respectively.  Note
how after the first `readline`, the pipe is moved down in
Figure~\ref{fig:read2}, ready to read the next line.

![The effect of the first \kode{f.readline()}\label{fig:read1}](images/ch6/read1.png)

![The effect of the second \kode{f.readline()}\label{fig:read2}](images/ch6/read2.png)

When we write `f.seek(0)`, we are telling the file to reset the pipe to the
beginning of the file.

Now, we're finally ready to write some code in `show-menu.py` (see
Listing~\ref{code:find_duck1}).

\begin{codelisting}
\label{code:find_duck1}
\codecaption{}
```python, options: "linenos": true
f = open("menu.txt", "r")
lines = f.readlines()
for food in lines:
    print("They have %s." % food)
    if food == "roast duck":
        print("Ooo, they have duck!  Yummy!")
f.close()
```
\end{codelisting}

The code in Listing~\ref{code:find_duck1} opens the file and retrieves all of
the lines as a list of strings. Then, we use a `for` loop to print each one of
the lines; in the loop we call each line `food`.  If the food happens to be
`"roast duck"` we print an especially excited message.  At the end of the code,
we close the file.  It is always good practice to remember to close any files
you open.

Save your code file and run it.  Does the output look like what you would expect
(I would guess the answer is "no")?  Let's look at the output.

```console
They have roast duck
.
They have ribeye steak
.
They have wood-fired pizza
.
They have plank-seared salmon
.
They have caesar salad
.
```

First of all, we don't see our excited message at all.  Second, the period at
the end of each `print` statement is on the next line.

Look again at the list value returned by `f.readlines()`, which is `['roast
duck\textbackslash n', 'ribeye steak\textbackslash n', 'wood-fired pizza\textbackslash n', 'plank-seared salmon\textbackslash n',
'caesar salad\textbackslash n']`.  Every string value within the list includes a `"\textbackslash n"` at the
end.  The `"\textbackslash n"` is the newline that separates the text on each line.  Since
`print` normally inserts a newline after it prints its string, and since the
string has a newline, too, there are two newlines that get printed: one before
the period and one after the period.

This also causes our `if` statement to fail.  When we compare `"roast duck"` to
`"roast duck\textbackslash n"`, these are technically different strings because the second one
has a `"\textbackslash n"` character at the end.  That's why we never see our excited message.
The expression `"roast duck" == "roast duck\textbackslash n"` is `False`.

Let's fix this code; see Listing~\ref{code:find_duck}.

\begin{codelisting}
\label{code:find_duck}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [4]
f = open("menu.txt", "r")
lines = f.readlines()
for food in lines:
    food = food.rstrip()
    print("They have %s." % food)
    if food == "roast duck":
        print("Ooo, they have duck!  Yummy!")
f.close()
```
\end{codelisting}

The `rstrip` function removes any "whitespace" characters from the end of the
string.  Whitespace characters include spaces, tabs, and newlines.  Make sure
you remember to call the `rstrip` function using parentheses.  It's a common
mistake to forget.  It is perfectly "legal" in Python to do this:

```python
food = food.rstrip     # This is INCORRECT.
```

Instead of this

```python
food = food.rstrip()   # This is correct.
```

The second one is correct.  The first one is wrong but does not cause an error.
Variables can store *references* to functions, so the first statement would
change the variable food from a string to a function.  There are reasons why we
would want to put function references in variables (which you may have
encountered if you read "optional" Section~\ref{sec:func_prog}), but this is not
one of those instances.  So, be sure to call the function by using parentheses.  

Another way we could have accomplished this is to use the singular `readline`
instead of `readlines`.  Consider Listing~\ref{code:find_duck_singular}.

\begin{codelisting}
\label{code:find_duck_singular}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [2,8]
f = open("menu.txt", "r")
food = f.readline()
while food != "":
    food = food.rstrip()
    print("They have %s." % food)
    if food == "roast duck":
        print("Ooo, they have duck!  Yummy!")
    food = f.readline()
f.close()
```
\end{codelisting}

We retrieve the first food using `f.readline()`.  As long as the food is not an
empty string, we can display it using the code in the body of the `while` loop.
At the end of the `while` loop, we need to remember to retrieve the next line
from the file.  When we have reached the end of the file, `f.readline()` returns
an empty string (that is, `""`).

## Reading File Records
\label{sec:read_records}

In the previous section, we had a file that contained a list of food items.
What if we wanted to store more information about each food item beyond simply
its name?  Suppose we wanted to also track how many calories and carbohydrates
the food item contains?  One way we might do this is to store each piece of
information on a separate line in a new file (let's name it `new-menu.txt`),
like this.

```console
roast duck
1284
0
ribeye steak
847
0
wood-fired pizza
1680
200
```

The attributes of each item are now listed on three separate lines.  The first
line is the name of the food item.  The second line is the calorie count.  The
third line is the number of carbohydrates ("carbs") in grams.

Let's write code to show all of the items and their attributes, and at the end
of the program, let's announce which food has the lowest calorie count.  Let's
focus on the first part initially (see Listing~\ref{code:show_records}), and
then we'll come back and add to the code to print out the item with the lowest
calorie count.

\begin{codelisting}
\label{code:show_records}
\codecaption{Showing all records in a file}
```python, options: "linenos": true
infile = open("new-menu.txt", "r")
item = infile.readline()
while item != "":
    item = item.rstrip()
    calories = int(infile.readline().rstrip())
    carbs = int(infile.readline().rstrip())
    print("%s contains %d cal and %d carbs." \
              % (item, calories, carbs))
    item = infile.readline()
infile.close()
```
\end{codelisting}

In Listing~\ref{code:show_records}, we attempt to read lines in sets of three's
since each item now consists of three lines of attributes, the item name, the
calorie count, and the carbohydrate count.  If we ever get an empty string for
the first line in the next set of three lines, we know we have reached the end
of the file.

Now, let's add the code to track which food as the lowest calorie count.  For
now, if there is a tie, we will announce only the first food with the lowest
calorie count (see Listing~\ref{code:lowcal_record}).

\begin{codelisting}
\label{code:lowcal_record}
\codecaption{Finding lowest calorie count in a set of file records}
```python, options: "linenos": true, "hl_lines": [1,2,13,14,15,21,22]
lowcal = 100000   # a really big number!
lowitem = ""

infile = open("new-menu.txt", "r")
item = infile.readline()
while item != "":
    item = item.rstrip()
    calories = int(infile.readline().rstrip())
    carbs = int(infile.readline().rstrip())
    print("%s contains %d cal and %d carbs." \
              % (item, calories, carbs))

    if lowcal > calories:
        lowcal = calories
        lowitem = item

    item = infile.readline()

infile.close()

print("The food with the least calories is %s with %d cal." % \
      (lowitem, lowcal))
```
\end{codelisting}

In Listing~\ref{code:lowcal_record}, we make two variables before the loop
starts.  `lowitem` keeps track of the name of the lowest calorie item and
`lowcal` keeps track of how many calories it was.  Then, inside the loop, we
check each item to see if its calorie count is lower than what we've seen so far
in the file.  Once the loop is finished and we've examined all items, we print
our findings.

Storing related values on separate lines is not uncommon, though real-world data
is often stored differently.  It is very common to find data stored in files
using the comma-separated values (CSV) format.  Let's explore how to read CSV
files.  To do this, let's make yet another new file and name it `menu.csv` (note
the `.csv` file extension).  The contents of this file should appear as follows.

```console
#item,cal,carb
roast duck,1284,0
ribeye steak,847,0
wood-fired pizza,1680,200
```

Now, the information for each item is stored on a single line, and each
“attribute” is separated by commas.  It is fairly common to have the first line
in the file not contain actual data, but rather it contains a description of the
order of attributes in each subsequent line.  This first line is often called
the *header line* or *header row* of information.  In the code we will write, we
will need to remember to read that header line, but then simply ignore its
contents.

Our CSV-related code becomes Listing~\ref{code:lowcal_csv}.

\begin{codelisting}
\label{code:lowcal_csv}
\codecaption{Finding lowest calorie count in CSV file}
```python, options: "linenos": true, "hl_lines": [13,14,15,16]
lowcal = 100000   # a really big number!
lowitem = ""

infile = open("menu.csv", "r")

# Read the header and throw it away.
line = infile.readline()

# Get the actual first line.
line = infile.readline()

while line != "":
    attributes = line.rstrip().split(",")
    item = attributes[0]
    calories = int(attributes[1])
    carbs = int(attributes[2])
    print("%s contains %d cal and %d carbs." \
              % (item, calories, carbs))

    if lowcal > calories:
        lowcal = calories
        lowitem = item

    line = infile.readline()
infile.close()

print("The food with the least calories is %s with %d cal." % \
      (lowitem, lowcal))
```
\end{codelisting}

We use `.split(",")` to split the line into its three pieces: the item, the
calories, and the carbs.  Then, we proceed as we did previously.


## Writing Information to Files

So far in this chapter, we have written code to read information from existing
files.  Let's learn how to write code that writes to files.  That is, we may
want to create new files, or we may wish to update existing files.

We shall continue with another food-related example, and we'll hope that you're
not reading this book close to meal time, otherwise it may be hard to
concentrate!

Suppose we want to create a program that allows us to make a menu for a meal
that we would then save for later use.  Let's save this code into a file named
`write_menu.py`.  Let's ask for each menu item, one after another, until the
user enters a bare enter/return (i.e., an empty string). Then, we'll write each
menu item line to a file that we will name `menu.txt`.
Listing~\ref{code:write_menu} shows the code to accomplish this in all its
wonderous Python-y glory.

\begin{codelisting}
\label{code:write_menu}
\codecaption{Creating \kode{menu.txt}}
```python, options: "linenos": true
f = open("menu.txt", "w")
food = input("What do you want to eat? (Enter nothing to quit.) ")
while food != "":
    f.write(food + "\n")
    food = input("What do you want to eat? (Enter nothing to quit.) ")
f.close()
```
\end{codelisting}

Give this code a try.  After the program ends, a file named `menu.txt` should
"magically" appear in the same folder as your code file `write_menu.py`.  Go
ahead and open `menu.txt` and verify that all the items you typed when you first
ran the program do in fact appear in the file, each on a separate line.

Take note of line 1 in Listing~\ref{code:write_menu}.  See how we changed the
second parameter of the function call to `open`?  Instead of `"r"`, which means
"read", we typed `"w"`, which means "write."

Also, consider line 4 in Listing~\ref{code:write_menu}.  The file variable `f`
has a function named `write`.  Unlike `print`, which always inserts a newline
(`\textbackslash n`) at the end of output, `write` does not automatically add a
newline. Thus, we must manually insert the newline by passing the string
expression `food + "\textbackslash n"` to our call to `f.write`.  If we omitted
the `"\textbackslash n"`, all of the food items you entered would be squished
together on one unreadable line.

There is a downside to this program.  Whenever we run this code,
`open("menu.txt", "w")` obliterates any pre-existing `menu.txt` file.  Any menu
that we have previously created is destroyed.  That's maybe not such a good
thing.  It might be a good idea to show users the menu we already have, if there
is one, and then ask if they want to create a new menu.

Okay, here we go!  Check out Listing~\ref{code:check_and_write_menu}.

\begin{codelisting}
\label{code:check_and_write_menu}
\codecaption{Show and re-create \kode{menu.txt}}
```python, options: "linenos": true
infile = open("menu.txt", "r")
print("The current menu on file is:")
for menuitem in infile:
    print(menuitem.rstrip())
infile.close()
print()

create_new = input("Would you like to throw away this menu " +
                   "and create a new one? (y/n): ")

if create_new == "y":
    outfile = open("menu.txt", "w")
    food = input("What do you want to eat? (Enter nothing to quit.) ")
    while food != "":
        outfile.write(food + "\n")
        food = input("What do you want to eat? (Enter nothing to quit.) ")
    outfile.close()
```
\end{codelisting}

Run the code in Listing~\ref{code:check_and_write_menu}.  It should show you the
contents of `menu.txt` and then ask you if you want to create a new menu.  Enter
`n` and press enter/return.  Re-run the code.  Your menu items should still be
intact!  Now run the program again.  When it asks you if you want to create a
new menu, enter `y`.  You will be able to enter several new menu items.  When
you are finished entering items, you should be able to see those menu items
whenever you re-run the program.

Our code does suffer from at least one problem, however.  Line 1 of
Listing~\ref{code:check_and_write_menu} assumes there is a file named
`menu.txt`.  What if there isn't?  In other words, if we were to run this
program for the first time without creating a `menu.txt` ahead of time, what
will happen.  Well, let's try that.  Delete the file `menu.txt`.  Re-run the
program.  Kablooey!

```console
Traceback (most recent call last):
  File "t.py", line 1, in <module>
    infile = open("menu.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'menu.txt'
```

Our code is brittle.  We will fix this in Section~\ref{sec:except}.

## Exceptions
\label{sec:except}

Let's not delay in fixing Listing~\ref{code:check_and_write_menu}.  The code,
again, for the sake of convenience, is:

```python, options: "linenos": true
infile = open("menu.txt", "r")
print("The current menu on file is:")
for menuitem in infile:
    print(menuitem.rstrip())
infile.close()
print()

create_new = input("Would you like to throw away this menu " +
                   "and create a new one? (y/n): ")

if create_new == "y":
    outfile = open("menu.txt", "w")
    food = input("What do you want to eat? (Enter nothing to quit.) ")
    while food != "":
        outfile.write(food + "\n")
        food = input("What do you want to eat? (Enter nothing to quit.) ")
    outfile.close()
```

To recap, the problem lies in line 1, which assumes that we already have a file
named `menu.txt` that resides in the same folder as our code.  If that file does
not exist, then our code will crash at line 1.  Furthermore, lines 2 through 9
also rely on this assumption, namely, that we already have a menu saved.  So,
our first instinct might be to "protect" lines 1 through 9 with an `if`
statement.  The Python standard libraries has a package named `os` that has
functions that let us look at the contents of the current folder.  We can use it
as shown in Listing~\ref{code:menu_with_isfile}.

\begin{codelisting}
\label{code:menu_with_isfile}
\codecaption{Show and create menu with error checking}
```python, options: "linenos": true, "hl_lines": [1,3,5]
import os

create_new = "y"

if os.path.isfile("menu.txt"):
    infile = open("menu.txt", "r")
    print("The current menu on file is:")
    for menuitem in infile:
        print(menuitem.rstrip())
    infile.close()
    print()

    create_new = input("Would you like to throw away this menu " +
                        "and create a new one? (y/n): ")

if create_new == "y":
    outfile = open("menu.txt", "w")
    food = input("What do you want to eat? (Enter nothing to quit.) ")
    while food != "":
        outfile.write(food + "\n")
        food = input("What do you want to eat? (Enter nothing to quit.) ")
    outfile.close()
```
\end{codelisting}

In Listing~\ref{code:menu_with_isfile}, we've indented lines 6 through 14 from
our previous code (Listing~\ref{code:check_and_write_menu}).  We are now
importing the `os` module and using it in line 5 to ensure that `menu.txt`
exists before we try to open it and read from it.  We also need to initialize
the variable `create_new` since we only ask the question of whether to create a
new menu if we already have a menu created (see line 3).

Try to break this code.  Remove `menu.txt` and run the code.  What happens?

It looks like we've fixed everything, so congratulations!  Give yourself a pat
on the back.  If that is difficult, you may want to consider stretching your
shoulders more often (heh!).

The strategy we just used is one we've used before in this book, specifically,
we've used an `if` statement to "guard" a block of other statements.  That's not
the only way to solve this problem, however.  There is another way to do it, and
it is one that might make other problems easier to solve in the future as well.
The other way is to utilize *exceptions*.

You've seen exceptions before in code.  In fact, we saw one at the end of the
last section.

```console
Traceback (most recent call last):
  File "t.py", line 1, in <module>
    infile = open("menu.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'menu.txt'
```

`FileNotFoundError` is an exception!  An exception is an "exceptional condition"
that, if unhandled, can cause the program to crash.  We've seen others of these
earlier in the book as well: `NameError`, `TypeError`, `IndexError`, etc.

Notice what we just said about exceptions: they *can* cause a program to crash.
We can prevent them from causing a crash, however.  We can *catch* exceptions
when they happen, and then we can respond appropriately to them.

Before we go back to Listing~\ref{code:menu_with_isfile} and try to solve the
problem a different way, let's look at a more simple example that uses
exceptions.  Let's start with the following code.

```python
age = int(input("How old are you? "))
if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote yet.")
```

This code is all fine and dandy as long at the users properly enter an integer
as their input.  If the user types something other than an integer (say,
"cheetos"), the call to `int` will produce an exception named `ValueError`.

```console
Traceback (most recent call last):
  File "s.py", line 1, in <module>
    age = int(input("How old are you? "))
ValueError: invalid literal for int() with base 10: 'cheetos'
```

Instead, we can "try" a certain bit of code, and then also write code that
should be executed only in the event we receive an exception, like this:

```python, options: "linenos": "true", "hl_lines": [1,7,8]
try:
    age = int(input("How old are you? "))
    if age >= 18:
        print("You are old enough to vote.")
    else:
        print("You are not old enough to vote yet.")
except ValueError:
    print("That does not look like a valid age.")
```

We "try" lines 2 through 6.  If we encounter a `ValueError`, we immediately jump
down to line 8 and execute that code.  If we didn't have `try` and `except`, we
would have to write code like this:

```python
age = input("How old are you? ")
if age.isdigit():
    age = int(age)
    if age >= 18:
        print("You are old enough to vote.")
    else:
        print("You are not old enough to vote yet.")
else:
    print("That does not look like a valid age.")
```

One of the next things about `try`/`except` is we can focus on "normal"
conditions in our code and then handle "edge" cases in our `except` block.

For the sake of completeness in our terminology, when a function generates an
exception, we sometimes say that the function *throws* or *raises* an exception.
The `except` block is responsible for *catching* or *handling* an exception.

A `try` block can be followed by more than one `except` block.  You might think of each `except` block as being like an `elif` in that we can have different blocks of code to be executed depending on the type of exception we catch.  Consider Listing~\ref{code:multi_except}.

\begin{codelisting}
\label{code:multi_except}
\codecaption{Show and create menu with error checking}
```python, options: "linenos": true
# Try commenting out the different lines in the try block to see what
# exceptions get caught and handled.
try:
    float("cheetos")
    ["a","b"][7]
    x
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except:
    print("Error")
```
\end{codelisting}

Line 4 of Listing~\ref{code:multi_except} generates a `ValueError`.  If we
comment out line 4, then line 5 throws an `IndexError`.  If we comment out lines
4 and 5, then line 6 throws a `NameError` since `x` is not defined.  The last
`except` that starts on line 11 catches all other exceptions, including
`NameError`.  Thus, we do not necessarily need to state the type of exception to
catch.

Now, let's return to our file reading/writing example involving menus.  We can
use exceptions to deal with the situation where there is no `menu.txt` file.
Consider Listing~\ref{code:menu_with_try}.

\begin{codelisting}
\label{code:menu_with_try}
\codecaption{Show and create menu with exception handling}
```python, options: "linenos": true, "hl_lines": [3,12,13]
create_new = "y"

try:
    infile = open("menu.txt", "r")
    print("The current menu on file is:")
    for menuitem in infile:
        print(menuitem.rstrip())
    infile.close()
    print()
    create_new = input("Would you like to throw away this menu " +
                        "and create a new one? (y/n): ")
except:
    pass

if create_new == "y":
    outfile = open("menu.txt", "w")
    food = input("What do you want to eat? (Enter nothing to quit.) ")
    while food != "":
        outfile.write(food + "\n")
        food = input("What do you want to eat? (Enter nothing to quit.) ")
    outfile.close()
```
\end{codelisting}

The `except` block in Listing~\ref{code:menu_with_try} handles any exceptions
encountered in lines 4 through 11.  Since `except` must have a body and there's
really nothing more to do once the exception is caught, we simply write `pass`.
`pass` is just an empty statement in Python that doesn't do anything other than
serve as a placeholder.

## Bits, Bytes, and Machine Representation

This section and the sections that follow are currently being re-edited.

## (Optional) Introduction to Cryptography

## (Optional) Regular Expressions and File Encodings
