#!/usr/bin/env python3
import requests
import json
import sys
import time

def fetch_api_data():
    """获取API数据"""
    url = "http://我不是.摸鱼儿.com"
    
    headers = {
        "User-Agent": "okhttp/4.9.0",
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30, verify=True)
        
        print(f"HTTP状态码: {response.status_code}")
        
        # 尝试解析JSON
        try:
            data = response.json()
            print("✓ 获取到JSON数据")
            return data
        except json.JSONDecodeError:
            # 如果不是JSON，直接返回文本
            print("⚠ 返回数据不是有效JSON，保存原始响应")
            return response.text
            
    except Exception as e:
        print(f"✗ 请求异常: {e}")
        return {"error": str(e), "status": "failed"}

def save_data(data):
    """保存数据到文件"""
    try:
        with open("moyu_data.json", "w", encoding="utf-8") as f:
            if isinstance(data, dict):
                json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                f.write(str(data))
        
        print("✓ 数据已保存到 moyu_data.json")
        return True
    except Exception as e:
        print(f"✗ 保存失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    data = fetch_api_data()
    save_data(data)


