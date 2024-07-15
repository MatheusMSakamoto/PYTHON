def invert_text(text):
    text_list = list(text)
    text_list.reverse()
    text_reverso_str = "".join(text_list)
    print(text_reverso_str)
text = input("Digite o texto que deseja ver invertido: ")

invert_text(text)