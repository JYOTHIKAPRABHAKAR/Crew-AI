from crewai import Agent, Task, Crew
from gemini_llm import GeminiLLM

# Create Gemini instance
llm = GeminiLLM(api_key="AIzaSyAlqRJ7PMRK7Aj0qngoKSce2c6JyTxCzzQ")

# Define agents
# Define agents
destination_researcher = Agent(
    role='Destination Researcher',
    goal='Find best places to visit based on user interests and season',
    backstory='A travel expert who knows all trending and hidden spots.',
    llm=llm
)

itinerary_planner = Agent(
    role='Itinerary Planner',
    goal='Create a fun and balanced day-wise travel plan',
    backstory='A seasoned tour guide who loves planning perfect days.',
    llm=llm
)

# Define tasks
task_research_destinations = Task(
    description='Suggest 3 travel destinations for a 3-day weekend in July in India, good for nature and relaxation.',
    agent=destination_researcher,
    expected_output='List of 3 destinations with a short description of each.'
)

task_create_itinerary = Task(
    description='Using the selected destination, make a 3-day itinerary including places to visit, food spots, and rest time.',
    agent=itinerary_planner,
    expected_output='A detailed 3-day itinerary with morning, afternoon, and evening plans.'
)


crew = Crew(
    agents=[destination_researcher, itinerary_planner],
    tasks=[task_research_destinations, task_create_itinerary]
)

result = crew.kickoff()
print(result)
