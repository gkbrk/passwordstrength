"""
paswordstrength module can be used to get a password strength score of a string. It is based on various rules which are similar to those found in Wolfram Alpha.
"""

import string

class passwordstrength:
    def __init__(self, password):
        self.password = password
        self.password_length = len(password)
        
        #Calculating the score
        self.score = 0
        self.score += self.__lenght_score()
        self.score += self.__lower_upper_case_score()
        self.score += self.__digits_score()
        self.score += self.__special_score()
        self.score += self.__letters_only_score()
        self.score += self.__repeating_chars_score()
        self.score += self.__sequential_numbers_score()
        self.score += self.__dictionary_words_score()
    
    def __chars_of_type(self, chartype):
        chartype_count = 0
        for char in self.password:
            if char in chartype:
                chartype_count += 1
        return chartype_count
    
    def __lenght_score(self):
        return self.password_length * 4 #The way WA works.
    
    def __lower_upper_case_score(self):
        #This will return the number of upper and lower case characters if at least one of each is available.
        lower_score = self.__chars_of_type(string.lowercase)        
        upper_score = self.__chars_of_type(string.uppercase)
                
        if lower_score and upper_score:
            return lower_score + upper_score
        else:
            return 0
    
    def __digits_score(self):
        digit_count = self.__chars_of_type(string.digits)
        return digit_count * 4 #The way WA works.
    
    def __special_score(self):
        special_char_count = self.__chars_of_type(string.punctuation)
        return special_char_count * 6 #The way WA works.
    
    def __letters_only_score(self):
        letter_count = self.__chars_of_type(string.lowercase + string.uppercase)
        if self.password_length == letter_count:
            return -self.password_length #If the password is all letters, return the negative form of the password length. The way WA works.
        else:
            return 0 #If the password contains something else than letters, don't affect the score.
    
    def __numbers_only_score(self):
        digit_count = self.__chars_of_type(string.digits)
        if self.password_length == digit_count:
            return -self.password_length #If the password is all numbers, return the negative form of the password length. The way WA works.
        else:
            return 0 #If the password contains something else than numbers, don't affect the score.
    
    def __repeating_chars_score(self):
        repeating_char_count = 0
        for char in self.password:
            if str(char)+str(char) in self.password:
                repeating_char_count += 1
        return -repeating_char_count
    
    def __sequential_numbers_score(self):
        sequential_number_count = 0
        
        for i in xrange(1000):
            if str(i) + str(i + 1) in self.password:
                sequential_number_count += 2
        return -sequential_number_count * 3
    
    def __dictionary_words_score(self):
        dict_words = "Hello world how are you doing".split()
        
        for word in dict_words:
            if word in self.password:
                return -20
        return 0
    
    def get_score(self):
        return self.score
    
    def get_readable_score(self):
        if self.score < 0:
            return "Very weak"
        elif self.score >= 0:
            return "Weak"
        elif self.score >= 30:
            return "OK"
        elif self.score >= 60:
            return "Strong"
        elif self.score >= 80:
            return "Very strong"
