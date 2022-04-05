"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Crypto Berry Bot."""


if __name__ == "__main__":
    main(prog_name="CryptoBerryBot")  # pragma: no cover
