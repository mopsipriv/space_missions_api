from fastapi import FastAPI, HTTPException, Query
from api.models import Mission, MissionCreate, MissionUpdate, Stats, Agency, Status
from typing import Optional

app = FastAPI(title="Space Missions API",description="Space Missions", version="1.0.0")

missions_db: dict[int, Mission] = {}
next_id: int = 1

@app.get("/")
def hello():
    return{"message": "Space Missions API is working","docs_url": "/docs"}

@app.get("/missions", response_model=list[Mission])
def get_missions(
    agency: Optional[Agency] = Query(None,description="filter by agency"),
    status: Optional[Status] = Query(None,description="filter by status"),
    crewed: Optional[bool] = Query(None,description="with crew filter"),
    year_from: Optional[int] = Query(None,description="year of launch from"),
    year_to: Optional[int] = Query(None,description="year of launch to"),
):
    result=list(missions_db.values())
    if agency is not None:
        result= [m for m in result if m.agency==agency]
    if status is not None:
        result= [m for m in result if m.status==status]
    if crewed is not None:
        result= [m for m in result if m.crewed==crewed]
    if year_from is not None:
        result= [m for m in result if m.launch_year>=year_from]
    if year_to is not None:
        result= [m for m in result if m.launch_year<=year_to]    

    return result

@app.post("/missions",response_model=Mission, status_code=201)
def post_missions(
    mission: MissionCreate
):
    global next_id
    new_mission=Mission(id=next_id, **mission.model_dump())
    missions_db[next_id]= new_mission
    next_id+=1
    return new_mission

@app.delete("/missions")
def delete_missions():
    global next_id
    missions_db.clear()
    next_id=1
    return{"message":"All missions are deleted"}

@app.get("/missions/{mission_id}", response_model=Mission)
def get_mission_id(
    mission_id: int
):
    if mission_id not in missions_db:
        raise HTTPException(
            status_code=404,detail="Mission is not found"
        )
    return missions_db[mission_id]

@app.put("/missions/{mission_id}", response_model=Mission)
def put_mission_id(
    mission_id:int,
    mission: MissionCreate
):
    if mission_id not in missions_db:
        raise HTTPException(
            status_code=404,detail="Mission is not found"
        )
    new_mission=Mission(id=mission_id, **mission.model_dump())
    missions_db[mission_id]= new_mission
    return new_mission

@app.patch("/missions/{mission_id}",response_model=Mission)
def patch_mission_id(
    mission_id: int,
    update: MissionUpdate
):
    if mission_id not in missions_db:
        raise HTTPException(
            status_code=404,detail="Mission is not found"
        )
    current=missions_db[mission_id]
    current_data=current.model_dump()
    update_data=update.model_dump(exclude_unset=True)
    current_data.update(update_data)
    updated= Mission(**current_data)
    missions_db[mission_id]= updated
    return updated

@app.delete("/missions/{mission_id}", status_code=204)
def delete_mission_id(
    mission_id: int
):
    if mission_id not in missions_db:
        raise HTTPException(
            status_code=404,detail="Mission is not found"
        )
    del missions_db[mission_id]
    return None

@app.get("/stats", response_model=Stats)
def get_stats():
    total = len(missions_db)
    by_agency = {}
    by_status = {}
    crewed_count = sum(1 for m in missions_db.values() if m.crewed)
    for m in missions_db.values():
        agency_name = m.agency.value 
        by_agency[agency_name] = by_agency.get(agency_name, 0) + 1
        status_name = m.status.value
        by_status[status_name] = by_status.get(status_name, 0) + 1
    return Stats(
        total=total,
        by_agency=by_agency,
        by_status=by_status,
        crewed_count=crewed_count
    )