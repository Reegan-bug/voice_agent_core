import time

def get_ai_response_with_retry(prompt: str, max_retries: int = 3):
    attempts = 0
    while attempts < max_retries:
        try:
            # Simulación o llamada real a la API de OpenAI/Gemini con timeout
            # response = openai.chat.completions.create(...)
            return "Respuesta procesada exitosamente por el agente"
        except Exception as e:
            attempts += 1
            if attempts == max_retries:
                raise Exception(f"Fallo crítico tras {max_retries} intentos: {str(e)}")
            time.sleep(2 ** attempts) # Backoff exponencial