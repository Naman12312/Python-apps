import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
with open("F:\\home pc\\my pandrive data\\ACROBAT-7.0\\don't open its nessesary.txt",'r') as f:
    iff=f.read()
mail.login('subhashhodal808@gmail.com', iff)
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, "ALL")

ids = data[0] # data is a list.
id_list = ids# ids is a space separated string
latest_email_id = id_list[-1] # get the latest

result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

raw_email = data[0] # here's the body, which is raw text of the whole email
# including headers and alternate payloads
print(raw_email)
