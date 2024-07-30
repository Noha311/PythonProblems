# # ------------------------
# # -- Function Recursion --
# # ------------------------
# # ---------------------------------------------------------------------
# # -- To Understand Recursion, You Need to First Understand Recursion --
# # ---------------------------------------------------------------------

# # Test Word [ WWWoooorrrldd ] # print(x[1:])

# def cleanWord(word):

#   if len(word) == 1:

#     return word

#   print(f"Print Start Function {word}")

#   if word[0] == word[1]:

#     print(f"Print Before Condition {word}")

#     return cleanWord(word[1:])

#   print(f"Print Before Return {word}")

#   return word[0] + cleanWord(word[1:])

#   # Stash [ World ]

# print(cleanWord("WWWoooorrrldd"))
def clean_repeated(text):
    if len(text) == 1:
        return text
    else:
        if text[0] == text[1]:
            return (clean_repeated(text[1:]))
        else:
            return(text[0]+clean_repeated(text[1:]))
print(clean_repeated("nnohhaa"))