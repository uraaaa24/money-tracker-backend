"""20250520_change

Revision ID: 91c92529e919
Revises: f6ceeb442d6e
Create Date: 2025-05-20 05:18:45.292638

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "91c92529e919"
down_revision: Union[str, None] = "f6ceeb442d6e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_index(op.f("ix_categories_id"), "categories", ["id"], unique=False)
    op.create_index(
        op.f("ix_categories_user_id"), "categories", ["user_id"], unique=False
    )

    categories_table = sa.table(
        "categories",
        sa.column("user_id", sa.String),
        sa.column("name", sa.String),
        sa.column("type", sa.String),
    )
    op.bulk_insert(
        categories_table,
        [
            {"user_id": None, "name": "Food", "type": "expense"},
            {"user_id": None, "name": "Transportation", "type": "expense"},
            {"user_id": None, "name": "entertainment", "type": "expense"},
            {"user_id": None, "name": "utilities", "type": "expense"},
            {"user_id": None, "name": "health", "type": "expense"},
            {"user_id": None, "name": "education", "type": "expense"},
            {"user_id": None, "name": "Salary", "type": "income"},
            {"user_id": None, "name": "Additional income", "type": "income"},
        ],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_categories_user_id"), table_name="categories")
    op.drop_index(op.f("ix_categories_id"), table_name="categories")
    op.drop_table("categories")
    # ### end Alembic commands ###
