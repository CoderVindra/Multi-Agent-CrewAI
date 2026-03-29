from dotenv import load_dotenv
from crew import stock_crew


# Load env 
load_dotenv()


def run(stock : str):
    result = stock_crew.kickoff(inputs={"stock": stock})
    print("Answer : \n")
    print(result)

if __name__ == "__main__":
    run("APPLE")