from crewai import Crew
from agents.trader_agent import trader_agent
from agents.analyst_agent import analyze_agent
from tasks.analyst_task import get_stock_analysis
from tasks.trade_task import trade_decision

stock_crew = Crew(
    agents=[analyze_agent, trader_agent],
    tasks=[get_stock_analysis, trade_decision],
    verbose=True
)