class HistoryManager:
    """
    Менеджер истории развития TheSelf.
    Сохраняет последовательность событий, изменений состояний и стадий развития.
    """

    def __init__(self):
        self.history = []  # Список записей истории

    def add_record(self, record: str):
        """
        Добавить новую запись в историю.
        """
        self.history.append(record)

    def list_history(self) -> list:
        """
        Получить всю историю развития.
        """
        return self.history

    def clear_history(self):
        """
        Очистить всю историю.
        """
        self.history.clear()
