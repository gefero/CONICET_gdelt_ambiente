from newspaper import Article, Config
import pandas as pd
import csv

#%%
#out = pd.read_csv('./data/output/out.csv')
df = pd.read_csv('./data/input/salida_gdelt_gbq_test.csv')

#url =['https://www.diarioregistrado.com/internacionales/joe-biden-se-quedo-dormido-en-plena-cumbre-de-cambio-climatico-y-tuvieron-que-ir-a-despertarlo_a6180356e6859e41994c02a2b', 'https://www.telam.com.ar/notas/202111/574205-compromisos-metas-acuerdo--paris-cop26.html']

#%%
config = Config()
config.language = 'es'


def get_article(link):
    article = Article(url=link)
    article.download()
    article.parse()
    
    text = article.title
    title = article.text
    
    return(title, text)
#%%

articles = [["id", "url", "title", "text"]]

it = 0
for row in df.itertuples():
    it = it + 1
    ntot = str(df.shape[0])
    print('Fila ' + str(it) + ' de ' + ntot)
    url = row.DocumentIdentifier
    GKGID = row.GKGRECORDID
  
    try:
        title, text = get_article(link=url)
        print('\t' + 'OK')
    except:
        title = 'Sin datos'
        text = 'Sin datos'
        print('\t' + 'Error')
    
    articles.append([GKGID, url, title, text])
    
    if it%100 == 0:
        with open("./data/output/out2.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(articles)

#%%

with open("./data/output/out2.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(articles)
    
