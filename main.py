import TextTrainProject

def main():
    textTrain = TextTrainProject.Aception("Juan Soria sabe")
    matches = TextTrainProject.MatchTrainText(textTrain,textTrain)
    for i in matches:
        print(i)
    TextTrainProject.PlotMatchTrain(matches)

if __name__=="__main__":
    main()