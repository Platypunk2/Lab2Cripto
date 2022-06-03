import requests
import json

def generateEmail():
    url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
    response = requests.get(url)
    data = json.loads(response.text)
    return data[0]

def readMails(mail):
    user = mail.split('@')[0]
    domain = mail.split('@')[1]
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def readMail(mail,id):
    user = mail.split('@')[0]
    domain = mail.split('@')[1]
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={id}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def ObenterBodyMail(email, num):
    id = readMails(email)[num]['id']
    return readMail(email,id)['body'] 

def ObtenerLinkCL(email):
    text = ObenterBodyMail(email,0)
    lo = text.find("target=")-2
    li = text.find("https://www.pclinkstore.cl/customer/password/")
    return text[li:lo]

def ObtenerLinkES(email):
    text = ObenterBodyMail(email,0)
    li = text.find("text-align:center;border-radius:0;")+45
    lo = text.find("padding:0 20px 0 20px;background-color:#007d1e")-40
    return text[li:lo]

#print(ObtenerLinkCL("3lm1053@vddaz.com"))


#https://www.1secmail.com/api/