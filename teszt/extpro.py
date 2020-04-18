
#if  check in "Where" or check in "Who" or check in "When" :
def textpro(text):
    out_text = text.capitalize()
    print(out_text.split(" ") [0])
    check = out_text.split(" ") [0]

    if  check in ["Where", "Who", "When"] :
       out_text =  out_text + "?"
    else:
       out_text =  out_text + "."

    return  out_text

s = input("kerem a szoveget :")

print(textpro(s))