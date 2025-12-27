from selenium_engine import SeleniumEngine
from action_runner import run_actions
from task import TASK

engine = SeleniumEngine()

try:
    run_actions(engine, TASK)
finally:
    engine.quit()
