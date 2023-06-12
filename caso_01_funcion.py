import requests
def get_patiotuerca (search_text: str):
    user_agent={'User-agent': 'Mozilla/5.0'}
    keywords = search_text
    url=f"https://ecuador.patiotuerca.com/ptx/api/v2/nitros?type={keywords}"
    r=requests.get(url, headers = user_agent)
    result=r.json()['data']['result_set']
    precio_sum=0
    num_elementos=len(result)
    
    if num_elementos == 0:
        return {
            "num_results": num_elementos,
            "precio_promedio": None,
            "resultados": [],
        }

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

    return {
        "num_results": num_elementos,
        "price_avg": precio_promedio,
        "results": resultados,
        }