# -*- coding: utf-8 -*-

"""Helper module with different usefull functions."""

import clearbit
import json
import requests

from django.conf import settings


def is_email_valid(email):
    """Check if a given email address is deliverable and has been found on the internet using hunter.io."""

    result = requests.get(
        f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={settings.HUNTER_IO_API_KEY}'
    ).json()

    return True if result.get('data').get('status') == 'valid' else False


def enrich_user_by_email(email):
    """Try to get additional user info by email using clearbit service."""

    result = {}
    if settings.ENRICH_DATA:
        clearbit.key = settings.CLEARBIT_API_KEY
        try:
            result = clearbit.Enrichment.find(email=email, stream=True)
        except:
            result = {}

    return result
