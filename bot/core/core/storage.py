from .controller import BaseController


class BaseStorage:
    class _Keys:
        pass

    def __init__(self, controller: BaseController):
        self.state = controller.state

    async def get(self, key: str):
        data = await self.state.get_data()
        return data[key]

    async def set(self, key: str, value):
        await self.state.update_data({key: value})
