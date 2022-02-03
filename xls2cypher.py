#!/usr/bin/env python3
import re
import pandas as pd

fn = 'TPG Dependency Matrix - Provider Consumer.xlsx'
df = pd.read_excel(fn, header=1)

print('match (n) optional match (n)-[r]-() delete n,r;')


def tolabel(s):
    return 'l' + s.replace(")", "").replace("(", "").replace(" ", "_").replace('.','_').replace('/', '_').replace('-', '_')


for index, row in df.iterrows():
    system_name_src = row['TPG Applications In Scope']
    if not system_name_src:
        break
    print(f'merge (s:{tolabel(system_name_src)} {{name: "{system_name_src}"}});')
    i = 4
    while s := row[i]:
        if pd.isnull(row[i]):
            break
        (system_name, rel) = re.match("^(.*) :(.*)$", s).groups()
        print(f'merge (s:{tolabel(system_name)} {{name: "{system_name}"}});')
        print(f'match (s {{name: "{system_name_src}"}}), (d {{name: "{system_name}"}}) merge (s)<-[:{rel}]-(d);')
        i += 1
        if i == df.shape[1]:
            break
