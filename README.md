# VoiceAgent-Core

Backend asíncrono y altamente resiliente desarrollado en FastAPI, diseñado para la orquestación de agentes de voz interactivos, manejo de canales bidireccionales en tiempo real, validación estricta de datos conversacionales y persistencia atómica.

## Características Principales
* **Arquitectura Asincrónica y WebSockets:** Implementación de canales bidireccionales en tiempo real (`/ws/voice-call`) para la transmisión de datos y simulación de flujos de voz conversacionales.
* **Validación de Esquemas:** Integración de esquemas estrictos con Pydantic para filtrar, limpiar y estructurar los datos extraídos por el agente antes de procesarlos.
* **Resiliencia y Manejo de Errores:** Implementación de bloques de control de excepciones y reintentos inteligentes (exponential backoff) ante fallos de red o tiempos de espera de la API.
* **Persistencia Segura:** Gestión de estados conversacionales y almacenamiento estructurado mediante SQLModel (compatible con SQLite y MySQL).

## Stack Tecnológico
* **Python 3.10+**
* **FastAPI:** Framework web asíncrono y soporte para WebSockets.
* **SQLModel / SQLite o MySQL:** Capa de persistencia.
* **Pydantic:** Validación estricta de esquemas de datos.

## Instalación y Ejecución Local
1. Clona el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/voice_agent_core.git](https://github.com/tu-usuario/voice_agent_core.git)
   cd voice_agent_core