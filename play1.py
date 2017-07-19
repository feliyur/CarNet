#%%
import time
import urllib3
import urllib.request
import webbrowser
import json
import os

http = urllib3.PoolManager()


#%%
def requestImage(query, PageNum):
    directory='C:\\Users\\COMP\\Desktop\\temporary\\'+query
    ImageName='image'+query
    if not os.path.exists(directory):
        os.makedirs(directory)
    for iter in range (1,PageNum):
        start='&start='+str(iter*10+1)
        r = http.request('GET', 
        'https://www.googleapis.com/customsearch/v1?' + 
        'key=' +
        '&cx=' +'&q='+
        query+start+'&num=10', headers={'User-Agent': 'Mozilla/5.0'}); 
        j = json.loads(r.data.decode('utf-8'))
        l=len(j['items'])
        for ind in range (0,l): 
            new_item=j['items'][ind]['pagemap']
            if new_item.get('cse_image')!=None :
                src = j['items'][ind]['pagemap']['cse_image'][0]['src']
                NewImName=directory+ImageName+str(iter*l+ind)+".jpg"
                data = urllib.request.urlretrieve(src, NewImName)
        print("pause 10 sec")
        time.sleep(10)    # pause 10 seconds
        print("continue...")
        return iter
        
query='suzuki+alto'
PageNum=10
it=requestImage(query, PageNum)

    

