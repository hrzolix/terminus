import json
import pprint as pp
import yaml

with open('donuts.json', 'r') as openfile:
    d2 = json.load(openfile)

#Printing key- value pairs using for loop

for k, v in d2.items():
    if k == 'batters':
        for k2, v2, in v.items():
            print(k,':', '\n', '\t', k2)
            for i in v2:
                for h, r in i.items():
                    print('\t\t', h,':', r)
    elif k == 'topping':
        print(k)
        for j in v:
            for o, p in j.items():
                print('\t\t', o, ':', p)
    
    else:
        print(k,':', v)

#Printing using pprint
pp.pprint(d2)

#Printing using yaml
print(yaml.dump(d2, indent = 10))
