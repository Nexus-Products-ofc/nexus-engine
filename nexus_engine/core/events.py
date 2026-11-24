"""Sistema de eventos (Event Bus) da Nexus Engine"""

from collections import defaultdict
from typing import Callable, Any, Dict, List
import uuid


class Event:
    def __init__(self, name: str, data: Any = None):
        self.name = name
        self.data = data
        self.cancelled = False

    def cancel(self):
        self.cancelled = True


class EventBus:
    def __init__(self):
        self._listeners: Dict[str, List[tuple]] = defaultdict(list)

    def subscribe(self, event_name: str, callback: Callable, priority: int = 0) -> str:
        listener_id = str(uuid.uuid4())
        self._listeners[event_name].append((listener_id, callback, priority))
        self._listeners[event_name].sort(key=lambda x: -x[2])
        return listener_id

    def unsubscribe(self, event_name: str, listener_id: str):
        self._listeners[event_name] = [
            (lid, cb, prio) for lid, cb, prio in self._listeners[event_name]
            if lid != listener_id
        ]

    def emit(self, event_name: str, data: Any = None) -> Event:
        event = Event(event_name, data)
        for _, callback, _ in self._listeners.get(event_name, []):
            if event.cancelled:
                break
            try:
                callback(event)
            except Exception as e:
                print(f"[NexusEngine] Erro no listener de '{event_name}': {e}")
        return event

    def clear(self, event_name: str = None):
        if event_name:
            self._listeners[event_name].clear()
        else:
            self._listeners.clear()
