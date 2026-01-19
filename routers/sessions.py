from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter(prefix="/sessions", tags=["sessions"])  # THIS MUST BE NAMED 'router'

# Example endpoint
@router.post("/", response_model=schemas.Session)
def create_session(session: schemas.SessionCreate, db: Session = Depends(database.get_db)):
    return crud.create_session(db, session)

@router.get("/", response_model=list[schemas.Session])
def read_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_sessions(db, skip=skip, limit=limit)
