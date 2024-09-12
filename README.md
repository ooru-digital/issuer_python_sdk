# Python SDK for CredIssuer API

This SDK provides an interface for interacting with the CredIssuer platform. It allows you to log in and issue verifiable credentials programmatically using Python.

## Features

- **Login**: Authenticate with the CredIssuer API using email and password, receiving an authentication token.
- **Issue Credentials**: Issue verifiable credentials using recipient information.

## Requirements

- Python 3.7+
- `requests` for making HTTP calls.
- `PyYAML` for parsing YAML configuration files.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the SDK

1. Create a `config.yaml` file with the following format:

    ```yaml
    base_url: "https://app.credissuer.com"
    email: "your-email@example.com"
    password: "your-password"
    csrf_token: "your-csrf-token"
    credential_template: "your-credential-template-id"
    recipient_info:
      data:
        recipient_first_name: "FirstName"
        recipient_last_name: "LastName"
        recipient_email: "recipient@example.com"
    ```

2. Run the Python driver to authenticate and issue a credential:

    ```bash
    python driver.py
    ```

This will log you in and issue a credential using the provided recipient information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
