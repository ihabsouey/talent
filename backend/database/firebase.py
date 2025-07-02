import firebase_admin
from firebase_admin import credentials
import json
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

def get_firebase_config():
    """Get Firebase configuration from file or environment variables"""
    try:
        # Try to load from file first
        with open('configs/firebase_config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        # If file not found, try environment variables
        required_keys = [
            "apiKey", "authDomain", "databaseURL", "projectId",
            "storageBucket", "messagingSenderId", "appId"
        ]
        
        config = {}
        for key in required_keys:
            env_key = f"FIREBASE_{key.upper()}"
            if env_value := os.getenv(env_key):
                config[key] = env_value
            else:
                raise ValueError(f"Missing required Firebase config: {env_key}")
        return config

def get_service_account():
    """Get Firebase service account from file or environment variable"""
    try:
        # Try to load from file first
        with open('configs/firebase_service_account.json', 'r') as key_file:
            return json.load(key_file)
    except FileNotFoundError:
        # If file not found, try environment variable
        service_account_json = os.getenv('FIREBASE_SERVICE_ACCOUNT_KEY')
        if not service_account_json:
            raise ValueError("Missing FIREBASE_SERVICE_ACCOUNT environment variable")
        return json.loads(service_account_json)

# Get configurations
firebase_config_json = get_firebase_config()
service_account_key_json = get_service_account()

# Initialize the app with a service account
if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_key_json)
    firebase_admin.initialize_app(cred)

# Initialize Firebase with configuration
firebase = pyrebase.initialize_app(firebase_config_json)

# Get database and auth instances
db = firebase.database()
authUser = firebase.auth()

# Helper functions for StudyConnect specific operations
def init_studyconnect_collections():
    """Initialize StudyConnect specific collections in Firebase"""
    try:
        # Initialize collections if they don't exist
        collections = [
            "students",
            "professionals", 
            "companies",
            "schools",
            "skill_validations",
            "opportunities",
            "applications",
            "notifications",
            "skills_catalog"
        ]
        
        for collection in collections:
            # Check if collection exists, if not create empty structure
            existing = db.child(collection).get().val()
            if not existing:
                db.child(collection).set({})
                print(f"Initialized {collection} collection")
        
        # Initialize skills catalog with common skills
        skills_catalog = {
            "programming": {
                "python": {"category": "programming", "description": "Python programming language"},
                "javascript": {"category": "programming", "description": "JavaScript programming language"},
                "java": {"category": "programming", "description": "Java programming language"},
                "react": {"category": "frontend", "description": "React.js framework"},
                "nodejs": {"category": "backend", "description": "Node.js runtime"}
            },
            "design": {
                "photoshop": {"category": "design", "description": "Adobe Photoshop"},
                "figma": {"category": "design", "description": "Figma design tool"},
                "ui_ux": {"category": "design", "description": "UI/UX Design"}
            },
            "marketing": {
                "digital_marketing": {"category": "marketing", "description": "Digital Marketing"},
                "seo": {"category": "marketing", "description": "Search Engine Optimization"},
                "social_media": {"category": "marketing", "description": "Social Media Marketing"}
            },
            "business": {
                "project_management": {"category": "business", "description": "Project Management"},
                "data_analysis": {"category": "business", "description": "Data Analysis"},
                "communication": {"category": "business", "description": "Communication Skills"}
            }
        }
        
        existing_skills = db.child("skills_catalog").get().val()
        if not existing_skills:
            db.child("skills_catalog").set(skills_catalog)
            print("Initialized skills catalog")
            
        print("StudyConnect collections initialized successfully!")
        
    except Exception as e:
        print(f"Error initializing StudyConnect collections: {str(e)}")

def get_user_by_type(user_id: str, user_type: str):
    """Get user data based on user type"""
    try:
        collection_map = {
            "student": "students",
            "professional": "professionals", 
            "company": "companies",
            "school": "schools"
        }
        
        if user_type not in collection_map:
            return None
            
        collection = collection_map[user_type]
        user_data = db.child(collection).child(user_id).get().val()
        return user_data
        
    except Exception as e:
        print(f"Error getting user data: {str(e)}")
        return None

def create_notification(user_id: str, notification_type: str, message: str, data: dict = None):
    """Create a notification for a user"""
    try:
        import uuid
        from datetime import datetime
        
        notification_id = str(uuid.uuid4())
        notification_data = {
            "id": notification_id,
            "user_id": user_id,
            "type": notification_type,
            "message": message,
            "data": data or {},
            "read": False,
            "created_at": datetime.now().isoformat()
        }
        
        db.child("notifications").child(notification_id).set(notification_data)
        return notification_id
        
    except Exception as e:
        print(f"Error creating notification: {str(e)}")
        return None

def get_user_notifications(user_id: str, unread_only: bool = False):
    """Get notifications for a user"""
    try:
        all_notifications = db.child("notifications").order_by_child("user_id").equal_to(user_id).get().val() or {}
        
        notifications = []
        for notif_id, notif_data in all_notifications.items():
            if unread_only and notif_data.get("read", False):
                continue
            notifications.append(notif_data)
        
        # Sort by creation date (newest first)
        notifications.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return notifications
        
    except Exception as e:
        print(f"Error getting notifications: {str(e)}")
        return []

def mark_notification_as_read(notification_id: str):
    """Mark a notification as read"""
    try:
        db.child("notifications").child(notification_id).update({"read": True})
        return True
    except Exception as e:
        print(f"Error marking notification as read: {str(e)}")
        return False

# Initialize collections on import (optional - can be called manually)
# init_studyconnect_collections()
