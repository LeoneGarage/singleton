import time

class Singleton:
  _value = None

  def __init__(self):
    self._value = str(time.perf_counter_ns())

  def getValue(self):
    return self._value
