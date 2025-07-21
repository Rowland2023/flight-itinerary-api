from collections import defaultdict
def flight_ticket(tickets,start_airport):
    graph = defaultdict(list)

    for origin,destination in tickets:
        graph[origin].append(destination)
    for origin in graph:
        graph[origin].sort(reverse=True)

    route = []

    def dfs(airport):
        while graph[airport]:
            next_dest = graph[airport].pop()
            dfs(next_dest)
        route.append(airport)

    dfs(start_airport) 

    if len(route) == len(tickets) + 1:
        return route[::-1]
    else:
        return []
    