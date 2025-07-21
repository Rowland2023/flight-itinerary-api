from collections import defaultdict
class FlightTicket:
    def __init__(self,tickets,starting_airport):
        self.tickets = tickets
        self.starting_airport = starting_airport
        self.graph = defaultdict(list)
        self.route = []

    def build_graph(self):
        for origin,dest in self.tickets:
            self.graph[origin].append(dest)
        for origin in self.graph:
            self.graph[origin].sort(reverse=True)

    def dfs(self,airport):
        while self.graph[airport]:
            next_dest = self.graph[airport] .pop()
            self.dfs(next_dest)
        self.route.append(airport)
    def air_ticket(self):
        self.build_graph()
        self.dfs(self.starting_airport)
        if len(self.route) == len(self.tickets) + 1:
            return self.route[::-1]
        else:
            return []
            