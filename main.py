while (expression := input()):
    try:
        res = eval(expression)
        print(expression + ' = ' + str(res))
    except Exception as error:
        print(error)
    