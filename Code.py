def Coding(phrase):

    # 1 Строка в двоичном представлении
    ASCII_array = [ord(x) for x in phrase]
    bin_str = [bin(x)[2:] for x in ASCII_array]

    # 2 "Выравниваем" длину элементов двоичного массива
    for i in range(len(bin_str)):
        if len(bin_str[i]) < 11:
            null_count = '0' * (11 - len(bin_str[i]))
            bin_str[i] = null_count + bin_str[i]

    # Создание массива из нулевых векторов
    cod = ['000000000000000'] * len(bin_str)

    # Кодирование
    for i in range(len(bin_str)):
        ind = 0
        for j in range(len(cod[0])): # начинается с нуля
            if j != 7 and j != 11 and j != 13 and j != 14:
                cod[i] = cod[i][:j] + bin_str[i][ind:ind+1] + cod[i][j+1:]
                ind += 1
        # Характеристические уравнения
        # 1
        if (int(cod[i][12:13]) + int(cod[i][10:11]) + int(cod[i][8:9]) + int(cod[i][6:7]) + int(cod[i][4:5]) + int(cod[i][2:3]) + int(cod[i][:1])) % 2 != 0:
            cod[i] = cod[i][:14] + '1'
        # 2
        if (int(cod[i][12:13]) + int(cod[i][9:10]) + int(cod[i][8:9]) + int(cod[i][5:6]) + int(cod[i][4:5]) + int(cod[i][1:2]) + int(cod[i][:1])) % 2 != 0:
            cod[i] = cod[i][:13] + '1' + cod[i][14:]
        # 4
        if (int(cod[i][10:11]) + int(cod[i][9:10]) + int(cod[i][8:9]) + int(cod[i][3:4]) + int(cod[i][2:3]) + int(cod[i][1:2]) + int(cod[i][:1])) % 2 != 0:
            cod[i] = cod[i][:11] + '1' + cod[i][12:]
        # 8
        if (int(cod[i][6:7]) + int(cod[i][5:6]) + int(cod[i][4:5]) + int(cod[i][3:4]) + int(cod[i][2:3]) + int(cod[i][1:2]) + int(cod[i][:1])) % 2 != 0:
            cod[i] = cod[i][:7] + '1' + cod[i][8:]
    Codir_str = ' '.join(cod)
    return Codir_str

def Decoding(cod):

    # Формирование транспонированной матрицы Н
    H_mass = [bin(x)[2:] for x in range(1, 16)]
    for i in range(len(H_mass)):
        if len(H_mass[i]) < 4:
            null_count = '0'*(4 - len(H_mass[i]))
            H_mass[i] = null_count + H_mass[i]
    H_mass.reverse()

    # Исключения
    str_cod = cod.split()
    for i in range(len(str_cod)):
        if len(str_cod[i]) != 15:
            return 'Длина одного из закодированных символов некорректна'
        for j in str_cod[i]:
            if j != '1' and j != '0':
                return 'В записи присутствуют недопустимые символы'

    # Исправление ошибки и декодирование
    dec_mass = []

    for i in range(len(str_cod)):
        sindrom = []
        summ_mass = []

        # Выбор строк тр. Н для суммирования
        for j in range(len(str_cod[0])):
            if str_cod[i][j:j+1] == '1':
                summ_mass.append(H_mass[j])

        # Суммирование и нахождение места ошибки
        for j in range(4):
            summ = 0
            for k in range(len(summ_mass)):
                summ += int(summ_mass[k][j:j+1])
            if summ % 2 == 0:
                sindrom.append('0')
            else:
                sindrom.append('1')

        # Место ошибки в 10-ой системе счисления
        sindrom = int(''.join(sindrom), 2)

        # Исправление
        if sindrom != 0:
            if str_cod[i][ - sindrom: - sindrom + 1] == '1':
                str_cod[i] = str_cod[i][: - sindrom] + '0' + str_cod[i][ - sindrom + 1:]
            else:
                str_cod[i] = str_cod[i][: - sindrom] + '1' + str_cod[i][- sindrom + 1:]

        # Декодирование
        dec = str_cod[i][:7] + str_cod[i][8:11] + str_cod[i][12:13]
        dec_mass.append(dec)

    # Из 2-ой в символы ASCII
    Ten_str = [int(x,2) for x in dec_mass]
    ASCII_str = ''.join([chr(x) for x in Ten_str])
    return ASCII_str