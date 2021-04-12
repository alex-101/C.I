#CI.py by Alexplazz.
letters = [
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
" ",
",",
".",
"!",
"\"",
"$",
"&",
"+",
"-",
"/",
"#",
"@",
"0",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"?"
]

if input("E/D\n>").lower() == "e":
    # Encode.
    result = []
    text = input(">")
    for x in range(0,len(text)):
        v = text[x]
        ii=0
        for i in letters:
            if i == v.lower():
                result.append(str(ii))
            ii=ii+1
    print(":".join(result))
    print("---------------------")
else:
    text = input(">")
    result = ""
    for x in text.split(":"):
        result=result+letters[int(x)]
    print(result)

input()
exit()
