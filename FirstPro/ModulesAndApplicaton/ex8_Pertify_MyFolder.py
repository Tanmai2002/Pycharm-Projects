#Used to arrange the files
#func(path,fileContaingNamesOfFilesNotToBeTouched,extensionToBeArragenedINNumericalOrder)
#otherfilesfirstLetterISCapitalised
def petrify(path,exclusionfiles,extensionTobrNumbered):
    import os
    try:
        os.chdir(path)
    except :
        print("Error in path")
        return
    l=os.listdir()
    with open(exclusionfiles) as f:
        exclusion=str.split(f.read(),"\n")
    l=list(filter(lambda x:checkExclusions(x,exclusion),l))
    l2=list(map(lambda x:os.rename(x,str.capitalize(x)),l))
    i=1
    print(l)
    for item in l:
        if str(item).__contains__(f".{extensionTobrNumbered}"):
            os.rename(str(item).capitalize(),f"{i}.{extensionTobrNumbered}")
            i=i+1





def checkExclusions(lisElement,exclusions):
    for ele in exclusions:
        if str(lisElement).__contains__(ele):
            return False
    return True


petrify("C:\\Users\\Tanmai\\PycharmProjects\\FirstPro\\ModulesAndApplicaton\\Test",
        "C:\\Users\\Tanmai\\PycharmProjects\\FirstPro\\Basics\\text.txt",
        "txt")








