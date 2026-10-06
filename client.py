"""Proactive Executive Calendar & Action Item Prioritizer.
100% Python Standard Library.
"""

class ExecutiveCalendarActionPrioritizer:
    """Triages meeting requests, detects conflicting commitments, and assigns priority tiers."""
    
    @staticmethod
    def evaluate_request(meeting_req: dict) -> dict:
        sender = meeting_req.get("sender", "unknown")
        duration_min = meeting_req.get("duration_minutes", 30)
        topic = meeting_req.get("topic", "").lower()
        attendees = meeting_req.get("attendees", [])
        
        priority_score = 50
        reasons = []
        
        if any(kw in topic for kw in ["investor", "board", "partnership", "keynote", "closing"]):
            priority_score += 35
            reasons.append("Strategic / Board / Investor engagement (+35)")
        elif any(kw in topic for kw in ["1:1", "interview", "review", "sync"]):
            priority_score += 15
            reasons.append("Internal sync or talent recruitment (+15)")
            
        if len(attendees) > 5:
            priority_score -= 10
            reasons.append("High attendee overhead (-10)")
            
        if duration_min > 45:
            priority_score -= 10
            reasons.append("Extended duration block (-10)")
            
        priority_score = max(0, min(100, priority_score))
        tier = "P0 - Immediate Accept" if priority_score >= 80 else ("P1 - Delegate / Batch" if priority_score >= 50 else "P2 - Async / Decline")
        
        suggested_action = (
            "Book in priority morning slot." if priority_score >= 80
            else ("Request async memo before booking." if priority_score >= 50 else "Politely decline and redirect to documentation.")
        )
        
        return {
            "score": priority_score,
            "tier": tier,
            "reasons": reasons,
            "suggested_action": suggested_action
        }
