import os
import csv
import tempfile
from datetime import datetime, timedelta
import pytest

from session_dashboard import SessionManager, Session


@pytest.fixture
def manager() -> SessionManager:
    return SessionManager()


def create_session(session_id, user_id, start_offset_days, amount):
    start = datetime(2023, 1, 15) + timedelta(days=start_offset_days)
    end = start + timedelta(hours=1)
    return Session(session_id, user_id, start, end, amount)


def test_add_session_valid(manager):
    s = create_session("s1", "u1", 0, 10.0)
    manager.add_session(s)
    dashboard = manager.get_dashboard(datetime(2023, 1, 1))
    assert dashboard["session_count"] == 1
    assert dashboard["revenue"] == 10.0


def test_add_session_invalid_amount(manager):
    s = create_session("s2", "u2", 0, -5.0)
    with pytest.raises(ValueError):
        manager.add_session(s)


def test_dashboard_metrics_multiple_sessions(manager):
    # Jan sessions
    manager.add_session(create_session("s1", "u1", 0, 10.0))
    manager.add_session(create_session("s2", "u2", 1, 20.0))
    # Feb session
    manager.add_session(create_session("s3", "u1", 31, 15.0))

    jan_dashboard = manager.get_dashboard(datetime(2023, 1, 1))
    assert jan_dashboard["session_count"] == 2
    assert jan_dashboard["revenue"] == 30.0
    # No previous month data, churn_rate should be None
    assert jan_dashboard["churn_rate"] is None

    feb_dashboard = manager.get_dashboard(datetime(2023, 2, 1))
    assert feb_dashboard["session_count"] == 1
    assert feb_dashboard["revenue"] == 15.0
    # Prev month users: u1, u2; current month users: u1 -> churned u2
    assert feb_dashboard["churn_rate"] == 0.5


def test_churn_rate_no_previous_month(manager):
    # Only current month sessions
    manager.add_session(create_session("s1", "u1", 0, 10.0))
    dashboard = manager.get_dashboard(datetime(2023, 3, 1))
    assert dashboard["churn_rate"] is None


def test_export_to_csv(manager, tmp_path):
    # Add sessions for March
    manager.add_session(create_session("s1", "u1", 60, 10.0))
    manager.add_session(create_session("s2", "u2", 61, 20.0))

    csv_file = tmp_path / "march_sessions.csv"
    manager.export_to_csv(str(csv_file), datetime(2023, 3, 1))

    # Verify file content
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == ["session_id", "user_id", "start_time", "end_time", "amount"]
    assert len(rows) == 3  # header + 2 sessions
    assert rows[1][0] == "s1"
    assert rows[1][1] == "u1"
    assert rows[1][4] == "10.00"
    assert rows[2][0] == "s2"
    assert rows[2][1] == "u2"
    assert rows[2][4] == "20.00"
