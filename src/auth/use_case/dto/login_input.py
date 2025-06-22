from pydantic import BaseModel, field_validator


class LoginInputDTO(BaseModel):
    username: str
    password: str

    @field_validator("username", check_fields=False)
    def username_is_null(cls, value):
        if not value.strip():
            raise ValueError("username cannot be empty")
        return value

    @field_validator("password", check_fields=False)
    def password_is_null(cls, value):
        if not value.strip():
            raise ValueError("password cannot be empty")
        return value
