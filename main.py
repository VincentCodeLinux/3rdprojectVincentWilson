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
graphics.setup_dearpygui()
graphics.show_viewport()
graphics.start_dearpygui()
graphics.destroy_context()