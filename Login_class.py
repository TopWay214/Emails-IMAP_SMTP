class Login:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def get_email(self):
        return self.email

    def set_email(self, novo_email):
        self.email = novo_email

    def get_senha(self):
        return self.senha

    def set_senha(self, nova_senha):
        self.senha = nova_senha