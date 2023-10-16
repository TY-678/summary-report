# 資料處理程式 v1.0


## 版本資訊

- **版本號：** 1.0
- **最後更新日期：** 2023-10-16

這個 Python 程式允許使用者根據特定日期，從指定的資料夾中處理資料，並根據使用者的選擇，將結果以 CSV、JSON 或 TXT 格式輸出。


![image](https://github.com/TY-678/summary-report/blob/e6956df5d23450f00bc2fba3aa1df1ab63d9153f/summary_report_gui.png)

## 前置需求

- Python 3.x
- tkinter 函式庫（通常包含在標準 Python 發行版中）

## 使用方式

1. 複製 專案內容到您的電腦中。
2. 執行 summary_report.exe 執行檔或是 Python 腳本 `summary_report.py`。
3. 在提示時輸入日期，格式為 `YYYYMMDD`。
4. 使用提供的選擇按鈕選擇輸出格式（CSV、JSON 或 TXT）。
5. 點擊“計算”按鈕以處理資料。
6. 選擇將處理後的檔案保存的目錄。

## 檔案結構

- `summary_report.exe`：不需透過Python編譯器可直接執行的應用程式 。
- `summary_report.py`：包含 GUI 和資料處理邏輯的主要 Python 腳本。
- `README.md`：說明檔案，解釋程式的使用方法和目的。

## 程式運作原理

該程式根據提供的日期從指定的資料夾（AVI、II、R）中讀取資料。它計算並匯總資料，然後將結果以選擇的格式輸出。


## 開發者

- 開發者：TY-678
- 聯繫方式：tyyyy66@icloud.com


