import requests

user_agent={'User-agent': 'Mozilla/5.0'}
url="https://ecuador.patiotuerca.com/ptx/api/v2/nitros?type=autos"
r=requests.get(url, headers = user_agent)
result=r.json()['data']['result_set']
precio_sum=0
num_elementos=len(result)

resultados=[]
for r in result:
    articulo ={
    "marca": r["BrandValue"],
    "modelo": r["ModelValue"],
    "precio": r["PriceValue"],
    "anio": r["YearValue"]
    }
    resultados.append(articulo)
    precio_sum+=r["PriceValue"]
precio_promedio=precio_sum/num_elementos

for articulo in resultados:
    for x,y in articulo.items():
        print(x,": ",y)
    print('\n')


print(num_elementos, precio_sum,precio_promedio)