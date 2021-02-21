PyTest in all it's glory
========================

For this weeks write-up, I was asked to put a little bit more time into making
PyTest work on my system. For this, I found a great website with a pretty
straight-forward guide on how to get PyTest to work on almost any system
(Linux and Windows). Those Steps are as follows.

What is PyTest
--------------
According to Real Python (https://realpython.com/pytest-python-testing/),
PyTest is a feature-rich, plugin-based ecosystem for testing your Python code.
It is a framework that makes building simple and scalable tests easy. The tests
are easily readable with no need for boilerplate code (sections of code that are
repeated in multiple places with little to no variation)

It utilizes explicit dependency declarations rather than implicit which can lead
to complex code that another user may have to figure out in order to
understand. Pytest utilizes fixtures that create or test doubles or initialize
some system state for the test suite. Any test that wants to use a fixture, must
explicitly accept it as an argument, so dependencies are always stated up front
and are easier to understand.  We don't write code for the computer, yes, a
computer interprets our code, but we write code for other programmers.  They
are the ones who have to read our code. Computers see our code as 0's and 1's,
and then react accordingly. Keeping our code as clean and easily understandable
is crucial.

Is your code growing? Maybe you want to only run a handful of tests, rather
than the hundreds you have created. Well, pytest has your back in the form of
test filtering. Within Pytest, you can utilize name based filtering, directory
scoping, and test categorization.

There are many other features that pytest has that will revolutionize your
testing capabilities, and I would highly recommend doing a little bit of
research on it. It is truly fascinating.

So... On to the good stuff..

How to Install PyTest
---------------------
1. Run the following command in your command line:

.. code-block:: python

   pip install -U pytest

2. Check that you installed the correct version:

.. code-block:: python

   pytest -- version

Create your first test
----------------------
Now that you have pytest installed, you will want to create a simple test
function to ensure everything is working properly. As you read in my Week 2
Write Up, I utilized the code below.

.. code-block:: python
    :linenos:

    def func(x):
        return x + 5

    def test_method():
        assert func(3) == 5

Again, those eagle-eyed programmers out there will point out that this test
will fail because 8 !=5. I did this on purpose so that the test would fail.
Baby steps. If I ran this test, and it fails, I know that pytest is working
and I can easily go back in and adjust my code to be true.

That's it, pytest is not only up and running on your system, but you can now
dive deep into unit testing within Python.  From here, the sky is the limit,
or as Michael Jordan once said "the ceiling is the roof". You can assert that a
certain exception is raised, you can group multiple tests into a class, you can
request a unique temporary directory for functional tests, you can even COMBINE
tests or run a duration report to see what tests could use a little TLC to speed
up the process. there are even a number of plugins available such as
pytest-randomly which can uncover tests that depend on running in specific
order, or pytest-cov which measures how well your tests cover your
implementation code, along with a slew of other plugins. It truly is very
robust.

As you have read above, pytest is not only easy to install, but is very robust
and offers a huge set of features that can filter and optimize your test
scripts. It also offers a very flexible plugin system that adds even more value.

Week 3 Write Up
---------------

This week was interesting to say the least. I met with my professor for my
weekly CAPSTONE meeting on February 3rd for 30 minutes.

As stated above, this week I was tasked with providing details on how to get
pytest to work on your system. It's pretty straightforward and I spent 2:40
researching not only pytest, but also it's capabilities, and most importantly,
how to get it to work.

From there, I spent the vast majority of my time this week trying to get sphinx
and python to work properly as I installed Node.js, and in doing so, I
apparently changed a directory and PyCharm was no longer recognizing that I
even had Python installed on my system. I spent 5:06 troubleshooting the
following error::

    No Python at 'C:\Users\Trent's PC\AppData\Local\Programs\Python\Python39\
    python.exe'

After much Googling, and a lot of YouTube, I finally had to waive the white flag
and reach out to my professor for some help. After attempting to change the
interpreter within PyCharm, I had to resort to uninstalling Python completely
from my system (I had several versions installed). Once I uninstalled Python,
and downloaded and reinstalled Python, everything worked as planned and I was
able to close out this week's write-up and finish.

Finally, I spent 20 minutes cleaning up my write-up and submitting it.

This week was really eye-opening, and also VERY  frustrating as I could not
for the life of me figure out what happened. I honestly still am not 100%
certain what happened, but do know that it was working just fine, then when I
installed Node.js along with Chocolatey that came with it, it quit working.

The only thing I can think of is that while installing those programs for my
Advanced Web Development course at Simpson College, it changed my path for
where I had Python installed and the sphinx template could no longer reference
it.

As I come across more and more of these issues, it's good to know that with
some hard work, and dedication, you can eventually get it figured out and carry
on with your project. Keep your head down, stay focused, and good things will
happen.

Week 3 Time Sheet
-----------------
.. figure:: /images/TrentFulcherTimeSheetWeek3.png
    :alt: Excel Time Sheet
    :class: with-shadow
