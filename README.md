📘 README.md for GitHub Repo flight-itinerary-api
markdown
# ✈️ Flight Itinerary API

This backend project reconstructs a complete travel itinerary using all provided flight tickets, starting from a specified airport. The algorithm guarantees the path follows the smallest lexical order and is implemented using depth-first search (DFS). It's exposed through a clean and intuitive Flask API.

---

## 🚀 Features

- 📊 Graph-based ticket organization
- 🧭 DFS traversal with lexical ordering
- ✅ Input validation and error handling
- 🌍 RESTful API design using Flask

---

## 💻 Technologies

- Python 3
- Flask
- `collections.defaultdict`
- REST principles

---

## 📦 Installation

```bash
git clone https://github.com/Rowland2023/flight-itinerary-api.git
cd flight-itinerary-api
pip install -r requirements.txt
python app.py
🔍 Sample Request
POST /tickets

json
{
  "tickets": [
    ["JFK", "ATL"],
    ["ATL", "SFO"],
    ["SFO", "JFK"]
  ],
  "start": "JFK"
}
Response

json
{
  "itinerary": ["JFK", "ATL", "SFO", "JFK"]
}
🧪 Future Add-ons
Swagger UI documentation

Docker containerization

Unit tests with pytest

Deployment instructions (Render, Railway, Vercel)

🧠 Author
Developed by Rowland2023

MIT License


---

### 📄 CV/Portfolio Description

> **Flight Itinerary API**  
> Built a Python backend that reconstructs the correct sequence of flight routes using depth-first graph traversal and lexical sorting. Implemented with Flask, the API accepts JSON ticket data and returns a complete travel path. Includes input validation and error handling. Designed for scalability and future deployment.

---


