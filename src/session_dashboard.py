import csv
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Set


@dataclass
class Session:
    session_id: str
    user_id: str
    start_time: datetime
    end_time: datetime
    amount: float


class SessionManager:
    """
    In-memory session manager that tracks paid sessions,
    provides dashboard metrics per month, and can export data to CSV.
    """

    def __init__(self) -> None:
        self._sessions: List[Session] = []

    def add_session(self, session: Session) -> None:
        """
        Add a new session to the store.
        """
        if session.amount <= 0:
            raise ValueError("Session amount must be positive")
        self._sessions.append(session)

    def _month_key(self, dt: datetime) -> str:
        """
        Return a string key 'YYYY-MM' for the month of the given datetime.
        """
        return dt.strftime("%Y-%m")

    def _sessions_by_month(self) -> Dict[str, List[Session]]:
        """
        Group sessions by month key.
        """
        by_month: Dict[str, List[Session]] = {}
        for s in self._sessions:
            key = self._month_key(s.start_time)
            by_month.setdefault(key, []).append(s)
        return by_month

    def get_dashboard(self, month: datetime) -> Dict[str, Optional[float]]:
        """
        Return dashboard metrics for the given month:
        - session_count: int
        - revenue: float
        - churn_rate: float or None
        """
        month_key = self._month_key(month)
        by_month = self._sessions_by_month()

        current_sessions = by_month.get(month_key, [])
        session_count = len(current_sessions)
        revenue = sum(s.amount for s in current_sessions)

        # Compute churn rate relative to previous month
        prev_month_dt = (month.replace(day=1) - timedelta(days=1))
        prev_month_key = self._month_key(prev_month_dt)
        prev_sessions = by_month.get(prev_month_key, [])

        prev_users: Set[str] = {s.user_id for s in prev_sessions}
        current_users: Set[str] = {s.user_id for s in current_sessions}

        if not prev_users:
            churn_rate: Optional[float] = None
        else:
            churned = prev_users - current_users
            churn_rate = len(churned) / len(prev_users)

        return {
            "session_count": session_count,
            "revenue": revenue,
            "churn_rate": churn_rate,
        }

    def export_to_csv(self, file_path: str, month: datetime) -> None:
        """
        Export all sessions for the given month to a CSV file.
        Columns: session_id,user_id,start_time,end_time,amount
        """
        month_key = self._month_key(month)
        sessions = [s for s in self._sessions if self._month_key(s.start_time) == month_key]

        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["session_id", "user_id", "start_time", "end_time", "amount"])
            for s in sessions:
                writer.writerow(
                    [
                        s.session_id,
                        s.user_id,
                        s.start_time.isoformat(),
                        s.end_time.isoformat(),
                        f"{s.amount:.2f}",
                    ]
                )
