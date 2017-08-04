# Lists
\label{ch:lists}

## List Operations
\label{sec:list_ops}

Yay!  Finally, we get to talk about *lists*.  Lists are very useful and powerful
structures in Python, and their use is critical when we start working with
real-world data.  So, let's get cracking!

Let's motivate the need for lists.  Suppose I wanted to write software that
keeps track of students' names and test scores.  Let's store their names first.
Given what we know so far, we would need a separate variable for each student
name.

```python, options: "linenos": true
student1 = "John Smith"
student2 = "Judy Adams"
student3 = "Frank Johnson"
```

If we had another student enroll in the class, we'd need to add another
variable.

```python, options: "linenos": true, "hl_lines": [4]
student1 = "John Smith"
student2 = "Judy Adams"
student3 = "Frank Johnson"
student4 = "Paige McConnell"
```

How many variables do we need?  Well, I guess we'd need as many as we think we
might possibly need.  If we were using this software at a large public
university, we might have 500 students in a Computer Science 1 class, so our
code might look like this:

```python
student1 = "John Smith"
student2 = "Judy Adams"
student3 = "Frank Johnson"
# ...
# ...
# ... definitions for student4 through student498 omitted ...
# ...
# ...
student499 = "Sally Schmidt"
student500 = "Maxwell Masterson"
```

That's a lot of variables, and this is getting ridiculous.

What if instead of a whole bunch of variables to store all of our students, we
could have just one variable to store all of the students.  We can!  Contrast
the code we've presented so far with the code in Listing~\ref{code:list_ex1}.

\begin{codelisting}
\label{code:list_ex1}
\codecaption{}
```python
students = ["John Smith", "Judy Adams", "Frank Johnson", "Paige McConnell"]
```
\end{codelisting}

The `students` variable holds a *list* of values.  In this case, each value is a
single string value, and there are four strings stored in this list.  We use
the square bracket symbols `[` and `]` when we want to create a list.

In Listing \ref{code:list_ex1}, whenever we want to store more students, we
don't need to create more variables.  We can just dump their names into this
`students` variable.  Cool, huh?  Actually, we haven't even scratched the
surface of how useful this is going to be.

So, what can we do with a list once we've made one?  Table~\ref{tbl:list_ops}
shows several handy list expressions and list functions.  To make sense of the
table, suppose we have the following variables.

```
Let L be a list,
    L1 be a sub-list of L,
    v be a value we wish to store in a list,
    i be an index integer,
    j be another index integer,
    s be a string
    p be a string
```

You'll notice in Table~\ref{tbl:list_ops} that some of the same operations that can be performed on strings can also be performed on lists.  

\begin{table}
\caption{List Operations\label{tbl:list_ops}}
\begin{tabular}{|l|l|}
  \hline
  Expression & Explanation \\
  \hline
  \kode{v = L[i]} & The indexing operator: gets the $i^{th}$ item from \kode{L} and places it in the variable \kode{v}. \\
  \kode{L1 = L[i:j]} & The slicing operator: makes a new list \kode{L1}, which is a sub-list of \kode{L} consisting of \kode{L}'s items from index \kode{i} up to--but not including--index \kode{j}. Both \kode{i} and \kode{j} may be omitted.  If \kode{i} is omitted, the beginning of the list is assumed.  If \kode{j} is omitted, the end of the list is assumed. \\
  \kode{L.append(v)} & Adds the value \kode{v} to the end of the list \kode{L}. \\
  \kode{L.insert(i, v)} & Inserts the value \kode{v} into the list \kode{L} at position \kode{i}. \\
  \kode{L.remove(v)} & Removes the first instance of the value \kode{v} in the list \kode{L}.  If there are more instances of \kode{v} in \kode{L}, they will be ignored.  If \kode{v} does not exist in \kode{L}, the program will trigger a \kode{ValueError}. \\
  \kode{v = L.pop(i)} & Removes the value in \kode{L} at index \kode{i} and places it in the variable \kode{v}.  \kode{i} may be omitted, in which case the last item in the list is removed. \\
  \kode{L = s.split()} & Uses the parts of a string to make a list.  Does so by splitting a string up into pieces separated by whitespace and placing the resulting items into the list \kode{L}. It does not modify the original string \kode{s}. \\
  \kode{L = s.split(p)} & Uses the parts of a string to make a list. Does so by splitting a string up into pieces separated by the string pattern \kode{p} and placing the resulting items into the list \kode{L}. It does not modify the original string \kode{s}. \\
  \kode{s = p.join(L)} & Joins the items in the list \kode{L} to form a new string (stored in \kode{s}) by joining the items together with the string \kode{p}. \\
  \hline
\end{tabular}
\end{table}

The more you program, the easier it will become to read tables like
Table~\ref{tbl:list_ops}.  For most beginning programmers, however, it is easier
to learn by looking at examples. Listing~\ref{code:list_ops_ex} demonstrates a
few "toy" examples of how to use these list operations.  The result of most of
the operations is printed, and the effect of each statement is shown in a
comment to the right of the statement.

\begin{codelisting}
\label{code:list_ops_ex}
\codecaption{}
```python
cheeses = ["cheddar", "swiss", "feta", "gouda", "parmesan"]
line = "red,green,blue,teal,cyan"

print(cheeses[1])           # prints swiss
print(cheeses[0:2])         # prints ["cheddar", "swiss"]
print(cheeses[-1])          # prints parmesan
print(cheeses[3:])          # prints ["gouda", "parmesan"]
print(cheeses[:2])          # prints ["cheddar", "swiss"]

cheeses.remove("parmesan")  # cheeses is now ["cheddar", "swiss", "feta", "gouda"]
cheeses.pop(-1)             # cheeses is now ["cheddar", "swiss", "feta"]
cheeses.pop()               # cheeses is now ["cheddar", "swiss"]
cheeses.append("jack")      # cheeses is now ["cheddar", "swiss", "jack"]
cheeses.insert(0, "brie")   # cheeses is now ["brie", "cheddar", "swiss", "jack"]

colors = line.split(",")    # colors is now ["red","green","blue","teal","cyan"]
print(len(colors))          # prints 5
print(", ".join(colors))    # prints red, green, blue, teal, cyan
print(" -> ".join(colors))  # prints red -> green -> blue -> teal -> cyan
```
\end{codelisting}

Okay, let's test our understanding by trying to apply what we've learned.
Suppose we have a list named `lst` defined as:

```
lst = ["Maria", "Sheryl", "Barbara", "Shafi"]
```

Can we write code to modify `lst` so that the first item is moved to the end of
the list?  In other words, the end result should look like this:

```
lst = ["Sheryl", "Barbara", "Shafi", "Maria"]
```

We can use any number of statements that we want.  Try it.  Try mocking up a
solution using comments first, and then write your code beneath each of the
comments.

Here's one approach.  First, let's start with comments.

```
# Remove the first item and store it.

# Put the stored item on the end of the list.
```

Now, let's fill in the details of how we accomplish these steps.

```
# Remove the first item and store it.
value = lst.pop(0)

# Put the stored item on the end of the list.
lst.append(value)
```

Good!  This is a suitable way to accomplish this task, and more importantly, it
is easy to read what the code does even if there are no comments to explain the
statements.  To see what I mean, let's strip away the comments.

```
value = lst.pop(0)
lst.append(value)
```

We can clearly see that the first statement extracts the first item, and the
second statement puts it back on the end of the list.  We should always try to
write our code in such a way that it is easily read and understood.  This was
best articulated in the preface of the book _Structure and Interpretation of
Computer Programs_ (a.k.a. "SICP") by Harold Abelson and Gerald Sussman:

> "Programs must be written for people to read, and only incidentally for machines
to execute."

We could have also written this code as a one-liner, like this:

```
lst.append(lst.pop(0))
```

One could argue this is harder to read, at least initially.

Let's try another example.  What if we wanted to "swap" the locations of the
first and second items in the list?  Consider the following definition of `lst`.

```
lst = ["Maria", "Sheryl", "Barbara", "Shafi"]
```

Can we write code that makes `lst` look like this?

```
lst = ["Sheryl", "Maria", "Barbara", "Shafi"]
```

Try to write code that does this.  Make a good, honest attempt before reading
ahead.

We know that we want the value of the expression `lst[0]` to be changed to the
value of the expression `lst[1]` and vice versa.  So, our first attempt might be
Listing~\ref{code:swap_bad}.

\begin{codelisting}
\label{code:swap_bad}
\codecaption{First attempt at swapping value in a list}
```python
lst[0] = lst[1]
lst[1] = lst[0]
```
\end{codelisting}

Consider the effect of the first statement `lst[0] = lst[1]`, which is shown in
Figure~\ref{fig:swap_bad}.

![\label{fig:swap_bad}](images/ch5/swap-bad.png)

Uh oh!  Our first statement overwrites "Maria" and she disappears forever!  That
is not good at all.

What we need to do is save "Maria" somewhere first so she doesn't get
obliterated.  So let's create a *temporary variable* -- a one-use variable that
will help us accomplish a task, and then we'll likely never use it again.  Think
of a temporary variable (or just "temp variable" for short) like a Post-It note.
We may write something on a Post-It note to remind ourselves of something for a
brief period of time.  Consider our next attempt in Listing~\ref{code:swap_good}.

\begin{codelisting}
\label{code:swap_good}
\codecaption{Swapping values in a list}
```python
temp = lst[0]
lst[0] = lst[1]
lst[1] = temp
```
\end{codelisting}

Let's visualize how this works (see Figure~\ref{fig:swap_good}).

![\label{fig:swap_good}](images/ch5/swap-good.png)

The statement labeled number `1` copies the value at index `0` (in this case,
`"Maria"`) into the `temp` variable for safe keeping.  Then, statement number
`2` writes the value at index `1` over the top of the value at index `0`.  At
this point (after executing statement number `2`), there are two "Sheryl"
strings in the list, but that's okay because we have saved `"Maria"` in our temp
variable.  Finally, in statement number `3`, we take the value saved in `temp`
and we overwrite the value in index `1` with `temp`'s value.  The list contents
are now correctly `["Sheryl", "Maria", "Barbara", "Shafi"]`.

Index `0` and index `1` are hardcoded in Listing~\ref{code:swap_good}.  If we
wanted, we could invent two variables `i` and `j` to hold the indices whose
values we wish to swap (see Listing~\ref{code:swap_good_nohc}).

\begin{codelisting}
\label{code:swap_good_nohc}
\codecaption{Swapping values in a list, no hard-coded indices}
```python
i = 0  # or, whatever index we wish
j = 1  # or, whatever other index we wish
temp = lst[i]
lst[i] = lst[j]
lst[j] = temp
```
\end{codelisting}

## Assignment Statements Revisited: Multiple Assignment
\label{sec:multi_assign}

Since this book is purely an introduction to programming more so than a
definitive guide to the nuances of Python, we could stop our discussion right
here.  This same programming technique will work with most other programming
language as you encounter them (e.g., C++, Java, etc.).  However, Python has a
really cool way of performing swaps called *multiple assignment* that your
author (that's me!) simply can't help himself from showing you!  We can replace
the code in Listing~\ref{code:swap_good_nohc}) with
Listing~\ref{code:swap_good_multiassign}).

\begin{codelisting}
\label{code:swap_good_multiassign}
\codecaption{Swapping values in a list, no hard-coded indices}
```python
i = 0  # or, whatever index we wish
j = 1  # or, whatever other index we wish
lst[i], lst[j] = lst[j], lst[i]
```
\end{codelisting}

Wizardry!

How does this work?  Let's approach it visually as in
Figure~\ref{fig:multi_assign}.

![\label{fig:multi_assign}](images/ch5/multi_assign.png)

Multiple assignment is a Python feature known in the computer science community
as *syntactic sugar*.  Syntax is how you arrange a statement so that it can be
understood.  In the English language, sentences have a syntax consisting of a
noun phrase followed by a verb phrase.  That's how we start *parsing* (or
"breaking apart and making sense of") a sentence.  "Sugar" in this case means
non-essential.  So, syntactic sugar refers to language features that make
something easier or more expressive but are non-essential.  Usually, syntactic
sugar is converted behind the scenes to another form through a process called
*desugaring*.  If you continue on in studying computer science, this won't be
the last time you hear about desugaring, hopefully.

Desugaring in this case first evaluates the expressions on the RHS, and then
converts this

```python
lst[i], lst[j] = "Sheryl", "Maria"
```

behind the scenes to this

```python
lst[i] = "Sheryl"
lst[j] = "Maria"
```


FIXME Do I at some point mention trailing comma list syntax using multiline example?

## List Variables: References Versus Values
\label{sec:list_refs}

Here is some fairly simple code that creates variables, changes one of them, and
then prints their values.

\begin{codelisting}
\label{code:simple_assign}
\codecaption{Simple Assignment Statements}
```python
x = 3
y = x
x = x + 1
print(x)   # prints 4
print(y)   # prints 3
```
\end{codelisting}

Let’s do something similar, only this time we’ll use lists of numbers.

\begin{codelisting}
\label{code:list_assign}
\codecaption{Assignment with List Variables}
```python
xlist = [2, 4, 6]
ylist = xlist
xlist.append(8)
print(xlist)
print(ylist)
```
\end{codelisting}


You may have expected the first print statement to yield `[2, 4, 6, 8]` and the
second one to yield `[2, 4, 6]`, but that isn’t what happens at all!  Instead,
the output is:

```console
[2, 4, 6, 8]
[2, 4, 6, 8]
```

How is it that changing `xlist` has the side-effect of changing `ylist`?  What
is this sorcery?!

The good news is that the reason is really fairly simple, especially when we
explain it with pictures.  Consider the first example in
Listing~\ref{code:simple_assign} where we had integer variables `x` and `y` (see
picture in Figure~\ref{fig:inc_assign}).

![\label{fig:inc_assign}](images/ch5/inc_assign.png)

No surprises there.  Now, let’s see what happens in the example with `xlist` and
`ylist`.  It turns out that list variables don’t actually contain lists
themselves.  Instead, they contain something called a *reference* to a list. The
list is actually stored somewhere else.  Think of a reference as being like a
"pointer" or an arrow to somewhere else in the computer’s memory.  With this in
mind, we can represent the code in Listing~\ref{code:list_assign} visually in
Figure~\ref{fig:list_assign}.

![\label{fig:list_assign}](images/ch5/list_assign.png)

If we attempt to modify `xlist` or `ylist`, either will affect the same list.
You might ask why this happens in Python, and there is a perfectly good reason
that we will explore in Section~\ref{sec:list_funcs}.  For now, recognize that
we want to know how to make `ylist` be a copy of `xlist`.  We could do the
following.

```python
ylist = xlist[:]    # the right way to make a copy of a list
```

This code assigns a slice of `xlist` to the new variable `ylist`.  Why no integers before or after the colon (`:`)?  Recall that the integers around the colon are optional.  If no integers are given, it selects the entire list.  The end result is shown in Figure~\ref{fig:list_copy}.

![\label{fig:list_copy}](images/ch5/list_copy.png)

Now if we perform `xlist.append(8)` this time, we end up with the result in Figure~\ref{fig:list_append_after_copy}.

![\label{fig:list_append_after_copy}](images/ch5/list_append_after_copy.png)

## Functions with Lists
\label{sec:list_funcs}

In the previous section, we learned that list variables do not contain the lists
themselves.  Rather, they contain a *reference* to a list.  There are a number
of perfectly good reasons for this, the first of which has to do with how
functions interact with lists.

Let’s consider an example.  Suppose we have a list of strings that happen to be
integers, like `["1", "2", "3", "4"]`.  We wish to change the list so that the
values are actually integers rather than strings, that is, `[1, 2, 3, 4]`.  We
would need to pass the list to the function as an argument.

```python
def make_int_list(lst):
    # function body goes here


# main section of code
numbers = [ """Somehow we get a bunch of strings here.""" ]
make_int_list(numbers)
# Now 'numbers' has been changed from a list of strings
# to a list of integers.
```

We have named the parameter `lst`, but you can name it whatever seems
appropriate.  We named it `lst` rather than `list` since the word `list` is
already used in Python as the name of a type.

As we learned in Section \ref{sec:params}, Python passes arguments to function
parameters by value.  That is, a copy of the value in the main program is sent
to the function.  Imagine if list variables contained the lists themselves.  In
the above example, a copy of the numbers list would be sent to `make_int_list`,
so `lst` would be a complete copy of numbers (see Figure~\ref{fig:numbers_copy}).

![\label{fig:numbers_copy}](images/ch5/numbers_copy.png)

If we program properly, `make_int_list` would convert all the strings in the
list to integers so the end result would be as shown in
Figure~\ref{fig:numbers_lst_diff}.

![\label{fig:numbers_lst_diff}](images/ch5/numbers_lst_diff.png)

But, the original list that we wanted to change, namely `numbers`, hasn’t
changed!  Now, consider what happens since list variables contain references to
lists.  The reference is passed by value, so `lst` now "points" at the same list
as `numbers` (see Figure~\ref{fig:numbers_lst_same}).

![\label{fig:numbers_lst_same}](images/ch5/numbers_lst_same.png)

Now when `make_int_list` has returned, all changes made to `lst` are also made
to `numbers` because both `lst` and `numbers` refer to the same list (see
Figure~\ref{fig:numbers_lst_mod})!

![\label{fig:numbers_lst_mod}](images/ch5/numbers_lst_mod.png)

We should probably go ahead and write the function’s body.  We use a loop to
walk through each index.  At each index, we can convert the string to an `int`.

```python
def make_int_list(lst):
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])
```

That’s it!

There is another advantage to passing a list to a function given that lists are
stored by reference rather than by value.  Suppose we had a very large list of
information (say, 500 million strings).  If the entire list was passed to the
function rather than just a reference to the list, Python would have to make a
copy of the entire list, all 500 million items.  That takes precious time, and
even though computers are fast, there are limits even to what computers can do
(more on this in a later chapter).  It also uses an unnecessary amount of
memory, because now instead of having one list containing 500 million strings,
we now have two lists containing a cumulative total of 1 billion strings.  There
are some computer languages that let you pick whether you pass arguments to
functions by value or by reference no matter what the type of the variable is.
It is common practice in those languages to pass large lists by reference for
that reason alone.

Let’s look at another way we might use functions on lists.  We won’t always
define functions that modify lists directly.  Sometimes, we will pass a list to
a function, and then the function will *return* a value or an entirely new list
based on the original list.  For example, there is a function named `sum` that
takes a list of numbers and returns the sum of all the numbers in the list.  We
could use it like this.

```python
money = [30.50, 72.25, 10.00]
grand_total = sum(money)
print("You have $%.2f." % grand_total)
```

`sum` takes a list as a parameter and returns a `float`.  It does not modify the list in any way.  How did the person who wrote the `sum` function do it?   Let’s find out by writing our own, only we need to give ours a different name.  Let’s call it `total`.  Once we define our function named `total`, we will be able to do this.

```python
money = [30.50, 72.25, 10.00]
grand_total = total(money)
print("You have $%.2f." % grand_total)
```

Let’s begin.  We know that we need the name of the function to be `total`, and
it needs to accept a single list parameter, so we can write:

```python
def total(numbers):
    # function body goes here
```

Now, the function body will need to loop through the list of numbers and add
each of them to a variable.  The variable will keep track of the running total.
So, let’s create the variable (we’ll call it `running_total`) and then write the
loop.

```python
def total(numbers):
    running_total = 0.0
    for i in range(0, len(numbers)):
        running_total += numbers[i]
    return running_total
```

This should work.  Go ahead and test it out.  The key ideas here are: 1.) we’re
passing a list to a function, 2.) we’re using a loop to walk through the list’s
items, and 3.) we’re creating a variable that we will update in each iteration
of the loop.  These key ideas will show up a lot when we write functions that
operate on lists.

Let’s try out a different example, and let’s see if we can apply some of the same ideas mentioned in the prior paragraph......

FIXME: find smallest, biggest, valid candidates



## (Optional) Functional Programming with Lists
\label{sec:func_prog}

## (Optional) List Comprehensions
\label{sec:list_comprehensions}

## Exercises
\label{sec:lists_exercises}
