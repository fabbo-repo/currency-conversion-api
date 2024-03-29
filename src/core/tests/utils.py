from rest_framework.test import APIClient
import json
from django.urls import reverse


def get(client: APIClient, url: str, content_type="application/json"):
    return client.get(
        url,
        content_type=content_type
    )


def post(client: APIClient, url: str, data: dict, content_type="application/json"):
    return client.post(
        url,
        data=json.dumps(
            data
        ),
        content_type=content_type
    )


def put(client: APIClient, url: str, data: dict, content_type="application/json"):
    return client.put(
        url,
        data=json.dumps(
            data
        ),
        content_type=content_type
    )


def patch(client: APIClient, url: str, data: dict, content_type="application/json"):
    return client.patch(
        url,
        data=json.dumps(
            data
        ),
        content_type=content_type
    )


def delete(client: APIClient, url: str, content_type="application/json"):
    return client.delete(
        url,
        content_type=content_type
    )
