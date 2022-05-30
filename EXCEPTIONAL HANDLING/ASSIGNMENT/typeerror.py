#wap which explain typeerror
x="hooooooooooooooooooooooo"
if not type(x) is int:
    print("gla")
    try: #handling the error 
        raise TypeError("only integers are allowed")
    except:
        print("lllll")
