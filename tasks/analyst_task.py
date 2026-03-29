from crewai import Task
from agents.analyst_agent import analyze_agent


get_stock_analysis = Task(
    description=(
        "Analyze the recent performance of the stock: {stock}. use the live stock information tool to retrieve. "
        "current price, percentage change, trading volume and other market data. Provide a summary of how the stock "
        "is performing today and highlight any key observations from the data."
    ),
    expected_output=(
        "A clear bullet point summary of \n"
        "- Current stock priec \n"
        "- Daily price change and percentage \n"
        "- Volume and volatitlity \n"
        "- Any immediate trends or observations"
    ),
    agent=analyze_agent
)