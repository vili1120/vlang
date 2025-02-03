import vlang

while True:
    text = input("vlang> ")
    result, error = vlang.run("<stdin>", text)

    if error: print(error.as_string())
    else: print(result)
