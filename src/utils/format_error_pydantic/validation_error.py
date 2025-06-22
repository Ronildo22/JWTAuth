from pydantic import ValidationError


def format_error_menssage(error: ValidationError) -> list[str]:
    return [
        f"{'.'.join(map(str, e['loc']))}: {e['msg']}" for e in error.errors()
    ]
