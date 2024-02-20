cid = str(input('Em que cidade você nasceu?\n'))
form = cid.strip().title() # tira os espaços e formata o texto
print(form[:5] == 'Santo')
