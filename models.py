from sqlmodel import Field, SQLModel, create_engine


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    # task_description: str
    # urgency: int
