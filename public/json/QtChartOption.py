import copy
import json


class OptionsModifier:
    def __init__(self):
        self.options ={
          "width": 800,
          "height": 1200,
          "timeScale": {"timeVisible": "true", "secondsVisible": "false"},
          "priceScale": {"autoScale": "true", "scaleMargins": {"top": 0.1, "bottom": 0.2}},
          "priceFormatter": {"style": "currency", "currency": "KRW"},
          "movingAverages": {
              "ma5": {"color": "rgba(255, 0, 0, 1)", "lineWidth": 2, "priceLineVisible": "false"},
              "ma10": {"color": "rgba(0, 0, 255, 1)", "lineWidth": 2, "priceLineVisible": "false"},
              "ma30": {"color": "rgba(0, 244, 255, 1)", "lineWidth": 2, "priceLineVisible": "false"},
              "ma40": {"color": "rgba(0, 244, 255, 1)", "lineWidth": 2, "priceLineVisible": "false"},
              "ma50": {"color": "rgba(0, 244, 255, 1)", "lineWidth": 2, "priceLineVisible": "false"},
              "ma60": {"color": "rgba(0, 244, 255, 1)", "lineWidth": 2, "priceLineVisible": "false"},
              "ma70": {"color": "rgba(0, 244, 255, 1)", "lineWidth": 2, "priceLineVisible": "false"},
              "ma80": {"color": "rgba(0, 244, 255, 1)", "lineWidth": 2, "priceLineVisible": "false"},
              "ma90": {"color": "rgba(0, 244, 255, 1)", "lineWidth": 2, "priceLineVisible": "false"},
              "ma100": {"color": "rgba(0, 244, 255, 1)", "lineWidth": 12, "priceLineVisible": "false"},
              "ma300": {"color": "rgba(0, 0, 255, 1)", "lineWidth": 12, "priceLineVisible": "false"},
          },
          "crosshair": {
              "vertLine": {"width": 8, "color": "#C3BCDB44", "labelBackgroundColor": "#9B7DFF"},
              "horzLine": {"color": "#9B7DFF", "labelBackgroundColor": "#9B7DFF"},
          },
        "font": {
            "layout": {
                "fontFamily": "'Roboto', sans-serif"
            }
        },
      }


    def modify_options(self):
        modified_options = copy.deepcopy(self.options)

        for i in range(5, 301, 5):
            ma_key = f"ma{i}"
            if ma_key not in modified_options["movingAverages"]:
                modified_options["movingAverages"][ma_key] = {
                    "color": "rgba(0, 244, 255, 1)",
                    "lineWidth": 2,
                    "priceLineVisible": "false",
                }

        modified_options["movingAverages"] = dict(
            sorted(modified_options["movingAverages"].items(), key=lambda x: int(x[0][2:]))
        )

        return modified_options

    def write_to_json(self, file_path):
        modified_options = self.modify_options()
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(modified_options, file, indent=4)

        return modified_options


chartOptions=OptionsModifier().modify_options()
OptionsModifier().write_to_json("/Users/hg/DEV/WebDocuments/public/json/QtChartOption.json")

print(chartOptions)