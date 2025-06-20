from dataclasses import asdict, dataclass, field


@dataclass
class HttpResponseDTO:
    status_code: int
    headers: dict = field(default_factory=dict)
    body: dict = field(default_factory=dict)
    content_type: str = field(default="content-type: application/json")

    def to_dict(self):
        return asdict(self)
