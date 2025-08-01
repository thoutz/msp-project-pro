
import httpx
from app.config import settings

class AutotaskService:
    def __init__(self):
        self.base_url = settings.AUTOTASK_BASE_URL
        self.api_key = settings.AUTOTASK_API_KEY

    async def get_ticket(self, ticket_id: str):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/Tickets/{ticket_id}", headers=headers)
            return response.json()
