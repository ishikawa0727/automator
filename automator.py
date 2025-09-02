import json
import time
import argparse
import pyautogui
import os


def run_sequence(sequence, iteration=0):
    for action in sequence:
        act = action.get("action")

        if act == "loop":
            count = action.get("count", 1)
            for i in range(count):
                run_sequence(action.get("sequence", []), iteration=i)

        elif act == "screenshot":
            left = action.get("left", 0)
            top = action.get("top", 0)
            width = action.get("width", 100)
            height = action.get("height", 100)
            filename = action.get("filename", "screenshot-{iteration}.png")
            filename = filename.replace("{iteration}", str(iteration))
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            img = pyautogui.screenshot(region=(left, top, width, height))
            img.save(filename)
            print(f"Saved screenshot: {filename}")

        elif act == "keyDown":
            key = action.get("key")
            if key:
                pyautogui.keyDown(key)
                pyautogui.keyUp(key)
                print(f"Pressed key: {key}")

        elif act == "click":
            x = action.get("x", None)
            y = action.get("y", None)
            button = action.get("button", "left")
            if x is not None and y is not None:
                pyautogui.click(x, y, button=button)
                print(f"Clicked at ({x}, {y}) with {button} button")
            else:
                print("Click action requires 'x' and 'y'")

        elif act == "sleep":
            t = action.get("time", 1)
            print(f"Sleeping {t} seconds...")
            time.sleep(t)

        else:
            print(f"Unknown action: {act}")


def main():
    parser = argparse.ArgumentParser(description="Run automation sequence from config file")
    parser.add_argument("config", help="Path to JSON config file")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    run_sequence(config.get("sequence", []))


if __name__ == "__main__":
    main()
