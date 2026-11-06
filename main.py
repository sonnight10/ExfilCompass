"""Point d'entrée : python main.py  (option --demo pour tester sans le jeu)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from exfilcompass.app import UI_DIR, Api  # noqa: E402


def main() -> None:
    if len(sys.argv) >= 3 and sys.argv[1] == "--mini":
        from exfilcompass.mini import run  # noqa: E402
        try:
            run(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 0,
                sys.argv[4] if len(sys.argv) > 4 else "full", sys.argv[5] if len(sys.argv) > 5 else "m")
        except BaseException:
            import traceback
            try:
                Path(sys.argv[2] + ".err").write_text(traceback.format_exc(), encoding="utf-8")
            except OSError:
                pass
            raise
        return
    try:
        import webview
    except ImportError:
        print("pywebview n'est pas installé : pip install -r requirements.txt")
        raise SystemExit(1)

    api = Api()
    window = webview.create_window(
        "ExfilCompass",
        url=str(UI_DIR / "index.html"),
        js_api=api,
        width=1440,
        height=900,
        min_size=(480, 380),
        background_color="#0a0c12",
    )
    api._attach(window)
    if "--demo" in sys.argv:
        window.events.loaded += lambda: api.demo()
    try:
        webview.start(debug="--debug" in sys.argv)
    finally:
        api.shutdown()


if __name__ == "__main__":
    main()
