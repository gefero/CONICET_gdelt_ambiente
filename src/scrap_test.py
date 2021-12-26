from newspaper import Article, Config
import pandas as pd
import csv

#%%
df = pd.read_csv('./data/input/salida_gdelt_gbq_test.csv')

## HACER VARIABLES DE ESTADO... RUTAS DE OUTPUT Y DEMAS

#%%
config = Config()
config.language = 'es'


def get_article(link):
    #article = Article(url=link, language='es')
    article = Article(url=link, config=config)
    article.download()
    article.parse()
    
    title = article.title
    text = article.text
    
    return(title, text)
#%%

articles = [["id", "url", "media", "title", "text"]]

it = 0
for row in df.itertuples():
    it = it + 1
    ntot = str(df.shape[0])
    print('Fila ' + str(it) + ' de ' + ntot)
    url = row.DocumentIdentifier
    GKGID = row.GKGRECORDID
    media = row.SourceCommonName
  
    try:
        title, text = get_article(link=url)
        print('\t' + 'OK')
    except:
        title = 'Error'
        text = 'Error'
        print('\t' + 'Error')
    
    articles.append([GKGID, url, media, title, text])
   
    if it%100 == 0:
        with open("./data/output/out_test3.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(articles)

#%%

with open("./data/output/out_test_3.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(articles)
    
