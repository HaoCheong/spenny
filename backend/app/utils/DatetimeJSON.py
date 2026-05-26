import json
from datetime import datetime, timezone
from sqlalchemy.types import TypeDecorator, Text

class DatetimeJSON(TypeDecorator):
    impl = Text
    cache_ok = True

    def __init__(self, model=None):
        super().__init__()
        self._model = model

    def process_result_value(self, value, dialect):
        if value is not None:
            d = json.loads(value, object_hook=self._deserialize)
            if self._model is not None:
                return self._model.model_validate(d)
            return d
        return value

    def process_bind_param(self, value, dialect):
        if value is not None:
            if hasattr(value, "model_dump"):
                value = value.model_dump()
            return json.dumps(value, default=self._serialize)
        return value

    @staticmethod
    def _serialize(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    @staticmethod
    def _deserialize(d):
        # PFIX: Is this the best way to introduce timezone utc into the code base?
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