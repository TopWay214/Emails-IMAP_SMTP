import email
import imaplib
from Login_class import Login


endereco_email = 'caio.cunha@inoveh.com.br'
senha = 'LuIVkcpMTF1y'
servidor = 'mail.inoveh.com.br'

mail = imaplib.IMAP4_SSL(servidor)
mail.login(endereco_email, senha)
mail.select('inbox')

status, data = mail.search(None, 'ALL')
ids = []
for block in data:
    ids = block.split()

for i in ids:
    status, data = mail.fetch(i, '(RFC822)')


for response_part in data:
    # se for a tupla a extraímos o conteúdo
    if isinstance(response_part, tuple):
        # o primeiro elemento da tupla é o cabeçalho
        # de formatação e o segundo elemento possuí o
        # conteúdo que queremos extrair
        message = email.message_from_bytes(response_part[1])

        # com o resultado conseguimos pegar as
        # informações de quem enviou o email e o assunto
        mail_from = message['from']
        mail_subject = message['subject']

        # agora para o texto do email precisamos de um
        # pouco mais de trabalho pois ele pode vir em texto puro
        # ou em multipart, se for texto puro é só ir para o
        # else e extraí-lo do payload, caso contrário temos que
        # separar o que é anexo e extrair somente o texto
        if message.is_multipart():
            mail_content = ''

            # no caso do multipart vem junto com o email
            # anexos e outras versões do mesmo email em
            # diferentes formatos como texto imagem e html
            # para isso vamos andar pelo payload do email
            for part in message.get_payload():
                # se o conteúdo for texto text/plain que é o
                # texto puro nós extraímos
                if part.get_content_type() == 'text/plain':
                    mail_content += part.get_payload()
        else:
            mail_content = message.get_payload()

        print(f'From: {mail_from}')
        print(f'Subject: {mail_subject}')
        print(f'Content: {mail_content}')

        print("Dawsdaweas")