"""Add the task requester foreign key.

Revision ID: 20261005_01
Revises:
Create Date: 2026-10-05

"""

from typing import Sequence, Union

from alembic import op

revision: str = "20261005_01"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key(
        "fk_tarefas_solicitantes",
        "tarefas",
        "solicitantes",
        ["solicitante_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_tarefas_solicitantes",
        "tarefas",
        type_="foreignkey",
    )