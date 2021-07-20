import requests	
from Internet_Module import check_inernet_connection
from Output_Module import output

def get_news():
    if check_inernet_connection():
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "673d07fd9c3740848cf0c95a2b4bdb90"
        }
        main_url = " https://newsapi.org/v1/articles"

        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()

        # getting all articles in a string article
        article = open_bbc_page["articles"]

        # empty list which will
        # contain all trending news
        results = []
        
        for ar in article:
            results.append(ar["title"])
            result=''
        for i in range(len(results)):
            
            # printing all trending news
            result=result+str(i + 1)+' '+ results[i]+'\n'
           
        return result + '\n These were the top news of today'
    else:
        return 'Check your Internet connection First'
    


