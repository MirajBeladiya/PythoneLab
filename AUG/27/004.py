# Understading the decorator in Python

def add_before_UI_after_UI(func):
    # two parts
    # wrapper&call
    def wrapper():
        print("Before the running UI")
        print("after the running UI")
        func
        print("ABC")
    return wrapper()


@add_before_UI_after_UI
def xyz():
    print("buviu")

xyz
