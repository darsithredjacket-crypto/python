class reversestring:
    def __init__(self,text):
        self.text=text
    
    def reverse_words(self):
        words=self.text.split()
        words.reverse()
        return"".join(words)
s=reversestring("python is easy to learn")
print(s.reverse_words())