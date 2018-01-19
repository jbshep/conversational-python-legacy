# Dictionaries
\label{ch:dict}

## Creating and using dictionaries
\label{sec:crud_dict}

We can do a lot of things in code using what we know so far.  Some of the things
we can do in code is kind of, well, "clunky."  Consider the following example.
Suppose we want to keep track of a group of students and their major field of
study.  The only way we know how to do that currently is with lists.

```python
names = ["Shayla Succotash", "Amy Avocado", "Larry Linguini", "Kevin Kumquat"]
majors = ["Comp Sci", "Accounting", "Math", "Comp Sci"]
```

We are using lists to store corresponding attributes of each student.  Each
student has a unique index for their attributes.  Suppose we ran the code that
follows.

```python
print(names[1])
print(majors[1])
print()
print(names[3])
print(majors[3])
```

The resulting output of this code is:

```console
Amy Avocado
Accounting

Kevin Kumquat
Comp Sci
```

This is all fine, but it's also a bit awkward.  If we want to know a student's
major, we have to find their location in the first list, and then use their
index to look up their major in the second list, like in Listing~\ref{code:find_major}.

\begin{codelisting}
\label{code:find_major}
\codecaption{}
```python, options: "linenos": true
x = "Kevin Kumquat"
found = False

for i in range(0, len(names)):
    if names[i] == x:
        print(majors[i])

if not found:
    print("Couldn't find a major for %s." % x)
```
\end{codelisting}

Yuck.  What we really want to do is something like this:

```python
x = "Kevin Kumquat"
m = get_major(x)
# m is now "Comp Sci"
```

We could easily define a function like `get_major`, but fortunately we don't
have to.

To make this easier, we will forgo lists (for now) and use a *dictionary*.  At
first glance, a dictionary is just like an English dictionary.  With an English
dictionary, we look up a word (which is a string) and next to the word is its
definition (also a string).  Python dictionaries can be used on more than just
strings, but we'll focus on strings for now.  We can apply this concept of an
English dictionary to, say, look up `"Amy Avocado"` and receive `Accounting`.

Let's create a dictionary to *associate* names with majors.  Here is how we do
it (see Listing~\ref{code:majors_dict_def}).

\begin{codelisting}
\label{code:majors_dict_def}
\codecaption{}
```python, options: "linenos": true
majors = {    
    "Shayla Succotash" : "Comp Sci",
    "Amy Avocado" : "Accounting",
    "Larry Linguini" : "Math",
    "Kevin Kumquat" : "Comp Sci",
}
```
\end{codelisting}

Now, we can _look up_ majors by typing this:

```python
print(majors["Shayla Succotash"])
print(majors["Larry Linguini"])
```

This produces:

```console
Comp Sci
Math
```

Notice how we _create_ a dictionary.  We use curly braces to denote the
dictionary type (which is called `dict` kind of like other types such as `str`
and `int`).  We use colons `:` to separate the name from the major.  Also,
notice how we use dictionaries to _look up_ values.  We use square brackets,
which looks a lot like how we used lists.

Terminology time!  The values on the left side of the `:` in our dictionary
definition (e.g., `"Shayla Succotash"`, etc.) are called *keys*.  The values on
the right (e.g., `"Comp Sci"`, etc.) are simply called *values*.  Each entry in
the dictionary that associates a name with a major is called a *key-value pair*.
`"Larry Linguini"` and  `"Math"` is an example of a key-value pair.

Okay, so now what?  Well, in this book we often ask questions that start with
"What happens if..." or "What happens when...?" to enhance our understanding of
a topic.  Here's one: What happens if we try to look up something that doesn't
exist in the dictionary?  Can we create an example of this in code?  You try it
without looking at the next paragraph.

Were you able to come up with an example?  If so, did it look like
Listing~\ref{code:dict_no_key}?

\begin{codelisting}
\label{code:dict_no_key}
\codecaption{}
```python
print(majors["Brooklyn Broccolini"])
```
\end{codelisting}

Clearly, there is no key for `"Brooklyn Broccolini"` defined in `majors` in
Listing~\ref{code:majors_dict_def}.  What happens when we run the
Listing~\ref{code:dict_no_key} code?

Did you try it?  What did you find out?

If we try to specify a key that does not exist in the dictionary, the code
produces a `KeyError`.  We could handle `KeyError` if we so chose, like the code
example found in Listing~\ref{code:dict_no_key_except}.

\begin{codelisting}
\label{code:dict_no_key_except}
\codecaption{}
```python
try:
    student = "Brooklyn Broccolini"
    print(majors[student])
except KeyError:
    print("There is no major listed for %s." % student)
```
\end{codelisting}

If we didn't want to rely on handling `KeyError`s, we could check first to see
if a certain key exists in a dictionary (see
Listing~\ref{code:dict_no_key_check}).

\begin{codelisting}
\label{code:dict_no_key_check}
\codecaption{}
```python, options: "linenos": true
if "Brooklyn Broccolini" in majors:
    print(majors["Brooklyn Broccolini"])
else:
    print("No major listed for that student.")
```
\end{codelisting}

Even though line 2 could technically raise a `KeyError`, the `if` statement in
line 1 checks first to make sure line 2 won't raise a `KeyError`.

To see a different example, let's return to the idea of a Python dictionary as
being similar to an English dictionary.  In an English dictionary, we can look
up a word and find its definition.  The word is a key.  The definition is the
word's value.

We will now write a program that creates a very small English dictionary that
allows the user to look up definitions of words (see
Listing~\ref{code:eng_dict_str}).

\begin{codelisting}
\label{code:eng_dict_str}
\codecaption{}
```python, options: "linenos": true
d = {
    "alpaca" : "A domesticated camelid",
    "bow" : "A weapon that shoots arrows",
    "rose" : "A prickly bush that produces fragrant flowers",
}

word = input("Enter a word to lookup (enter nothing to quit): ")
while word != "":
    if word in d:
        print("Definition:", d[word])
    else:
        print("There is no definition for '%s'" % word)

    word = input("Enter a word to lookup (enter nothing to quit): ")
```
\end{codelisting}

This is lovely, but English dictionaries often have more than one definition for
a word.  In Listing~\ref{code:eng_dict_str}, the key `"rose"` is a homophone.
The word "rose" could also mean "the past tense of rise."

It appears that we want a key to have multiple values, potentially.  If we
wanted to store multiple values in the past, we have relied on `list`s.  So, we
shall use `list`s once again.  Let us modify the definition of `d` in
Listing~\ref{code:eng_dict_str} so that the values are no longer strings, but
rather lists of strings (that is, a `list` of `str`).

```python
d = {
    "alpaca" : ["A domesticated camelid"],
    "bow" : ["A weapon that shoots arrows",
             "To bend at the waist",
             ],
    "rose" : ["A prickly bush that produces fragrant flowers",
              "The past tense of rise",
              ],
}
```

The expression `d["rose"]` now yields a `list` of two items: `"A prickly bush ..."`
and `"The past ..."`.  Because the expression `d["rose"]` produces a `list`, I
can do `list`-things to it.  For example, the expression `len(d["rose"])`
produces the `int` value `2`, and the expression `d["rose"][1]` produces the
`str` value `"The past tense of rise"`.

When we look up a word the user enters, we can use a `for` loop to show each of
the definitions.  See how we have modified Listing~\ref{code:eng_dict_str} to
create Listing~\ref{code:eng_dict_list}.

\begin{codelisting}
\label{code:eng_dict_list}
\codecaption{}
```python, options: "linenos": true
d = {
    "alpaca" : ["A domesticated camelid"],
    "bow" : ["A weapon that shoots arrows",
             "To bend at the waist",
             ],
    "rose" : ["A prickly bush that produces fragrant flowers",
              "The past tense of rise",
              ],
}

word = input("Enter a word to lookup (enter nothing to quit): ")
while word != "":
    if word in d:
        for defn in d[word]:
            print("Definition:", defn)
    else:
        print("There is no definition for '%s'" % word)

    word = input("Enter a word to lookup (enter nothing to quit): ")
```
\end{codelisting}

There's an interesting tidbit in Listing~\ref{code:eng_dict_list} you may have
missed.  Note lines 14 and 15.  My initial choice for a variable name was `def`.
However, `def` is a reserved keyword in Python, which we know is used to define
functions.  So, I had to chose another variable name.  Instead, I chose `defn`
to stand for "definition."

What if we want to remove a key-value pair from a dictionary?  We can use the
`del` keyword to accomplish this.  Consider Listing~\ref{code:del_dict_pair},
specifically line 13.

\begin{codelisting}
\label{code:del_dict_pair}
\codecaption{}
```python, options: "linenos": true, "hl_lines": [13]
d = {
    "alpaca" : ["A domesticated camelid"],
    "bow" : ["A weapon that shoots arrows",
             "To bend at the waist",
             ],
    "rose" : ["A prickly bush that produces fragrant flowers",
              "The past tense of rise",
              ],
}

word = input("Enter a word to remove from the dictionary: ")
if word in d:
    del d[word]
else:
    print("Sorry, %s doesn't seem to be defined in our dictionary." % word)
```
\end{codelisting}

If the user were to type `alpaca`, the pair for the key `"alpaca"` would be
removed.  Only the pairs for the keys `"bow"` and `"rose"` would remain.
(Readers will note that removing alpacas from the dictionary would be a terrible
calamity because they are adorable and charming.  Llamas, on the other hand, are
jerks.)

## Iterating through dictionaries
\label{sec:iter_dict}

There may be instances where we wish to iterate through a `dict` similar to how
we might traverse a `list`.  Suppose have the following dictionary definition.

```python
calories = {
    "egg" : 80.0,
    "milk" : 80.0,
    "cheerios" : 100.0,
    "blueberry" : 0.78,
    "strawberry" : 4.0,
}
```

`calories` is a `dict` that acts as a food database.  It allows programmers to
look up the calories for a given food.  Thus, `calories["strawberry"]` gives us
`4.0`.  Suppose we want to see all the foods in our database.  We might write
the following code.

```python
for food in calories:
    print(food)
```

When a `for` loop operates on a dictionary, the value assigned to the variable
`food` is actually the *key*.  The output of this code is each of the keys (the
food names), one on each line.

Now, run this code.  Run it several times.  What do you notice?  In all
likelihood, the ordering changes for the food names.  We cannot rely on the keys
to be kept in order when we use a dictionary.  If we want the keys to be sorted
alphabetically, we would need to do something like what we see in
Listing~\ref{code:sorted_dict_iter}.

\begin{codelisting}
\label{code:sorted_dict_iter}
\codecaption{}
```python, options: "linenos": true
for food in sorted(calories.keys()):
    print(food)
```
\end{codelisting}

`keys()` creates a `list` of the keys in `calories`.  `sorted` then returns a
new `list` with the keys in alphabetical order.

If you're curious why the keys are ordered differently when you iterate through
them using a loop, you'll learn more when you take a class on data structures
and learn about *hash tables*. Hash tables are used to make dictionaries.  (Very
curious readers should look on YouTube for a video from PyCon 2010 titled
"Mighty Dictionary." This will give you an idea how hash tables work and how
they organize the internals of a dictionary.)

## Exercises
\label{sec:dict_exercises}

FIXME
