"""
paswordstrength module can be used to get a password strength score of a string. It is based on various rules which are similar to those found in Wolfram Alpha.
"""

import string

class passwordstrength:
    def __init__(self, password):
        self.password = password
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
    
    def __lenght_score(self):
        return len(self.password) * 4 #The way WA works.
    
    def __lower_upper_case_score(self):
        #This will return the number of upper and lower case characters if at least one of each is available.
        lower_score = 0
        for char in self.password:
            if char in string.lowercase:
                lower_score += 1
        
        upper_score = 0
        for char in self.password:
            if char in string.uppercase:
                upper_score += 1
        
        if lower_score and upper_score:
            return lower_score + upper_score
        else:
            return 0
    
    def __digits_score(self):
        score = 0
        for char in self.password:
            if char in string.digits:
                score += 1
        return score * 4 #The way WA works.
    
    def __special_score(self):
        score = 0
        for char in self.password:
            if char in string.punctuation:
                score += 1
        return score * 6 #The way WA works.
    
    def __letters_only_score(self):
        for char in self.password:
            if not str(char).lower() in string.lowercase:
                return 0 #If it contains something else than letters, don't affect the score.
        return -5 #If it only contains letters, decrease the score by 5.
    
    def __numbers_only_score(self):
        for char in self.password:
            if not char in string.digits:
                return 0 #If it contains something else than numbers, don't affect the score.
        return -5 #If it only contains numbers, decrease the score by 5.
    
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
        dict_words = []
        dict_words.append("hello")
        dict_words.append("world")
        dict_words.append("how")
        dict_words.append("are")
        dict_words.append("you")
        dict_words.append("doing")
        
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
