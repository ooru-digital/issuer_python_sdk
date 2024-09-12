import requests

class APIClient:
    """
    A base client to perform REST operations.
    """
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        self.csrf_token = None

    def post(self, endpoint, headers=None, data=None):
        """
        Perform a POST request.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def set_token(self, token):
        """
        Store the authentication token for future requests.
        """
        self.token = token

    def set_csrf_token(self, csrf_token):
        """
        Set CSRF token if needed for additional requests.
        """
        self.csrf_token = csrf_token

    def get_auth_headers(self):
        """
        Generate authorization headers for requests requiring authentication.
        """
        if not self.token:
            raise ValueError("Token not set. Login first.")
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

class CredIssuerSDK:
    """
    SDK for interacting with the credissuer platform.
    """
    def __init__(self, base_url):
        self.api_client = APIClient(base_url)

    def login(self, email, password, csrf_token):
        """
        Login to the platform and store the auth token.
        """
        login_data = {
            "email": email,
            "password": password
        }
        headers = {
            "X-CSRFToken": csrf_token,
            "Content-Type": "application/json"
        }
        response = self.api_client.post("/api/users/login/", headers=headers, data=login_data)
        
        # Extract the token from the response and store it
        token = response.get('token')  # Assuming the token is returned in the 'token' key
        if token:
            self.api_client.set_token(token)
            print("Login successful, token stored.")
        else:
            raise ValueError("Token not found in the response.")
    
    def issue_credential(self, credential_template, recipient_data):
        """
        Issue a credential using the previously stored token.
        """
        headers = self.api_client.get_auth_headers()
        endpoint = f"/api/credentials/issue/single?credential_template={credential_template}"
        response = self.api_client.post(endpoint, headers=headers, data=recipient_data)
        
        return response