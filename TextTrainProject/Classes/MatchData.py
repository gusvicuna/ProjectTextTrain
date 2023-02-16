class MatchData:
    
    matchWords100 = False
    matchWords75 = False
    matchedCharsPercent = 0
    totalChars = 0
    
    def __init__(self, totalWords:int, matchedWords:int, totalChars:int, matchedChars:int) -> None:
        self.matchedCharsPercent = round(100 * matchedChars / totalChars)
        self.matchWords75 = 100 * matchedWords / totalWords >= 75
        self.matchWords100 = 100 * matchedWords / totalWords == 100
        self.totalChars = totalChars
    
    def __str__(self) -> str:
        return f"100:{self.matchWords100} 75:{self.matchWords75} percent:{self.matchedCharsPercent} totalchars:{self.totalChars}"