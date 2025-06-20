from dataclasses import asdict, dataclass, field


@dataclass
class HttpRequestDTO:
    method: str
    url: str
    headers: dict = field(default_factory=dict)
    body: dict = field(default_factory=dict)
    params: dict = field(default_factory=dict)

    def __post_init__(self):
        self.method = self.method.upper()

    def to_dict(self):
        return asdict(self)
