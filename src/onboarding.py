import json
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

@dataclass
class Session:
    id: str
    timestamp: str

class Onboarding:
    def __init__(self):
        self.sessions = {}

    def start_session(self):
        session_id = str(uuid4())
        timestamp = datetime.now().isoformat()
        self.sessions[session_id] = Session(session_id, timestamp)
        return session_id, timestamp

    def log_session(self, session_id, timestamp):
        self.sessions[session_id] = Session(session_id, timestamp)

    def get_session(self, session_id):
        return self.sessions.get(session_id)

class AIAssistant:
    def __init__(self):
        self.onboarding = Onboarding()

    def open_panel(self):
        session_id, timestamp = self.onboarding.start_session()
        self.onboarding.log_session(session_id, timestamp)
        return session_id, timestamp

    def get_session(self, session_id):
        return self.onboarding.get_session(session_id)
