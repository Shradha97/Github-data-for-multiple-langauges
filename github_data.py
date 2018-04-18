import urllib.request, urllib.parse, urllib.error
import json
import ssl

def get_url():
    url = 'https://api.github.com/search/repositories?q=fork:true+language:C&sort=stars&order=desc'
    print('Retrieving', url)
    return url

def write_repo_name(js, repo):
    fp.write("The repository name is: ")
    fp.write(js["items"][repo]["name"])
    fp.write("\n")
    fp.write("The repository url is: ")
    fp.write(js["items"][repo]["html_url"])
    fp.write("\n")
    fp.write("Languages used    ")
    fp.write("Lines of Code\n\n")
    return

def write_language(js):
    for i in js:
        fp.write(i)
        fp.write("      :       ")
        fp.write(str(js[i]))
        fp.write("\n")
    fp.write("\n\n")
    return

def get_languages(count, repos, url):
    while repos < 10:
        while count<2:
            count = count+1
            uh = urllib.request.urlopen(url, context = ctx)
            data = uh.read().decode()

            try:
                js = json.loads(data)
            except:
                js = None

                if not js or 'status' not in js or js['status'] !='OK':
                    print('==== Failure To Retreive')

            if count != 2:
                write_repo_name(js, repos)
                url = js["items"][repos]["languages_url"]

        write_language(js)
        url = get_url()
        count = 0
        repos = repos + 1

##################################################################################################
## MAIN ##

#Ignoring SSL Validation

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
repos = 0

fp = open('github_data1.txt', 'w+')

url = get_url()
get_languages(count, repos, url)

fp.close()
