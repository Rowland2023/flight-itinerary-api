import unittest
from models.itinerary import FlightTicket

class TestFlightTicket(unittest.TestCase):

    def test_valid_itinerary(self):
        tickets = [
            ["JFK", "ATL"],
            ["ATL", "SFO"],
            ["SFO", "JFK"]
        ]
        planner = FlightTicket(tickets, "JFK")
        result = planner.air_ticket()
        expected = ["JFK", "ATL", "SFO", "JFK"]
        self.assertEqual(result, expected)

    def test_empty_itinerary_due_to_missing_connection(self):
        tickets = [
            ["JFK", "ATL"],
            ["SFO", "LAX"]  # disconnected from JFK route
        ]
        planner = FlightTicket(tickets, "JFK")
        result = planner.air_ticket()
        self.assertEqual(result, [])  # can't use all tickets from start point

    def test_cycle_in_itinerary(self):
        tickets = [
            ["JFK", "ATL"],
            ["ATL", "SFO"],
            ["SFO", "JFK"]
        ]
        planner = FlightTicket(tickets, "JFK")
        result = planner.air_ticket()
        expected = ["JFK", "ATL", "SFO", "JFK"]
        self.assertEqual(result, expected)

    def test_lexical_order_preference(self):
        tickets = [
            ["MUC", "LHR"],
            ["JFK", "MUC"],
            ["SFO", "SJC"],
            ["LHR", "SFO"]
        ]
        planner = FlightTicket(tickets, "JFK")
        result = planner.air_ticket()
        expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
