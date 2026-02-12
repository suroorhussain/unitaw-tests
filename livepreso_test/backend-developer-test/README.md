Please don’t fork this repo using GitHub. It makes it very easy for the next
person to copy your answers! Instead, clone it (see below) and, if you want to
ship it back to us using GitHub, add and push to a new remote.

# Summary

This is a job application project. Our aim is that it won't take too much of
your time, while still allowing you to demonstrate how great you are.

# Your goal

Your goal is to make the tests in this project pass. You can do this by writing
code in `titanic.py` to read a CSV and produce some summary values from it.

We've written test cases to check these values, but since you haven't written
any code yet, those tests are failing. Once all the tests are passing, you're
done.

You can run the test suite by running `pytest` once your dependencies are
installed (see below).

# Getting set up

Please don’t fork this repo using GitHub. It makes it very easy for the next
person to copy your answers! Instead, clone it as described below and, if you
want to ship it back to us using GitHub, add and push to a new remote.

You’ll need Python 3 on your system. Then, clone the repo, create a virtual
environment, activate it and install the dependencies like so:

```
$ git clone https://github.com/LivePreso/backend-developer-test.git livepreso-backend-developer-test
$ cd livepreso-backend-developer-test
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements
```

If you already know what you’re doing and have a different approach (poetry,
pyenv, ...) to the above, do what works best for you.

You can now check your setup is OK by running `pytest`. You should see some
failing tests, which is expected until you’ve written the code to make them
pass. If pytest fails to run any tests, it’s not quite working yet.

# Getting the work back to us

Use one or more commits to record your work as though this were a real project.
Push it up to somewhere you can link us (e.g. GitHub, GitLab, ...), or you can
make a tarball of the project and email that over instead. Inventive technical
alternatives to delivering the code will be looked upon favourably.

# Different skill levels

If you're new to Python and we've linked you here, do your best and we'll take
it into account. If you know what a particular function needs to do but can't
spell it in Python, write what you're thinking in a comment instead.

On the other hand if you've been doing this a while and find this all a bit
easy, we've included some optional stretch goals (or you can make up your own).

# FAQ

## Are there any rules?

- You can’t change the existing test assertions. You can make changes to
  the way the tests call your functions if you want to arrange things
  differently.
- You need to do the work yourself. Referring to docs or StackOverflow is fine.
- You can’t hard-code the results; they need to be calculated from titanic.csv.

## How about style and formatting?

We’ve included black and flake8 in the requirements because this is how
LivePreso projects look. If you don’t know what these are or prefer an
alternative, that’s fine. We will be looking at readability, not convention.

## What can I change in titanic.py?

We’ve included some stub definitions in this file so it’s clear how to get
started, but you are free to remove those and start again if you prefer. As
long as the tests still pass, you’re good. 

You can make changes to the way the tests call your functions if you want to
arrange things differently.

## Can I use a library?

Yes. Approach this question like you’re doing regular work. We’re not trying to
get you to write a particular algorithm here -- any genuine solution is OK. If
there is an existing package on PyPI or in the standard library which improves
your code please feel free to use it.

## What’s part of the test, and what’s ignored?

We’ll be looking at:

- Your approach to the problem
- Whether it works :)
- Code readability -- we like brief, clear and unsurprising code.
- Comments explaining “why” as necessary. Avoid comments explaining what the code
  already says.
- Logic and/or syntax errors
- Appropriate data structures, if used
- Appropriate algorithms, if used
- How you organised and wrote your commits

# Stretch goals

If you feel this test didn’t really stretch your legs, here are some ideas for
you:

- Use Hypothesis to test any invariants in your code.
- Add type annotations
- Run the tests with GitHub Actions, GitLab CI or equivalent.
- Find which passenger attributes correlate best with survival.
- Analyse the performance of your code.
- Do something totally unrelated but cool.

We recognise having to do a different technical test for each job you apply for
is an imposition on your time, so these are strictly optional.
