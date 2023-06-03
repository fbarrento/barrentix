from app.bootstrap import app  # type: ignore

app = app()


def main() -> None:
    print(app.config)


if __name__ == "__main__":
    main()
