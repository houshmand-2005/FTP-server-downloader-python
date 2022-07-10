from os import path
import wget # pip install wget
import pathlib
import ftplib
print("1.Donwlaod the file from the url")
print("2.Delete the file from the server")
user_ch = input("Enter : ")
server = ftplib.FTP()
server.connect('URL', 8000) # instead of 8000 Enter your port
server.login('User_Name','Password')
server.cwd("/Uploads") # if you need
if user_ch == "1":
    url = input("Enter the URL : ")
    get_yn =input("Are you sure you want to download this file?(y/n) : ")
    if get_yn == "y":
        with open(wget.download(url), "rb") as file:
            server.storbinary('STOR %s' % path.basename(url), file)
        server.dir()
        print("________________File uploaded________________")
        print(f"https://YourURl.com/media/Uploads/{path.basename(url)}")
        print("____________________________________________")
        input("Press Enter to Exit...")
    if get_yn == "n":
        print("File not downloaded")
        input("Press Enter to Exit...")
elif user_ch == "2":
    Url_file = input("Enter the URL : ")
    get_yn =input("Are you sure you want to Delete this file?(y/n) : ")
    if get_yn == "y":
        server.delete(path.basename(Url_file))
    if get_yn == "n":
        print("File not Delete")
        input("Press Enter to Exit...")
