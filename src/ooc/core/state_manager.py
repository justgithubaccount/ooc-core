class StateManager:
    """
    Управление внутренними состояниями Я.
    Отвечает за активные эмоции и состояния сознания.
    """

    def __init__(self):
        self.active_states = []  # Список текущих активных состояний

    def activate_state(self, state: str):
        """
        Активировать новое состояние.
        """
        if state not in self.active_states:
            self.active_states.append(state)

    def deactivate_state(self, state: str):
        """
        Деактивировать состояние.
        """
        if state in self.active_states:
            self.active_states.remove(state)

    def is_state_active(self, state: str) -> bool:
        """
        Проверить, активно ли состояние.
        """
        return state in self.active_states

    def list_active_states(self) -> list:
        """
        Вернуть список всех активных состояний.
        """
        return self.active_states
