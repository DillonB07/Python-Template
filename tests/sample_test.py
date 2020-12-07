import pytest # pip install pytest

# Examples taken from docs.pytest.org

#####################

def func(x):
  return x + 1
  
def test_answer():
  assert func(3) == 4

#####################

def systemExitError():
  raise SystemExit(1)

def test_systemexit():
  with pytest.raises(SystemExit):
    f()
