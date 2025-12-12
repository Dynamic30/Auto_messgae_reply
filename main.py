import pyautogui
import pyperclip
from ollama import chat
from ollama import ChatResponse

pyautogui.moveTo(920,215,2)
# pyautogui.click(1735,986,2)
pyautogui.dragTo(2450,1290,button='left',duration=1)


# pyautogui.hotkey('ctrl', 'a')
    
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'c')



text = pyperclip.paste()
print(text)
want_to_proceed = input("Want to proceed(Y/N):").strip().lower()
if want_to_proceed in ['y','yes']:
    ChatResponse = chat(model='gemma3:12b', messages=[
    {
        'role': 'you are a bot who reply on behalf of Person without others finding out',
        'content': text,
    },
    ])
    msg = ChatResponse.message.content
    print(msg)
    send = input("Do you want to send the message(y/n): ").strip().lower()

    if send == 'y':
        pyautogui.moveTo(919,1413,2)
        pyautogui.click(919,1413)
        pyautogui.write('WhatsApp', interval=0.25)
        pyautogui.click(1110,861,2)
        pyautogui.moveTo(450,520,2)
        pyautogui.click(450,520,2)
        pyautogui.write(msg)
    else:
        print("Task completed")

    
elif want_to_proceed in ['n','']:
    print("Task cancelled")