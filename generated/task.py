from dataclasses import dataclass, field
    from datetime import datetime
    from typing import Optional


    @dataclass
    class Task:
        id: int
        title: str
        description: str
        priority: str
        completed: bool = False
        created_at: datetime = field(default_factory=datetime.utcnow)
        completed_at: Optional[datetime] = None
