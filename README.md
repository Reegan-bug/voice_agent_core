# VoiceAgent-Core

Backend asíncrono y altamente resiliente desarrollado en FastAPI, diseñado para la orquestación de agentes de voz interactivos, validación estricta de datos conversacionales y persistencia atómica.

## Características Principales
* **Arquitectura Asincrónica:** Construido con FastAPI y Python para optimizar el rendimiento y la gestión de peticiones concurrentes de llamadas.
* **Validación de Esquemas:** Integración de esquemas estrictos con Pydantic para filtrar, limpiar y estructurar los datos extraídos por el agente antes de procesarlos.
* **Resiliencia y Manejo de Errores:** Implementación de bloques de control de excepciones, reintentos inteligentes (exponential backoff) ante fallos de red o tiempos de espera de la API.
* **Persistencia Segura:** Gestión de estados conversacionales y almacenamiento estructurado mediante SQLModel (compatible con SQLite y MySQL).

## Stack Tecnológico
* **Python 3.10+**
* **FastAPI:** Framework web asíncrono.
* **SQLModel / SQLite o MySQL:** Capa de persistencia.
* **Pydantic:** Validación de datos.

## Instalación y Ejecución Local
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Reegan-bug/voice_agent_core.git
   cd voice_agent_core