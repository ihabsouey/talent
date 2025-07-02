from fastapi import APIRouter, Depends, HTTPException
from classes.schemas_dto import Company, CompanyBase, Opportunity
from routers.router_auth import get_current_user
from database.firebase import db
from typing import List

router = APIRouter(prefix='/companies', tags=['Entreprises'])

@router.get('/profile', response_model=Company)
async def get_company_profile(current_user: dict = Depends(get_current_user)):
    """Récupère le profil de l'entreprise connectée"""
    if current_user.get('user_type') != 'company':
        raise HTTPException(status_code=403, detail="Réservé aux entreprises")
    
    try:
        company_data = db.child("companies").child(current_user['uid']).get().val()
        if not company_data:
            raise HTTPException(status_code=404, detail="Profil entreprise non trouvé")
        return Company(**company_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/opportunities', response_model=List[Opportunity])
async def get_company_opportunities(current_user: dict = Depends(get_current_user)):
    """Récupère toutes les opportunités de l'entreprise"""
    if current_user.get('user_type') != 'company':
        raise HTTPException(status_code=403, detail="Réservé aux entreprises")
    
    try:
        opportunities = db.child("opportunities").order_by_child("company_id").equal_to(current_user['uid']).get().val() or {}
        return [Opportunity(**opp) for opp in opportunities.values()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
