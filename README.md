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
