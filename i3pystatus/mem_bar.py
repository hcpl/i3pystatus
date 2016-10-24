from i3pystatus import IntervalModule
from psutil import virtual_memory
from i3pystatus.core.color import ColorRangeModule
from i3pystatus.core.util import make_bar


class MemBar(IntervalModule, ColorRangeModule):
    """
    Shows memory load as a bar.

    Requires `psutil`, `colour` (from PyPI)

    .. rubric:: Available formatters

    * `{used_mem_bar}`
    """

    format = "{used_mem_bar}"
    color = "#00FF00"
    warn_color = "#FFFF00"
    alert_color = "#FF0000"
    warn_percentage = 50
    alert_percentage = 80
    multi_colors = False

    def init(self):
        self.colors = self.get_hex_color_range(self.color, self.alert_color, 100)

    settings = (
        ("format", "Format string used for output"),
        ("warn_percentage", "Minimal percentage for warn state"),
        ("alert_percentage", "Minimal percentage for alert state"),
        ("color", "Default color"),
        ("warn_color", "Color used when warn percentage is exceeded"),
        ("alert_color", "Color used when alert percentage is exceeded"),
        ("multi_colors", "Whether to use range of colors from 'color' to 'alert_color' based on memory usage."),
    )

    def run(self):
        memory_usage = virtual_memory()

        if self.multi_colors:
            color = self.get_gradient(memory_usage.percent, self.colors)
        elif memory_usage.percent >= self.alert_percentage:
            color = self.alert_color
        elif memory_usage.percent >= self.warn_percentage:
            color = self.warn_color
        else:
            color = self.color

        self.output = {
            "full_text": self.format.format(
                used_mem_bar=make_bar(memory_usage.percent)),
            "color": color
        }
