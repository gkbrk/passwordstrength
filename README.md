#Python passwordstrength module#

##What does it do?##

It checks a passwords strength using several rules based on the ones found at [Wolfram Alpha Password Strength Checker](http://www.wolframalpha.com/input/?i=password+strength+of+hell0).

##Aim##

To provide a reliable module for calculating the strength score of a password.

##Installation##

###Using `pip`###

To get the latest source via pip, use

`pip install -e git+https://github.com/gkbrk/passwordstrength.git#egg=passwordstrength`

###From Source###

1. Download and extract this repo
2. Open a Terminal or Command Prompt in this new folder.
3. Enter:

Linux:

    sudo python setup.py install

Windows:

    python setup.py install

##Usage##

In a Python Script:

    import passwordstrength
    
    strength = passwordstrength.passwordstrength("hello-world")
    score = strength.get_score()
    readable_score = strength.get_readable_score()

***

In the Terminal or Command Prompt:

    passwordstrength [-h] [-r] [-v]

optional arguments:

      -h, --help      show this help message and exit
      -r, --readable  Outputs the english score.
      -v, --verbose   Outputs a scoring table.


##Score Calculation Rules##

1. A good length - **Done!**
2. Upper-case letters - **Done!**
3. Lower-case letters - **Done!**
3. Numbers - **Done!**
4. Special Characters - **Done!**
5. Middle numbers or special characters - **Done!**
6. Not letters only - **Done!**
7. Not numbers only - **Done!**
8. No repeating characters - **Done!**
9. No consecutive upper-case letters - **Done!**
10. No consecutive lower-case letters - **Done!**
11. No consecutive numbers - **Done!**
12. No sequential letters - **Done!**
13. No sequential numbers - **Done!**
14. No dictionary words - **Done!**

##To do's##

1. Accept a list of passwords
2. Output a list of passwords + their score