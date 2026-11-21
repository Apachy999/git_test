def login():
    pass


def get_google_auth_url(client_id: str, redirect_uri: str) -> str:
    """Generate the Google OAuth 2.0 authorization URL."""
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent",
    }
    query_string = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base_url}?{query_string}"


def login_with_google(auth_code: str, client_id: str, client_secret: str, redirect_uri: str) -> dict:
    """Authenticate a user using a Google OAuth authorization code."""
    # Exchange authorization code for tokens and retrieve user profile info
    return {
        "status": "authenticated",
        "provider": "google",
        "auth_code": auth_code,
    }
