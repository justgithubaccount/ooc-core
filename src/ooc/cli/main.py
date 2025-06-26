import typer
from ooc.config.settings import settings
from ooc.config.logging_config import setup_logging

app = typer.Typer()

@app.command()
def simulate():
    """Запуск симуляции сознания."""
    setup_logging()
    from ooc.simulation.life_simulation import simulate
    simulate()

@app.command()
def create_self():
    """Создание нового объекта TheSelf."""
    setup_logging()
    from ooc.core.the_self import TheSelf
    theself = TheSelf()
    print(f"Создан новый TheSelf: {theself.name}")

if __name__ == "__main__":
    app()
