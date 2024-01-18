#email protocol:
'''
SMTP: send e-mail
POP: read e-mail
IMAP: read e-mail
'''
'''
Before, go to your email account, security, turn on the 2-step verification, click on
2-step verification, go to app passwords, add a name password and copy your passwor to put
in the variable password below.
'''
import smtplib
import email.message
corpo_email = """
    Testando
    """#what you´ll send

msg = email.message.Message()
msg['Subject'] = "Teste"
msg['From'] = 'yours@gmail.com'#put yours
msg['To'] = 'someones@gmail.com'#put someones
password = 'your_password'#put your password
msg.set_payload(corpo_email)


s = smtplib.SMTP('smtp.gmail.com: 587') #lembrando que aqui será adicionado o smtp do gmail,hotmail (cada um possui um diferente)
s.starttls()#security
# Login Credentials for sending the mail
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Verify your e-mail')
s.quit()