# import du framework
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Import des routers
import routers.router_auth
import routers.router_skills
import routers.router_matching
import routers.router_students
import routers.router_professionals
import routers.router_companies

# Documentation
from documentation.description import api_description

# Initialisation de l'API
app = FastAPI(
    title="StudyConnect - Plateforme de Validation et Mise en Relation",
    description=api_description,
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ajouter les routers dédiés
app.include_router(routers.router_auth.router)
app.include_router(routers.router_skills.router)
app.include_router(routers.router_matching.router)
app.include_router(routers.router_students.router)
app.include_router(routers.router_professionals.router)
app.include_router(routers.router_companies.router)

# Route racine
@app.get("/")
async def root():
    return {
        "message": "Bienvenue sur StudyConnect API",
        "description": "Plateforme de validation de compétences et mise en relation étudiants-entreprises",
        "version": "1.0.0",
        "endpoints": {
            "auth": "/auth",
            "skills": "/skills", 
            "matching": "/matching",
            "students": "/students",
            "professionals": "/professionals",
            "companies": "/companies"
        }
    }

# Route de santé de l'API
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "StudyConnect API"}
