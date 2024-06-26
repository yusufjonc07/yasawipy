from fastapi import APIRouter, HTTPException
from app.db import Base, ActiveSession
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel
from typing import Optional

class Resource(APIRouter):


    def __init__(
        self, 
        name: str,
        modelClass: Base, 
        createForm: BaseModel,
        editForm: Optional[BaseModel] = None,
        label: str = '', 
        pluralLabel: str = '',
        navigationIcon: str = 'folder',
        activeNavigationIcon: str = '',
        navigationGroup: str = '',
        simple: bool = False,
        tags=[]
    ):
        
        if not activeNavigationIcon:
            activeNavigationIcon = navigationIcon

        
        self.name = name
        self.simple = simple
        self.modelClass = modelClass
        self.createForm = createForm
        self.editForm = editForm
        self.label = label
        self.pluralLabel = pluralLabel
        self.activeNavigationIcon = activeNavigationIcon    
        self.navigationIcon = navigationIcon
        self.navigationGroup = navigationGroup

        super().__init__(tags=tags, prefix=f"/{name}")

        if not editForm:
            editForm = createForm
        
        @self.get("")
        async def get_all(db: Session = ActiveSession):
            return db.query(modelClass).all()
        
        @self.post("/create")
        async def create_one(form_data: createForm, db: Session = ActiveSession):

            try:
                new_model = modelClass(**form_data)
                db.add(new_model)
                db.commit()

                return HTTPException(200, 'Created successfully')

            except Exception:
                return HTTPException(400, 'Something went wrong')
            
        @self.get("/{id}")
        async def get_one(id: int, db: Session = ActiveSession):

            try:

                record = db.get(modelClass, id)

                if not record:
                    raise HTTPException(400, "Record was not found")

                return record

            except IntegrityError as e:
                return HTTPException(400, e.args)
           
            
        @self.put("/update/{id}")
        async def update_one(id: int, form_data: editForm, db: Session = ActiveSession):

            try:

                record = db.get(modelClass, id)

                if not record:
                    raise HTTPException(400, "Record was not found")

                db.query(modelClass).filter_by(id=id).update(dict(form_data))
                db.commit()

                return HTTPException(200, 'Updated successfully')

            except IntegrityError as e:
                return HTTPException(400, e.args)
            except Exception as e:
                return HTTPException(400, e.args)
            
        @self.delete("/delete/{id}")
        async def delete_one(id: int,  db: Session = ActiveSession):

            try:

                record = db.get(modelClass, id)

                if not record:
                    raise HTTPException(400, "Record was not found")

                db.query(modelClass).filter_by(id=id).delete()
                db.commit()

                return HTTPException(200, 'Updated successfully')

            except Exception:
                return HTTPException(400, 'Something went wrong')
            
        



        