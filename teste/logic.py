def gameLogic(randomWord, wordTyped):
    check = {}
    list_result = []
    dooble_ckeck = {}
    win = 0

    # Faz a contagem da letra existente no randomWord
    def quantityLetters(typedLetter):
        countTotal = 0
        for count in randomWord:
            if count == typedLetter: countTotal += 1
        return countTotal

    # Função para comparar a palavra digitada pelo usuário com a palavra sorteada e a posição
    def checkPosition(indexTyped, letterTyped):
        for index, random in enumerate(randomWord):
            if letterTyped == random and index == indexTyped:
                return True
        return False
    

    def verify_true(letter, quant_values_letter):
        quant_true = 0
        for indece, typed in enumerate(wordTyped):
            if letter == typed:
                if len(list_result) > indece:
                    if list_result[indece] == 'Verde':
                        quant_true += 1
        if quant_true == quant_values_letter:
            return True
        else:
            return False
    
    def verify(letter, win,quant_values_letter):
        replacement = False
        for indece, typed in enumerate(wordTyped):
            if letter == typed:
                if not verify_true(letter, quant_values_letter):
                    if list_result[indece] == 'Amarelo':
                        list_result[indece] = 'Cinza'
                        replacement = True
                        break
                elif verify_true(letter, quant_values_letter):
                    break
        if not verify_true(letter, quant_values_letter):
            if replacement:
                result = checkPosition(index, typed)
                if result:
                    win += 1
                    list_result.append('Verde') # Verde
                else:
                    list_result.append('Amarelo') # Amarelo
        else:
            list_result.append('Cinza') # Cinza

    
    def verify_letter(letter, win, index):
        replacement = False
        for indece, typed in enumerate(wordTyped):
            if letter == typed:
                if not verify_true(letter, quant_values):
                    if list_result[indece] == 'Amarelo':
                        list_result[indece] = 'Cinza'
                        replacement = True
                        break
                elif verify_true(letter, quant_values):
                    break
        if replacement:
            dooble_ckeck[typed][quant_letter] = quant_values - 1
            result = checkPosition(index, typed)
            if result:
                win += 1
                list_result.append('Verde') # Verde
                dooble_ckeck[typed][quant_letter] = quant_values
                if verify_true(letter, quant_values):
                    for indece, typed in enumerate(wordTyped):
                        if typed == letter:
                            if len(list_result) > indece:
                                if list_result[indece] == 'Amarelo':
                                    list_result[indece] = 'Cinza'
            else:
                dooble_ckeck[typed][quant_letter] = quant_values
                list_result.append('Amarelo') # Amarelo

        elif not replacement:
            list_result.append('Cinza')


    # For para palavra digitada pelo usuário
    for index, typed in enumerate(wordTyped):
        if typed in randomWord:
            if typed not in check:
                quant_letter = quantityLetters(typed)
                if quant_letter == 1:
                    result = checkPosition(index, typed)
                    if result:
                        win += 1
                        list_result.append('Verde') # Verde
                        check[typed] = 'Verde'
                    else:
                        list_result.append('Amarelo') # Amarelo
                        check[typed] = 'Amarelo'
                else:
                    if typed in dooble_ckeck:
                        quant_values = dooble_ckeck[typed][quant_letter]
                        if quant_values == quant_letter:
                            verify_letter(typed, win, index)
                        else:
                            dooble_ckeck[typed][quant_letter] = quant_values + 1
                            result = checkPosition(index, typed)
                            if result:
                                win += 1
                                list_result.append('Verde') # Verde
                            else:
                                list_result.append('Amarelo') # Amarelo
                    else:
                        dooble_ckeck[typed] = {quant_letter: 1}
                        result = checkPosition(index, typed)
                        if result:
                            win += 1
                            list_result.append('Verde') # Verde
                        else:
                            list_result.append('Amarelo') # Amarelo
            else:
                verify(typed, win,quant_values_letter=1)
        else:
                list_result.append('Cinza') # Cinza

    for index, valeu in enumerate(list_result):
        if valeu == 'Verde':
            print(f'{"\033[32m"}{wordTyped[index]}{'\033[0m'}', end=' ') # Verde
        elif valeu == 'Amarelo':
            print(f'{'\033[93m'}{wordTyped[index]}{'\033[0m'}', end=' ') # Amarelo
        else:
            print(f'{'\033[90m'}{wordTyped[index]}{'\033[0m'}', end=' ') # Cinza


    if win == 5:
        return 'Win'
    else:
        return 'Lose'
    # False = Amarelo
    # True = Verde
    # None = Cinza
    
"""
print(f'{"\033[32m"}{typed}{'\033[0m'}', end=' ') # Verde
print(f'{'\033[93m'}{typed}{'\033[0m'}', end=' ') # Amarelo
print(f'{'\033[90m'}{typed}{'\033[0m'}', end=' ') # Cinza
"""