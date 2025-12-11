# --- 1. Імпорти та базове налаштування SQLAlchemy ---
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime   # ORM-поля
from sqlalchemy.ext.declarative import declarative_base                             # база моделей
from sqlalchemy.orm import sessionmaker                                             # сесії БД
from datetime import datetime                                                       # час/дата
from config import DATABASE_URL                                                     # підключення до БД

Base = declarative_base()                                                           # створення бази моделей


# --- 2. Модель таблиці "users" ---
class User(Base):
    """Модель користувача."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    registration_date = Column(DateTime, default=datetime.utcnow)


# --- 3. Модель таблиці "user_word_progress" ---
class UserWordProgress(Base):
    """Історія отриманих слів."""
    __tablename__ = 'user_word_progress'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    word_id = Column(Integer, nullable=False)
    sent_date = Column(DateTime, default=datetime.utcnow)


# --- 4. Ініціалізація двигуна БД, створення таблиць, сесій ---
engine = create_engine(DATABASE_URL)                                                # створення двигуна
Base.metadata.create_all(engine)                                                    # створення таблиць
Session = sessionmaker(bind=engine)                                                 # фабрика сесій


# --- 5. Функція: додавання користувача ---
def add_user(telegram_id):
    """Додає нового користувача."""
    session = Session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()

    if not user:                                                                    # якщо немає — створюємо
        user = User(telegram_id=telegram_id)
        session.add(user)

    session.commit()
    session.close()


# --- 6. Функція: збереження факту отримання слова ---
def save_word_progress(telegram_id, word_id):
    """Зберігає факт, що слово було відправлено."""
    session = Session()
    progress = UserWordProgress(user_id=telegram_id, word_id=word_id)
    session.add(progress)
    session.commit()
    session.close()


# --- 7. Функція: чи отримував користувач слово сьогодні ---
def has_user_received_today(telegram_id):
    """
    Перевіряє, чи отримував користувач слово СЬОГОДНІ.
    Повертає True, якщо вже отримував.
    """
    session = Session()

    # шукаємо останній запис для конкретного користувача
    last_entry = (
        session.query(UserWordProgress)
        .filter_by(user_id=telegram_id)
        .order_by(UserWordProgress.sent_date.desc())
        .first()
    )

    session.close()

    if last_entry:
        # порівнюємо дату останнього запису з сьогоднішньою
        if last_entry.sent_date.date() == datetime.utcnow().date():
            return True

    return False


# --- 8. Функція: повернути всіх активних користувачів ---
def get_all_active_users():
    session = Session()
    users = session.query(User).filter_by(is_active=True).all()
    session.close()

    return [u.telegram_id for u in users]
