from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class GenerationRequest(BaseModel):
    type: str
    content: dict

@app.post("/generate/")
async def generate(request: GenerationRequest):
    try:
        model_type = request.type.lower()
        content = request.content
        # Here, we would invoke the Danbri AI model to generate content.
        # This is a placeholder for the actual model invocation logic.
        if model_type == "website":
            return {"message": "Website generated successfully", "content": content}
        elif model_type == "app":
            return {"message": "App generated successfully", "content": content}
        elif model_type == "graphic":
            return {"message": "Graphic generated successfully", "content": content}
        elif model_type == "video":
            return {"message": "Video generated successfully", "content": content}
        else:
            raise HTTPException(status_code=400, detail="Invalid generation type")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the Danbri AI FastAPI service! Use the /generate endpoint to create content."}