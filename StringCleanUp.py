print("="*30 + " WELCOME TO OUR PYTHON JOURNEY " + "="*24)
print("="*30 + " HELLO TO MY 'String Clean Up' " + "="*24)
print("-"*80)
def clean_repeated(text):
    if len(text) == 1:
        return text
    else:
        if text[0] == text[1]:
            return (clean_repeated(text[1:]))
        else:
            return(text[0]+clean_repeated(text[1:]))
word=input("Please Enter the word you want to clean up: ")
print(f"The Word after Cleaning: {clean_repeated(word)} .")