import warnings
from crew import support_report_crew
from IPython.display import display, Markdown

warnings.filterwarnings('ignore')

support_crew = support_report_crew
result = support_crew.kickoff()

display(Markdown(result.raw))