import socket
import wikipedia
def check_inernet_connection():
    IPaddress=socket.gethostbyname(socket.gethostname())
    if IPaddress=="127.0.0.1":
       return False
    else:
        return True

def check_on_wikipedia(query):
    query=query.lower()
    query=query.replace('who is','')
    query=query.replace('what is','')
    query=query.replace('do you know','')
    query=query.replace('tell me','')
    query=query.replace('tell me about','')
    query=query.replace('search on wikipedia','')
    query=query.replace('wikipedia','')
    
    query=query.strip()
 #   print(query)
    
    try:
       data=wikipedia.summary(query,sentences=2)
       #print(data)
       return data
    except Exception as e:
        print(e)
        return ''
#print(check_on_wikipedia('who is narendra  modi search on wikipedia'))