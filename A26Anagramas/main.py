def saoAnagramas(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    if len(str1) != len(str2):
        return False

    str1Sorted = "".join(sorted(str1))
    str2Sorted = "".join(sorted(str2))

    return str1Sorted == str2Sorted


print("---------------------------------")
str1 = input("  Digite a primeira string:     ")
print("---------------------------------")

print("---------------------------------")
str2 = input("  Digite a segunda string:      ")
print("---------------------------------")

if saoAnagramas(str1, str2):
    print("---------------------------------")
    print("| As strings são anagramas!     |")
    print("---------------------------------")
else:
    print("---------------------------------")
    print("| As strings não são anagramas! |")
    print("---------------------------------")
