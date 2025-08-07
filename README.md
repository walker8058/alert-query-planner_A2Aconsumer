# Alert Query Planner A2A Consumer

這是一個基於 Google ADK (Agent Development Kit) 的 Agent-to-Agent (A2A) 消費者代理項目，專門用於測試和消費 Graylog 警示分析功能。

## 專案概述

本項目實現了一個消費者代理，能夠與遠端的 Graylog 警示分析代理進行通信。主要功能包括：

- 接收和處理 Graylog 警示資訊
- 將任務委派給遠端的警示查詢規劃代理
- 提供測試環境用於驗證 A2A 通信功能

## 專案結構

```
alert-query-planner_A2Aconsumer/
├── agent/
│   ├── __init__.py
│   └── agent.py          # 主要的代理實現
├── requirements.txt      # Python 依賴套件
├── .gitignore           # Git 忽略文件配置
├── .env                 # 環境變數配置
└── README.md            # 專案說明文件
```

## 功能特色

### 🤖 A2A 代理架構
- **消費者代理**: `test_consumer` - 主要的測試代理
- **遠端代理**: `alert_query_planner_remote` - 遠端 Graylog 警示分析代理

### 🔗 遠端代理整合
- 透過 Agent Card 配置遠端代理連接
- 支援跨服務的代理通信
- 自動任務委派和結果處理

### 🎯 Graylog 警示處理
- 專門針對 Graylog 警示資訊進行分析
- 智能查詢規劃和執行
- 測試驗證功能

## 安裝和設定

### 1. 環境需求

- Python 3.8+
- Google ADK
- 網路連接至遠端代理服務

### 2. 安裝依賴

```bash
# 建立虛擬環境
python -m venv .venv

# 啟動虛擬環境 (Windows)
.venv\Scripts\activate

# 安裝依賴套件
pip install -r requirements.txt
```

### 3. 環境配置

確保遠端代理服務正在運行：
- 遠端代理服務地址: `http://localhost:8001`
- Agent Card 端點: `http://localhost:8001/.well-known/agent.json`

### 4. 運行代理

```python
from agent.agent import root_agent

# 啟動消費者代理
root_agent.run()
```

## 使用方法

### 基本用法

1. **啟動代理**:
   ```python
   from agent.agent import root_agent
   root_agent.run()
   ```

2. **發送 Graylog 警示**:
   當用戶提供 Graylog 警示資訊時，代理會自動將任務委派給遠端的 `alert_query_planner_remote` 代理進行處理。

### 代理配置

- **模型**: Gemini 2.0 Flash
- **名稱**: test_consumer
- **功能**: 測試 Graylog 警示分析功能
- **子代理**: alert_query_planner_remote

## API 參考

### RemoteA2aAgent 配置

```python
alert_planner_agent = RemoteA2aAgent(
    name="alert_query_planner_remote",
    description="遠端的Graylog警示分析代理程式",
    agent_card="http://localhost:8001/.well-known/agent.json"
)
```

### Agent 配置

```python
root_agent = Agent(
    model="gemini-2.0-flash",
    name="test_consumer",
    instruction="...",
    sub_agents=[alert_planner_agent]
)
```

## 開發指南

### 程式碼結構

- `agent/agent.py`: 主要代理實現
- `agent/__init__.py`: 模組初始化

### 測試

專案包含測試代理，可用於驗證：
- A2A 通信功能
- Graylog 警示處理流程
- 遠端代理整合

### 擴展功能

要添加新功能，可以：
1. 修改代理指令 (`instruction`)
2. 添加新的子代理
3. 自定義警示處理邏輯

## 故障排除

### 常見問題

1. **無法連接遠端代理**
   - 檢查遠端服務是否正在運行
   - 確認網路連接和防火牆設定
   - 驗證 Agent Card URL 是否正確

2. **依賴套件錯誤**
   - 確保已安裝所有 requirements.txt 中的套件
   - 檢查 Python 版本相容性

3. **代理通信失敗**
   - 檢查代理配置
   - 驗證 Agent Card 格式
   - 確認遠端代理服務狀態

## 授權

本專案使用 [LICENSE] 授權。

## 貢獻

歡迎提交 Issue 和 Pull Request 來改善這個專案。

## 聯絡方式

如有問題或建議，請聯絡專案維護者。

---

**注意**: 請確保遠端代理服務在使用前已正確配置和啟動。
