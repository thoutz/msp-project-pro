
class SLAService:
    def calculate_sla(self, tickets):
        if not tickets:
            return 100
        on_time = sum(1 for t in tickets if t.status == 'OnTime')
        return (on_time / len(tickets)) * 100
