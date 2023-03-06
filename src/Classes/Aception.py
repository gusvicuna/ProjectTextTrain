class Aception:

    def __init__(self, text=str, driver=str, component=str) -> None:
        self.text = text
        self.driver = driver
        self.component = component

    def __str__(self) -> str:
        return f"{self.text}"

    def Words(self):
        return self.text.split(" ")

    def Characters(self):
        return list(str(self.text))

    def CountCharactersWithoutSpaces(self) -> int:
        splited_text = [i for i in self.Characters() if i != " "]
        return len(splited_text)
