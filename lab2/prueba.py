import requests

mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
mail_split = mail.json()[0].split("@")
print(mail_split)
contenido = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+mail_split[0]+"&domain="+mail_split[1])
print(contenido.json())