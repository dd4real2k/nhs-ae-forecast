from fastapi import FastAPI, HTTPException
from api.schemas import PredictionRequest, PredictionResponse
from api.utils import load_model, prepare_input

app = FastAPI(title="NHS A&E Forecast API")

model = load_model()


@app.get("/")
def root():
    return {"message": "NHS A&E Forecast API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        input_df = prepare_input(request.model_dump())
        prediction = model.predict(input_df)[0]
        return PredictionResponse(predicted_attendance=float(prediction))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
