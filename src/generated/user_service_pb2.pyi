from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id", "name", "email", "age", "is_active")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    email: str
    age: int
    is_active: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., age: _Optional[int] = ..., is_active: bool = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("name", "email", "age")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    email: str
    age: int
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("page", "page_size")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "total_count")
    USERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    total_count: int
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class UserService(_service.service): ...

class UserService_Stub(UserService): ...
