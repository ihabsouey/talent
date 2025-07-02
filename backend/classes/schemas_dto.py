from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
from enum import Enum

# DTO : Data Transfert Object ou Schema
# Représente la structure de la données (data type) en entrée ou en sortie de notre API.
# Model Pydantic = Datatype

# Enums pour le nouveau projet
class CompetenceLevel(str, Enum):
    DEBUTANT = "débutant"
    INTERMEDIAIRE = "intermédiaire"
    AVANCE = "avancé"
    EXPERT = "expert"

class ValidationStatus(str, Enum):
    EN_ATTENTE = "en_attente"
    VALIDEE = "validée"
    REFUSEE = "refusée"

class UserType(str, Enum):
    STUDENT = "student"
    PROFESSIONAL = "professional"
    COMPANY = "company"
    SCHOOL = "school"

# Modèles utilisateurs existants
class TodoNoID(BaseModel):
    name: str

class Todo(BaseModel):
    id: str
    name: str

class User(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str
    
    class Config:
        schema_extra = {
            "exemple": {
                "email": "benalioune6@gmail.com",
                "password": "abcdef"
            }
        }

# Modèles étudiants
class StudentBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    school: str
    formation: str
    year_of_study: int
    cv_url: Optional[str] = None
    phone: Optional[str] = None
    linkedin_url: Optional[str] = None

class StudentCreate(StudentBase):
    password: str

class Student(StudentBase):
    id: str
    competences: List[str] = []
    validated_skills: Dict[str, CompetenceLevel] = {}
    user_type: UserType = UserType.STUDENT
    profile_complete: bool = False
    created_at: Optional[datetime] = None

# Modèles professionnels
class ProfessionalBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    company: str
    position: str
    expertise_domains: List[str]
    years_experience: int
    phone: Optional[str] = None
    linkedin_url: Optional[str] = None
    bio: Optional[str] = None

class ProfessionalCreate(ProfessionalBase):
    password: str

class Professional(ProfessionalBase):
    id: str
    validation_count: int = 0
    rating: float = 0.0
    user_type: UserType = UserType.PROFESSIONAL
    verified: bool = False
    created_at: Optional[datetime] = None

# Modèles entreprises
class CompanyBase(BaseModel):
    name: str
    sector: str
    size: str  # TPE, PME, ETI, Grande entreprise
    description: str
    website: Optional[str] = None
    address: Optional[str] = None
    city: str
    country: str = "France"
    logo_url: Optional[str] = None

class CompanyCreate(CompanyBase):
    email: str
    password: str
    contact_person: str
    contact_position: str

class Company(CompanyBase):
    id: str
    email: str
    contact_person: str
    contact_position: str
    active_offers: int = 0
    user_type: UserType = UserType.COMPANY
    verified: bool = False
    created_at: Optional[datetime] = None

# Modèles validation de compétences
class SkillValidationRequest(BaseModel):
    student_id: str
    skill_name: str
    level_claimed: CompetenceLevel
    evidence_description: str
    portfolio_links: Optional[List[str]] = None
    project_description: Optional[str] = None

class SkillValidation(SkillValidationRequest):
    id: str
    professional_id: Optional[str] = None
    status: ValidationStatus = ValidationStatus.EN_ATTENTE
    professional_feedback: Optional[str] = None
    validated_level: Optional[CompetenceLevel] = None
    validation_date: Optional[datetime] = None
    created_at: datetime

# Modèles opportunités
class OpportunityType(str, Enum):
    STAGE = "stage"
    ALTERNANCE = "alternance"
    EMPLOI = "emploi"
    PROJET = "projet"
    FREELANCE = "freelance"

class OpportunityBase(BaseModel):
    title: str
    company_id: str
    type: OpportunityType
    description: str
    required_skills: List[str]
    preferred_skills: Optional[List[str]] = []
    location: str
    remote_possible: bool = False
    duration: Optional[str] = None
    compensation: Optional[str] = None
    requirements: Optional[List[str]] = []
    benefits: Optional[List[str]] = []

class OpportunityCreate(OpportunityBase):
    pass

class Opportunity(OpportunityBase):
    id: str
    applications_count: int = 0
    views_count: int = 0
    created_at: datetime
    deadline: Optional[datetime] = None
    status: str = "active"  # active, closed, paused

# Modèles candidatures
class ApplicationStatus(str, Enum):
    ENVOYEE = "envoyée"
    VUE = "vue"
    EN_COURS = "en_cours"
    ACCEPTEE = "acceptée"
    REFUSEE = "refusée"

class ApplicationBase(BaseModel):
    student_id: str
    opportunity_id: str
    cover_letter: str
    additional_documents: Optional[List[str]] = []

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: str
    status: ApplicationStatus = ApplicationStatus.ENVOYEE
    applied_at: datetime
    company_feedback: Optional[str] = None
    interview_date: Optional[datetime] = None

# Modèles écoles (bonus)
class SchoolBase(BaseModel):
    name: str
    type: str  # université, école d'ingénieur, école de commerce, etc.
    city: str
    country: str = "France"
    website: Optional[str] = None
    description: Optional[str] = None

class School(SchoolBase):
    id: str
    students_count: int = 0
    partnerships_count: int = 0
    created_at: Optional[datetime] = None

# Anciens modèles restaurant (conservés pour compatibilité)
class PizzaBase(BaseModel):
    name: str
    price: float
    ingredients: List[str]
    size: str  # S/M/L/XL

class PizzaCreate(PizzaBase):
    pass

class Pizza(PizzaBase):
    id: str

class OrderItem(BaseModel):
    pizza_id: str
    quantity: int
    customizations: Optional[List[str]] = None

class OrderCreate(BaseModel):
    items: List[OrderItem]
    customer_name: str
    delivery_type: str  # sur place/à emporter/livraison

class Order(OrderCreate):
    id: str
    status: str  # reçue/en préparation/prête/livrée
    order_time: datetime

# Données de test (conservées)
users = [
    User(email="benalioune6@gmail.com", password="pass")
]


