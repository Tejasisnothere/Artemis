from intent_extractor.constants.application import DATA_PATH
import os
import gzip
import json
import pandas as pd 

file_path = os.path.join(DATA_PATH, "Electronics.jsonl.gz")


limit = 10000   
data = []

with gzip.open(file_path, "rt", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= limit:
            break
        data.append(json.loads(line))

df = pd.DataFrame(data)

df_path = os.path.join(DATA_PATH, "unzipped.csv")
df.to_csv(df_path)

print(df.shape)
