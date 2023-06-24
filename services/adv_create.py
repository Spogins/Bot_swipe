import base64
import json
from aiohttp import ClientSession
from configs.settings import BOT, API_ROOT
from services.user_data import get_new_token, get_user


async def get_base64(image):
    file_info = await BOT.get_file(image)
    file = await BOT.download_file(file_info.file_path)
    file_base64 = base64.b64encode(file.read()).decode('utf-8')
    return file_base64


async def json_adv_data(data):
    scheme_base64 = await get_base64(data.get('scheme'))

    gal_base64 = await get_base64(data.get('photo_gallery'))

    flat_data = {
        "residential_complex": {
            "name": f"{data.get('res_complex')}"
        },
        "section": {
            "name": f"{data.get('section')}"
        },
        "floor": {
            "name": f"{data.get('floor')}"
        },
        "corps": {
            "name": f"{data.get('corps')}"
        },
        "scheme": f"{scheme_base64}",
        "photo_gallery": [
            {
                f"image": f"{gal_base64}"
            }
        ],
        "room_amount": data.get('room_amount'),
        "price": data.get('price'),
        "square": data.get('square'),
        "kitchen_square": data.get('kitchen'),
        "balcony": data.get('balcony'),
        "commission": data.get('commission'),
        "district": f"{data.get('district')}",
        "micro_district": f"{data.get('micro_district')}",
        "living_condition": f"{data.get('living_condition')}",
        "planning": f"{data.get('planning')}"
    }
    flat_data_json = json.dumps(flat_data)
    return flat_data_json


async def adv_request(user_id, data):
    await get_new_token(user_id)
    user = await get_user(user_id)
    flat_data = await json_adv_data(data)
    async with ClientSession() as session:
        async with session.post(
            url=f'{API_ROOT}/api/v1/flat/',
            headers={
                'Authorization': f'Bearer {user.get("access_token")}',
                'Content-Type': 'application/json'
            },
            data=flat_data
        ) as response:
            _json = await response.json()
    return _json
