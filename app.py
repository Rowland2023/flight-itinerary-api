from collections import defaultdict
from flasgger import Swagger


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
            
#Build API

from flask import Flask,request,jsonify

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/tickets', methods=['POST'])
def tickets():
    """
    Reconstruct flight itinerary from input tickets
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            tickets:
              type: array
              items:
                type: array
                items:
                  type: string
              description: List of flight ticket pairs [from, to]
            start:
              type: string
              description: Starting airport code
    responses:
      200:
        description: Returns the reconstructed itinerary
        schema:
          type: object
          properties:
            itinerary:
              type: array
              items:
                type: string
    """

    try:
        data = request.get_json()
        if not isinstance(data.get('tickets'),list) or 'start' not in data:
            raise ValueError("Missing required field")
        planner = FlightTicket(data['tickets'],data['start'])
        itinerary = planner.air_ticket()
        return jsonify({'itinerary':itinerary}),200
    except Exception as e:
        return jsonify({'error': f'Missing field:{str(e)}'})
if __name__=="__main__":
    app.run(debug=True)