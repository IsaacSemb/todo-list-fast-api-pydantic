# FastAPI + Pydantic TODO API 📝

This is a small, hands-on project I'm building to deepen my understanding of **FastAPI** and **Pydantic**.

I've always preferred learning by doing, and this TODO app gives me the perfect space to explore:

- ✅ FastAPI for building modern, high-performance Python APIs
- ✅ Pydantic for data validation, parsing, and typing
- ✅ Swagger / ReDoc docs generation (automatically!)
- ✅ File-based persistence using JSON (no DB yet)
- ✅ Clean model separation (input vs full object)
- ✅ Serialization/deserialization handling (including `datetime`)
- ✅ Real-world developer practices like version control & modularity

The goal is not just to build a working API, but to **understand the "why" behind each step**.

More features to come (CRUD, filtering, error handling, maybe even persistence with a database).  
For now — this project represents my **learning journey in public**.

# Legacy JSON-Based Version of ToDo Application

This branch, `legacy-json-db`, captures the **original architecture** of this ToDo application before it was upgraded to use a relational SQL database (SQLite) and a modular file structure.

It serves as a **historical snapshot** for educational, archival, and comparison purposes.

---

## 📦 What This Version Contains

- ✅ A simple, file-based JSON "database" (`data.json`)
- ✅ Flat file structure with minimal folder separation
- ✅ Basic Pydantic models and routing logic
- ✅ No SQLAlchemy or database migrations
- ✅ Manually handled I/O operations to read/write JSON

---

## 🔄 Why It Was Archived

This version was archived to preserve the evolution of the application. It was actively used while prototyping and learning the FastAPI framework with:

- Minimal dependencies
- Simplicity and direct control over data
- Quick iteration and experimentation

However, it was eventually replaced by a more robust SQL-backed architecture which has since become the default on `main`.

---

## 🚀 How to Run This Legacy Version

Ensure you have Python 3.9+ installed. Then:

1. Clone the repo and checkout this branch:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   git checkout legacy-json-db



---

### 💡 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- Python 3.11+
- JSON for storage (DB is kind of overkill for a start)

---

### 🚀 Running the Project

```bash
uvicorn main:app --reload
