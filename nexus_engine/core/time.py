"""Sistema de tempo da Nexus Engine (estilo Unity Time)"""

import time as _time


class Time:
    """Gerencia delta time, tempo total, time scale, etc."""

    def __init__(self):
        self._start_time = _time.perf_counter()
        self._last_frame = self._start_time
        self._delta_time = 0.0
        self._unscaled_delta_time = 0.0
        self._time_scale = 1.0
        self._frame_count = 0
        self._fixed_delta_time = 1.0 / 60.0
        self._accumulated_fixed = 0.0

    def tick(self):
        now = _time.perf_counter()
        self._unscaled_delta_time = now - self._last_frame
        self._delta_time = self._unscaled_delta_time * self._time_scale
        self._last_frame = now
        self._frame_count += 1
        self._accumulated_fixed += self._delta_time

    @property
    def delta_time(self) -> float:
        return self._delta_time

    @property
    def unscaled_delta_time(self) -> float:
        return self._unscaled_delta_time

    @property
    def time(self) -> float:
        return (_time.perf_counter() - self._start_time) * self._time_scale

    @property
    def unscaled_time(self) -> float:
        return _time.perf_counter() - self._start_time

    @property
    def frame_count(self) -> int:
        return self._frame_count

    @property
    def time_scale(self) -> float:
        return self._time_scale

    @time_scale.setter
    def time_scale(self, value: float):
        self._time_scale = max(0.0, value)

    @property
    def fixed_delta_time(self) -> float:
        return self._fixed_delta_time

    @fixed_delta_time.setter
    def fixed_delta_time(self, value: float):
        self._fixed_delta_time = max(0.001, value)

    def should_fixed_update(self) -> bool:
        if self._accumulated_fixed >= self._fixed_delta_time:
            self._accumulated_fixed -= self._fixed_delta_time
            return True
        return False

    def fps(self) -> float:
        if self._unscaled_delta_time <= 0:
            return 0.0
        return 1.0 / self._unscaled_delta_time
