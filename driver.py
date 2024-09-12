import yaml
from sdk import CredIssuerSDK  # Assuming your SDK is saved in `sdk.py`

def load_config_from_yaml(file_path):
    """
    Load the configuration from a YAML file.
    """
    with open(file_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(f"Error loading YAML: {exc}")
            return None

def run_with_yaml_config(file_path):
    """
    Driver function that reads config from YAML and runs SDK actions.
    """
    config = load_config_from_yaml(file_path)

    if not config:
        print("Invalid configuration file.")
        return

    # Extract necessary information from YAML
    base_url = config.get("base_url", "https://app.credissuer.com")
    email = config.get("email")
    password = config.get("password")
    csrf_token = config.get("csrf_token")
    credential_template = config.get("credential_template")
    recipient_info = config.get("recipient_info")

    if not (email and password and csrf_token and credential_template and recipient_info):
        print("Missing required fields in the YAML file.")
        return

    # Initialize the SDK with the base URL
    sdk = CredIssuerSDK(base_url)

    # Step 1: Login and retrieve token
    sdk.login(email=email, password=password, csrf_token=csrf_token)

    # Step 2: Issue a credential (token will be automatically used)
    issue_response = sdk.issue_credential(credential_template=credential_template, recipient_data=recipient_info)

    print("Credential Issued:", issue_response)

if __name__ == "__main__":
    # Path to the YAML config file
    yaml_file = "config.yaml"

    # Run the driver function
    run_with_yaml_config(yaml_file)
