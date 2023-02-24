from src.Classes.Aception import Aception
from src.DataBase.database import GetDatabase


def DBtoAceptions():
    aceptions = []
    database = GetDatabase()
    for driver in database:
        for ut in database[driver]:
            for code_word in database[driver][ut]["code_words"]:
                for phrase in database[driver][ut]["phrases"]:
                    aception_text = f"{code_word.lower()} {phrase.lower()}"
                    aception = Aception(aception_text, driver, ut)
                    aceptions.append(aception)
    return aceptions


if __name__ == "__main__":
    DBtoAceptions()
