class Aception:

    text = ""
    words = []
    characters = []
    wordCount = 0
    charCount = 0

    def __init__(self, text, driver, ut) -> None:
        self.text = text
        self.words = self.SplitIntoWords()
        self.characters = self.SplitIntoCharacters()
        self.wordCount = len(self.words)
        self.charCount = len(self.characters)
        self.driver = driver
        self.ut = ut

    def __str__(self) -> str:
        return f"{self.text}"

    def SplitIntoWords(self):
        return self.text.split(" ")

    def SplitIntoCharacters(self):
        return [*self.text]

    def CountCharactersWithoutSpaces(self) -> int:
        splited_text = [i for i in self.characters if i != " "]
        return len(splited_text)
