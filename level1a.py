import json
with open('level1a.json') as f:
    data = json.load(f)
    
total_capacity=data['vehicles']['v0']['capacity']
start = data['restaurants']['r0']['neighbourhood_distance']
all_distance = {'r0': start}


dist=[]
places=[]
route=[]
fin_cost=[]

for i in range(20):
    key = i
    
    all_distance[key] = [data['neighbourhoods']['n' + str(i)]['order_quantity'],data['neighbourhoods']['n' + str(i)]['distances']]


def calc_cap(sorted_distance,total_capacity,cost):
    path=[]
    for i in range(len(sorted_distance)):
        if i!=len(sorted_distance)-1:

            if total_capacity-sorted_distance[i][1][0]<=0:
                
                total_capacity=600
                route.append(path)
                path=[]
                path.append(sorted_distance[i][0])
                total_capacity-=sorted_distance[i][1][0]
            else:
                
                path.append(sorted_distance[i][0])
                total_capacity-=sorted_distance[i][1][0]
        else:
            path.append(sorted_distance[i][0])
            route.append(path) 
            
      
sorted_distance = sorted(all_distance.items(),key=lambda x:x[1])
sorted_distance.pop()

start=sorted_distance[0]
    

cost=data['restaurants']['r0']['neighbourhood_distance'][2]
fin_cost.append(cost)
calc_cap(sorted_distance,total_capacity,cost)
print(route)

import json



paths = {}
for i, lst in enumerate(route):
    
    path_key = f"path{i + 1}"
    nodes = []
    nodes.append("r0")
    for num in lst:
        nodes.append(f"n{num}")
    nodes.append("r0")
    paths[path_key] = nodes


result = {"v0": paths}

with open("level1a_output.json", "w") as file:
    json.dump(result, file)

