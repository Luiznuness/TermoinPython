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

        """ 

            O Jogo termo tem o intuito de gerar uma palavra aleatória e permitir que o usuario digite uma palavra com cinco letras,
            buscando adivinhar a palavra sorteada pelo programa.

            Para cada letra dentro da palavra digitada teremos três possiveis retornos:

            Verde
                A letra do está correta (Indice e Letra).
            
            Amarelo
                A letra do está correta (Letra).

            Vermelho 
                A letra não existe no palavra Aleatória. 
        
        """

        self.loop()
        self.mostrar_resultado()

    def loop(self):

        # Loop entre as letras que contem a palavra digitada pelo usúario
        
        for indiceLetra, letra in enumerate(self.palavraUsuario):
            quant_letras = self.quant_letras(letra)
            self.verifica(letra, indiceLetra, quant_letras)
    
    
    def verifica(self, letra_aleatoria, index_aleatoria, quant_letra):
        """

        Essa Função tem o intuito de verificar a cor de cada letra da palavra digitada pelo usuario.

        Fazemos isso atrás de um IF ELSE, que verifica se contem algum valor na lista 'list_result'.

            Se tiver algum valor dentro da lista ele executa um loop na palavra digitada pelo usuario pegando letra por letra e seu index.
            O intuido desse loop é verificar se a letra que foi recebida já foi entrada e está como 'verde' e se essa mesma letra se entra como
            como 'Amarela' dentro de nossa lista, se tiver alguma letra igual a recebida estiver como 'Amarela' temos que deixar ela como 'Cinza'.

            Depois que ele sai do loop ele cai em outro IF ELSE, onde ele irá verificar se a letra recebida já foi encontrada.
            Se a letra recebida não estiver sido encontrada ela entra no IF onde faremos uma verificação pra saber se a letra é 'Amarela' ou 'Verde'.
            Agora se ela já estiver sido encontrada, temos que pintar a letra recebida como 'Cinza'.

        Se não tiver nenhum valor dentro da lista.
            Faremos uma verificar pra saber se a letra recebida está dentro da palavra aleatória.
            Se ela estiver verificaremos se a letra é 'Amarela' ou 'Verde'.
            Agora se ela não estiver dentro da palavra aleatória temos que pintar a letra de 'Cinza'.
        
        """
        if len(self.list_result) != 0:

            for index_usuario, letra_usuario in enumerate(self.palavraUsuario):
                if letra_aleatoria == letra_usuario:
                    if self.verifica_valores_encontrados(letra_aleatoria, quant_letra):
                        if len(self.list_result) > index_usuario:
                            if self.list_result[index_usuario] == 'Amarelo':
                                self.list_result[index_usuario] = 'Cinza'

            if not self.verifica_valores_encontrados(letra_aleatoria, quant_letra):
                if self.verificar_posicao(index_aleatoria, letra_aleatoria):
                    self.win += 1
                    self.list_result.append('Verde') # Verde
                else:
                    self.list_result.append('Amarelo') # Amarelo
            else:
                self.list_result.append('Cinza') # Cinza
        
        else:
            if letra_aleatoria in self.palavraAleatoria:
                if self.verificar_posicao(index_aleatoria, letra_aleatoria):
                    self.win += 1
                    self.list_result.append('Verde') # Verde
                else:
                    self.list_result.append('Amarelo') # Amarelo
            else:
                self.list_result.append('Cinza') # Cinza


    def verificar_posicao(self, index_usuario, letra_usuario):
        """ 

            Esse função tem o intuido de receber uma letra e se index e verificar se essa letra e esse index são iguais ao que tem na palavra aleatória.

                Se for igual retornamos True.
                Agora se não retornamos False.

        """

        for index_aleatoria, letra_aletoria in enumerate(self.palavraAleatoria):
            if letra_usuario == letra_aletoria and index_aleatoria == index_usuario:
                return True
        return False

    def mostrar_resultado(self):

        """ 
        
            Essa função tem o intuido de imprimir no terminal a palavra digitada pelo usuario e a cor de cada letra seguindo o que foi explicado no inicio.

        """

        for index, valor in enumerate(self.list_result):
            if valor == 'Verde':
                print(f'{"\033[32m"}{self.palavraUsuario[index]}{'\033[0m'}', end=' ') # Verde
            elif valor == 'Amarelo':
                print(f'{'\033[93m'}{self.palavraUsuario[index]}{'\033[0m'}', end=' ') # Amarelo
            else:
                print(f'{'\033[90m'}{self.palavraUsuario[index]}{'\033[0m'}', end=' ') # Cinza

    def quant_letras(self, letra_usuario):

        """ 

            Essa função tem o intuito de retornar quantas vezes a letra recebida aparece na palavra aleatória.

        """

        countTotal = 0
        for count in self.palavraAleatoria:
            if count == letra_usuario: countTotal += 1
        return countTotal
    
    def verifica_valores_encontrados(self, letra, quant_letra):

        """ 

            Essa função tem o intuito de receber uma letra e a quantidade de vezes que ela aparece na palavra aleatória.

            Com isso temos que retornar True se a quantidade de vezes que ela aparece na palavra aleatória está como 'Verde', em suma,
            se a letra recebida estiver como 'Verde' em todas as vezes que ela apareceu na palavra digitada pelo usuário e essas vezes
            forem iguais a quantidade de vezes que ela aparece na palavra aleatória retornamos True.

            Se não retornamos False
        
        """

        quant_valores_letra = 0
        for index_usuario, letra_usuario in enumerate(self.palavraUsuario):
            if letra == letra_usuario:
                if len(self.list_result) > index_usuario:
                    if self.list_result[index_usuario] == 'Verde':
                        quant_valores_letra += 1
        if quant_valores_letra == quant_letra:
            return True
        else:
            return False
        

if __name__ == "__main__":
    palavra_aletoria = 'teste'
    palavra_usuario = 'saebe'

    Termo = Termo(palavraAleatoria=palavra_aletoria, palavraUsuario=palavra_usuario)
    print()