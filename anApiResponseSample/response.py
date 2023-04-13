"""Response Format and Formation util
"""
import json
from dataclasses import dataclass, field, asdict
from typing import List, Tuple, Union, NoReturn
from flask import Response

NoneType: type = type(None)


def pagination_response_struct():
    """schmea of pagination parameters"""

    @dataclass
    class Page:
        total: int = 0
        current: Union[int, NoneType] = None
        next: Union[int, NoneType] = None
        prev: Union[int, NoneType] = None
        link: dict = field(default_factory=lambda: {"next": None, "prev": None})

    return Page()


@dataclass
class JsonApiResponse:
    """schema of a json response type"""

    message: str = ""
    code: str = None
    data: Union[List[dict], Tuple[dict], dict] = None
    page: dict = field(default_factory=pagination_response_struct)
    http_status_code: int = 200

    def make(self, paginated=False) -> Response:
        """makes a flask response"""

        _mimetype = "application/json"
        if not isinstance(self.data, (type(None), list, dict, tuple)):
            raise TypeError(f"Input Data should be any of types : {[list, dict, tuple]}")

        response = dict(message=self.message, code=self.code, data=self.data)
        if paginated:
            response["page"] = asdict(self.page)
        json_response = json.dumps(response, default=str)
        return Response(
            response=json_response,
            status=self.http_status_code,
            mimetype=_mimetype,
        )


