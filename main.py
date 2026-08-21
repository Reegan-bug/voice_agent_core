from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from sqlmodel import Session
from models import CallDataExtract, CallSession
from database import get_session, engine
import asyncio

app = FastAPI(title="VoiceAgent-Core API")

@app.post("/process-call/")
async def process_call(data: CallDataExtract):
    try:
        # Lógica previa de guardado que ya tenías
        return {"status": "success", "message": "Datos capturados y guardados correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el servidor: {str(e)}")


# --- NUEVO: ENDPOINT DE WEBSOCKET PARA STREAMING DE VOZ / TEXTO ---
@app.websocket("/ws/voice-call")
async def voice_call_websocket(websocket: WebSocket):
    await websocket.accept()
    print("🔌 Cliente conectado al canal de voz en tiempo real.")
    
    try:
        while True:
            # Recibimos el mensaje o chunk enviado por el cliente (simulando lo que dice el usuario)
            user_input = await websocket.receive_text()
            print(f"📥 Mensaje recibido del cliente: {user_input}")
            
            # Simulamos una respuesta del agente dividida en fragmentos (chunks) para imitar streaming
            agent_response_tokens = [
                "Entiendo", " perfectamente.", " Permíteme", " verificar", 
                " tus", " datos", " en", " el", " sistema", " MySQL."
            ]
            
            # Enviamos cada fragmento de forma asíncrona simulando el flujo de streaming de un LLM
            for token in agent_response_tokens:
                await websocket.send_text(token)
                await asyncio.sleep(0.1) # Pequeña pausa natural entre tokens
                
            # Enviamos un marcador de fin de turno
            await websocket.send_text("[DONE]")
            
    except WebSocketDisconnect:
        print("❌ Cliente desconectado de la llamada.")