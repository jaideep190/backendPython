from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from .generate_image import generate_image

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/generate-image/")
async def generate_image_endpoint(input: TextInput):
    if not input.text:
        raise HTTPException(status_code=400, detail="No text provided")
    image_path = generate_image(input.text)
    return {"message": "Image generated successfully", "image_url": f"/images/{os.path.basename(image_path)}"}

@app.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = f"generated_images/{image_name}"
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
