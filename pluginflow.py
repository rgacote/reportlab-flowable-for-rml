#!/usr/bin/env python3.11
"""Example ReportLab plugInFlowable for RML template."""
# Copyright © 2023 Appropriate Solutions, Inc. All rights reserved.

from io import BytesIO
from pathlib import Path

import matplotlib.pyplot as plt
from lxml.etree import XMLSyntaxError
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Flowable
from rlextra.rml2pdf import rml2pdf
from svglib.svglib import svg2rlg


class SvgFlowable(Flowable):
    """Convert byte stream containing SVG into a Reportlab Flowable."""

    def __init__(self, svg: BytesIO) -> None:
        """Convert SVG to RML drawing on initializtion."""
        svg.seek(0)
        self.drawing: Drawing = svg2rlg(svg)
        self.width: int = self.drawing.minWidth()
        self.height: int = self.drawing.height
        self.drawing.setProperties({"vAlign": "CENTER", "hAlign": "CENTER"})

    def wrap(self, *_args):
        """Return diagram size."""
        return (self.width, self.height)

    def draw(self) -> None:
        """Render the chart."""
        renderPDF.draw(self.drawing, self.canv, 0, 0)


def create_pdf():
    """Create a ReportLab PDF."""
    rml_path = Path(__file__).resolve().parent / "template.rml"
    rml = rml_path.read_text()

    try:
        rml2pdf.go(
            rml,
            outputFileName="PluginFlow.pdf",
        )
    except (ValueError, XMLSyntaxError) as err:
        print(str(err))


def chart(title) -> SvgFlowable:
    """Generate a Matplotlib chart wrapped in a ReportLab Flowable."""
    plt.style.use("ggplot")
    plt.figure(figsize=(3, 2))
    x = ["A", "B", "C"]
    x_pos = [i for i, _ in enumerate(x)]
    y = [10, 20, 30]
    plt.bar(x, y)
    plt.xlabel("Alpha")
    plt.ylabel("Numeric")
    plt.xticks(x_pos, x)
    plt.title(title)
    # Save SVG in memory.
    svg = BytesIO()
    plt.savefig(svg, format="svg")
    return SvgFlowable(svg)


if __name__ == "__main__":
    create_pdf()
