
def FIND_BIRTHDAY(format):
    filetxt = open("Birthday_data.txt")

    data = filetxt.readlines()

    def searchName(format,text):
        string = format
        # reversing words in a given string
        s = string.split()[::-1]
        l = []
        for i in s:
            # apending reversed words to l
            l.append(i)
        # printing reverse words
        r_name=" ".join(l)
        index = text.find(format)
        index2 = text.find(r_name)
        if (index >=0):
            return 1
        elif(index2>=0) :
            return 1
        else:
            return 0

    found = []
    for i in data:
        if (searchName(format,i)):
            key = i
            found.append(key)
        else:
            key = "UNKNOWN"
            continue
    key = key.strip()
    return found

# print(FIND_BIRTHDAY(format=format))