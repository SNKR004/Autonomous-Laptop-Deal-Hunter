from crewai import Agent, LLM

llm = LLM(
    model="ollama/llama3.1",
    base_url="http://localhost:11434"
)

deal_analyst = Agent(
    role="Laptop Deal Analyst",
    goal=(
        "Find the best value products "
        "from scraped shopping data"
    ),
    backstory=(
        "Expert in laptops, GPUs, pricing, "
        "and spotting value-for-money deals."
    ),
    llm=llm,
    verbose=True
)