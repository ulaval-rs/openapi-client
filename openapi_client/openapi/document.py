from dataclasses import dataclass

from openapi_client.openapi.info import Info
from openapi_client.openapi.path import Path


@dataclass
class Document:

    openapi: str  # OpenAPI version

    info: Info
    paths: dict[str, Path]

    def __post_init__(self):
        self.info = Info(**self.info)
        self.paths = {k: Path(**v) for k, v in self.paths.items()}

    def __repr__(self) -> str:
        return f'Document(openapi={self.openapi}, info=Info(title={self.info.title}, version={self.info.version}), ...)'
