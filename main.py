import pyautogui
import keyboard
import time
import random

# --- هذه الأرقام ستغيرها من الكمبيوتر لاحقاً ---
TARGET_X = 1000  
TARGET_Y = 500   
TARGET_COLOR = (88, 101, 242) # لون ديسكورد الأزرق

active = False

print("--- نظام صيد التكتات جاهز ---")
print("اضغط F8 للتشغيل | F9 للإيقاف")

while True:
    if keyboard.is_pressed('f8'):
        active = True
        print("تم التفعيل.. جاري مراقبة الشاشة")
        time.sleep(0.5)

    if keyboard.is_pressed('f9'):
        active = False
        print("تم الإيقاف")
        time.sleep(0.5)

    if active:
        # فحص اللون بسرعة فائقة
        if pyautogui.pixelMatchesColor(TARGET_X, TARGET_Y, TARGET_COLOR, tolerance=15):
            pyautogui.click(TARGET_X, TARGET_Y)
            print("تم صيد التكت!")
            active = False # يتوقف فوراً للأمان
    
    time.sleep(0.001)
  
