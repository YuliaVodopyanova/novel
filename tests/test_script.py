from pathlib import Path

SCRIPT_PATH = Path(__file__).parent.parent / 'game' / 'script.rpy'

def test_jumps():
    """
    Tests if there is label for every jump
    Returns:
    """
  with open(SCRIPT_PATH, 'r') as f:
      content = f.read()
      n_jumps = content.count('jump')
      n_labels = content.count('label')
      assert (n_jumps + 1) == n_labels
                              
