import time

class SingletonProvider:
  _instance = None
  _clazz = None

  def __init__(self, clazz):
    self._instance = None
    self._clazz = clazz

  def getInstance(self):
    return self._instance

  def createInstance(self):
    return self._clazz()

  def __getstate__(self):
    """Return state values to be pickled."""
    return self._clazz

  def __setstate__(self, state):
    """Restore state from the unpickled state values."""
    self._clazz = state
    if self._instance is None:
      self._instance = self.createInstance()
