import os
from tkinter.messagebox import *
from typing import List, Optional

from lib.controller.utils import is_url
from lib.model.setting import Config


def parse(law_inputs: List[str]) -> Optional[Config]:
    proxy = law_inputs[0]
    port = law_inputs[1]
    place = law_inputs[2]

    if not validation(proxy, port, place):
        return

    ret = Config(proxy_address=proxy, port=int(port))
    return ret


def validation(proxy: str, port: str, place: str) -> bool:
    # URLチェック
    if not is_url(proxy):
        showerror("アドレスが無効です。正しいURLを入力してください。")
        return False

    # ポート番号チェック
    if not port.isnumeric():
        showerror("ポート番号は数値で入力してください。")
        return False

    if not (0 <= int(port) <= 65535):
        showerror("ポート番号が無効です。0〜65535の間で指定してください。")
        return False

    # ファイルチェック
    if not os.path.exists(place):
        showerror("ファイルが見つかりませんでした。パスを確認してください。")
        return False

    return True
