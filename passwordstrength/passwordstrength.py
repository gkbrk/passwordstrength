"""
paswordstrength module can be used to get a password strength score of a string. It is based on various rules which are similar to those found in Wolfram Alpha.
"""

#only load it once.
with open('english', 'r') as f:
    words = {word[:-1] for word in f.readlines()}


from argparse import ArgumentParser
import getpass
import string

class passwordstrength:
    def __init__(self, password, verbose=False):
        self.words = words
        self.password = password
        self.password_length = len(password)
        self.verbose = verbose
        if verbose:
            print('                                        count        value\n' + '='*80)
        #Calculating the score
        self.score = 0
        self.score += self.__length_score()
        self.score += self.__lower_upper_case_score()
        self.score += self.__digits_score()
        self.score += self.__special_score()
        self.score += self.__middle_score()
        self.score += self.__letters_only_score()
        self.score += self.__numbers_only_score()
        self.score += self.__repeating_chars_score()
        self.score += self.__consecutive_case_score()
        self.score += self.__sequential_letters_score()
        self.score += self.__sequential_numbers_score()
        self.score += self.__dictionary_words_score()
        self.score += self.__extra_score()
    
    def __table_print(self, title, count, value):
        if self.verbose:
            sign = '+ '
            if value<0:
                sign = '- '
                value *= -1
            print title + ' '*(40-len(title)) + str(count) + ' '*(13-len(str(count))) + sign + str(value)

    def __chars_of_type(self, chartype):
        chartype_count = 0
        for char in self.password:
            if char in chartype:
                chartype_count += 1
        return chartype_count
    
    def __length_score(self):
        self.__table_print('length', self.password_length, self.password_length * 4)
        return self.password_length * 4 #The way WA works.
    
    def __lower_upper_case_score(self):
        #This will return the number of upper and lower case characters if at least one of each is available.
        nUpper = self.__chars_of_type(string.uppercase)
        nLower = self.__chars_of_type(string.lowercase)
        upper_score = 0
        lower_score = 0
        if nUpper:
            upper_score = (self.password_length - nUpper) * 2
        if nLower:
            lower_score = (self.password_length - nLower) * 2
        self.__table_print('upper case letters', nUpper, upper_score)
        self.__table_print('lower case letters', nLower, lower_score)
        if lower_score and upper_score:
            return lower_score + upper_score
        else:
            return 0
    
    def __digits_score(self):
        digit_count = self.__chars_of_type(string.digits)
        self.__table_print('numbers', digit_count, digit_count * 4)
        return digit_count * 4 #The way WA works.
    
    def __special_score(self):
        special_char_count = self.__chars_of_type(string.punctuation)
        self.__table_print('special characters', special_char_count, special_char_count * 6)
        return special_char_count * 6 #The way WA works.

    def __middle_score(self):
        # WA doesn't count special characters in this score (which probably is a mistake), but we will.
        i = 0
        middle_chars_count = 0
        middle_chars = set(string.punctuation + string.digits)
        for char in self.password:
            if i!=0 and i!=self.password_length-1 and char in middle_chars:
                middle_chars_count += 1
            i += 1
        self.__table_print('middle numbers or special characters', middle_chars_count, middle_chars_count * 2)
        return middle_chars_count * 2 #The way WA works
        
    
    def __letters_only_score(self):
        letter_count = self.__chars_of_type(string.lowercase + string.uppercase)
        if self.password_length == letter_count:
            self.__table_print('letters only', 'yes', -self.password_length)
            return -self.password_length #If the password is all letters, return the negative form of the password length. The way WA works.
        else:
            self.__table_print('letters only', 'no', 0)
            return 0 #If the password contains something else than letters, don't affect the score.
    
    def __numbers_only_score(self):
        digit_count = self.__chars_of_type(string.digits)
        if self.password_length == digit_count:
            self.__table_print('numbers only', 'yes', -self.password_length)
            return -self.password_length #If the password is all numbers, return the negative form of the password length. The way WA works.
        else:
            self.__table_print('numbers only', 'no', 0)
            return 0 #If the password contains something else than numbers, don't affect the score.
    
    def __repeating_chars_score(self):
        repeating_char_count = self.password_length - len(set(self.password))
        self.__table_print('repeating characters', repeating_char_count, -repeating_char_count)
        return -repeating_char_count #The way WA works
    
    def __consecutive_case_score(self):
        consecutive_uppers = 0
        consecutive_lowers = 0
        consecutive_numbers = 0
        
        lowers = string.lowercase
        uppers = string.uppercase
        numbers = string.digits

        previous = '*'  #Because an empty string is in all sets, somehow.

        for char in self.password:
            if char in lowers and previous in lowers:
                consecutive_lowers += 1
            elif char in uppers and previous in uppers:
                consecutive_uppers += 1
            elif char in numbers and previous in numbers:
                consecutive_numbers += 1
            previous = char

        self.__table_print('consecutive upper-case letters', consecutive_uppers, -2*(consecutive_uppers))
        self.__table_print('consecutive lower-case letters', consecutive_lowers, -2*(consecutive_lowers))
        self.__table_print('consecutive numbers', consecutive_numbers, -2*(consecutive_numbers))
        
        return -2*(consecutive_uppers) + -2*(consecutive_lowers) + -2*(consecutive_numbers) #The way WA works

    def __sequential_numbers_score(self):
        sequential_number_count = 0
        for i in xrange(1000):
            if str(i) + str(i + 1) in self.password:
                sequential_number_count += 2
        self.__table_print('sequential numbers', sequential_number_count, -sequential_number_count*2)
        return -sequential_number_count * 2

    def __sequential_letters_score(self):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        password = self.password.lower()
        sequential_letter_count = 0
        sequential_indexes = []
        for i in range(len(self.password)-1):
            if password[i] in string.lowercase and password[(i+1)] in string.lowercase:
                if alphabet.index(password[i])+1 == alphabet.index(password[i+1]):
                    sequential_letter_count += 1
                    if i not in sequential_indexes: #If it hasn't been counted yet.
                        sequential_letter_count += 1
                    sequential_indexes += [i, i+1]
        if sequential_letter_count > 2:
            self.__table_print('sequential letters', (sequential_letter_count - 2), -(sequential_letter_count - 2) * 2)
            return -(sequential_letter_count - 2) * 2 #The way WA works
        else:
            self.__table_print('sequential letters', 0, 0)
            return 0

    def __substrings(self, word):
        for i in range(len(word)):
            for j in range(i+3, len(word)+1):
                yield word[i:j]

    def __dictionary_words_score(self):
        #generate all substrings
        password_substrings = self.__substrings(self.password)
        if self.words.intersection(password_substrings):
            self.__table_print('contains dictionary word', 'yes', -20)
            return -20
        else:
            self.__table_print('contains dictionary word', 'no', 0)
            return 0

    def __extra_score(self):
        upper = False
        lower = False
        special = False
        number = False
        if self.password_length >= 8:
            for char in self.password:
                if char in string.uppercase:
                   upper = True
                elif char in string.lowercase:
                    lower = True
                elif char in string.punctuation:
                    special = True
                elif char in string.digits:
                    number = True
            if upper and lower and (special or number):
                self.__table_print('extra criteria', 'yes', 8)
                return 8
        self.__table_print('extra criteria', 'no', 0)
        return 0
    
    def get_score(self):
        return self.score
    
    def get_readable_score(self):
        # this was broken; fixed. :)
        if self.score < 0:
            return 'Very weak'
        elif self.score in range(0, 30):
            return 'Weak'
        elif self.score in range(30, 60):
            return 'OK'
        elif self.score in range(60, 80):
            return 'Strong'
        elif self.score >= 80:
            return 'Very strong'

def main():
    ap = ArgumentParser(description='Checks the strength of a password.')
    ap.add_argument('-r', '--readable', action='store_true',
                    help="Outputs the english score.")
    ap.add_argument('-v', '--verbose', action='store_true',
                    help='Outputs a scoring table.')
    args = ap.parse_args()
    
    strength = passwordstrength(getpass.getpass("Password: "), verbose=args.verbose)
    if args.readable:
        print "Score:", strength.get_score()
        print strength.get_readable_score()
    else:
        print "Score:", strength.get_score()

if __name__ == "__main__":
    main()
