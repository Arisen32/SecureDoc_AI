# SecureDoc AI Engine – Multi-Tenant RAG API

API REST multi-inquilino (*multi-tenant*) containerizada desarrollada en **Django REST Framework** para la gestión segura de documentos y consultas con **RAG (Retrieval-Augmented Generation)** integrando **Azure AI Search**.

## 🚀 Arquitectura y Características

- **Autenticación Segura**: Implementación de JWT (JSON Web Tokens) con `simplejwt` bajo encabezados `Authorization: Bearer`.
- **Aislamiento Multi-Tenant**: Cadena de seguridad donde los documentos e índices están vinculados al `owner` (usuario), garantizando privacidad de datos (Principios SC-100).
- **Procesamiento de Archivos**: Ingesta e indexación de archivos en formato `multipart/form-data`.
- **Motor RAG con Azure AI Search**: Búsqueda vectorial y semántica para generar respuestas contextuales en tiempo real a partir de los documentos del usuario.
- **Entorno Containerizado**: Configuración lista para despliegue mediante Docker y Docker Compose.

---

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python, Django, Django REST Framework (DRF)
- **Autenticación**: PyJWT / `djangorestframework-simplejwt`
- **IA / Búsqueda**: Azure AI Search, Azure OpenAI / RAG Engine
- **Base de Datos**: PostgreSQL / SQLite (Desarrollo)
- **Despliegue & DevOps**: Docker, Docker Compose, Git

---

## 📋 Endpoints Principales

### 🔑 Autenticación
| Método | Endpoint | Descripción | Requiere Auth |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/v1/auth/login/` | Inicia sesión y obtiene los tokens `access` y `refresh`. | No |

### 📄 Gestión de Documentos
| Método | Endpoint | Descripción | Requiere Auth |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/v1/documents/` | Lista los documentos pertenecientes al usuario autenticado. | Sí (`Bearer`) |
| `POST` | `/api/v1/documents/` | Subida de archivos (`multipart/form-data` con `title` y `file`). | Sí (`Bearer`) |

### 🤖 Motor de IA (RAG)
| Método | Endpoint | Descripción | Requiere Auth |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/v1/ai/query/` | Envía una pregunta en JSON (`{"query": "..."}`) sobre el contenido de los documentos. | Sí (`Bearer`) |

---

## 💻 Configuración Local

### Prerrequisitos
- Docker y Docker Compose
- Python 3.10+ (si se ejecuta fuera de Docker)
- Cuenta/Recurso en Azure AI Search

### Variables de Entorno (`.env`)
Crea un archivo `.env` en la raíz del proyecto basándote en la siguiente estructura:

```env
SECRET_KEY=tu_django_secret_key
DEBUG=True
AZURE_SEARCH_SERVICE_ENDPOINT=[https://tu-servicio.search.windows.net](https://tu-servicio.search.windows.net)
AZURE_SEARCH_API_KEY=tu_api_key
AZURE_SEARCH_INDEX_NAME=tu-indice
