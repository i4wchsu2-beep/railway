# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:25:01 2026

@author: 402
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

# 車站代碼字典
STATION_CODES = {
    "基隆": "1000-基隆", "七堵": "1000-七堵", "南港": "1000-南港", "松山": "1000-松山",
    "臺北": "1000-臺北", "台北": "1000-臺北", "萬華": "1010-萬華", "板橋": "1020-板橋",
    "樹林": "1030-樹林", "桃園": "1080-桃園", "中壢": "1100-中壢", "楊梅": "1120-楊梅",
    "新竹": "1210-新竹", "竹北": "1180-竹北", "竹南": "1230-竹南", "苗栗": "1250-苗栗",
    "台中": "1319-台中", "臺中": "1319-臺中", "彰化": "1324-彰化", "嘉義": "1418-嘉義",
    "台南": "1514-台南", "臺南": "1514-臺南", "高雄": "1600-高雄", "屏東": "1632-屏東",
    "宜蘭": "1700-宜蘭", "花蓮": "1800-花蓮", "台東": "1900-台東"
}

def get_station_code(name):
    clean_name = name.strip()
    return STATION_CODES.get(clean_name, f"0000-{clean_name}")

class RailwayApp(App):
    def build(self):
        self.title = "台鐵時刻表查詢"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=8)

        # 輸入區：起終站
        layout.add_widget(Label(text="起終站 (如: 竹北-臺北 或 輸入 1 反轉):", size_hint_y=None, height=30))
        self.station_input = TextInput(text="竹北-臺北", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.station_input)

        # 輸入區：日期
        now = datetime.now()
        default_date = now.strftime("%Y/%m/%d")
        layout.add_widget(Label(text=f"日期 (格式 YYYY/MM/DD):", size_hint_y=None, height=30))
        self.date_input = TextInput(text=default_date, multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.date_input)

        # 查詢按鈕
        search_btn = Button(text="🔍 開始查詢時刻表", size_hint_y=None, height=50, background_color=(0.2, 0.6, 1, 1))
        search_btn.bind(on_press=self.query_railway)
        layout.add_widget(search_btn)

        # 顯示結果的滾動區域
        self.result_label = Label(text="請點擊下方按鈕開始查詢...", size_hint_y=None, markup=True)
        self.result_label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        
        scroll = ScrollView()
        scroll.add_widget(self.result_label)
        layout.add_widget(scroll)

        return layout

    def query_railway(self, instance):
        station_text = self.station_input.text.strip()
        
        # 判斷起終站
        if station_text == "" or station_text == "竹北-臺北":
            start_station, end_station = STATION_CODES["竹北"], STATION_CODES["臺北"]
        elif station_text == "1":
            start_station, end_station = STATION_CODES["臺北"], STATION_CODES["竹北"]
        elif "-" in station_text:
            s_name, e_name = station_text.split("-", 1)
            start_station = get_station_code(s_name)
            end_station = get_station_code(e_name)
        else:
            start_station, end_station = STATION_CODES["竹北"], STATION_CODES["臺北"]

        ride_date = self.date_input.text.strip()
        now = datetime.now()
        start_time = now.strftime("%H:%M")
        end_time = (now + timedelta(hours=2)).strftime("%H:%M")

        self.result_label.text = "⏳ 正在查詢中..."

        # 發送 Request
        url = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime"
        headers = {"User-Agent": "Mozilla/5.0"}
        post_data = {
            "startStation": start_station,
            "endStation": end_station,
            "transfer": "ONE",
            "rideDate": ride_date,
            "startOrEndTime": "true",
            "startTime": start_time,
            "endTime": end_time,
            "trainTypeList": "ALL",
            "query": "查詢"
        }

        try:
            r = requests.post(url, data=post_data, headers=headers, timeout=10)
            r.encoding = "utf8"
            soup = BeautifulSoup(r.text, "html.parser")
            tag_table = soup.find("table", class_="itinerary-controls") or soup.find("table", class_="table")

            if not tag_table:
                self.result_label.text = "❌ 找不到時刻表資料。"
                return

            trip_rows = tag_table.find_all("tr", class_="trip-column") or tag_table.find_all("tr")[1:]
            
            output = [f"📌 查詢：{start_station.split('-')[-1]} ➔ {end_station.split('-')[-1]}\n"]
            for row in trip_rows:
                cells = [ " ".join(cell.text.split()) for cell in row.find_all(["td", "th"]) ]
                if cells:
                    output.append(" | ".join(cells))

            self.result_label.text = "\n\n".join(output) if len(output) > 1 else "ℹ️ 該時段無班次。"

        except Exception as e:
            self.result_label.text = f"❌ 發生錯誤: {str(e)}"

if __name__ == "__main__":
    RailwayApp().run()