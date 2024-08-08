from ftplib import FTP


# signin function
def signin(user, password):
    try:
        result_login = ftp.login(user, password)
        if result_login:
            return result_login
    except Exception as e:
        print(e)


# server host to connect to
server = "172.23.174.40"
uname = "doctor"
pword = "docto"

passwordList = ["root", "doctor", "tryhackme"]

# making ftp connection to server pc
ftp = FTP(server)

res_login = signin(uname, pword)

if res_login:
    print("......................")
    # list dir
    res_dir = ftp.retrlines("LIST")
    print(res_dir)
    print("......................")
    # close conn
    res_close = ftp.quit()
    print(res_close)
    print("......................")

print("How is the josh")
