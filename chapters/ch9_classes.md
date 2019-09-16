# Objects, Classes, and Interactive Graphics
\label{ch:classes}

## Getting Started
\label{sec:getting_started}

You're still reading this book?!  Hurray!  Good for you.  Now that you're here,
you'll be pleased to know that this is the best chapter of the whole book, so
pay attention!

Thus far, all of our programs have been text-only programs.  In this chapter, we
will make programs that have graphics.  To do this, we'll use a Python code
library named *Pygame*.  Very shortly, we'll learn how to install Pygame on your
computer.  Then, we'll write some simple graphical programs and eventually
animate the graphics to make them move around the screen.

Cool, huh?

We will reach a point in learning about graphics where things will get a little
frustrating.  We will want to detect when two graphical things collide, and that
will seem kind of hard to manage, especially when we have lots of graphical
things flying around the screen.  So, we will need to learn about things called
*objects* and *classes* that will help us tremendously, and will make
programming graphical video games way more fun.


Let's get started by installing Pygame.  Open Thonny and find the `Tools` menu.
Under the `Tools` menu you will see an option named "Manage packages..."  Click
that option.  A dialog window will be displayed to you.  The dialog has a
textbox and a button at the top of its window.  Enter "pygame" into the textbox
and press the button (which reads "Find package from PyPI").  Information about
the `pygame` package should then be displayed in the main part of the dialog
window, and beneath it should be a button labeled "Install".  Click the
"Install" button.  After pygame has installed, click the "Close" button.

How do you know if the installation worked?  In the Python shell window, you
should be able to type `import pygame`.  If nothing bad happens, it worked!  If
instead that statement makes Python puke red text, it did not work.  At that
point, you may wish to solicit help from the nearest knowledgeable, techie human.

Assuming everything worked, it's time to write code that uses Pygame!

## Basic Pygame: Drawing Graffiti
\label{sec:basic_graffiti}

Pygame can do a lot for us as programmers.  Pygame can make a separate window to
display our graphical program.  Pygame allows us to draw graphics on that
separate window.  Pygame allows us to draw different types of graphics (shapes,
colors, etc.), play sounds, and use a whole host of other features.

Because Pygame does a lot, the first Pygame program you see might look a bit
daunting.  So, let's dive in.  You can see our first Pygame program in
Listing~\ref{code:pygame_template}, and if you'd like to avoid typing this code
or using copy/paste, you can download the code directly from [this
link](https://raw.githubusercontent.com/jbshep/conversational-python/master/code/pygame-template.py).
In the paragraphs that follow, we will break down
Listing~\ref{code:pygame_template} section by section.

\begin{codelisting}
\label{code:pygame_template}
\codecaption{A basic Pygame code template}
```python, options: "linenos": true
import pygame
from pygame.locals import *

pygame.init()

white = (255, 255, 255)
black = (  0,   0,   0)
green = (  0, 255,   0)

screenWidth = 800
screenHeight = 600
screenSize = [screenWidth, screenHeight]
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("WINDOW TITLE HERE")

clock = pygame.time.Clock()

done = False

while not done:
    # 1. Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 2. Program logic, change variables, etc.

    # 3. Draw stuff
    screen.fill(white)
    pygame.draw.line(screen, green, [100, 200], [150, 300], 3)
    pygame.draw.line(screen, green, [150, 300], [200, 200], 3)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
```
\end{codelisting}

The result of the code in Listing~\ref{code:pygame_template} is the window shown in Figure~\ref{fig:pygame_template}.

![The window produced by the code in Listing~\ref{code:pygame_template}\label{fig:pygame_template}](images/ch9/pygame_template.png)

That's a lot of code to throw at someone, or at least it seems that way right
now.  It's actually not a huge deal.  Let's take this code step by step.  We'll
look at a block of code and then we'll explain what it does.

```python
import pygame
from pygame.locals import *

pygame.init()
```

The first two lines in this code snippet make it so we can use Pygame variables
and functions in our code.  The last line gets Pygame ready to start making
graphical windows.  

```python
white = (255, 255, 255)
black = (  0,   0,   0)
green = (  0, 255,   0)
```

In this code snippet, we define colors that we think we'll use in our program.
Colors are "mixed" together using amounts of red, green, and blue (in that
order, specifically).  The amounts of each range from `0` to `255`.  Thus, when
we type `green = (0, 255, 0)`, we are telling Python to make a color that has
`0` of red, lots of green (`255`, which is the maximum), and `0` of blue.

You might be wondering what the parentheses do.  Note that this:

```python
(0, 255, 0)
```

Kind of looks like this:

```python
[0, 255, 0]
```

Notice all we did was change the type of braces -- parentheses versus square
brackets.  We know that square brackets surround lists.  If we use parentheses,
it makes a list-like thing called a *tuple*.  A tuple is a list that cannot be
changed once it is created.  We use tuples to make colors.

Sometimes students are bothered by the indentation I've used in the above code
snippet.  Here is the code again:

```python
white = (255, 255, 255)
black = (  0,   0,   0)
green = (  0, 255,   0)
```

Notice the extra spacing around the zeroes.  This extra spacing doesn't do
anything special.  It just makes the code look more readable. You're allowed
(and encouraged) to be artistic in writing code.  Make your code pretty!

```python
screenWidth = 800
screenHeight = 600
screenSize = [screenWidth, screenHeight]
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("WINDOW TITLE HERE")
```

This code actually creates a graphical window.  It chooses a width and height
and then uses the function `pygame.display.set_mode` to set up the window, which
makes it appear on the screen for the first time.  The part of the code that
reads `pygame.display` is the name of a code module that contains the `set_mode`
function.  Much of the code in Pygame is stored in different modules that have
descriptive names.

The last line changes the text in the title bar of the window.  This text is
called the window's *caption*.

```python
clock = pygame.time.Clock()
```

This line of code creates a "clock" that "ticks."  We'll talk more about what
this `clock` variable is for in a little bit, but for now just remember that we
created a variable named `clock`.

```python
done = False

while not done:
```

You've seen loops a lot in this book.  Often, we've used loops to repeatedly ask
for a number, a string, or a value in a list.  In this case, the loop is going
to repeatedly draw things on the screen.

Computer programs that create graphics don't just draw those graphics on the
screen and then wait.  Computer monitors continually refresh their graphics
on-screen, so programs need to be written to continually re-paint their shapes,
colors, and images.  This is the start of the loop that accomplishes this.

We create a Boolean variable named `done`.  The loop will keep running until
`done` is `True`.  Presumably, something inside the loop will change `done` from
`False` to `True`.  We'll see that very shortly.

```python
# 1. Process events

# 2. Program logic, change variables, etc.

# 3. Draw stuff
```

Okay, so I've removed some code so that you can focus on the three main comment
sections of the loop.  In fact, I've labeled them 1, 2, and 3.  Each time
through the loop, we're going to do three basic things.  

First, we'll handle events.  Events are things like the user pressing a keyboard
key or moving the mouse.

Second, we'll perform program logic.  If we want to change where graphics show
up on the screen, or possibly check to see if there are any collisions between
our graphics, we would do that in this section of code.  We will use variables
to keep track of where things should appear on the screen, and in this section
we will update the values of those variables.

Third and finally, we'll use the variables modified in the second section of
code to actually draw shapes on the screen.

It is a really good idea to stick to this organization in the loop.  Consider if
we decided to try to draw something on-screen in part 1.  It is possible that
whatever we drew would end up erased or overwritten in part 3.  This would also
make our code really hard to debug.

Now, let's look at the code under each of these comment sections.

```python
# 1. Process events
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True
```

The function `pygame.event.get` gives us a list of all the events that have
happened to the program.  This could be mouse clicks, key presses, etc.  We are
using a `for` loop to cycle through the events, one at a time.  If the event
happens to be a `pygame.QUIT` event, this tell us that the user has clicked on
the "close" button typically found at the top corner of the window.  We should
respond by setting `done` to `True` so that the loop can exit at the top of the
`while` loop and then the program can end.

In future Pygame programs, we will handle more types of events in different
ways.

```python
# 2. Program logic, change variables, etc.
```

There's no code in this section right now.  This is because in this code sample,
all we are doing in the next section (part 3) is drawing two lines at
fixed locations.  There is no real program logic.

```python
# 3. Draw stuff
screen.fill(white)
pygame.draw.line(screen, green, [100, 200], [150, 300], 3)
pygame.draw.line(screen, green, [150, 300], [200, 200], 3)
```

Think of drawing on the screen in Pygame as being like painting on a wall or a
canvas.  When we start painting on a surface, we want to make sure the canvas is
clear and uniform.  If our canvas already had drawings on it and we wanted to
start over, perhaps we could paint over the existing drawings using one
background color.  That is what we accomplish in the first line with
`screen.fill(white)`.

Each of the next two lines of code draw a single line using the `green` color on
the `screen` variable we created earlier.  The `pygame.draw.line` function
accepts five arguments.  The first is the `screen`.  The next is the color.  The
third and fourth arguments are lists, each of which represents a point on the
screen.  The points are the ends of the line segment we wish to draw.  Each list
is of the form `[X, Y]` where `X` is the x-coordinate and `Y` is the
y-coordinate.  However, the x's and y's work a little differently than what you
might be used to in past mathematics courses or other experiences in life.

FIXME Figure here showing x's getting larger as we go down from the origin point

```python
pygame.display.flip()
clock.tick(20)
```

```python
pygame.quit()
```


## Objects and Classes
\label{sec:objects_and_classes}

## Pygame Sprites
\label{sec:sprites}
