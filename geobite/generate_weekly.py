#!/usr/bin/env python3
"""
GeoBite 每週課程生成器
一次過生成 monday 至 friday 課程

用法: python3 generate_weekly.py
"""

import subprocess
import sys
import os

WEEKLY_TOPICS = {
    "monday": "美中科技戰：半導體脫鉤新常態",
    "tuesday": "歐洲能源危機：普京時代的終結與啟示", 
    "wednesday": "南中國海主權爭端：亞洲版的權力遊戲",
    "thursday": "中美金融戰：人民幣國際化之路",
    "friday": "台海局勢：全球供應鏈的心臟地帶",
}

def main():
    print("🌍 GeoBite 每週課程生成器")
    print("=" * 40)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    generator = os.path.join(script_dir, "generate_course.py")
    
    for day, topic in WEEKLY_TOPICS.items():
        print(f"\n📅 {day.upper()}: {topic}")
        result = subprocess.run(
            [sys.executable, generator, topic, day],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"   ✅ 完成")
        else:
            print(f"   ❌ 失敗: {result.stderr}")
    
    print("\n" + "=" * 40)
    print("🎉 整週課程生成完畢！")
    print("\n每週 topics:")
    for day, topic in WEEKLY_TOPICS.items():
        print(f"  • {day}: {topic}")

if __name__ == "__main__":
    main()
