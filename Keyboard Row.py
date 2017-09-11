# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


# American keyboard


# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = {1:set(['q', 'w', 'e', 'r', 't', 'y','u', 'i', 'o', 'p']),
                2:set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']), 
                3:set(['z', 'x', 'c', 'v', 'b' ,'n', 'm'])}
        result=[]
        for word in words:
            base=[i for i,row in rows.items() if word[0].lower() in row]
            for chari in word:
                if chari.lower() not in rows[base[0]]:
                    break
            else:
                result.append(word)
        return result
