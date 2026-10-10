"""Strict, JSON-first animation specification validator (schema v0.2)."""
import json
import math
from pathlib import Path

KINDS = {"appear", "draw_edge", "highlight", "wait"}
LAYOUTS = {"horizontal"}
OUTPUTS = {"json", "png", "gif", "mp4"}

def validate_spec(data):
    if not isinstance(data, dict):
        raise ValueError("Root must be an object")
    if data.get("schema_version") != "0.2":
        raise ValueError("schema_version must be 0.2")
    title = data.get("title", "")
    locale = data.get("locale", "zh-TW")
    if not isinstance(title, str) or len(title) > 100:
        raise ValueError("Invalid title")
    if locale not in ("zh-TW", "zh-CN", "en"):
        raise ValueError("Unsupported locale")
    nodes, edges = data.get("nodes"), data.get("edges", [])
    if not isinstance(nodes, list) or not 1 <= len(nodes) <= 8:
        raise ValueError("Expected 1–8 nodes")
    if not isinstance(edges, list) or len(edges) > 20:
        raise ValueError("Expected at most 20 edges")
    ids = {}
    for i, node in enumerate(nodes):
        if not isinstance(node, dict) or not isinstance(node.get("id"), str) or not isinstance(node.get("label"), str):
            raise ValueError("Each node requires id and label")
        if not 1 <= len(node["id"]) <= 64 or not 1 <= len(node["label"]) <= 80 or node["id"] in ids:
            raise ValueError("Invalid or duplicate node")
        ids[node["id"]] = i
    edge_ids = set()
    for i, edge in enumerate(edges):
        if not isinstance(edge, dict) or edge.get("from") not in ids or edge.get("to") not in ids:
            raise ValueError("Unknown edge endpoint")
        if ids[edge["from"]] >= ids[edge["to"]]:
            raise ValueError("Only forward edges supported")
        edge_id = edge.get("id", f"edge_{i}")
        if not isinstance(edge_id, str) or not 1 <= len(edge_id) <= 64 or edge_id in ids or edge_id in edge_ids:
            raise ValueError("Invalid or duplicate edge id")
        edge_ids.add(edge_id)
    layout = data.get("layout", {"direction": "horizontal"})
    if not isinstance(layout, dict) or layout.get("direction") not in LAYOUTS:
        raise ValueError("Only horizontal layout supported")
    output = data.get("output", {"width": 1920, "height": 1080, "fps": 15, "formats": ["json"]})
    if not isinstance(output, dict):
        raise ValueError("Invalid output")
    width, height, fps = output.get("width"), output.get("height"), output.get("fps")
    if not isinstance(width, int) or not isinstance(height, int) or width < 320 or height < 180 or width > 3840 or height > 2160 or width * 9 != height * 16:
        raise ValueError("Output must be 16:9 and within bounds")
    if not isinstance(fps, int) or not 1 <= fps <= 60:
        raise ValueError("Invalid fps")
    formats = output.get("formats")
    if not isinstance(formats, list) or not formats or any(x not in OUTPUTS for x in formats):
        raise ValueError("Invalid output formats")
    timeline = data.get("timeline")
    if not isinstance(timeline, list) or not 1 <= len(timeline) <= 60:
        raise ValueError("Timeline must contain 1–60 events")
    duration = 0.0
    for event in timeline:
        if not isinstance(event, dict) or event.get("kind") not in KINDS:
            raise ValueError("Invalid animation event")
        kind, target, seconds = event["kind"], event.get("target"), event.get("duration")
        if isinstance(seconds, bool) or not isinstance(seconds, (int, float)) or not math.isfinite(seconds) or not 0.05 <= seconds <= 30:
            raise ValueError("Invalid event duration")
        if kind in ("appear", "highlight") and target not in ids:
            raise ValueError("Event references unknown node")
        if kind == "draw_edge" and target not in edge_ids:
            raise ValueError("Event references unknown edge")
        if kind == "wait" and target is not None:
            raise ValueError("Wait must not target an object")
        duration += seconds
    if duration > 180:
        raise ValueError("Animation exceeds 180 seconds")
    return data

def load_spec(path):
    return validate_spec(json.loads(Path(path).read_text(encoding="utf-8")))
