import typer
from typing import Optional,List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from phi.model.google import Gemini
from phi.embedder.google import GeminiEmbedder
import google.generativeai as genai




import os
from dotenv import load_dotenv
load_dotenv()

#os.environ["GROQ_API_KEY"] =os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "sk-dummy")
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"



knowledge_base=PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(collection="recipes_new_768",db_url=db_url,embedder=GeminiEmbedder(model="text-embedding-004")))

knowledge_base.load()

storage=PgAssistantStorage(table_name="pdf_assistant19",db_url=db_url) 

def pdf_assistant19(new: bool=False, user: str = "user"):
 run_id: Optional[str] = None
 
 if not new:
       existing_run_ids: List[str] = storage.get_all_run_ids(user)
       if len(existing_run_ids) > 0:
           run_id = existing_run_ids[0]

 assistant=Assistant(
     run_id=run_id,
     user_id=user,
     knowledge_base=knowledge_base,
     storage=storage,
      show_tool_calls=True,
       search_knowledge=False,
       read_chat_history=True,
       model=Gemini(id="gemini-2.0-flash"),
    markdown=True
 )
 if run_id is None:
        run_id = assistant.run_id
        print(f"Started Run: {run_id}\n")
 else:
        print(f"Continuing Run: {run_id}\n")

 while True:
        assistant.cli_app(markdown=True)

if __name__ == "__main__":
   typer.run(pdf_assistant19)




""" 
  docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16"""