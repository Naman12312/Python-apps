import imaplib
def recieve():
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login("subhashhodal808@gmail.com", input("Password:   "))
    message = imap.select("INBOX")
    # print(message)
    msg = imap.fetch(str(message),"(RFC822)")
    print(msg)
recieve()