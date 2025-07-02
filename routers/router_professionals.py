from fastapi import APIRouter, Depends, HTTPException
from classes.schemas_dto import Professional, ProfessionalBase
from routers.router_auth import get_current_user
from database.firebase import db

router = APIRouter(prefix='/professionals', tags=['Professionnels'])

@router.get('/profile', response_model=Professional)
async def get_professional_profile(current_user: dict = Depends(get_current_user)):
    """Récupère le profil du professionnel connecté"""
    if current_user.get('user_type') != 'professional':
        raise HTTPException(status_code=403, detail="Réservé aux professionnels")
    
    try:
        professional_data = db.child("professionals").child(current_user['uid']).get().val()
        if not professional_data:
            raise HTTPException(status_code=404, detail="Profil professionnel non trouvé")
        return Professional(**professional_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/validation-stats')
async def get_validation_statistics(current_user: dict = Depends(get_current_user)):
    """Récupère les statistiques de validation du professionnel"""
    if current_user.get('user_type') != 'professional':
        raise HTTPException(status_code=403, detail="Réservé aux professionnels")
    
    try:
        validations = db.child("skill_validations").order_by_child("professional_id").equal_to(current_user['uid']).get().val() or {}
        
        stats = {
            "total_validations": len(validations),
            "validations_this_month": 0,  # À calculer selon la date
            "average_rating": 0.0,
            "expertise_domains": []
        }
        
        return stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
