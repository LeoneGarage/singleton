import time

class SingletonProvider:
  _instance = None

  def __init__(self):
    self._instance = None

  def get(self):
    return self._instance

  def __getstate__(self):
    """Return state values to be pickled."""
    return { 'a': 0 }

  def __setstate__(self, state):
    """Restore state from the unpickled state values."""
    if self._instance is None:
        self._instance = Singleton()

class Singleton:
  _value = None

  def __init__(self):
    self._value = str(time.perf_counter_ns())

  def getValue(self):
    return self._value

