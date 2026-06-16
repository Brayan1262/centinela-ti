# 🛡️ Centinela TI - Centro de Mando Predictivo

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

**Centinela TI** es una plataforma SaaS de grado Enterprise diseñada para el monitoreo de servidores en tiempo real y la detección predictiva de anomalías utilizando Inteligencia Artificial.

En lugar de ser un dashboard estático, este sistema funciona como una "Sala de Control" viva que analiza el tráfico y consumo de la computadora (CPU, RAM, Disco) enviando transmisiones instantáneas (Latencia Cero) a una interfaz inmersiva, a la vez que un motor de Machine Learning predice desbordamientos de memoria antes de que ocurran.

---

## ✨ Características Principales

*   **⚡ Arquitectura en Tiempo Real:** Comunicación fluida mediante WebSockets (STOMP) para actualizaciones al milisegundo sin recargar la página.
*   **🧠 Núcleo de Inteligencia Artificial:** Un script en Python entrenando un modelo de Regresión Lineal (`scikit-learn`) en caliente para proyectar el uso de memoria a futuro.
*   **🔒 Seguridad de Grado Bancario:** Autenticación Stateless basada en JWT (JSON Web Tokens) controlada por Spring Security.
*   **🎨 Frontend Inmersivo (SPA):** Interfaz Single Page Application interactiva con efectos Glassmorphism, animaciones CSS avanzadas, modo pantalla completa, y alertas sonoras.
*   **📄 Generación de Reportes:** Capacidad para exportar historiales de alertas generadas por IA a documentos PDF descargables.
*   **🐳 Orquestación DevOps:** Ecosistema completo dockerizado. Cuatro microservicios levantados al unísono a través de `docker-compose`.

---

## 🛠️ Stack Tecnológico

| Módulo | Tecnología |
| :--- | :--- |
| **Backend REST & WS** | Java 21, Spring Boot, Spring Security (JWT), Hibernate / JPA |
| **Inteligencia Artificial** | Python 3.12, scikit-learn, Pandas, NumPy, Requests |
| **Frontend Dashboard** | HTML5, CSS3, JavaScript Vanilla, Chart.js, SockJS, jsPDF |
| **Base de Datos** | PostgreSQL 15 |
| **Despliegue (DevOps)** | Docker, Docker Compose, NGINX |

---

## ⚙️ Cómo ejecutar el proyecto (Modo Local)

El proyecto está diseñado para ser desplegado fácilmente utilizando contenedores.

### Prerrequisitos
1. Tener instalado [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Tener instalado [Python 3.10+](https://www.python.org/) en tu máquina anfitriona (para ejecutar el agente recolector de métricas).

### Paso 1: Levantar la Infraestructura Core
Abre una terminal en la raíz del proyecto y ejecuta el orquestador:

```bash
docker-compose up --build
```
> Esto descargará, compilará y ejecutará la Base de Datos (Postgres), la API (Java), el Predictor de IA (Python) y el Servidor Web (Nginx).

### Paso 2: Iniciar el Agente Recolector
Para que la base de datos reciba información de tu propia computadora, debes iniciar el agente recolector local. Abre una **nueva terminal**:

```bash
cd agent-collector
python -m venv venv
# Activar entorno (En Windows):
.\venv\Scripts\Activate.ps1
# Instalar dependencias:
pip install -r requirements.txt

# Ejecutar el recolector:
python collector.py
```
> Empezarás a ver cómo los datos de tu CPU, RAM y Disco son enviados al servidor.

### Paso 3: Entrar al Centro de Mando
1. Abre tu navegador web y dirígete a: **http://localhost:8090**
2. Inicia sesión con las credenciales por defecto:
   * **Usuario:** `admin`
   * **Contraseña:** `admin123`
3. ¡Disfruta del monitoreo en tiempo real!

---

## 📂 Estructura del Proyecto

*   `/backend-core` - API en Spring Boot y WebSockets.
*   `/ai-predictor` - Contenedor con IA analizando datos del backend.
*   `/agent-collector` - Script local que extrae las métricas del hardware.
*   `/frontend-dashboard` - Interfaz gráfica y assets.
*   `docker-compose.yml` - Archivo maestro de orquestación.

---
*Desarrollado como proyecto de exhibición técnica para arquitectura Full-Stack, IA y DevOps.*
