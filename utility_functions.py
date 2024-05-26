import ctypes
import os
import sys


def place_window_in_center(master, width, height, multiply=False, window_name=None):
    """
    Center the Application in the middle of the screen (window_name is None)
        Center the window in the middle of the Application window (window_name is not None)
    :param master: root
    :param width: the desired width of the window (int)
    :param height: the desired height of the window (int)
    :param window_name: default = None
    :param multiply: default = False
    """

    scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100

    if multiply is False or scale_factor == 1:

        multiply_by = scale_factor

    else:

        multiply_by = scale_factor

    multiplication_scale = 2 * multiply_by

    if window_name is None:

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        x_coordinate = int((screen_width - width) / (multiplication_scale * scale_factor))
        y_coordinate = int((screen_height - height) / (multiplication_scale * scale_factor))

        master.geometry('{}x{}+{}+{}'.format(width, height, x_coordinate, y_coordinate))

    else:

        root_height = master.winfo_height()
        root_width = master.winfo_width()

        root_x = master.winfo_x()
        root_y = master.winfo_y()

        x = int((root_width - width) / (multiplication_scale / scale_factor))
        y = int((root_height - height) / (multiplication_scale / scale_factor))

        window_name.geometry('{}x{}+{}+{}'.format(width, height, x + root_x, y + root_y))

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
