import json
print("Interface Status")
print("=======================================================================================")
print("DN                                                 Description           Speed   MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

x=open("D:\Git\PP2\TSIS4\sample-data.json")

y=json.load(x)

for i in y["imdata"]:
    print(i['l1PhysIf']['attributes']["dn"], "\t", "\t", i['l1PhysIf']['attributes']['speed'], '\t', i['l1PhysIf']['attributes']['mtu'])




        
        