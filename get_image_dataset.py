import argparse
import requests
import json as JSON
import os
import cv2

API_KEY="c869c51907df4b1b85c8e5738cb27b44"
MAX=20
GROUP_SIZE=50

URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

parser=argparse.ArgumentParser()
parser.add_argument("-q","--query", required=True)
parser.add_argument("-o","--output", required=False)

args=vars(parser.parse_args())

term=args['query']
headers={"Ocp-Apim-Subscription-Key" : API_KEY}
params={"q":term, "offset":0, "count":GROUP_SIZE}

search=requests.get(URL, headers=headers, params=params)
result=search.json()
result_num=min(result['totalEstimatedMatches'], MAX)
# EXCEPTION=[set([IOError, FileNotFoundError,
# 	exception.RequestException, exception.HTTPError,
# 	exception.ConnectionError, exception.Timeout])]
# parsed=JSON.loads(search)
# print(JSON.dumps(parsed, indent=4))
# 
total=0
for i in range(0, result_num, GROUP_SIZE):
    params["offset"]=i
    # print(params)
    searches = requests.get(URL, headers=headers, params=params)
    results=searches.json()

    
    try:
        for v in result["value"]:
            rq=requests.get(v["contentUrl"], timeout=30)
            ext=v["contentUrl"][v["contentUrl"].rfind("."):v["contentUrl"].rfind(".")+4]
            p = os.path.sep.join([args["output"], "{}{}".format(str(total).zfill(8), ext)])
            # print(p)
            total=total+1
            f=open(p, "wb")
            f.write(rq.content)
            f.close()

            image=cv2.imread(p)
            if image is None:
                os.remove(p)

    except Exception as e:
            continue

   
