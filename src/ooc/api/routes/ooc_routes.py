from fastapi import APIRouter
from pydantic import BaseModel
from ooc.core.the_self import TheSelf
from ooc.core.growth_event import GrowthEvent

router = APIRouter()

# Временное хранилище TheSelf
the_self_instance = TheSelf()

class EventRequest(BaseModel):
    name: str
    impact: float
    type_: str

@router.post("/event")
def send_event(event: EventRequest):
    """
    Отправить событие во внутренний мир TheSelf.
    """
    growth_event = GrowthEvent(
        name=event.name,
        impact=event.impact,
        type_=event.type_
    )
    result = the_self_instance.perceive_event(growth_event)
    return {
        "message": result,
        "current_stage": the_self_instance.ego.stage.name,
        "current_stability": round(the_self_instance.ego.stability, 2)
    }

@router.get("/self")
def get_self_state():
    """
    Получить текущее состояние TheSelf и Ego.
    """
    return {
        "name": the_self_instance.name,
        "ego_stage": the_self_instance.ego.stage.name,
        "ego_stability": round(the_self_instance.ego.stability, 2),
        "active_states": the_self_instance.state_manager.list_active_states(),
        "active_defenses": the_self_instance.defense_system.list_active_defenses()
    }
