Demo_String = "I love Information retrieval"

#To extract particular character or range of characters from string
print("First character is "+ Demo_String[0])
#To extract retrieval
print("Character at position [19-28] is " +Demo_String[19:28])

#s.find(t) index of first instance of string t inside s (-1 if not found)
print("First Position of Information is ")
print(Demo_String.find("Information"))
      
#s.rfind(t) index of last instance of string t inside s (-1 if not found)
print("Recent position of Information is ")
print(Demo_String.rfind("Information"))
      

#s.split(t) split s into a list wherever a t is found(whitespace by default)
print("Splitting the text from Information gives ")
print(Demo_String.split("Information"))

#s.splitlines() split s into a list of strings, one per line
print("Splitting lines gives")
print(Demo_String.splitlines())

#s.lower() a lowercased version of the string s
print("Lover case of the text is ")
print(Demo_String.lower())

#s.upper() an uppercased version of the string s
print("Uppercase of String is ")
print(Demo_String.upper())

#s.title() a titlecased version of the string s
print("Title case of string is ")
print(Demo_String.title())


#s.replace(t, u) replace instances of t with u inside s
print("Replacing Information by formation gives")
print(Demo_String.replace("Information", "formation"))

