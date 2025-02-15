import vlang
import sys

if len(sys.argv) > 1:
    text = f'run("{sys.argv[1]}")'
    result, error = vlang.run("<stdin>", text)
    if error: print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
else:
    while True:
        text = input("vlang> ")
        if text.strip() == "": continue
        result, error = vlang.run("<stdin>", text)

        if error: print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
