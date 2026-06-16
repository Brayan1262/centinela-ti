# Centinela TI 🛡️

> Plataforma SaaS de grado Enterprise diseñada para el monitoreo de servidores en tiempo real y la detección predictiva de anomalías utilizando Inteligencia Artificial. Analiza tráfico y consumo (CPU, RAM, Disco) enviando métricas instantáneas y prediciendo desbordamientos de memoria.
>
> ![Java](https://img.shields.io/badge/JAVA-21-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white) ![Spring Boot](https://img.shields.io/badge/SPRING_BOOT-3-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white) ![Python](https://img.shields.io/badge/PYTHON-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/POSTGRESQL-15-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/DOCKER-Compose-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) ![JavaScript](https://img.shields.io/badge/JAVASCRIPT-Vanilla-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)

---

## 🚀 Características Principales

- **Arquitectura en Tiempo Real:** Comunicación fluida mediante WebSockets (STOMP) para actualizaciones al milisegundo sin recargar la página (Latencia Cero).
- **Núcleo de Inteligencia Artificial:** Script en Python entrenando un modelo de Regresión Lineal (`scikit-learn`) en caliente para proyectar y predecir el uso de memoria a futuro.
- **Seguridad de Grado Bancario:** Autenticación Stateless basada en tokens JWT controlada rigurosamente por Spring Security.
- **Frontend Inmersivo (SPA):** Interfaz interactiva ("Sala de Control") con efectos Glassmorphism, animaciones CSS avanzadas, modo pantalla completa, y alertas sonoras.
- **Generación de Reportes:** Exportación de historiales de alertas generadas por IA a documentos PDF descargables dinámicamente.
- **Orquestación DevOps:** Ecosistema 100% dockerizado. Cuatro microservicios levantados al unísono a través de `docker-compose`.

---

## 🛠️ Stack Tecnológico

| Capa | Tecnologías |
| :--- | :--- |
| **Backend REST & WS** | Java 21, Spring Boot, Spring Security (JWT), Hibernate / JPA |
| **Motor Predictivo IA** | Python 3.12, scikit-learn, Pandas, NumPy, Requests |
| **Frontend Dashboard** | HTML5, CSS3, JavaScript Vanilla, Chart.js, SockJS, jsPDF |
| **Base de Datos** | PostgreSQL 15 |
| **Despliegue (DevOps)** | Docker, Docker Compose, NGINX |

---

## 🏗️ Arquitectura del Sistema

El proyecto opera bajo una arquitectura de microservicios distribuidos:

```text
/backend-core        ➔ API central en Spring Boot y WebSockets.
/ai-predictor        ➔ Contenedor con IA analizando datos del backend.
/agent-collector     ➔ Script local que extrae métricas de hardware de la máquina.
/frontend-dashboard  ➔ Interfaz gráfica inmersiva y dashboard analítico.
docker-compose.yml   ➔ Archivo maestro de orquestación.
```

---

## ⚙️ Cómo ejecutar el proyecto (Modo Local)

El proyecto está diseñado para ser desplegado fácilmente utilizando contenedores.

### Prerrequisitos
1. Tener [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado.
2. Tener [Python 3.10+](https://www.python.org/) en tu máquina anfitriona (para ejecutar el agente recolector de métricas locales).

### 1. Levantar la Infraestructura Core
Abre una terminal en la raíz del proyecto y ejecuta el orquestador:
```bash
docker-compose up --build
```
> Esto descargará, compilará y ejecutará la BD (Postgres), la API (Java), el Predictor de IA (Python) y el Servidor Web (Nginx).

### 2. Iniciar el Agente Recolector Local
Para que el servidor reciba la información de tu propia computadora, debes iniciar el agente recolector. En una **nueva terminal**:
```bash
cd agent-collector
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python collector.py
```
> Empezarás a ver cómo los datos de tu CPU, RAM y Disco son extraídos y enviados al backend en tiempo real.

### 3. Entrar al Centro de Mando
1. Abre tu navegador web y dirígete a: **http://localhost:8090**
2. Inicia sesión con las credenciales por defecto:
   - **Usuario:** `admin`
   - **Contraseña:** `admin123`

---

## 👨‍💻 Autor

**Brayan Jair Chavez Oscor**
*Ingeniería de Software / Arquitectura Backend*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Brayan1262)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brayan-chavez-218088334/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=web&logoColor=white)](https://brayan1262.github.io/portafolio-brayan/)

> *Desarrollado como proyecto de exhibición técnica integral para arquitectura Full-Stack, IA y DevOps.*
