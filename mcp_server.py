"""MCP server for Executive Calendar & Action Item Prioritizer."""
import sys
import json
from client import ExecutiveCalendarActionPrioritizer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "prioritize_calendar_request",
                "description": "Evaluates calendar invitation for strategic priority and suggested action",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "meeting_req": {"type": "object"}
                    },
                    "required": ["meeting_req"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "prioritize_calendar_request":
            req_data = params.get("arguments", {}).get("meeting_req", {})
            res = ExecutiveCalendarActionPrioritizer.evaluate_request(req_data)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
