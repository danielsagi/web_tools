filter(lambda x: __import__("socket").socket().connect_ex(("localhost", x)) == 0, range(8070, 8081))