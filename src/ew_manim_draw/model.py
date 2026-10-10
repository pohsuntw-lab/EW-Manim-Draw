"""Validate declarative flow JSON."""
import json
from pathlib import Path

def load_spec(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Root must be an object")
    nodes, edges = data.get("nodes"), data.get("edges", [])
    if not isinstance(nodes, list) or not 1 <= len(nodes) <= 8:
        raise ValueError("v0.1 supports 1–8 nodes")
    if not isinstance(edges, list) or len(edges) > 20:
        raise ValueError("edges must be a list of at most 20 items")
    ids = {}
    for index, node in enumerate(nodes):
        if not isinstance(node, dict) or not isinstance(node.get("id"), str) or not isinstance(node.get("label"), str):
            raise ValueError("Each node requires string id and label")
        if not 1 <= len(node["id"]) <= 64 or not 1 <= len(node["label"]) <= 80 or node["id"] in ids:
            raise ValueError("Invalid, duplicate or oversized node")
        ids[node["id"]] = index
    for edge in edges:
        if not isinstance(edge, dict) or edge.get("from") not in ids or edge.get("to") not in ids:
            raise ValueError("Edge references unknown node")
        if ids[edge["from"]] >= ids[edge["to"]]:
            raise ValueError("v0.1 supports only forward left-to-right edges")
    return {"title": str(data.get("title", ""))[:100], "nodes": nodes, "edges": edges}
