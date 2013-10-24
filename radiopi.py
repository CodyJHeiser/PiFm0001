import os     #Imports for the OS package
import time   #Imports for the TIME package

print "Please choose a frequency between 87.1 and 108.1"
time.sleep(1)
freq = float(raw_input()) #The frequency that it will play on [float for numbers (float(_))]
if freq <= 87.1 : #Keep the freq less than 87.1
    print "\nPlease keep the frequancy above 87.1"
elif freq >= 108.1 : #Keep the freq more than 108.1
    print "\nPlease keep the frequency below 108.1"
else:
    time.sleep(1)
    print "\nGreat what artist would you like to be played on " + str(freq) +"\n" #Change to string using str(_)
    time.sleep(0.5)
    os.system("ls")#List directories
    artist = raw_input("\nDo not put spaces in the name and capitalize the first letter\n")
print "\nWhat song would you like to be played?\n"
time.sleep(0.5)
os.chdir(artist) #Change directories
    #os.system("pwd") to get the directory (DEBUGGING)
time.sleep(1)
os.system("ls") #List directories
time.sleep(0.5)
print "\nDo not type to ending (.WAV or .wav)"
song = raw_input("Type in all lowercase no spaces\n") #What song will play (No spaces)
print "\n" +artist +" will now play on " + str(freq) +" with the song " +song #confermation of the information
time.sleep(1)
print "If this is correct type \"Yes\" or type \"No\"" 
correct = raw_input()
if correct == "Yes" : #Defalt
    print "Your song will now play on " + str(freq)
    time.sleep(1)
    os.chdir("../") #Go back a directory
    os.system("sudo ./pifm " +artist +"/" +song +".WAV " +str(freq))
    print "Thanks for using Pifm By Cody Heiser"
elif correct == "No" : #If "correct" is No
    print "Please type what is wrong..."
    time.sleep(0.2)
    print "Artist | Song | Frequency" #Troubleshooting multiple choice
    wrong = raw_input()
    if wrong == "Artist" : #Troubleshooting ARTIST
        print "Please enter the name of the artist that you would like to replace"
        time.sleep(0.2)
        os.chdir("../") #Go back a directory
        os.system("ls") #List the directories
        time.sleep(0.3)
        artist = raw_input()
        print "\nWhat song would you like to be played by " +artist +"\n"
        os.chdir(artist)
        os.system("ls") #List the directories
        song = raw_input() #New song input
        time.sleep(0.3)
        print "Your song will now play on " + str(freq)
        time.sleep(1)
        os.chdir("../")
        os.system("sudo ./pifm " +artist +"/" +song +".WAV " + str(freq)) #Transmiting signal
        print "Thanks for using Pifm By Cody Heiser" #Signature
    elif wrong == "Song" : #Troubleshooting SONG
        print "Please enter the name of the song that you would like to replace"
        time.sleep(0.2)
        os.system("ls")
        time.sleep(0.3)
        song = raw_input("Type in all lowercase no spaces\n")
        time.sleep(0.3)
        print "Your song will now play on " + str(freq)
        time.sleep(1)
        os.chdir("../") #Go back a directory
        os.system("sudo ./pifm " +artist +"/" +song +".WAV " +str(freq)) #Transmiting signal
        print "Thanks for using Pifm By Cody Heiser"
    elif wrong == "Frequency" : #Troubleshooting FREQUENCY
        print "Please enter the frequency that you would like to replace"
        time.sleep(0.3)
        freq = float(raw_input())
        time.sleep(0.3)
        print "Your song will now play on " + str(freq)
        time.sleep(1)
        os.chdir("../") #Go back a directory
        os.system("sudo ./pifm " +artist +"/" +song +".WAV " +str(freq)) #Transmiting signal
        print "Thanks for using Pifm By Cody Heiser"
    else: #Troubleshooting UNKNOWN
        print "Sorry I didn't get that"
