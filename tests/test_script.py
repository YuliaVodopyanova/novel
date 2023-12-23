from pathlib import Path
import re

SCRIPT_PATH = Path(__file__).parent.parent / 'game' / 'script.rpy'

def test_jumps():
    """
    Tests if there is label for every jump
    Returns:
    """
  with open(SCRIPT_PATH, 'r') as f:
      content = f.read()
      n_jumps = re.findall(r'jump\s+(.+)', content)
      n_labels = re.findall(r'label\s+(.+)', content)
      assert set(n_jumps) == set(n_labels)
