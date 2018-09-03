

user, passwd = 'alex', 'abc123'
def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":

                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("User has passed authentication!")
                    return func(*args, **kwargs)
                else:
                    exit("Invalid username or password")
            elif auth_type == "ladp":
                print("bbbbbbbbbbbb")
        return wrapper
    return outer_wrapper
def index():
    print("welcome to index page")
@auth(auth_type = "local")
def home():
    print("welcome to home page")
    return "from home"
@auth(auth_type = "ladp")
def bbs():
    print("welcome to bbs page")

index()
print(home())

bbs()