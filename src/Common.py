#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')
gi.require_version('Gio', '2.0')
gi.require_version('GObject', '2.0')
gi.require_version('Pango', '1.0')
from gi.repository import Gtk, Gdk, Gio, GObject, Pango

import os

from locale import gettext as _tr

from Config import Config


class ListStoreItem(GObject.Object):
    __gtype_name__ = 'ListStoreItem'

    def __init__(self, item_name):
        super().__init__()

        self._item_name = item_name

    @GObject.Property
    def item_name(self):
        return self._item_name


def dropdown_model(item_list):
    """
    Generate a model (ListStore) and add items to model.
    """

    model = Gio.ListStore(item_type=ListStoreItem)
    for line_data in item_list:
        model.append(ListStoreItem(item_name=line_data))

    return model


def dropdown_signal_list_item_factory():
    """
    Generate and connect DropDown signals.
    """

    factory = Gtk.SignalListItemFactory()
    factory.connect("setup", on_list_item_factory_setup)
    factory.connect("bind", on_list_item_factory_bind)

    return factory


def on_list_item_factory_setup(factory, list_item):
    """
    Generate child widget of the list item.
    This widget can be simple or complex widget.
    """

    label = Gtk.Label()
    label.set_halign(Gtk.Align.START)
    list_item.set_child(label)


def on_list_item_factory_bind(factory, list_item):
    """
    Bind the list item to the row widget.
    """

    label = list_item.get_child()
    list_data = list_item.get_item()
    label.set_label(str(list_data.item_name))


def main_tab_togglebutton(text, image_name):
    """
    Generate main tab ToggleButton and its widgets.
    """

    # ToggleButton
    togglebutton = Gtk.ToggleButton()
    togglebutton.set_group(None)

    # Grid
    grid = Gtk.Grid.new()
    grid.set_row_homogeneous(True)
    grid.set_halign(Gtk.Align.CENTER)
    grid.set_valign(Gtk.Align.CENTER)
    togglebutton.set_child(grid)

    # Image
    image = Gtk.Image()
    image.set_from_icon_name(image_name)
    image.set_pixel_size(24)
    grid.attach(image, 0, 0, 1, 1)

    # Label
    label = Gtk.Label()
    label.set_label(text)
    grid.attach(label, 0, 1, 1, 1)

    return togglebutton


def sub_tab_togglebutton(text, image_name):
    """
    Generate Performance tab sub-tab ToggleButton and its widgets.
    """

    # ToggleButton
    togglebutton = Gtk.ToggleButton()
    togglebutton.set_group(None)

    # Grid
    grid = Gtk.Grid.new()
    grid.set_column_spacing(3)
    grid.set_valign(Gtk.Align.CENTER)
    grid.set_margin_top(2)
    grid.set_margin_bottom(2)
    togglebutton.set_child(grid)

    # Image
    image = Gtk.Image()
    image.set_from_icon_name(image_name)
    image.set_pixel_size(24)
    grid.attach(image, 0, 0, 1, 1)

    # Label
    label = Gtk.Label()
    label.set_label(text)
    grid.attach(label, 1, 0, 1, 1)

    return togglebutton


def reset_button():
    """
    Generate "Reset" button for menus and windows.
    """

    button = Gtk.Button()
    button.set_label(_tr("Reset"))
    button.set_halign(Gtk.Align.CENTER)

    return button


def dropdown_and_model(item_list):
    """
    Generate DropDown and its model.
    """

    dropdown = Gtk.DropDown()

    # Model (DropDown) - precision (CPU)
    model = dropdown_model(item_list)
    factory = dropdown_signal_list_item_factory()
    dropdown.set_model(model)
    dropdown.set_factory(factory)

    return dropdown


def text_attribute_bold_2x():
    """
    Define text attributes for bold and 2x labels.
    """

    global attribute_list_bold_2x

    attribute_list_bold_2x = Pango.AttrList()
    attribute = Pango.attr_weight_new(Pango.Weight.BOLD)
    attribute_list_bold_2x.insert(attribute)
    attribute = Pango.attr_scale_new(2.0)
    attribute_list_bold_2x.insert(attribute)


def text_attribute_bold():
    """
    Define text attributes for bold labels.
    """

    global attribute_list_bold

    attribute_list_bold = Pango.AttrList()
    attribute = Pango.attr_weight_new(Pango.Weight.BOLD)
    attribute_list_bold.insert(attribute)


def text_attribute_bold_underlined():
    """
    Define text attributes for bold and underlined labels.
    """

    global attribute_list_bold_underlined

    attribute_list_bold_underlined = Pango.AttrList()
    attribute = Pango.attr_weight_new(Pango.Weight.BOLD)
    attribute_list_bold_underlined.insert(attribute)
    attribute = Pango.attr_underline_new(Pango.Underline.SINGLE)
    attribute_list_bold_underlined.insert(attribute)


def tab_title_label(text):
    """
    Generate tab title Label.
    """

    if 'attribute_list_bold_2x' not in globals():
        text_attribute_bold_2x()

    # Label
    label = Gtk.Label()
    label.set_halign(Gtk.Align.START)
    label.set_margin_end(60)
    label.set_attributes(attribute_list_bold_2x)
    label.set_label(text)

    return label


def title_label(text):
    """
    Generate title Label.
    """

    if 'attribute_list_bold' not in globals():
        text_attribute_bold()

    label = Gtk.Label()
    label.set_attributes(attribute_list_bold)
    label.set_label(text)
    label.set_halign(Gtk.Align.START)

    return label


def menu_title_label(text):
    """
    Generate menu title Label.
    """

    if 'attribute_list_bold' not in globals():
        text_attribute_bold()

    label = Gtk.Label()
    label.set_attributes(attribute_list_bold)
    label.set_label(text)
    label.set_halign(Gtk.Align.CENTER)
    label.set_margin_bottom(10)

    return label


def device_vendor_model_label():
    """
    Generate device vendor model information Label.
    """

    if 'attribute_list_bold' not in globals():
        text_attribute_bold()

    label = Gtk.Label()
    label.set_halign(Gtk.Align.START)
    label.set_selectable(True)
    label.set_ellipsize(Pango.EllipsizeMode.END)
    label.set_attributes(attribute_list_bold)
    label.set_label("--")

    return label


def device_kernel_name_label():
    """
    Generate device kernel name information Label.
    """

    label = Gtk.Label()
    label.set_halign(Gtk.Align.START)
    label.set_selectable(True)
    label.set_ellipsize(Pango.EllipsizeMode.END)
    label.set_label("--")

    return label


def static_information_label(text):
    """
    Generate static information Label. Information on this label is not changed after it is set.
    """

    label = Gtk.Label()
    label.set_label(text)
    label.set_ellipsize(Pango.EllipsizeMode.END)
    label.set_halign(Gtk.Align.START)

    return label


def dynamic_information_label():
    """
    Generate dynamic information Label. Information on this label is changed by the code.
    """

    label = Gtk.Label()
    label.set_selectable(True)
    label.set_attributes(attribute_list_bold)
    label.set_label("--")
    label.set_ellipsize(Pango.EllipsizeMode.END)
    label.set_halign(Gtk.Align.START)

    return label


def clickable_label(text):
    """
    Generate clickable label. Mouse cursor is changed when mouse hover action is performed.
    """

    if 'attribute_list_bold_underlined' not in globals():
        text_attribute_bold_underlined()

    label = Gtk.Label()
    label.set_attributes(attribute_list_bold_underlined)
    label.set_label(text)
    label.set_ellipsize(Pango.EllipsizeMode.END)
    label.set_halign(Gtk.Align.START)
    cursor_link = Gdk.Cursor.new_from_name("pointer")
    label.set_cursor(cursor_link)

    return label


def tab_grid():
    """
    Generate tab Grid (root widget of the tab in the tab module).
    """

    tab_grid = Gtk.Grid()
    tab_grid.set_row_spacing(10)
    tab_grid.set_margin_top(2)
    tab_grid.set_margin_bottom(2)
    tab_grid.set_margin_start(2)
    tab_grid.set_margin_end(2)

    return tab_grid


def menu_main_grid():
    """
    Generate menu main grid.
    """

    main_grid = Gtk.Grid()
    main_grid.set_row_spacing(2)
    main_grid.set_margin_top(2)
    main_grid.set_margin_bottom(2)
    main_grid.set_margin_start(2)
    main_grid.set_margin_end(2)

    return main_grid


def style_provider_scrolledwindow_separator():
    """
    Define style provider for ScrolledWindow and Separator on for styled information.
    """

    global style_provider_scrolledwindow, style_provider_separator

    # Define style provider for scrolledwindow for border radius.
    css = b"scrolledwindow {border-radius: 8px 8px 8px 8px;}"
    style_provider_scrolledwindow = Gtk.CssProvider()
    style_provider_scrolledwindow.load_from_data(css)

    # Add separators for showing lines with contrast colors between some the performance data and set color of the separators.
    css = b"separator {background: rgba(50%,50%,50%,0.6);}"
    style_provider_separator = Gtk.CssProvider()
    style_provider_separator.load_from_data(css)


def styled_information_scrolledwindow(text1, tooltip1, text2, tooltip2):
    """
    Generate styled information ScrolledWindow (grid, labels, separators on it).
    """

    if 'style_provider_scrolledwindow' not in globals() or 'style_provider_separator' not in globals():
        style_provider_scrolledwindow_separator()

    # ScrolledWindow (text1 and text2)
    scrolledwindow = Gtk.ScrolledWindow()
    scrolledwindow.set_has_frame(True)
    scrolledwindow.get_style_context().add_provider(style_provider_scrolledwindow, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    scrolledwindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.NEVER)

    # Grid (text1 and text2)
    grid = Gtk.Grid()
    grid.set_column_homogeneous(True)
    grid.set_row_spacing(3)
    grid.set_margin_top(5)
    grid.set_margin_bottom(5)
    grid.set_margin_start(5)
    grid.set_margin_end(5)
    grid.set_valign(Gtk.Align.CENTER)
    scrolledwindow.set_child(grid)

    # Label (text1)
    label = static_information_label(text1)
    if tooltip1 != None:
        label.set_tooltip_text(tooltip1)
    label.set_halign(Gtk.Align.CENTER)
    grid.attach(label, 0, 0, 1, 1)

    # Label (text2)
    label = static_information_label(text2)
    if tooltip2 != None:
        label.set_tooltip_text(tooltip2)
    label.set_halign(Gtk.Align.CENTER)
    grid.attach(label, 1, 0, 1, 1)

    # Separator
    separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    separator.set_halign(Gtk.Align.CENTER)
    separator.set_valign(Gtk.Align.CENTER)
    separator.set_size_request(60, -1)
    separator.get_style_context().add_provider(style_provider_separator, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    grid.attach(separator, 0, 1, 1, 1)

    # Separator
    separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    separator.set_halign(Gtk.Align.CENTER)
    separator.set_valign(Gtk.Align.CENTER)
    separator.set_size_request(60, -1)
    separator.get_style_context().add_provider(style_provider_separator, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    grid.attach(separator, 1, 1, 1, 1)

    # Label (text1)
    label1 = dynamic_information_label()
    label1.set_halign(Gtk.Align.CENTER)
    grid.attach(label1, 0, 2, 1, 1)

    # Label (text2)
    label2 = dynamic_information_label()
    label2.set_halign(Gtk.Align.CENTER)
    grid.attach(label2, 1, 2, 1, 1)

    return scrolledwindow, label1, label2


def menu_colorchooserdialog(title_text, parent_window):

    if 'colorchooserdialog' not in globals():
        global colorchooserdialog
        colorchooserdialog = Gtk.ColorChooserDialog().new(title=title_text, parent=parent_window)
        colorchooserdialog.set_modal(True)

    return colorchooserdialog


def scrolledwindow_searchentry(text):
    """
    Generate SearchEntry.
    """

    searchentry = Gtk.SearchEntry()
    searchentry.props.placeholder_text = text
    searchentry.set_max_width_chars(100)
    searchentry.set_hexpand(True)
    searchentry.set_halign(Gtk.Align.CENTER)
    searchentry.set_valign(Gtk.Align.CENTER)

    return searchentry


def number_of_logical_cores():
    """
    Get number of online logical cores.
    """

    try:
        # First try a faster way: using "SC_NPROCESSORS_ONLN" variable.
        number_of_logical_cores = os.sysconf("SC_NPROCESSORS_ONLN")
    except ValueError:
        # As a second try, count by reading from "/proc/cpuinfo" file.
        with open("/proc/cpuinfo") as reader:
            proc_cpuinfo_lines = reader.read().split("\n")
        number_of_logical_cores = 0
        for line in proc_cpuinfo_lines:
            if line.startswith("processor"):
                number_of_logical_cores = number_of_logical_cores + 1

    return number_of_logical_cores


def device_vendor_model(modalias_output):
    """
    Get device vendor and model information.
    """

    # Define "udev" hardware database file directory.
    udev_hardware_database_dir = "/usr/lib/udev/hwdb.d/"
    # Some older Linux distributions use "/lib/" instead of "/usr/lib/" but they are merged under "/usr/lib/" in newer versions.
    if os.path.isdir(udev_hardware_database_dir) == False:
        udev_hardware_database_dir = "/lib/udev/hwdb.d/"
    if Config.environment_type == "flatpak":
        udev_hardware_database_dir = "/etc/udev/hwdb.d/"
    if Config.environment_type == "flatpak":
        udev_hardware_database_dir = os.path.dirname(os.path.realpath(__file__)) + "/../../../etc/udev/hwdb.d/"

    # Example modalias file contents for testing.
    # modalias_output = "usb:v0B95p1790d0100dcFFdscFFdp00icFFiscFFip00in00"
    # modalias_output = "virtio:d00000001v00001AF4"
    # modalias_output = "sdio:c00v02D0d4324"
    # modalias_output = "pci:v000010DEd00000DF4sv00001043sd00001642bc03sc00i00"
    # modalias_output = "pci:v0000168Cd0000002Bsv00001A3Bsd00002C37bc02sc80i00"
    # modalias_output = "pci:v000010ECd00008168sv00001043sd000016D5bc02sc00i00"
    # modalias_output = "pci:v00008086d00000116sv00001043sd00001642bc03sc00i00"
    # modalias_output = "pci:v00001B85d00006018sv00001B85sd00006018bc01sc08i02"
    # modalias_output = "pci:v0000144Dd0000A808sv0000144Dsd0000A801bc01sc08i02"
    # modalias_output = "of:NgpuT<NULL>Cnvidia,tegra210-gm20bCnvidia,gm20b"
    # modalias_output = "of:NgpuT(null)Cbrcm,bcm2835-vc4"
    # modalias_output = "scsi:t-0x05"
    # modalias_output = "scsi:t-0x00"

    # Determine device subtype.
    device_subtype, device_alias = modalias_output.split(":", 1)

    # Get device vendor, model if device subtype is PCI.
    if device_subtype == "pci":

        # Example pci device modalias: "pci:v000010DEd00000DF4sv00001043sd00001642bc03sc00i00".

        # Get device IDs from modalias file content.
        first_index = device_alias.find("v")
        last_index = first_index + 8 + 1
        device_vendor_id = device_alias[first_index:last_index]
        first_index = device_alias.find("d")
        last_index = first_index + 8 + 1
        device_model_id = device_alias[first_index:last_index]

        # Get search texts by using device IDs.
        search_text1 = "pci:" + device_vendor_id + "*" + "\n ID_VENDOR_FROM_DATABASE="
        search_text2 = "pci:" + device_vendor_id + device_model_id + "*" + "\n ID_MODEL_FROM_DATABASE="

        # Read database file for PCI devices.
        with open(udev_hardware_database_dir + "20-pci-vendor-model.hwdb", encoding="utf-8") as reader:
            # "encoding="utf-8"" is used for preventing "UnicodeDecodeError" errors during reading the file content if "C" locale is used.
            ids_file_output = reader.read()

        # Get device vendor, model names from device ID file content.
        if search_text1 in ids_file_output:
            rest_of_the_ids_file_output = ids_file_output.split(search_text1, 1)[1]
            device_vendor_name = rest_of_the_ids_file_output.split("\n", 1)[0]
            if search_text2 in ids_file_output:
                device_model_name = rest_of_the_ids_file_output.split(search_text2, 1)[1].split("\n", 1)[0]
            else:
                device_model_name = "Unknown"
        else:
            device_vendor_name = "Unknown"
            device_model_name = "Unknown"

    # Get device vendor, model if device subtype is virtio.
    elif device_subtype == "virtio":

        # Example virtio device modalias: "virtio:d00000001v00001AF4".

        # Get device IDs from modalias file content.
        first_index = device_alias.find("v")
        last_index = first_index + 8 + 1
        device_vendor_id = device_alias[first_index:last_index]
        first_index = device_alias.find("d")
        last_index = first_index + 8 + 1
        device_model_id = device_alias[first_index:last_index]
        # 1040 is added to device ID of virtio devices. For details: https://docs.oasis-open.org/virtio/virtio/v1.1/csprd01/virtio-v1.1-csprd01.html
        device_model_id = "d0000" + str(int(device_model_id.strip("d")) + 1040)

        # Get search texts by using device IDs.
        search_text1 = "pci:" + device_vendor_id + "*" + "\n ID_VENDOR_FROM_DATABASE="
        search_text2 = "pci:" + device_vendor_id + device_model_id + "*" + "\n ID_MODEL_FROM_DATABASE="

        # Read database file for VIRTIO devices.
        with open(udev_hardware_database_dir + "20-pci-vendor-model.hwdb") as reader:
            ids_file_output = reader.read()

        # Get device vendor, model names from device ID file content.
        if search_text1 in ids_file_output:
            rest_of_the_ids_file_output = ids_file_output.split(search_text1, 1)[1]
            device_vendor_name = rest_of_the_ids_file_output.split("\n", 1)[0]
            if search_text2 in ids_file_output:
                device_model_name = rest_of_the_ids_file_output.split(search_text2, 1)[1].split("\n", 1)[0]
            else:
                device_model_name = "Unknown"
        else:
            device_vendor_name = "Unknown"
            device_model_name = "Unknown"

    # Get device vendor, model if device subtype is USB.
    elif device_subtype == "usb":

        # Example usb device modalias: "usb:v0B95p1790d0100dcFFdscFFdp00icFFiscFFip00in00".

        # Get device IDs from modalias file content.
        first_index = device_alias.find("v")
        last_index = first_index + 4 + 1
        device_vendor_id = device_alias[first_index:last_index]
        first_index = device_alias.find("p")
        last_index = first_index + 4 + 1
        device_model_id = device_alias[first_index:last_index]

        # Get search texts by using device IDs.
        search_text1 = "usb:" + device_vendor_id + "*" + "\n ID_VENDOR_FROM_DATABASE="
        search_text2 = "usb:" + device_vendor_id + device_model_id + "*" + "\n ID_MODEL_FROM_DATABASE="

        # Read database file for USB devices.
        with open(udev_hardware_database_dir + "20-usb-vendor-model.hwdb") as reader:
            ids_file_output = reader.read()

        # Get device vendor, model names from device ID file content.
        if search_text1 in ids_file_output:
            rest_of_the_ids_file_output = ids_file_output.split(search_text1, 1)[1]
            device_vendor_name = rest_of_the_ids_file_output.split("\n", 1)[0]
            if search_text2 in ids_file_output:
                device_model_name = rest_of_the_ids_file_output.split(search_text2, 1)[1].split("\n", 1)[0]
            else:
                device_model_name = "Unknown"
        else:
            device_vendor_name = "Unknown"
            device_model_name = "Unknown"

    # Get device vendor, model if device subtype is SDIO.
    elif device_subtype == "sdio":

        # Example sdio device modalias: "sdio:c00v02D0d4324".

        # Get device IDs from modalias file content.
        first_index = device_alias.find("v")
        last_index = first_index + 4 + 1
        device_vendor_id = device_alias[first_index:last_index]
        first_index = device_alias.find("d")
        last_index = first_index + 4 + 1
        device_model_id = device_alias[first_index:last_index]

        # Get search texts by using device IDs.
        search_text1 = "sdio:" + "c*" + device_vendor_id + "*" + "\n ID_VENDOR_FROM_DATABASE="
        search_text2 = "sdio:" + "c*" + device_vendor_id + device_model_id + "*" + "\n ID_MODEL_FROM_DATABASE="

        # Read database file for SDIO devices.
        with open(udev_hardware_database_dir + "20-sdio-vendor-model.hwdb") as reader:
            ids_file_output = reader.read()

        # Get device vendor, model names from device ID file content.
        if search_text1 in ids_file_output:
            rest_of_the_ids_file_output = ids_file_output.split(search_text1, 1)[1]
            device_vendor_name = rest_of_the_ids_file_output.split("\n", 1)[0]
            if search_text2 in ids_file_output:
                device_model_name = rest_of_the_ids_file_output.split(search_text2, 1)[1].split("\n", 1)[0]
            else:
                device_model_name = "Unknown"
        else:
            device_vendor_name = "Unknown"
            device_model_name = "Unknown"

    # Get device vendor, model if device subtype is of.
    elif device_subtype == "of":

        # Example sdio device modalias (NVIDIA Tegra GPU on N.Switch device: "of:NgpuT<NULL>Cnvidia,tegra210-gm20bCnvidia,gm20b".

        device_vendor_name = device_vendor_id = device_alias.split("C", 1)[-1].split("C", 1)[0].split(",")[0].title()
        device_model_name = device_model_id = device_alias.split("C", 1)[-1].split("C", 1)[0].split(",")[1].title()

    # Get device vendor, model if device subtype is SCSI or IDE.
    elif device_subtype in ["scsi", "ide"]:

        # Example SCSI device modalias: "scsi:t-0x00".

        device_vendor_name = device_vendor_id = "[scsi_or_ide_disk]"
        device_model_name = device_model_id = "[scsi_or_ide_disk]"

    # Set device vendor, model if device subtype is not known so far.
    else:
        device_vendor_name = device_vendor_id = "Unknown"
        device_model_name = device_model_id = "Unknown"

    return device_vendor_name, device_model_name, device_vendor_id, device_model_id
