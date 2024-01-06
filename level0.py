import json


def find_min(route, places, distances, memo):
    min_val = float('inf')
    place = -1
    for i in range(len(distances)):
        if distances[i] != 0 and i not in places:
            if min_val > distances[i]:
                place = i
                min_val = distances[i]
    
    route.append(min_val)
    places.append(place)
    memo[tuple(places)] = min_val

def solve(data):
    start = data['restaurants']['r0']['neighbourhood_distance']
    all_distance = {'r0': start}
    memo = {}

    for i in range(20):
        key = 'n' + str(i)
        distances = data['neighbourhoods'][key]['distances']
        all_distance[key] = distances
    
    route = []
    places = []
    
    find_min(route, places, all_distance['r0'], memo)
    
    for i in range(1, 21):
        if i == 1:
            find_min(route, places, all_distance['n0'], memo)
        else:
            
            last_place = places[-1]
            
            find_min(route, places, all_distance['n' + str(last_place)], memo)

    routes = {}
    cost = sum(route[-2::-1])
    print('cost:', cost)
    print('route:', route)

    for i in range(len(route)-1):
        val = 'n' + str(places[i])
        routes[val] = route[i]

    print('routes:', routes)

    converted_path = []
    for key in routes.keys():
        converted_path.append(key)

    converted_path = ['r0'] + converted_path + ['r0']
    converted_output = {"v0": {"path": converted_path}}

    with open('level0_output.json', "w") as json_file:
        json.dump(converted_output, json_file)
    
    return converted_output


with open('level0.json') as f:
    data = json.load(f)

converted_output = solve(data)
print(converted_output)
