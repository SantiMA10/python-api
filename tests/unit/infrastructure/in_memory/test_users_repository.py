from expects import expect, equal

from src.domain.user import User
from src.infrastructure.in_memory.users_repository import InMemoryUsersRepository


class TestInMemoryUserRepository:
    def test_save_user(self) -> None:
        user = User(name="Jack", age=30)
        repository = InMemoryUsersRepository()

        repository.save(user)
        users = repository.find_all()

        expect(users).to(equal([user]))
