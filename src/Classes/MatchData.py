class MatchData:

    matchedCharsPercent = 0
    matchedWordsPercent = 0
    totalChars = 0

    def __init__(self,
                 matchTrainText,
                 totalWords: int,
                 matchedWords: int,
                 totalChars: int,
                 matchedChars: int) -> None:
        self.matchedCharsPercent = round(100 * matchedChars / totalChars)
        self.matchedWordsPercent = 100 * matchedWords / totalWords
        self.totalChars = totalChars
        self.matchTrainText = matchTrainText

    def __str__(self) -> str:
        return f"100:{self.matchWords100}75:{self.matchWords75}" +\
            f" percent:{self.matchedCharsPercent} totalchars:{self.totalChars}"

    def HasGreaterThan75PercentMatchedWords(self) -> bool:
        return self.matchedWordsPercent >= 75

    def Has100PercentMatchedWords(self) -> bool:
        return self.matchedWordsPercent == 100
