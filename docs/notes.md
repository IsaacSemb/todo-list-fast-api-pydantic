# ALEMBIC COMMANDS

### Initialising
- `alembic init alembic`

### create a migration
- `alembic revision --autogenerate -m "message"`

### apply all migrations
- `alembic upgrade head`

### apply all migration to specific migration
- `alembic upgrade <revision_id>`

### Downgrade migration by one
- `alembic downgrade -1`

### Downgrade all migrations
- `alembic downgrade base`

# GIT COMMANDS

### Deleting Last commitgit reset --soft HEAD~1  
- `git reset --soft HEAD~1`
