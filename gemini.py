import aiohttp


class GeminiAPIClient:
    token: str
    proxy: str
    model: str
    GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models"

    def __init__(self, model, token, proxy):
        self.token = token
        self.proxy = proxy
        self.model = model

    async def send_request(self, text):
        url = f"{self.GEMINI_API_URL}/{self.model}:generateContent?key={self.token}"

        headers = {
            "Content-Type": "application/json",
            "X-Geo-Location": "US",
        }
        json_body = {
            "contents": [{
                "parts": [{
                    "text": text
                }]
            }]
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(url, json=json_body, proxy=self.proxy) as response:
                if response.status == 200:
                    return await response.json()
