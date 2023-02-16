class Aception:
    
    text = ""
    words = []
    characters = []
    wordCount = 0
    charCount = 0
    
    def __init__(self, text) -> None:
        self.text = text
        self.words = self.SplitIntoWords()
        self.characters = self.SplitIntoCharacters()
        self.wordCount = len(self.words)
        self.charCount = len(self.characters)
    
    def __str__(self) -> str:
        return f"{self.text}"
    
    
    def SplitIntoWords(self):
        return self.text.split(" ")
    
    def SplitIntoCharacters(self):
        return [*self.text]
    