from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool
import json
import os
from lighthouseweb3 import Lighthouse
from pydantic import BaseModel, Field

class DataHash(BaseModel):
    """Data model"""
    cid: str = Field(..., description="CID of the report")

@tool("Lighthouse Storage Tool")
def lighthouse_storage_tool(file_path: str) -> str:
    """Stores veterinary analysis data on Filecoin via Lighthouse"""
    try:
        lighthouse_api_key = os.getenv("LIGHTHOUSE_API_KEY")
        lh = Lighthouse(token=lighthouse_api_key)
        response = lh.upload(file_path)
        return response.get('data', {}).get('Hash', 'Upload failed')
    except Exception as e:
        print(f"Error uploading to Lighthouse: {e}")
        return 'Upload failed'

@CrewBase
class VeterinaryInsightsAI:
    """VeterinaryInsightsAI crew for analyzing cat treatment data"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def medical_researcher(self) -> Agent:
        """Reads cat patient data from a JSON file and analyzes it."""
        json_path = os.path.join(os.path.dirname(__file__), "../../cat_patients.json")  # Correct path

        try:
            with open(json_path, "r") as file:
                data = json.load(file)  # Load JSON data
                print("✅ Loaded cat patient data successfully!")  # Debugging info
        except Exception as e:
            print(f"❌ Error reading JSON file: {e}")
            data = {}

        return Agent(
            config=self.agents_config['medical_researcher'],
            tools=[],  # No need for cat_data_reader
            verbose=True
        )

    @agent
    def treatment_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['treatment_analyst'],
            verbose=True
        )

    @agent
    def data_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['data_coordinator'],
            tools=[],
            verbose=True,
            max_iter=1
        )

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_task'])

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='veterinary_analysis_report.md'
        )

    @task
    def data_organization_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_organization_task'],
            output_json=DataHash
        )

    @crew
    def crew(self) -> Crew:
        """Creates the VeterinaryInsightsAI crew"""
        return Crew(
            agents=[
                self.medical_researcher(),
                self.treatment_analyst(),
                self.data_coordinator()
            ],
            tasks=[
                self.analysis_task(),
                self.reporting_task(),
                self.data_organization_task()
            ],
            process=Process.sequential,
            verbose=True,
        )