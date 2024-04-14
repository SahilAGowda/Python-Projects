#have a python dictionary that will have key value 
#that represent the word and the definition
#collect the input fro the user 
#print the definition

def main():
    word_dictionary={
        'hi':'a way of greeting',
        'eyes':'an organ for seeing',
        'hello':'a way of saying hello',
        'earth':'a planet where the species lives'        
    }
    while True:
        word =input("Enter any word")
        if word =="":
            break
        if word in word_dictionary:
            print(word,":",word_dictionary[word])

main()

