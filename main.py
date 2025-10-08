import dearpygui.dearpygui as graphics
import comp151Colors
graphics.create_context()
graphics.create_viewport(title="Vincents Picaso Art, width=900, height=900")
with graphics.window(label="Snowman", width=900, height=900):
    with graphics.drawlist(width=900, height=900):
        #This is where I made the body of the snowman
        graphics.draw_circle((400, 550), 100, fill=comp151Colors.WHITE)
        graphics.draw_circle((400, 450), 75, fill=comp151Colors.WHITE)
        graphics.draw_circle((400, 350), 65, fill=comp151Colors.WHITE)
        #This is where I add the buttons
        graphics.draw_circle((400, 420), 10, fill=comp151Colors.BLACK)
        graphics.draw_circle((400, 440), 10, fill=comp151Colors.BLACK)
        graphics.draw_circle((400, 460), 10, fill=comp151Colors.BLACK)
        #This is where I make the scarf
        graphics.draw_rectangle((335, 400), (465, 375), fill=comp151Colors.RED)
        graphics.draw_triangle((335, 390), (335, 401), (320, 395.5), fill=comp151Colors.RED, )
        graphics.draw_triangle((335, 390), (335, 375), (320, 382.5), fill=comp151Colors.RED, )
        #This is where I make the eyes
        graphics.draw_circle((375, 330), 10, fill=comp151Colors.BLACK)
        graphics.draw_circle((425, 330), 10, fill=comp151Colors.BLACK)
        #This is where I made the carrot as a nose
        graphics.draw_ellipse((350, 340), (420, 357), fill=comp151Colors.ORANGE)
        #This is the code for the smile with sticks
        graphics.draw_line((365, 362), (400, 370), color=comp151Colors.GRAY,
                                   thickness=5)
        graphics.draw_line((400, 370), (435, 352), color=comp151Colors.GRAY,
                           thickness=5)
        #This is where I make the hands...I made the end of the arrow look like actual branches
        graphics.draw_arrow((275, 375), (340, 430), color=comp151Colors.BLACK, thickness=20)
        graphics.draw_arrow((520, 375), (460, 430), color=comp151Colors.BLACK, thickness=20)
        #This is where I make the hat
        graphics.draw_rectangle((335, 300), (465, 280), fill=comp151Colors.BLACK)
        graphics.draw_rectangle((355, 210), (445, 280), fill=comp151Colors.BLACK)
        graphics.draw_rectangle((355, 260), (445, 280), fill=comp151Colors.RED)
        #This is where the code is for my name
        graphics.draw_text((500, 650), "Vincent Wilson", size=35)

graphics.setup_dearpygui()
graphics.show_viewport()
graphics.start_dearpygui()
graphics.destroy_context()