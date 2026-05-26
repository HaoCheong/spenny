import json
from datetime import datetime, timezone
from sqlalchemy.types import TypeDecorator, Text

class DatetimeJSON(TypeDecorator):
    impl = Text
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            return json.dumps(value, default=self._serialize)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return json.loads(value, object_hook=self._deserialize)
        return value

    @staticmethod
    def _serialize(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    @staticmethod
    def _deserialize(d):
        # Optionally parse ISO strings back to datetime on read
        for key, value in d.items():
            if isinstance(value, str):
                try:
                    dt = datetime.fromisoformat(value)
                    if dt.tzinfo is None:
                        dt = dt.replace(tzinfo=timezone.utc)
                    d[key] = dt
                except ValueError:
                    pass
        return d