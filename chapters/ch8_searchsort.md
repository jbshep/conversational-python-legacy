# Searching and Sorting
\label{ch:searchsort}

## The Sorting Problem
\label{sec:sort_prob}

Do you stream music online?  Do you click on a folder on your desktop to find
and organize your files?  Have you ever used Microsoft Excel to keep information
in a spreadsheet?  If we think for a moment about these software programs, we
might realize that they have some features in common.  One we might notice is
that they eventually allow a user to *sort* information.  In a music streaming
app, you might choose to order your songs by title or by artist to make certain
songs easier to find.  When you're looking at a folder full of files, you might
order your files by file name or by the date it was last modified.  In Excel, we
can sort a column of data, which has the effect of rearranging the rows into a
different order.

Sorting is a very common thing that programs do, and it is an interesting
problem that can be tackled in a lot of different ways.  In this introductory
book you're reading right now, we will look at only one of those ways.  In doing
so, we'll also get better at walking through a problem logically in order to
write a program that solves a problem.  The end result will be that we improve
our natural problem solving abilities, too.  If you continue learning about
computer science through other courses and other books, you'll encounter other
ways to perform sorting, some of which have really interesting capabilities.
Well, what are we waiting for?

## Towards an Algorithm for Sorting
\label{sec:sort_algo}

In this section, we will start developing an algorithm for sorting.  An
*algorithm* is a series of well defined steps for solving a problem that has an
input, an output, and completes in a reasonable amount of time.  (The meaning of
``reasonable'' in this context is discussed in greater detail in more advanced
computer science texts.)

Suppose we have a list of numbers, defined as such.

```python
numbers = [8, 4, 3, 9, 5]
```

If we were to sort this list into *ascending* order, it would look like this.

```python
numbers = [3, 4, 5, 9, 8]
```

A thoughtful reader might ask what happens if we have duplicate numbers.  In
other words, what if `numbers` were defined like this?

```python
numbers = [3, 2, 3, 1, 4]
```

Note that we have two 3's in our list.  The sorted version would look like this.

```python
numbers = [1, 2, 3, 3, 4]
```

The two 3's remain preserved in the sorted list.  We certainly wouldn't want to
lose items, so this makes sense.  We used the word *ascending* to describe how
we sorted the numbers, but that's not technically correct since the list does
not ``ascend'' between the first and second 3.  A more correct phrase would be
to describe the sort as *monotonically increasing*.  We should use that phrase
from here forward because 1.) it's technically correct, and 2.) it sounds
cooler.

So, how do we sort these numbers?  In other words, how do we change the
positions of the numbers in the list without losing any of the numbers?

Often, the best way to solve a problem is to think of a very simple instance of
that problem, and then invent a simple solution.  If we can find the smallest
number in the list, where in the list should it go?  The smallest number should
always come first in the list, right?

Suppose we have the following list.

```python
numbers = [8, 4, 3, 9, 5]
```

3 is the smallest number, so 3 should move to position 0, the start of the list.
However, if we're going to move the 3 to position 0, we need to find a new home
for the 8.  So, we'll put 8 where the 3 was.

```python
# Before
numbers = [8, 4, 3, 9, 5]
# After
numbers = [3, 4, 8, 9, 5]
```

None of the other numbers are touched in moving the 3 and the 8.  Exchanging
positions for the 3 and the 8 is called *swapping* the numbers.  In fact, you
learned how to swap values in a list back in Chapter 5.  Now would be a good
time to go back and view Listing \ref{code:swap_good} and Figure
\ref{fig:swap_good} in Section \ref{sec:list_ops} again.

Now that the smallest item has been moved into position 0, we can do the same
thing with the next smallest item.  Where should the next smallest item go?  In
other words, what position should hold the next smallest item?  If you said
position 1, you're correct!

```python
# Original list
numbers = [8, 4, 3, 9, 5]
# Moving the smallest to position 0 by swapping.
numbers = [3, 4, 8, 9, 5]
# Moving the next smallest to position 1 by swapping.
numbers = [3, 4, 8, 9, 5]
```

Oh dear!  Nothing changed!  Actually, nothing needed to change. The 4 was
already at its desired position.  The computer doesn't need to notice this.  We
don't need to check to see if they swap needs to happen.  We can always perform
the swap, because we can swap a number with itself with no unfortunate side
effects.

We can continue this procedure to move each subsequent number to the correct
position in the list.  When we have one final item remaining, we know that
number is the biggest the number, and it should simply remain at the end of the
list.

In each step `x`, we swap the next smallest value to position `x`.  We scan
across from position `x` to the end of the list, looking for and keeping track
of the position of the smallest.  When we are done scanning, we perform the
swap.  We can see what this procedure looks like in Figure
\ref{fig:selsort_steps}.  We've underlined the eventual position of smallest
item that we have selected and swapped.  In fact, this sort is named *selection
sort* because of how we select the smallest item in each step.

![\label{fig:selsort_steps}](images/ch8/selsort_steps.png)

There are a couple of things to note in the example shown that will help us
write actual code.  This is often how we come up with code that solves problems.
We make up an example to help us think more concretely, and then we use that
concrete example to help us see patterns that become our code.  In Figure
\ref{fig:selsort_steps}, you can see that we are starting each scan to find the
smallest item at positions 0, 1, 2, and finally 3.  3 is one less than the last
index in the list.  We will need a loop to perform the scan to select the
smallest item, and we will need another loop (outside of the scan loop) to
control where we start each scan.

Try to write the code yourself before going on to the next section.  Don't cheat
and look ahead.  Make a focused attempt, hand-written on paper before you
proceed.

## The Selection Sort
\label{sec:selsort}

Let's walk through the advice given at the end of Section \ref{sec:sort_algo}.
Rather than name our list 'numbers', we'll name it `L` (hey, fewer keystrokes!).

In each step of the selection sort, we scan across the list from beginning to
end looking for the smallest item.  We want to note the position/index where the
smallest item sits (we'll call it `smallpos`).

```python, options: "linenos": true
smallpos = 0
for i in range(1, len(L)):
    if L[i] < L[smallpos]:
        smallpos = i
```

This code assumes we start looking for the smallest at index 0.  We let index 0
be the first smallest, and then we scan across from index 1 onward.  However, we
don't want to start at index 0 every time.  We want to start at index 0 to find
the first smallest item, then we want to start at index 1 to find the next
smallest, and so forth.  So, the starting position needs to become a variable
since the starting position needs to change each time.  We'll named that
variable `start`.  Notice how the code changes on lines 1 and 2 of the code.

```python, options: "linenos": true
smallpos = start
for i in range(start+1, len(L)):
    if L[i] < L[smallpos]:
        smallpos = i
```

Now that we have a `start` variable to control the starting position of each
scan through the list, we need a loop to update it in each step of the
algorithm.

```python, options: "linenos": true
for start in range(...):
    smallpos = start
    for i in range(start+1, len(L)):
        if L[i] < L[smallpos]:
            smallpos = i
```

What should we put in `range` in line 1?  The first value of `start` should
clearly be 0.  What about the last value?  From looking at
Figure~\ref{fig:selsort_steps}, we want the last time through the loop to be the
next to last index.  Therefore, the expression that ends the loop should be
`len(L)-1`, like in the following code.

```python, options: "linenos": true
for start in range(0, len(L)-1):
    smallpos = start
    for i in range(start+1, len(L)):
        if L[i] < L[smallpos]:
            smallpos = i
```

This code now does successive scans across the list, but it doesn't actually
swap any values.  Once we're finished with the scan, but before we do another
scan, we need to swap values between the positions stored in `start` and
`smallpos`.  The final solution is shown in Listing~\ref{code:selsort}.

\begin{codelisting}
\label{code:selsort}
\codecaption{Selection Sort}
```python
for start in range(0, len(L)-1):
    # Find the smallest value and keep track of its position.
    smallpos = start
    for index in range(start+1, len(L)):
        if L[index] < L[smallpos]:
            smallpos = index

    # Swap the smallest value to the correct location,
    # i.e., where we started our walk through the list.
    temp = L[start]
    L[start] = L[smallpos]
    L[smallpos] = temp
```
\end{codelisting}

This code works for any list we name `L` that has values that can be compared
with the `<` operator.  If we fill `L` with numbers, this code works.  If we
fill `L` with strings, it also works (can you guess how it orders strings?).

We can take this one step further and wrap it into a function that we can call.  See Listing~\ref{code:selsort_func}.

\begin{codelisting}
\label{code:selsort_func}
\codecaption{Selection Sort as a Function}
```python
def selsort(L):
    for start in range(0, len(L)-1):
        # Find the smallest value and keep track of its position.
        smallpos = start
        for index in range(start+1, len(L)):
            if L[index] < L[smallpos]:
                smallpos = index

        # Swap the smallest value to the correct location,
        # i.e., where we started our walk through the list.
        temp = L[start]
        L[start] = L[smallpos]
        L[smallpos] = temp
```
\end{codelisting}

Then, we could call the function like this.

```python
numbers = [3, 4, 1, 5, 2]
names = ["Becky", "Allen", "Derek", "Casey"]
selsort(numbers)
selsort(names)
print(numbers)  # Output is [1, 2, 3, 4, 5]
print(names)    # Output is ["Allen", "Becky", "Casey", "Derek"]
```

## Searching for Items in Sorted Data

## (Optional) Using Recursion to Search
\label{sec:recursion}

## Exercises
\label{sec:searchsort_exercises}

1. Given the following `dict` definition
