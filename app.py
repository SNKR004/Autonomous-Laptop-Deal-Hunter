from crewai import Task, Crew, Process
from scraper import scrape_flipkart
from agents import deal_analyst

query = "gaming laptop RTX"

products = scrape_flipkart(query)

formatted_products = "\n".join(
    [
        f"{p['title']} | {p['price']}"
        for p in products
    ]
)

analysis_task = Task(
    description=f"""
    Analyze these products and identify:

    1. Best overall value
    2. Best budget option
    3. Suspicious/bad listings
    4. Which laptops are strongest for gaming

    Products:
    {formatted_products}
    """,
    expected_output="Detailed laptop recommendations",
    agent=deal_analyst
)

crew = Crew(
    agents=[deal_analyst],
    tasks=[analysis_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\nFINAL RESULT:\n")
print(result)