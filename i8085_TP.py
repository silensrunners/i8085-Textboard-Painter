#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "                                                                                                                                                                         "
print "########################################"
print "### Author : Ixent Gallego Lopez     ###"
print "### Version : 1.0                    ###"
print "### Date : 07/06/15                  ###"
print "### i8085 Textboard Painter          ###"
print "########################################"
print "   "

def acaba():
    return -1

def main():

    #Dictoinary containing all the char-hex relations for the i8085.
    charToHex = {"\n":"5F","^":"5E","":"5F","~":"7E","|":"7C","`":"60",'"':"22","'":"27","\\":"5C","/":"2F","{":"7B","}":"7D","(":"28",")":"29","=":"3D","_":"7E",">":"3E","<":"3C","0":"30","1":"31","2":"32","3":"33","4":"34","5":"35","6":"36","7":"37","8":"38","9":"39","%":"25","�":"A1",":":"3A",";":"3B","+":"2B","-":"2D","*":"2A",".":"2E",",":"2C","@":"40","!":"21","?":"3F","#":"23","$":"24","&":"5F","a":"61","b":"62","c":"63","d":"64","e":"65","f":"66","g":"67","h":"68","i":"69","j":"6A","k":"6B","l":"6C","m":"6D","n":"6E","o":"6F","p":"70","q":"71","r":"72","s":"73","t":"74","u":"75","v":"76","w":"77","x":"78","y":"79","z":"7A","A":"41","B":"42","C":"43","D":"44","E":"45","F":"46","G":"47","H":"48","I":"49","J":"4A","K":"4B","L":"4C","M":"4D","N":"4E","O":"4F","P":"50","Q":"51","R":"52","S":"53","T":"54","U":"55","V":"56","W":"57","X":"58","Y":"59","Z":"5A"," ":"5F"}
    #General variables
    text = []
    trads = []
    maxx = 0
    cont = 1

    fitxer = raw_input("Input file: ")
    nomFx = raw_input("Output name: ")
    complet = ".data E000h \n"
    fx = open(nomFx, 'w')

    #Saving every line of the input file in the 'text' variable (arrayList).
    with open(fitxer) as inputfile:
        for line in inputfile:
            line = line.replace("\r", "") #Removes the carriage returns.
            text.append(line)

    #Adding the '&' symbol at the end of every line in order to mark where's the end of the aforesaid line.
    for i in range(len(text)):
        while len(text[i]) <= 39:
            text[i] = str(text[i]) + "&"

    llarg = len(text)

    #Finding the longuest text line in the input file.
    for elem in text:
        if len(elem) > maxx:
            maxx = len(elem)

    # Checks if the input file surpases the bounds of the i8085 texboard.
    if llarg >= 25 or maxx > 40:
        print "Text surpases the bounds of the screen (i8085)."
        bye = raw_input("ENTER to finish")
        acaba()

    #Converts every line of the input file into a line redeable for the simulator using the dictionary declared.
    for elem in text:
        linia = ""
        i = 0
        for i in range(len(elem)):
            if i < len(elem)-1:
                linia = linia + charToHex[elem[i]] + "h,"
            else:
                linia = linia + charToHex[elem[i]] + "h"
        trads.append(linia)

    aux = 1
    #Concluding the right format of every line.
    for data in trads:
        complet = complet + "    line"+str(aux)+": dB " + str(data) + "\n"
        aux = aux + 1

    #Adding a line which indicates the end of the execution.
    complet = complet + "\n" + "\n" + ".org 50h \n" + "    HLT"
    #Writing the resoult into the output file.
    fx.write(complet)
    fx.close()
    print "File created successfully"
    bye = raw_input("ENTER to finish")

main()
