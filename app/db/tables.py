from dataclasses import dataclass
from ..db.models.user import User

@dataclass
class Tables:
    user: User

def load_db() -> Tables:
    
    return Tables(
        user=User(),
    )

db = load_db()