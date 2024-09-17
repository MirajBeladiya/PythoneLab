#Real life exampal

class Login_page:

    def __init__(self,email,passward):
        self.email = email
        self.passward = passward
    def login_confirm(self):
        if self.email == "mirajbeladiya@gmail.com" and self.passward == "Miraj123":
            print("Allow to log in")
        else:
            print("Not allow")
email = input("Enter your email\n")
password = input("Enter your pass\n")

object1 = Login_page(email,password)
object1.login_confirm()

