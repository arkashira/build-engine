from onboarding import Onboarding, AIAssistant, Session
from uuid import uuid4
from datetime import datetime

def test_start_session():
    onboarding = Onboarding()
    session_id, timestamp = onboarding.start_session()
    assert session_id in onboarding.sessions
    assert isinstance(onboarding.sessions[session_id], Session)

def test_log_session():
    onboarding = Onboarding()
    session_id = str(uuid4())
    timestamp = datetime.now().isoformat()
    onboarding.log_session(session_id, timestamp)
    assert session_id in onboarding.sessions
    assert isinstance(onboarding.sessions[session_id], Session)

def test_get_session():
    onboarding = Onboarding()
    session_id = str(uuid4())
    timestamp = datetime.now().isoformat()
    onboarding.log_session(session_id, timestamp)
    session = onboarding.get_session(session_id)
    assert session.id == session_id
    assert session.timestamp == timestamp

def test_open_panel():
    ai_assistant = AIAssistant()
    session_id, timestamp = ai_assistant.open_panel()
    assert session_id in ai_assistant.onboarding.sessions
    assert isinstance(ai_assistant.onboarding.sessions[session_id], Session)

def test_get_session_ai_assistant():
    ai_assistant = AIAssistant()
    session_id, timestamp = ai_assistant.open_panel()
    session = ai_assistant.get_session(session_id)
    assert session.id == session_id
    assert session.timestamp == timestamp
