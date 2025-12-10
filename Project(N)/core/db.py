# core/db.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DATABASE_URL

Base = declarative_base()


class User(Base):
    """Модель користувача."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    registration_date = Column(DateTime, default=datetime.utcnow)


class UserWordProgress(Base):
    """Історія отриманих слів."""
    __tablename__ = 'user_word_progress'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    word_id = Column(Integer, nullable=False)
    sent_date = Column(DateTime, default=datetime.utcnow)


# Ініціалізація бази даних
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def add_user(telegram_id):
    """Додає нового користувача."""
    session = Session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    if not user:
        user = User(telegram_id=telegram_id)
        session.add(user)
    session.commit()
    session.close()


def save_word_progress(telegram_id, word_id):
    """Зберігає факт, що слово було відправлено."""
    session = Session()
    progress = UserWordProgress(user_id=telegram_id, word_id=word_id)
    session.add(progress)
    session.commit()
    session.close()


def has_user_received_today(telegram_id):
    """
    Перевіряє, чи отримував користувач слово СЬОГОДНІ.
    Повертає True, якщо вже отримував.
    """
    session = Session()
    # Шукаємо останній запис для цього користувача
    last_entry = session.query(UserWordProgress) \
        .filter_by(user_id=telegram_id) \
        .order_by(UserWordProgress.sent_date.desc()) \
        .first()
    session.close()

    if last_entry:
        # Порівнюємо дату останнього запису з сьогоднішньою
        if last_entry.sent_date.date() == datetime.utcnow().date():
            return True

    return False


def get_all_active_users():
    session = Session()
    users = session.query(User).filter_by(is_active=True).all()
    session.close()
    return [u.telegram_id for u in users]