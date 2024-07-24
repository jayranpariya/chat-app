from datetime import datetime
from typing import Optional, List
from fastapi_camelcase import CamelModel
from pydantic import EmailStr, Field, constr, validator
from src.utils.constants import ROLE


class UserBase(CamelModel):
    first_name: str = Field(..., title="First Name",
                            description="The first name of the user")
    last_name: str = Field(..., title="Last Name",
                           description="The last name of the user")
    email: EmailStr = Field(..., title="Email",
                            description="The email of the user")
    role: str = Field(default=ROLE.USER, title="Role",
                      description="The role of the user")
    phone_number: Optional[str] = Field(
        None, title="Phone Number", description="The phone number of the user")
    request_count: int = Field(
        default=5, title="Request Count", description="The request count of the user")
    last_reset: Optional[datetime] = Field(
        None, title="Last Reset", description="The last reset of the user")
    is_subscribed: bool = Field(
        default=False, title="Is Subscribed", description="The subscription status of the user")
    subscribed_id: Optional[str] = Field(
        None, title="Subscribed ID", description="The subscription ID of the user")

    class Config:
        orm_mode = True


class UserCreateRequest(UserBase):
    password: constr(min_length=8) = Field(..., title="Password",
                                           description="The password of the user")
    confirm_password: str = Field(..., title="Confirm Password",
                                  description="The confirm password of the user")


class UserLoginRequest(CamelModel):
    email: EmailStr = Field(..., title="Email",
                            description="The email of the user")
    password: constr(min_length=8) = Field(..., title="Password",
                                           description="The password of the user")


class UserResponse(UserBase):
    id: str = Field(..., title="ID", description="The ID of the user")
    created_at: datetime = Field(..., title="Created At",
                                 description="The created date of the user")
    updated_at: datetime = Field(..., title="Updated At",
                                 description="The updated date of the user")


class UpdateUserRequest(CamelModel):
    first_name: Optional[str] = Field(
        None, title="First Name", description="The first name of the user")
    last_name: Optional[str] = Field(
        None, title="Last Name", description="The last name of the user")
    email: Optional[EmailStr] = Field(
        None, title="Email", description="The email of the user")
    phone_number: Optional[str] = Field(
        None, title="Phone Number", description="The phone number of the user")
    is_subscribed: Optional[bool] = Field(
        None, title="Is Subscribed", description="The subscription status of the user")
    subscribed_id: Optional[str] = Field(
        None, title="Subscribed ID", description="The subscription ID of the user")

    class Config:
        orm_mode = True
        extra = "forbid"


class ListUserResponse(CamelModel):
    users: List[UserResponse] = Field(..., title="Users",
                                      description="List of user objects")
    total: int = Field(..., title="Total", description="Total number of users")
    page: int = Field(1, title="Page", description="Current page number")
    size: int = Field(10, title="Size", description="Number of items per page")
    pages: int = Field(..., title="Pages", description="Total number of pages")

    class Config:
        orm_mode = True
