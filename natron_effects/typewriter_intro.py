class Intro:

    @staticmethod
    def set_color(param, frame, rgba):
        for i, v in enumerate(rgba):
            param.setValueAtTime(v, frame, i)

    @staticmethod
    def effect_intro(app1):

        node = app1.getNode("Intro")
        text_param = node.getParam("text")
        color_param = node.getParam("color")
        full_text = text_param.get()

        frames_per_char = 2
        pause_final_frames = 10
        underline = "_"

        start_frame = 40
        end_frame = start_frame + len(full_text) * frames_per_char + pause_final_frames

        text_param.removeAnimation()
        color_param.removeAnimation()

        for i in range(4):
            color_param.removeAnimation(i)

        for i in range(4):
            color_param.setValue(0.6631, i)

        text_param.setValueAtTime("", 1)
        text_param.setValueAtTime("", start_frame - 1)

        Intro.set_color(color_param, 1, (0.6631, 0.6631, 0.6631, 1.0))
        Intro.set_color(color_param, start_frame - 1, (0.6631, 0.6631, 0.6631, 1.0))

        current_text = ""

        for i in range(1, len(full_text) + 1):
            for b in range(3):
                frame_show = start_frame + (i - 1) * frames_per_char + b * 2
                frame_hide = frame_show + 1
                text_param.setValueAtTime(current_text + underline, frame_show)
                text_param.setValueAtTime(current_text, frame_hide)

            current_text += full_text[i - 1]
            frame_write = start_frame + (i - 1) * frames_per_char + 6
            text_param.setValueAtTime(current_text, frame_write)

        text_param.setValueAtTime(full_text, end_frame)
        Intro.set_color(color_param, end_frame - 1, (0.6631, 0.6631, 0.6631, 1.0))
        Intro.set_color(color_param, end_frame, (0.0, 1.0, 0.0159962922334671, 1.0))
        Intro.set_color(color_param, 300, (0.0, 1.0, 0.0159962922334671, 1.0))
