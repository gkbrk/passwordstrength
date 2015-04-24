"""
This script will use passwordstrength module for testing purposes.
"""
import random
import string
import sys
import os

sys.path.append(os.path.join(os.pardir, "passwordstrength"))

import passwordstrength

def random_pass():
    """Random password generator function."""
    charset = string.lowercase + string.uppercase + \
              string.digits + string.punctuation
    
    password = ""
    
    for i in range(random.randint(5,13)):
        password += str(random.choice(charset))
    
    return password

for i in range(15):
    password = random_pass()
    score = passwordstrength.passwordstrength(password).get_score()
    print "The password '%s' got the score %s" % (password, score)
