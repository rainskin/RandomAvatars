import config
from assets import PictureCategory
from .chats import Chats
from .pictures import Pictures
from .required_join import RequiredJoin
from .user import User


class Api:

    def __init__(self, base_url: str):
        self._base_url = base_url
        self.required_join = RequiredJoin(base_url + '/required-join')
        self.chats = Chats(base_url + '/chats')

    def user(self, user_id: int) -> User:
        return User(self._base_url + f'/user/{user_id}')

    def pictures(self, category: PictureCategory):
        return Pictures(self._base_url + f'/pictures/{category}')


api = Api(config.API_BASE_URL)
