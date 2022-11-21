# text_file = open(r"C:\Users\daniel.chancir\Desktop\Autoestudio\codember\challenge02\encrypted.txt")
# secret_message = text_file.readline()
# secret_message = secret_message.split(' ')
secret_message = ['115111109111115', '108101103105111110']
for secret_word in secret_message:
    aux_translator = ''
    translated_word = ''
    for token in secret_word:
        aux_translator+= str(token)
        coded_value = int(aux_translator)
        if (coded_value >= 97 and coded_value <= 122):
            translated_word+= chr(coded_value)
            aux_translator = ''
    print(translated_word)