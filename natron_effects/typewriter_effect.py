from NatronGui import *

node = app1.getNode("Text1")
text_param = node.getParam("text")
full_text = text_param.get()

frames_per_char = 2
pause_final_frames = 10
underline = "_"
blink_frames = 1

start_frame = 1
end_frame = start_frame + len(full_text) * frames_per_char + pause_final_frames

text_param.removeAnimation()

current_text = ""

for i in range(1, len(full_text) + 1):
    for b in range(3):  # pisca 3 vezes
        frame_show = start_frame + (i - 1) * frames_per_char + b * 2
        frame_hide = frame_show + 1
        text_param.setValueAtTime(current_text + underline, frame_show)
        text_param.setValueAtTime(current_text, frame_hide)

    current_text += full_text[i-1]
    frame_write = start_frame + (i - 1) * frames_per_char + 6
    text_param.setValueAtTime(current_text, frame_write)

text_param.setValueAtTime(full_text, end_frame)