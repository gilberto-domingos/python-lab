from dataclasses import dataclass
from datetime import datetime

class EvidenceSnapshot :
    id: int
    text_content: str
    html_path: str
    screenshot_path: str
    hash: str
    captured_at: datetime