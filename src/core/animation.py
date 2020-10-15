from src.core.main import clear_screen
import time

app_name = "TeaRun 2.0"
welcome_message = f"\nWelcome to {app_name}\n\nNow brewing"

fps = 6

frame1 = f"""
 (  )
  )
 ,--.
C|  |
 `=='

{welcome_message}.
"""

frame2 = f"""
  )  
    (
 ,--.
C|  |
 `=='

{welcome_message}.
"""

frame3 = f"""
    )
  ( (
 ,--.
C|  |
 `=='

{welcome_message}..
"""

frame4 = f"""
   )(
  ( 
 ,--.
C|  |
 `=='

{welcome_message}..
"""

frame5 = f"""
  )
    ) 
 ,--.
C|  |
 `=='
 
{welcome_message}...
"""

frame6 = f"""
    (
  ( )
 ,--.
C|  |
 `=='

{welcome_message}...
"""

frames = [frame1, frame2, frame3, frame4, frame5, frame6]

def animate_frame(frame):
    print(frame)
    time.sleep(1 / fps)
    clear_screen()

def welcome_animation(repetitions):
    count = 0
    while count < repetitions:
        for frame in frames:
            animate_frame(frame)
        count += 1