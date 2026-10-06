"""Example usage for Executive Calendar & Action Item Prioritizer."""
from client import ExecutiveCalendarActionPrioritizer

if __name__ == "__main__":
    req = {
        "sender": "board_member@venture.com",
        "topic": "Q3 Board Financial Strategy Sync",
        "duration_minutes": 40,
        "attendees": ["CEO", "Lead Director"]
    }
    triage = ExecutiveCalendarActionPrioritizer.evaluate_request(req)
    print("Priority Tier:", triage["tier"])
    print("Suggested Action:", triage["suggested_action"])
