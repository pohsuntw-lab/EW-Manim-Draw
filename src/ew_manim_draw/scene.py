"""Deterministic Manim scene consuming validated animation timeline."""
import os
from manim import *
from .model import load_spec

class FlowScene(Scene):
    spec_path = None

    def construct(self):
        spec = load_spec(self.spec_path)
        self.camera.background_color = WHITE
        nodes = spec["nodes"]
        step = min(3.2, 11.5 / max(len(nodes) - 1, 1))
        font = os.environ.get("EW_MANIM_FONT", "Noto Sans CJK TC")
        boxes = {}
        for i, node in enumerate(nodes):
            label = Text(node["label"], font=font, font_size=24, color=BLACK)
            if label.width > 2.1:
                label.scale_to_fit_width(2.1)
            rect = RoundedRectangle(width=2.45, height=1.25, corner_radius=0.16,
                                    color=BLUE_D, fill_color=BLUE_A, fill_opacity=0.25)
            label.move_to(rect.get_center())
            group = VGroup(rect, label)
            group.move_to(RIGHT * ((i - (len(nodes) - 1) / 2) * step))
            boxes[node["id"]] = group
        edges = {}
        for i, edge in enumerate(spec["edges"]):
            a, b = boxes[edge["from"]], boxes[edge["to"]]
            edges[edge.get("id", f"edge_{i}")] = Arrow(
                a.get_right(), b.get_left(), buff=0.08,
                color=BLUE_D, stroke_width=3, max_tip_length_to_length_ratio=0.15
            )
        for event in spec["timeline"]:
            kind, target, seconds = event["kind"], event.get("target"), event["duration"]
            if kind == "appear":
                self.play(FadeIn(boxes[target]), run_time=seconds)
            elif kind == "draw_edge":
                self.play(Create(edges[target]), run_time=seconds)
            elif kind == "highlight":
                self.play(Indicate(boxes[target], color=BLUE_D), run_time=seconds)
            else:
                self.wait(seconds)
