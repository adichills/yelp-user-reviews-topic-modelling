import json
from collections import  defaultdict

def get_useful_rows(filename,useful_keys,primary_key,start,end):
    useful_rows = defaultdict(int)
    with open(filename,'r',encoding='utf8') as f:
        useful_rows = defaultdict(int)
        i = 0
        for line in f:
            if i > end:
                break
            if i not in range(start,end):
                continue
            i+=1
            if i % 10000 == 0:
                print(i)
            row = json.loads(line)
            useful = row['useful']
            if useful > 0:
                payload =  {}
                for key in useful_keys:
                    payload[key] = row[key]
                useful_rows[row[primary_key]] = payload
    print(i)
    return useful_rows


def writeDictToFile(filename,d):
    with open(filename,'w',encoding='utf8') as f:
        for key in d:
            line = json.dumps(d[key])
            f.write(line + '\n')




useful_rows = get_useful_rows('input/yelp_academic_dataset_review.json',['business_id','text','stars','user_id'],'review_id',4000001,6000000)
print(len(useful_rows))
writeDictToFile('output/useful_reviews_3.json', useful_rows)