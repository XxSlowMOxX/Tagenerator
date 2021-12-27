Übergabe = ["1", "2", "3", "4", "5", '6']

def removeDuplicates(listofElements):
    uniqueList = []
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    return uniqueList

def Primer(Array, H):
    AusgabeRaw1 = []
    Test = Rekursiv([], Array)
    Hilfe = []
    print(Hilfe)
    for i in range(1,H):
        Hilfe = Test
        for thing in Hilfe:
            Test += Rekursiv(thing,Übergabe)
    for Element in Test:
        if len(Element) == H:
            Element.sort()
            AusgabeRaw1 += [Element]
    AusgabeRaw = removeDuplicates(AusgabeRaw1)
    print(AusgabeRaw)

def Rekursiv(Array, BasisArray):
    Ausgabe = []
    for Elemen in BasisArray:
        if (Elemen in Array) == False:
            Ausgabe.append(Array + [Elemen])
    return(Ausgabe)

Primer(Übergabe, 2)
