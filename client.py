"""
Gemini Client Initialization Module

This module initializes the Google Gemini client using a securely stored
API key imported from the credentials file. The client object can be reused
across the application to make requests to the Gemini API.
"""

from google import genai

from cred import gemini_api_key

# Function for creating client
client = genai.Client(api_key = gemini_api_key)