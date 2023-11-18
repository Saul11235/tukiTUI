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
def _fitToString(obj,dim):
    strobj=str(obj)
    if len(strobj)==dim: return strobj
    if len(strobj)>dim : 
        pass
    else:
        pass
#-----------------------------------


if __name__=="__main__":
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

    print(editArt(art,dicc))
