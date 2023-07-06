from starlette.requests import Request
from starlette.responses import Response, RedirectResponse
import httpx
from starlette.datastructures import URL


async def proxy(request: Request):
    target_url = "http://localhost:5151"  # Replace with your desired target URL
    target_path = request.path_params["path"]

    target_url_obj = URL(target_url)
    target_url = target_url_obj.replace(path=target_path, query=request.url.query)

    target_headers = {k: v for k, v in request.headers.items() if k.lower() != 'host'}
    async with httpx.AsyncClient() as client:
        target_response = await client.request(
            method=request.method,
            url=str(target_url),
            headers=target_headers,
            content=request.stream(),
            timeout=None
        )

    return Response(
        content=target_response.content,
        status_code=target_response.status_code,
        headers=target_response.headers,
    )


import typing as t

from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from sse_starlette.sse import EventSourceResponse

from fiftyone.server.events import (
    ListenPayload,
    add_event_listener,
    dispatch_polling_event_listener,
)
from fiftyone.server.decorators import route


class Events(HTTPEndpoint):
    @route
    async def post(
        self, request: Request, data: dict
    ) -> t.Union[t.Dict, EventSourceResponse]:
        polling = data.pop("polling", False)
        payload = await ListenPayload.from_dict(data)
        if polling:
            return await dispatch_polling_event_listener(request, payload)

        return EventSourceResponse(
            add_event_listener(request, payload),
            ping=2,
        )


async def proxy_media(request: Request):
    path = request.query_params["filepath"]
    if path.startswith("http"):
        return RedirectResponse(path)
    return await proxy(request)
