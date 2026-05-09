from fastapi import APIRouter, HTTPException
from datetime import date
from app.services.csv_service import get_historique

router = APIRouter()


@router.get("/graphique")
def graphique(date_debut: str):
    try:
        d = date.fromisoformat(date_debut)
    except ValueError:
        raise HTTPException(status_code=400, detail="Format de date invalide, utiliser YYYY-MM-DD")
    data = get_historique(d)
    if not data:
        raise HTTPException(status_code=404, detail="Aucune donnée depuis cette date")
    return {"data": data}
