import json
import aiohttp
import asyncio
from typing import Dict

class AriaEventStoreDataSource(CloseoutDataSource):
    """
    Источник данных для closeout-проверки, читающий состояние задачи
    напрямую из AGP‑шлюза (Agent Gateway Protocol).
    """

    def __init__(self, agp_gateway_url: str, task_group_id: str):
        self.url = agp_gateway_url
        self.group_id = task_group_id

    def load_data(self) -> Dict:
        """
        Синхронная обёртка вокруг асинхронного запроса.
        Возвращает словарь с ключами:
          - streams: список словарей, каждый содержит stream_id, completion_event,
                     completion_timestamp, artifact_path, worker_contract, pdm_entry
          - workspace: путь к рабочему пространству задачи
        """
        return asyncio.run(self._load_data_async())

    async def _load_data_async(self) -> Dict:
        params = {"group_id": self.group_id, "format": "closeout"}
        timeout = aiohttp.ClientTimeout(total=5)

        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(self.url, params=params) as resp:
                    if resp.status != 200:
                        raise RuntimeError(
                            f"AGP gateway returned {resp.status}: {await resp.text()}"
                        )
                    data = await resp.json()
        except aiohttp.ClientError as e:
            raise RuntimeError(f"Failed to connect to AGP gateway: {e}") from e

        if "streams" not in data:
            raise ValueError("AGP response missing 'streams' field")
        return data
Пояснения

Метод load_data остаётся синхронным ради совместимости с существующим CloseoutDataSource; внутри он запускает асинхронный HTTP‑вызов.

Используется aiohttp для эффективного сетевого взаимодействия (стек ARIA полностью асинхронен).

В запросе передаются group_id и format=closeout, чтобы AGP‑шлюз вернул именно ту структуру, которая нужна closeout-скрипту.

Добавлены таймаут (5 с), обработка ошибок сети и проверка HTTP‑статуса.

Интеграция с orchestration-closeout.py

В скрипте orchestration-closeout.py этот источник данных может быть выбран так:

python
source = AriaEventStoreDataSource(
    agp_gateway_url="http://agp-gateway:8080/api/v1/tasks",
    task_group_id="reset-password-2025-03-15"
)
data = source.load_data()
# data == {"streams": [...], "workspace": "/app/workspace/..."}
Теперь closeout-проверка может выполняться по реальным данным из AGP‑шины, без необходимости вручную формировать JSON‑файлы.

