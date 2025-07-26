from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.job_matching import get_job_matches
from services.personality_mapping import get_personality_matches
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to call this API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserProfile(BaseModel):
    skills: str
    interests: str
    personality: str
    description: str

@app.post("/recommend")
async def recommend_jobs(user: UserProfile):
    try:
        skill_matches = get_job_matches(user.skills, user.interests)
        personality_matches = get_personality_matches(user.personality)

        # Combine and dedupe by job_title
        job_map = {}
        for job in skill_matches + personality_matches:
            title = job["job_title"]
            if title not in job_map or job["match_score"] > job_map[title]["match_score"]:
                job_map[title] = job

        final_list = list(job_map.values())
        return {"recommendations": final_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
