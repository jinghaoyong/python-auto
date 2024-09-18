import pyautogui
import time
import subprocess
import platform

def open_chrome_with_default_profile(url):
    # Ensure the URL is valid
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url

    # Open Chrome with the default profile
    if platform.system() == 'Windows':
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        subprocess.Popen([chrome_path, '--profile-directory=Default', url], shell=False)
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', '-a', 'Google Chrome', '--args', '--profile-directory="Default"', url])
    elif platform.system() == 'Linux':
        subprocess.Popen(['google-chrome', '--profile-directory=Default', url])

    # Wait for Chrome to open
    time.sleep(5)

def select_chatroom():
    # Coordinates of the chatroom element (You must find the correct ones for your screen)
    chatroom_x, chatroom_y = -1508.5, 255   # 305 adjust with the actual coordinates you determined , you want more right then + on X, you want more bottom then - on Y
    print("Attempting to click at coordinates:", chatroom_x, chatroom_y)
    pyautogui.click(chatroom_x, chatroom_y)
    print("Click action performed.")
    time.sleep(2)


def send_messages(messages):
    for message in messages:
        print(f"Typing message: {message}")
        pyautogui.write(message)
        time.sleep(0.5)  # Adjust sleep time if needed
        pyautogui.press('enter')
        print("Message sent.")
        time.sleep(1)  # Add a short delay between messages to ensure they are sent properly


if __name__ == '__main__':
    # Step 1: Open Chrome and navigate to the chat page
    bookmark_url = 'https://web.whatsapp.com/'  # Replace with the actual chat URL
    open_chrome_with_default_profile(bookmark_url)

    # Step 2: Wait for the page to load, then select the chatroom (you may need to adjust the time)
    time.sleep(5)  # Adjust this if the page takes longer to load
    select_chatroom()

    # Step 3: Type and send multiple messages
    messages_to_send = [
        'Surprise ! last 5 seconds to celebrate your birthday!',
        '4!',
        '3!',
        '2!',
        '1!',
        'Happy 20th brithday !! My Beloved Lim Ke wei',
        'Click this link ! https://jinghaoyong.github.io/kewei20bday/'
    ]
    send_messages(messages_to_send)
