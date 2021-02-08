import twint

c = twint.Config()
#termos de pesquisa
c.Search = "Bolsonaro Covid"
#data
c.Since = "2020-03-01"
c.Until = "2020-08-31"
#lingua
c.Lang = "pt"
#salvar em csv
c.Store_csv = True
#nome da pasta (dava pra colocar "/nome do arquivo.csv" tambem)
c.Output = "bolsonaro_pandemia"

#roda a pesquisa com as configurações 
twint.run.Search(c)