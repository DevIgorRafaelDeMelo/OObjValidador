class ValidationLogin:
    def __init__(self, name, prymaryKey, secundaryKey):
        self._name = name
        self._prymaryKey = prymaryKey
        self._secundaryKey = secundaryKey
        self._Validador = False
        self._upercase = False
        self.validationPass()

    def validationPass(self):
        for letra in self._name:
            if letra.isupper():
                self._upercase = True

        if self._prymaryKey != self._secundaryKey:
            print("Senha são incompativeis !!!")
            return False

        if len(self._name) <= 5:
            print("Login deve conter mais de 5 Caracteres !!!")
            return False

        if len(self._prymaryKey) <= 7:
            print("Senha deve contar mais de 7 Caracteres !!!")
            return False

        if self._prymaryKey.isalnum():
            print("Senha deve conter pelo menos 1 caracter Especial !!!")
            return False

        if not self._upercase:
            print("Senha deve conter pelo menos uam Letra Maiuscula !!!")
            return False

        self._Validador = True and self._upercase

    def __str__(self):
        return f'O Usuario de login {self._name} a Senha Validada como: {self._Validador}'


# console
while (True):
    print("*********************************************")
    print("Validador de login")
    print("Seu login deve conter 1 letra Maiuscula e 6 digitos, o password devera conter 8 digitos e 1 caracter Especial, caso contrario sue login não Validara !!!")
    print("*********************************************")

    Login = str(input("Digite seu login :"))
    Psw1 = str(input("Diite sua senha :"))
    Psw2 = str(input("Repita sua senha :"))

    conta = ValidationLogin(Login, Psw1, Psw2)

    Lista_de_Contas = []

    Lista_de_Contas.append(conta)

    for Usuarios in Lista_de_Contas:
        print(Usuarios)
