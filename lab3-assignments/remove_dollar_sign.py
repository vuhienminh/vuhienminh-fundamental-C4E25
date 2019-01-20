
def remove(s):
    new = s.replace("$", "")
    print(new)
    return[s]

# remove("i want $")

string_with_no_dollars = remove("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
