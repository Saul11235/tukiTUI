# modulo to edit an ascci art to add info


#-----------------------------

def editArt(originalArt,dicChanges):
    dicChanges=_clearChanges(dicChanges)
    lines=str(originalArt).split("\n")
    first=True
    newArt=""
    for l in lines:
        if first: first=False
        else: newArt+="\n"
        newArt+=_editLineArt(l,dicChanges)
    return newArt

#---------------------------------

def _clearChanges(dicChanges):
    newChanges={}
    for element in dicChanges.keys(): 
        if element!=" " and element!="": newChanges[element]=dicChanges[element][:]
    return newChanges

#-----------------------------------

def _editLineArt(line,dicChanges):
    return line

#-----------------------------------
def fitToString(obj,dim):
    strobj=str(obj)
    if   len(strobj)==dim: return strobj
    elif len(strobj)>dim :return strobj[0:dim]
    else: return strobj+" "*(dim-len(strobj))
#-----------------------------------


if __name__=="__main__":
    print([fitToString(3,13)])
    print([fitToString("holslslsls",13)])
    print([fitToString("abc",13)])
    art=""" 

    ***********
    *         *  AAAAAAAAAAAAAAAAAA .
    *  X   X  *
    *         *  D1D1D1D1D1D1D1D1D1 .
    *  XXXXX  * 
    *         *  F02F02F02F02F02F02 .
    **********

    """

    dicc={"A":"hello world hello",
          "D1":12341243123412341234,
          "F02":True,
          " ": "kdkd"
          }

    #print(editArt(art,dicc))
