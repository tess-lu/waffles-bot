"""This module contains utilities for the database."""

import random

from sqlalchemy import create_engine, Column, Integer, String, DateTime, desc
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import DATABASE_URL
from utils.enums import QuestionStatus


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Question(Base):
    """Represent the 'questions' table in the database."""
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    status = Column(String, default=QuestionStatus.PENDING)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class Gif(Base):
    """Represent the 'gifs' table in the database."""
    __tablename__ = 'gifs'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


def get_question(status: str) -> str | None:
    """
    Retrieve the first question that matches the status.
    Update all records with an 'archived' status to 'pending' if no pending
    question is found, so we never run out of questions.
    """
    session = Session()
    question = session.query(Question).filter(Question.status == status).first()
    if not question:
        if status == QuestionStatus.PENDING:
            session.query(Question).filter(Question.status == QuestionStatus.ARCHIVED).update({Question.status: QuestionStatus.PENDING})
            session.commit()
            question = session.query(Question).filter(Question.status == QuestionStatus.PENDING).first()
            session.close()
        else:
            session.close()
            return None
    return question


def update_question_status(question_id: int, new_status: str) -> None:
    """
    Update the question status by question id.
    """
    session = Session()
    question = session.query(Question).filter(Question.id == question_id).first()
    if question:
        question.status = new_status
        session.commit()
        session.close()
    else:
        session.close()
        raise ValueError(f'Question with id {question_id} does not exist.')


def get_most_recently_archived_question() -> Question | None:
    """
    Retrieve the id of the most recently archived question.
    """
    with Session() as session:
        question = session.query(Question).filter(Question.status == QuestionStatus.ARCHIVED).order_by(desc(Question.updated_at)).first()
    if not question:
        return None
    return question


def pick_random_gif() -> str | None:
    """
    Pick a random GIF URL from the gifs table.
    """
    with Session() as session:
        gifs = session.query(Gif).all()
    if not gifs:
        return None
    return random.choice(gifs).url
