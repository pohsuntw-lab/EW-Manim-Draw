import copy
import pytest
from ew_manim_draw.model import validate_spec

BASE = {"schema_version":"0.2","title":"企業知識求解示範","locale":"zh-TW","nodes":[{"id":"ask","label":"使用者提問"},{"id":"knowledge","label":"知識服務"},{"id":"answer","label":"答案與證據"}],"edges":[{"id":"e1","from":"ask","to":"knowledge"},{"id":"e2","from":"knowledge","to":"answer"}],"layout":{"direction":"horizontal"},"output":{"width":1920,"height":1080,"fps":15,"formats":["json","png","gif","mp4"]},"timeline":[{"kind":"appear","target":"ask","duration":0.5},{"kind":"appear","target":"knowledge","duration":0.5},{"kind":"appear","target":"answer","duration":0.5},{"kind":"draw_edge","target":"e1","duration":0.5},{"kind":"draw_edge","target":"e2","duration":0.5},{"kind":"highlight","target":"answer","duration":0.8},{"kind":"wait","duration":1}]}

def test_valid():
    assert validate_spec(copy.deepcopy(BASE))["schema_version"] == "0.2"

@pytest.mark.parametrize("mutation", [
    lambda d: d["nodes"].append({"id":"ask","label":"duplicate"}),
    lambda d: d["edges"][0].update({"to":"missing"}),
    lambda d: d["timeline"][0].update({"target":"missing"}),
    lambda d: d["timeline"][0].update({"duration":-1}),
    lambda d: d["output"].update({"width":1000}),
])
def test_rejected(mutation):
    data = copy.deepcopy(BASE)
    mutation(data)
    with pytest.raises(ValueError):
        validate_spec(data)
