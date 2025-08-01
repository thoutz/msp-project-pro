
class AutomationService:
    def run_rule(self, rule, ticket):
        if rule.get("trigger") == "SLA_BREACH":
            self.notify_tech_lead(ticket)

    def notify_tech_lead(self, ticket):
        print(f"Notify tech lead about SLA breach for ticket {ticket.id}")
