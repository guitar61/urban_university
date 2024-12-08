from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Import your Base and models
from app.backend.db import Base  # Import Base from your db.py
from app.models.user import User  # Import User model
from app.models.task import Task  # Import Task model

# This is the Alembic Config object, which provides access to values in the alembic.ini file.
config = context.config

# Interpret the config file for Python logging. This sets up loggers.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the target metadata for Alembic
target_metadata = Base.metadata

# Offline mode migration configuration
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with a URL and not an Engine.
    Calls to context.execute() emit the given string to the script output.
    """
    url = config.get_main_option("sqlalchemy.url")  # Fetch the database URL from alembic.ini
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Online mode migration configuration
def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Determine whether to run migrations offline or online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
