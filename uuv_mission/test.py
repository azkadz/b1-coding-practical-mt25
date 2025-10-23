import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from uuv_mission.dynamic import Mission

def test_from_csv():
    m = Mission.from_csv("data/mission.csv")
    assert len(m.reference) > 0
    assert len(m.cave_height) == len(m.reference)
    assert len(m.cave_depth) == len(m.reference)
    assert isinstance(float(m.reference[0]), float)
    print("Mission loaded OK:", len(m.reference))

if __name__ == "__main__":
    test_from_csv()