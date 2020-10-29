import json
import os
import time
import sys
import requests


def jsonparse(jsonfile, rootfn):
    with open(jsonfile) as jf:
        data = json.load(jf)
        logfile = os.getcwd() + "\\" + rootfn + "\\" + "logfile.txt"
        if "channel" in data:
            filename = data["channel"]["name"]
            pathtofile = os.getcwd() + "\\" + rootfn + "\\" + filename
            dircreate(pathtofile, filename)

        if "messages" in data:
            count = 0
            for i in data["messages"]:
                if "content" in i:
                    if "http" in i["content"]:
                        if "png" in i["content"] \
                                or "gif" in i["content"] \
                                or "zip" in i["content"]\
                                or "pdf" in i["content"] \
                                or "jpeg" in i["content"] \
                                or "jpg" in i["content"] \
                                or "mp4" in i["content"]:
                            try:
                                name = data["channel"]["name"]
                                if "png" in i["content"]:
                                    fwrite = pathtofile + "\\" + \
                                        name + (str)(count) + ".png"
                                if "jpeg" in i["content"]:
                                    fwrite = pathtofile + "\\" + \
                                        name + (str)(count) + ".jpeg"
                                elif "gif" in i["content"]:
                                    fwrite = pathtofile + "\\" + \
                                        name + (str)(count) + ".gif"
                                elif "zip" in i["content"]:
                                    fwrite = pathtofile + "\\" + \
                                        name + (str)(count) + ".zip"
                                elif "pdf" in i["content"]:
                                    fwrite = pathtofile + "\\" + \
                                        name + (str)(count) + ".pdf"

                                with open(fwrite, 'wb') as f:
                                    f.write(requests.get(i["content"], allow_redirects=True).content)
                                f.close()

                                with open(logfile, 'a') as f:
                                    f.write("downloading " + i["content"] + " storing in: " + fwrite + "\n")
                                f.close()

                                count += 1
                            except:
                                with open(logfile, 'a') as f:
                                    f.write("FAILED  " + i["content"] + " : " + fwrite +  "\n")
                                f.close()

                elif "attachments" in i:
                    if "url" in i["attachments"]:
                        if "http" in i["attachments"]["url"]:
                            if "png" in i["attachments"]["url"] \
                                    or "gif" in i["attachments"]["url"] \
                                    or "zip" in i["attachments"]["url"] \
                                    or "pdf" in i["attachments"]["url"] \
                                    or "jpeg" in i["attachments"]["url"] \
                                    or "jpg" in i["attachments"]["url"] \
                                    or "mp4" in i["attachments"]["url"]:
                                try:
                                    name = data["attachments"]["filename"]
                                    if "png" in i["attachments"]["url"]:
                                        fwrite = pathtofile + "\\" + \
                                            name + (str)(count) + ".png"
                                    if "jpeg" in i["attachments"]["url"]:
                                        fwrite = pathtofile + "\\" + \
                                            name + (str)(count) + ".jpeg"
                                    elif "gif" in i["attachments"]["url"]:
                                        fwrite = pathtofile + "\\" + \
                                            name + (str)(count) + ".gif"
                                    elif "zip" in i["attachments"]["url"]:
                                        fwrite = pathtofile + "\\" + \
                                            name + (str)(count) + ".zip"
                                    elif "pdf" in i["attachments"]["url"]:
                                        fwrite = pathtofile + "\\" + \
                                            name + (str)(count) + ".pdf"

                                    with open(fwrite, 'wb') as f:
                                        f.write(requests.get(i["attachments"]["url"], allow_redirects=True).content)
                                    f.close()

                                    with open(logfile, 'a') as f:
                                        f.write("downloading " + i["attachments"]["url"] + " storing in: " + fwrite + "\n")
                                    f.close()

                                    count += 1
                                except:
                                    with open(logfile, 'a') as f:
                                        f.write("FAILED  " + i["attachments"]["url"] + " : " + fwrite +   "\n")
                                    f.close()


def dircreate(pathtofile, filename):
    if(not os.path.exists(pathtofile)):
        print(filename, " folder created")
        os.mkdir(pathtofile)

if(len(sys.argv) == 3):
    print("Usage: python downloader.py <Json Folder Name> <new Folder Name>")
    sys.exit()

os.chdir(sys.argv[1])
cwd = os.getcwd()

filename = sys.argv[2]
filepath = "\\" + filename
pathtoroot = os.path.join(os.getcwd() + filepath)
print(pathtoroot)
dircreate(pathtoroot, filename)

path = os.listdir()
test = path[0]

for i in path:
    jsonparse(i, filename)
