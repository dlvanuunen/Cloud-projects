# Cloud-Projects

A repo for small infrastructure and integration experiments. The goal is to test ideas quickly and learn how the pieces connect, not to build polished products.

Skills learned:
- Docker and Docker Compose
- Container networking and service configuration
- Building REST APIs with FastAPI
- Calendar integration with CalDAV
- Keeping credentials out of AI agents

## 📂 Projects

- Project 1 – **Superset + PostgreSQL Docker Stack**
  A minimal proof of concept that runs **Apache Superset** alongside a **PostgreSQL** data warehouse using **Docker Compose** and a lean Superset image.
 
- Project 2 – **Calendar Tool Server for Open WebUI**
  A **FastAPI** service that works as an external tool for **Open WebUI** and reads events from a **CalDAV** calendar on a mail provider.
  - Exposes simple endpoints (e.g. "get events for a date range") that the agent can call

