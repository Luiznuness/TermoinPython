class Termo:
    def __init__(self, palavraAleatoria, palavraUsuario):
        self.list_result = []
        self.win = 0
        self.palavraAleatoria = palavraAleatoria
        self.palavraUsuario = palavraUsuario

        self.main()

        if self.win == 5:
            self.placar = 'Win'
        else:
            self.placar = 'Lose'
    
    def main(self):
        self.loop()
        self.mostrar_resultado()

    def loop(self):
        """
        No Termo eu preciso fazer 3 expecificações simples:

        Verificar se a letra está no indice correto.
            Nesas verificação só podemos ter um retorno:
                Verde: Tem dentro da palavra e está no indice correto.
        Verificar se a letra tem dentro da palavra.
            Nessa verificação teriamos 2 tipos de retornos:
                Amarelo: Tem na palavra mas não está no indice correto.
                Cinza: Não tem na palavra.
        """

        # Loop entre as letras que contem a palavra digitada pelo usúario
        for indiceLetra, letra in enumerate(self.palavraUsuario):
            quant_values_letter = self.quantityLetters(letra)
            self.verify(letra, indiceLetra, quant_values_letter)
    
    def mostrar_resultado(self):
        for index, valeu in enumerate(self.list_result):
            if valeu == 'Verde':
                print(f'{"\033[32m"}{self.palavraUsuario[index]}{'\033[0m'}', end=' ') # Verde
            elif valeu == 'Amarelo':
                print(f'{'\033[93m'}{self.palavraUsuario[index]}{'\033[0m'}', end=' ') # Amarelo
            else:
                print(f'{'\033[90m'}{self.palavraUsuario[index]}{'\033[0m'}', end=' ') # Cinza

    def quantityLetters(self, typedLetter):
        countTotal = 0
        for count in self.palavraAleatoria:
            if count == typedLetter: countTotal += 1
        return countTotal
    
    def verify_true(self, letter, quant_values_letter):
        quant_true = 0
        for indece, typed in enumerate(self.palavraUsuario):
            if letter == typed:
                if len(self.list_result) > indece:
                    if self.list_result[indece] == 'Verde':
                        quant_true += 1
        if quant_true == quant_values_letter:
            return True
        else:
            return False
    
    def verify(self, letter, index, quant_values_letter):
        if len(self.list_result) != 0:
            for indece, typed in enumerate(self.palavraUsuario):
                if letter == typed:
                    if not self.verify_true(letter, quant_values_letter):
                        if len(self.list_result) > indece:
                            if self.list_result[indece] == 'Amarelo':
                                self.list_result[indece] = 'Cinza'
                                break
                    elif self.verify_true(letter, quant_values_letter):
                        break
            if not self.verify_true(letter, quant_values_letter):
                
                result = self.checkPosition(index, letter)
                if result:
                    self.win += 1
                    self.list_result.append('Verde') # Verde
                else:
                    self.list_result.append('Amarelo') # Amarelo
            else:
                self.list_result.append('Cinza') # Cinza
        else:
            if letter in self.palavraAleatoria:
                if self.checkPosition(index, letter):
                    self.win += 1
                    self.list_result.append('Verde') # Verde
                else:
                    self.list_result.append('Amarelo') # Amarelo
            else:
                self.list_result.append('Cinza') # Cinza


    def checkPosition(self, indexTyped, letterTyped):
        for index, random in enumerate(self.palavraAleatoria):
            if letterTyped == random and index == indexTyped:
                return True
        return False

if __name__ == "__main__":
    Termo = Termo()