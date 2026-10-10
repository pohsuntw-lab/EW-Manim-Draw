"""Render validated JSON using a controlled Manim scene."""
import os
from manim import *
from .model import load_spec

class FlowScene(Scene):
    spec_path = None

    def construct(self):
        if not self.spec_path:
            raise ValueError("spec_path required")
        spec = load_spec(self.spec_path)
        self.camera.background_color = WHITE
        nodes = spec["nodes"]
        n = len(nodes)
        step = min(3.2, 11.5 / max(n - 1, 1))
        boxes = {}
        font = os.environ.get("EW_MANIM_FONT", "Noto Sans CJK TC")
        for i, node in enumerate(nodes):
            label = Text(node["label"], font=font, font_size=24, color=BLACK)
            if label.width > 2.1:
                label.scale_to_fit_width(2.1)
            rect = RoundedRectangle(width=2.45, height=1.25, corner_radius=0.16,
                                    color=BLUE_D, fill_color=BLUE_A, fill_opacity=0.25)
            label.move_to(rect.get_center())
            group = VGroup(rect, label)
            group.move_to(RIGHT * ((i - (n - 1) / 2) * step))
            boxes[node["id"]] = group
        for node in nodes:
            self.play(FadeIn(boxes[node["id"]]), run_time=0.45)
        for edge in spec["edges"]:
            a, b = boxes[edge["from"]], boxes[edge["to"]]
            arrow = Arrow(a.get_right(), b.get_left(), buff=0.08,
                          color=BLUE_D, stroke_width=3,
                          max_tip_length_to_length_ratio=0.15)
            self.play(Create(arrow), run_time=0.5)
        self.wait(1)
