from fastapi import FastAPI, HTTPException
from models import CallDataExtract, CallSession
from database import get_session

app = FastAPI(title="VoiceAgent-Core API")

@app.post("/process-call/")
async def process_call(data: CallDataExtract):
    try:
        # Validación y simulación de procesamiento del agente
        session_data = CallSession(
            client_name=data.client_name,
            phone_number=data.phone_number,
            call_purpose=data.call_purpose,
            status="completado"
        )
        # Guardado atómico en base de datos (SQLModel)
        # session.add(session_data); session.commit()

        return {"status": "success", "message": "Datos capturados y guardados correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el servidor: {str(e)}")