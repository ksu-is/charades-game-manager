import tkinter as tk
import tktimerwidget

main_window = tk.Tk()
##setting 'buttons' to true adds default buttons, otherwise
##we would have to map our own buttons.
timer_widget = tktimerwidget.TkTimer(main_window, buttons=True)

##Class provides the following methods:
timer_widget.start_timer()
timer_widget.stop()
timer_widget.reset()
timer_widget.start_countdown(120)
##'update_widget' updates the StringVar used by the widget, normally this
## gets called automatically.
#timer_widget.update_widget()
timer_widget.add_seconds(10)
timer_widget.subtract_seconds(5)
timer_widget.set_elapsed(99)

main_window.mainloop()