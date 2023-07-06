ownerID = 4567

def ShowData():
    print("This is the user data")

def Redirect():
    print("Redirecting to the homepage")

def GetUserID():
    return 1234

if not GetUserID() == ownerID:
    print("You are not allowed to view this data")
    Redirect()
else:
    ShowData()
