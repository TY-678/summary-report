import os
import csv
import json
import tkinter as tk
from tkinter import filedialog

def parse_folder(folder_path):
    # 存儲資料的字典
    all_data = {}
    
    # 取得資料夾中的所有檔案
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # 遍歷每個檔案
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        
        # 讀取檔案中的資料
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            lines = file.readlines()
        
        # 從第14行開始的資料加總
        for line in lines[13:]:
            # 檢查行是否包含冒號
            if ':' in line:
                key, value = line.strip().split(':')
                key = key.strip()  # 清理項目名稱前後的空格
                try:
                    total_value = float(value.strip())  # 將值轉換為數字
                except ValueError:
                    total_value = 0  # 如果無法轉換為數字，將值設為0
                
                # 將加總結果儲存到字典中
                if key in all_data:
                    all_data[key] += total_value
                else:
                    all_data[key] = total_value
    all_data['UPH (pcs/h)'] = '{:.3f}'.format(all_data['UPH (pcs/h)'] / len(files))
    all_data['OVERALL YIELD'] = '{:.3f}'.format(all_data['NUMBER OF DEVICES Passed'] / all_data['NUMBER OF DEVICES INSPECTED'] * 100)
    all_data['PROCESS YIELD'] = '{:.3f}'.format(all_data['NUMBER OF DEVICES Failed'] / all_data['NUMBER OF DEVICES INSPECTED'] * 100)

    
    return all_data
#資料輸出成檔案
def on_calculate():
    # 取得使用者輸入的日期
    date = entry.get()
    
    # 構建資料夾路徑
    folder_path_avi = f'/Users/ty/Desktop/env_python_391/AVI_report/summary/{date}/AVI'
    folder_path_ii = f'/Users/ty/Desktop/env_python_391/AVI_report/summary/{date}/II'
    folder_path_r = f'/Users/ty/Desktop/env_python_391/AVI_report/summary/{date}/R'

    # 呼叫函數，取得資料
    avi_data = parse_folder(folder_path_avi)
    ii_data = parse_folder(folder_path_ii)
    r_data = parse_folder(folder_path_r)
    
    # 選擇輸出格式
    output_format = format_var.get()
    
    # 選擇儲存路徑
    output_folder = filedialog.askdirectory()
    if not output_folder:
        return  # 如果使用者取消選擇，不進行輸出
    
    # 輸出結果
    if output_format == "csv":
        with open(os.path.join(output_folder, f"{date}_AVI.csv"), 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for key, value in avi_data.items():
                csv_writer.writerow([key, value])
        with open(os.path.join(output_folder, f"{date}_II.csv"), 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for key, value in ii_data.items():
                csv_writer.writerow([key, value])
        with open(os.path.join(output_folder, f"{date}_R.csv"), 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for key, value in r_data.items():
                csv_writer.writerow([key, value])
        
    elif output_format == "json":
        with open(os.path.join(output_folder, f"{date}_AVI.json"), 'w', encoding='utf-8') as jsonfile:
            json.dump(avi_data, jsonfile, indent=4)
        with open(os.path.join(output_folder, f"{date}_II.json"), 'w', encoding='utf-8') as jsonfile:
            json.dump(ii_data, jsonfile, indent=4)
        with open(os.path.join(output_folder, f"{date}_R.json"), 'w', encoding='utf-8') as jsonfile:
            json.dump(r_data, jsonfile, indent=4)

    elif output_format == "txt":
        with open(os.path.join(output_folder, f"{date}_AVI.txt"), 'w', encoding='utf-8') as txtfile:
            for line in avi_data:
                txtfile.write("{:35s}:{:>10}\n".format(line, avi_data[line]))
        with open(os.path.join(output_folder, f"{date}_II.txt"), 'w', encoding='utf-8') as txtfile:
            for line in ii_data:
                txtfile.write("{:35s}:{:>10}\n".format(line, ii_data[line]))
        with open(os.path.join(output_folder, f"{date}_R.txt"), 'w', encoding='utf-8') as txtfile:
            for line in r_data:
                txtfile.write("{:35s}:{:>10}\n".format(line, r_data[line]))

    
    # 顯示完成訊息
    result_label.config(text=f"資料已輸出至 {output_folder}")

# 建立GUI視窗
root = tk.Tk()
root.title("資料處理程式")

# 使用者輸入框
entry_label = tk.Label(root, text="請輸入日期（格式：YYYYMMDD）:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# 選擇輸出格式的Radiobutton
format_var = tk.StringVar(value="csv")  # 預設選擇CSV
csv_radio = tk.Radiobutton(root, text="CSV", variable=format_var, value="csv")
json_radio = tk.Radiobutton(root, text="JSON", variable=format_var, value="json")
txt_radio = tk.Radiobutton(root, text="TXT", variable=format_var, value="txt")
csv_radio.pack()
json_radio.pack()
txt_radio.pack()

# 計算按鈕
calculate_button = tk.Button(root, text="計算", command=on_calculate)
calculate_button.pack()

# 顯示結果的標籤
result_label = tk.Label(root, text="")
result_label.pack()

# 啟動GUI主迴圈
root.mainloop()
