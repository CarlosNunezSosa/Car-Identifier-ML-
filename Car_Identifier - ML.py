from sklearn import tree
import pyttsx3 as py

engine = py.init()
features = []
labels = []


def copy_Data():
    # This def copies the data from the file and passes the data to its specific list
    file = open("Car_IdentifierData")
    for line in file:
        w = int(line[1:line.index(",")])
        s = int(line[line.index(",")+2:line.index("]")])
        features.append([w, s])
    file.close()

    file = open("Car_IdentifierData")
    for line in file:
        s = int(line[line.index("]")+1:])
        labels.append(s)
    file.close()


def identifier():
    # Takes in input in weight(kg) and amount of seats
    weight = int(input("Enter weight (kg) of a vehicle: "))
    seats = int(input("Enter amount of seats of a vehicle: "))

    # Creates classifier and changes the engines voice and rate
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(features, labels)
    engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.setProperty("rate", 150)

    # This if else verifies if the classifier is equal to one or zero and depending on that it
    # gives a certain output
    if classifier.predict([[weight, seats]]) == 1:
        features.append([weight, seats])
        labels.append(1)
        engine.say("The vehicle is a sports/compact car")
        engine.runAndWait()

    else:
        features.append([weight, seats])
        labels.append(0)
        engine.say("The vehicle is an SUV")
        engine.runAndWait()

    # Update the file data so the algorithm grows smarter in the future
    file = open("Car_IdentifierData", "w")
    counter = 0
    for i in features:
        file.write(str(i)+str(labels[counter])+"\n")
        counter = counter + 1

    # Lets you know that the data has been updates and terminates code
    engine.say("Data has been updated")
    engine.runAndWait()
    file.close()
    quit()


copy_Data()
print(" -----------------------------------")
print("|  MACHINE LEARNING CAR IDENTIFIER  |")
print(" -----------------------------------\n")
identifier()

