types = {
  "comum": [
    "nome",
    "sobrenome",
    "titulo",
    "ano"
  ],
  "livro": [
    "edicao", 
    "local", 
    "editora", 
  ],
  "capitulo": [
    "sobrenome_livro", 
    "nome_livro", 
    "titulo_livro", 
    "edição", 
    "local",
    "pagina",
  ],
  "artigo": [
    "nome_revista", 
    "local", 
    "volume", 
    "numero", 
    "mes",
    "pagina",
  ]
}

while True:

  selectedType = input("Insira o tipo de citação desejada: ")
  citation = dict()
  
  if selectedType in types:
    for campo in types["comum"]:
      citation[campo] = input(f"Insira {campo}: ")
    
    for campo in types[selectedType]:
      citation[campo] = input(f"Insira {campo}: ")
    
    # SOBRENOME, Nome. Título da obra. Edição. Cidade:  Editora, Ano de Publicação.
    if selectedType == "livro":
      print("{sobrenome}, {nome}. {titulo}. {edicao}. {local}: {editora}, {ano}".format(
        sobrenome = citation["sobrenome"], 
        nome = citation["nome"], 
        titulo = citation["titulo"], 
        edicao = citation["edicao"], 
        local = citation["local"], 
        editora = citation["editora"], 
        ano = citation["ano"]
      ))

    if selectedType == "capitulo":
      print("{sobrenome}, {nome}. {titulo}. In: {sobrenome_livro}, {nome_livro}. {titulo_livro}. {edicao}. {local}: {editora}, {ano}, {pagina}".format(
        sobrenome = citation["sobrenome"], 
        nome = citation["nome"], 
        titulo = citation["titulo"], 
        sobrenome_livro = citation["sobrenome_livro"],
        nome_livro = citation["nome_livro"],
        titulo_livro = citation["titulo_livro"],
        edicao = citation["edicao"], 
        local = citation["local"], 
        editora = citation["editora"], 
        ano = citation["ano"],
        pagina = citation["pagina"]
      ))

    if selectedType == "artigo":
      print("{sobrenome}, {nome}. {titulo}. {nome_revista}, {local}, v. {volume}, n. {numero}, p. {pagina}, {mes}. {ano}".format(
        sobrenome = citation["sobrenome"], 
        nome = citation["nome"], 
        titulo = citation["titulo"], 
        nome_revista = citation["nome_revista"],
        local = citation["local"], 
        volume = citation["volume"], 
        numero = citation["numero"], 
        pagina = citation["pagina"],
        mes = citation["mes"],
        ano = citation["ano"],
      ))
    
    
  else:
    print("\n**Selecione um tipo válido**")
  
  print("\n")