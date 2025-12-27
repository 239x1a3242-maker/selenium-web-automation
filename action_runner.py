def run_actions(engine, task):
    for step in task:
        try:
            action = step["action"]

            if action == "open":
                engine.open(step["url"])

            elif action == "click":
                engine.click(step["selector"])

            elif action == "type":
                engine.type(step["selector"], step["value"])

            elif action == "wait":
                engine.wait_seconds(step["seconds"])

            elif action == "wait_for":
                # THIS IS THE KEY FIX
                engine.wait_for_selector(step["selector"])

        except Exception as e:
            print("\nAutomation failed at step:")
            print(step)
            print("Error:", str(e))
            break
