import pandas
import json

data =[]

with open('Yelp_JSON/yelp_dataset/yelp_academic_dataset_checkin.json') as f:
    for line in f:
        data.append(json.loads(line))

df = pandas.DataFrame(data)
print(df)
df.to_csv("yelp_checkin.csv", index=False)

