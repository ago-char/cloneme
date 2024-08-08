from ftplib import FTP

ftp = FTP("172.23.174.40", "doctor", "doctr")
print(ftp.quit())
