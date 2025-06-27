import requests
import os

class WatsonXClient:
    """Connects to IBM Watsonx AI."""
    def __init__(self, api_key, project_id, url, model_id="ibm/granite-3-3-8b-instruct"):
        if not api_key or not project_id or not url:
            raise ValueError("Missing required WatsonX credentials")
        self.api_key = api_key
        self.project_id = project_id
        self.url = url
        self.model_id = model_id
        self.access_token = None

    def get_access_token(self):
        """Get IBM Cloud IAM access token."""
        try:
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
            }
            data = {
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": self.api_key
            }
            
            response = requests.post("https://iam.cloud.ibm.com/identity/token", 
                                   headers=headers, data=data, timeout=30)
            
            if response.status_code == 200:
                token_data = response.json()
                self.access_token = token_data.get("access_token")
                return self.access_token
            else:
                print(f"IAM Token Error: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            print(f"IAM Token Exception: {str(e)}")
            return None

    def generate(self, prompt: str) -> str:
        """Send a prompt and return the generated response."""
        try:
            # Get fresh access token
            if not self.get_access_token():
                return "Error: Failed to get IBM Cloud access token"

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.access_token}",
                "Accept": "application/json"
            }
            payload = {
                "model_id": self.model_id,
                "project_id": self.project_id,
                "input": prompt,
                "parameters": {
                    "max_new_tokens": 1000,
                    "temperature": 0.7
                }
            }

            request_url = f"{self.url}/ml/v1/text/generation?version=2023-05-29"
            response = requests.post(request_url, json=payload, headers=headers, timeout=30)

            if response.status_code != 200:
                print(f"WatsonX API Error: {response.status_code} - {response.text}")
                return f"Error: WatsonX API returned {response.status_code}"

            result = response.json()
            if "results" in result and len(result["results"]) > 0:
                return result["results"][0].get("generated_text", "No response generated")
            else:
                return "No response from WatsonX API"
                
        except Exception as e:
            print(f"WatsonX Client Error: {str(e)}")
            return f"Error: {str(e)}"