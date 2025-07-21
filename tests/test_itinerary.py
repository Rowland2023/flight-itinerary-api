import unittest
from models.itinerary import FlightTicket

class TestFlightTicket(unittest.TestCase):
    def test_valid_itinerary(self):
        tickets = [["JFK", "ATL"], ["ATL", "SFO"], ["SFO", "JFK"]]
        planner = FlightTicket(tickets, "JFK")
        self.assertEqual(planner.air_ticket(), ["JFK", "ATL", "SFO", "JFK"])

    def test_disconnected_tickets(self):
        tickets = [["JFK", "ATL"], ["SFO", "LAX"]]  # No connection
        planner = FlightTicket(tickets, "JFK")
        self.assertEqual(planner.air_ticket(), [])

    def test_cycle_path(self):
        tickets = [["A", "B"], ["B", "A"]]
        planner = FlightTicket(tickets, "A")
        self.assertEqual(planner.air_ticket(), ["A", "B", "A"])
