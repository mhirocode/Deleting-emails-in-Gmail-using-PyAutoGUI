import pyautogui
import time
import random

# ===== 事前準備 =====
# Gmailを開いておき、checkbox.png と delete_button.png を用意
# =====================

DELETE_COUNT = 5  # 削除する回数

time.sleep(3)  # 実行後の準備時間（ブラウザに切り替えるため）

for i in range(DELETE_COUNT):
    print(f"{i+1}回目の削除処理")

    # --- メールのチェックボックスを探してクリック ---
    checkbox_location = pyautogui.locateOnScreen("checkbox.png", confidence=0.8)
    if checkbox_location:
        center = pyautogui.center(checkbox_location)
        pyautogui.click(center.x, center.y)
        print("✅ メールを選択しました")
    else:
        print("⚠️ チェックボックスが見つかりませんでした")
        break

    # ランダムな待機（0.5〜1.5秒）
    sleep_time = random.uniform(2, 5)
    print(f"⌛ {sleep_time:.2f} 秒待機中...")
    time.sleep(sleep_time)

    # --- 削除ボタンを探してクリック ---
    delete_location = pyautogui.locateOnScreen("delete_button.png", confidence=0.8)
    if delete_location:
        center = pyautogui.center(delete_location)
        pyautogui.click(center.x, center.y)
        print("🗑️ 削除しました")
    else:
        print("⚠️ 削除ボタンが見つかりませんでした")
        break

    # 次のループに入る前もランダム待機（1〜3秒）
    sleep_time = random.uniform(1.0, 3.0)
    print(f"⌛ 次の処理まで {sleep_time:.2f} 秒待機中...")
    time.sleep(sleep_time)
