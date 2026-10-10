import json
import pytest
from ew_manim_draw.model import load_spec

def test_valid(tmp_path):
    p = tmp_path / "ok.json"
    p.write_text(json.dumps({"nodes":[{"id":"a","label":"A"},{"id":"b","label":"B"}],"edges":[{"from":"a","to":"b"}]}))
    assert len(load_spec(p)["edges"]) == 1

def test_bad_edge(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text(json.dumps({"nodes":[{"id":"a","label":"A"}],"edges":[{"from":"a","to":"missing"}]}))
    with pytest.raises(ValueError):
        load_spec(p)
