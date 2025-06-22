from pydantic import BaseModel, field_validator


class RefreshInputDTO(BaseModel):
    refresh_token: str

    @field_validator("refresh_token", check_fields=False)
    def username_is_null(cls, value):
        if not value.strip():
            raise ValueError("refresh_token cannot be empty")
        return value
