# consuming_agent.py
from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent


# 建立遠端代理的參考
alert_planner_agent = RemoteA2aAgent(
    name="alert_query_planner_remote",
    description="遠端的Graylog警示分析代理程式",
    agent_card="http://localhost:8001/.well-known/agent.json"
)

# 建立主要的消費者代理
root_agent = Agent(
    model="gemini-2.0-flash",
    name="test_consumer",
    instruction="""
    你是一個測試代理，專門用來測試 Graylog 警示分析功能。
    當用戶提供 Graylog 警示資訊時，請將任務委派給 alert_query_planner_remote 代理處理。
    """,
    sub_agents=[alert_planner_agent]
)
