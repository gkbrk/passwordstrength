#Python passwordstrength module#

##What does it do?##

It checks a passwords strength using several rules based on the ones found at [Wolfram Alpha Password Strength Checker](http://www.wolframalpha.com/input/?i=password+strength+of+hell0).

##Aim##

To provide a reliable module for calculating the strength score of a password.

##Usage##

    import passwordstrength
    print passwordstrength.passwordstrength("hello-world").get_score()

##Methods##

The passwordstrength class has two methods.

1. get_score() - Returns the score of the password.
2. get_readable_score() - Returns one of the strings "Very weak", "Weak", "OK", "Strong" and "Very strong"

##Score Calculation Rules##

1. A good length - **Done!**
2. Upper-case letters - **Done!**
3. Lower-case letters - **Done!**
3. Numbers - **Done!**
4. Special Characters - **Done!**
5. Middle numbers or special characters
6. Not letters only - **Done!**
7. Not numbers only - **Done!**
8. No repeating characters - **Done!**
9. No consecutive upper-case letters
10. No consecutive lower-case letters
11. No consecutive numbers
12. No sequential letters
13. No sequential numbers - **Done!**
14. No dictionary words - **Logic done**, need to add a common password list for good results.

##To do's##

1. Implement more functions
2. Configure
