from i3pystatus import IntervalModule


class Temperature(IntervalModule):
    """
    Shows CPU temperature of Intel processors

    AMD is currently not supported as they can only report a relative temperature, which is pretty useless

    .. rubric:: Available formatters

    `{temp}` — CPU temperature in degree Celcius
    """

    settings = (
        "format",
        ('display_if', 'Snippet that gets evaluated. If true, displays the module output'),
        ("color", "Default color"),
        ("file", "File from which temperature is retrieved"),
        ("alert_temp", "Temperature, above which is dangerous to exceed"),
        ("alert_color", "Color used when alert temperature is exceeded"),
    )
    format = "{temp} °C"
    color = "#FFFFFF"
    file = "/sys/class/thermal/thermal_zone0/temp"
    alert_temp = 90
    alert_color = "#FF0000"
    display_if = 'True'

    def run(self):
        with open(self.file, "r") as f:
            temp = float(f.read().strip()) / 1000

        if eval(self.display_if):
            self.output = {
                "full_text": self.format.format(temp=temp),
                "color": self.color if temp < self.alert_temp else self.alert_color,
            }
