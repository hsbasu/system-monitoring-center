#!/usr/bin/env python3

# ----------------------------------- EnvironmentVariables - EnvironmentVariables GUI Import Function (contains import code of this module in order to avoid running them during module import) -----------------------------------
def environment_variables_gui_import_func():

    global Gtk, os

    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
    import os


    global MainGUI, EnvironmentVariables, EnvironmentVariablesMenusGUI
    import MainGUI, EnvironmentVariables, EnvironmentVariablesMenusGUI


    # Import locale and gettext modules for defining translation texts which will be recognized by gettext application (will be run by programmer externally) and exported into a ".pot" file. 
    global _tr                                                                                # This arbitrary variable will be recognized by gettext application for extracting texts to be translated
    import locale
    from locale import gettext as _tr

    # Define contstants for language translation support
    global application_name
    application_name = "system-monitoring-center"
    translation_files_path = "/usr/share/locale"
    system_current_language = os.environ.get("LANG")

    # Define functions for language translation support
    locale.bindtextdomain(application_name, translation_files_path)
    locale.textdomain(application_name)
    locale.setlocale(locale.LC_ALL, system_current_language)


# ----------------------------------- EnvironmentVariables - EnvironmentVariables GUI Function (the code of this module in order to avoid running them during module import and defines "EnvironmentVariables" tab GUI objects and functions/signals) -----------------------------------
def environment_variables_gui_func():

    # Environment Variables tab GUI objects
    global treeview7101, searchentry7101, button7101, button7103
    global radiobutton7101, radiobutton7102, radiobutton7103
    global label7101


    # Environment Variables tab GUI objects - get
    treeview7101 = MainGUI.builder.get_object('treeview7101')
    searchentry7101 = MainGUI.builder.get_object('searchentry7101')
    button7101 = MainGUI.builder.get_object('button7101')
    button7103 = MainGUI.builder.get_object('button7103')
    radiobutton7101 = MainGUI.builder.get_object('radiobutton7101')
    radiobutton7102 = MainGUI.builder.get_object('radiobutton7102')
    radiobutton7103 = MainGUI.builder.get_object('radiobutton7103')
    label7101 = MainGUI.builder.get_object('label7101')


    # Environment Variables tab GUI functions
    def on_treeview7101_button_press_event(widget, event):
        if event.button == 3:                                                                 # Open Environment Variables tab right click menu if mouse is right clicked on the treeview (and on any variable, otherwise menu will not be shown) and the mouse button is pressed.
            environment_variables_open_right_click_menu_func(event)

    def on_treeview7101_button_release_event(widget, event):
        if event.button == 1:                                                                 # Run the following function if mouse is left clicked on the treeview and the mouse button is released.
            EnvironmentVariables.environment_variables_treeview_column_order_width_row_sorting_func()

    def on_searchentry7101_changed(widget):
        radiobutton7101.set_active(True)
        EnvironmentVariables.environment_variables_treeview_filter_search_func()

    def on_button7101_clicked(widget):                                                        # "Environment Variables Tab Customizations" button
        EnvironmentVariablesMenusGUI.popover7101p.popup()

    def on_button7103_clicked(widget):                                                        # "Environment Variables Tab Search Customizations" button
        EnvironmentVariablesMenusGUI.popover7101p2.popup()

    def on_radiobutton7101_toggled(widget):                                                   # "Show all environment/shell variables" radiobutton
        if radiobutton7101.get_active() == True:
            EnvironmentVariables.environment_variables_treeview_filter_show_all_func()

    def on_radiobutton7102_toggled(widget):                                                   # "Show all environment variables" radiobutton
        if radiobutton7102.get_active() == True:
            EnvironmentVariables.environment_variables_treeview_filter_show_all_func()
            EnvironmentVariables.environment_variables_treeview_filter_environment_variables_logged_in_only()

    def on_radiobutton7103_toggled(widget):                                                   # "Show all shell variables" radiobutton
        if radiobutton7103.get_active() == True:
            EnvironmentVariables.environment_variables_treeview_filter_show_all_func()
            EnvironmentVariables.environment_variables_treeview_filter_environment_variables_logged_out_only()



    # Environment Variables tab GUI functions - connect
    treeview7101.connect("button-press-event", on_treeview7101_button_press_event)
    treeview7101.connect("button-release-event", on_treeview7101_button_release_event)
    searchentry7101.connect("changed", on_searchentry7101_changed)
    button7101.connect("clicked", on_button7101_clicked)
    button7103.connect("clicked", on_button7103_clicked)
    radiobutton7101.connect("toggled", on_radiobutton7101_toggled)
    radiobutton7102.connect("toggled", on_radiobutton7102_toggled)
    radiobutton7103.connect("toggled", on_radiobutton7103_toggled)


    # Environment Variables Tab - Treeview Properties
    treeview7101.set_activate_on_single_click(True)                                           # This command used for activating rows and column header buttons on single click. Column headers have to clicked twice (or clicked() command have to be used twice) for the first sorting operation if this is not used.
    treeview7101.set_fixed_height_mode(True)                                                  # This command is used for lower CPU usage when treeview is updated. It prevents calculating of the row heights on every update. To be able to use this command, "'column'.set_sizing(2)" command have to be used for all columns when adding them into treeview.
    treeview7101.set_headers_clickable(True)
    treeview7101.set_show_expanders(False)
    treeview7101.set_enable_search(True)                                                      # This command is used for searching by pressing on a key on keyboard or by using "Ctrl + F" shortcut.
    treeview7101.set_search_column(1)                                                         # This command used for searching by using entry.
    treeview7101.set_tooltip_column(1)


# ----------------------------------- Environment Variables - Open Right Click Menu Function (gets right clicked variable name and opens right click menu) -----------------------------------
def environment_variables_open_right_click_menu_func(event):

    path, _, _, _ = treeview7101.get_path_at_pos(int(event.x), int(event.y))
    model = treeview7101.get_model()
    treeiter = model.get_iter(path)
    if treeiter is None:
        environment_variables_no_variable_selected_dialog()
    if treeiter is not None:
        global selected_variable_value, selected_variable_type
        selected_variable_value = EnvironmentVariables.variable_list[EnvironmentVariables.environment_variables_data_rows.index(model[treeiter][:])]    # "[:]" is used in order to copy entire list to be able to use it for getting index in the "environment_variables_data_rows" list to use it getting name of the variable.
        selected_variable_type = EnvironmentVariables.variable_type_list[EnvironmentVariables.variable_list.index(selected_variable_value)]
        if selected_variable_type == _tr("Environment Variable") or selected_variable_type == _tr("Environment & Shell Variable"):    # Perform following oprations if variable is not shell variable.
            EnvironmentVariablesMenusGUI.menuitem7102m.set_sensitive(True)                    # Set "Edit Environment Variable" item as sensitive
            EnvironmentVariablesMenusGUI.menuitem7102m.set_tooltip_text("")                   # Delete "Edit Environment Variable" item tooltip text
            EnvironmentVariablesMenusGUI.menuitem7103m.set_sensitive(True)                    # Set "Delete Environment Variable" item as sensitive
            EnvironmentVariablesMenusGUI.menuitem7103m.set_tooltip_text("")                   # Delete "Delete Environment Variable" item tooltip text
        if selected_variable_type == _tr("Shell Variable"):                                   # Perform following oprations if variable is shell variable.
            EnvironmentVariablesMenusGUI.menuitem7102m.set_sensitive(False)                   # Set "Edit Environment Variable" item as insensitive
            EnvironmentVariablesMenusGUI.menuitem7102m.set_tooltip_text(_tr("Shell variables cannot be edited."))    # Set "Edit Environment Variable" item tooltip text
            EnvironmentVariablesMenusGUI.menuitem7103m.set_sensitive(False)                   # Set "Delete Environment Variable" item as insensitive
            EnvironmentVariablesMenusGUI.menuitem7103m.set_tooltip_text(_tr("Shell variables cannot be deleted."))    # Set "Delete Environment Variable" item tooltip text
        EnvironmentVariablesMenusGUI.menu7101m.popup(None, None, None, None, event.button, event.time)


# ----------------------------------- Startup - No Startup Item Selected Dialog Function (shows a dialog when Open Startup Item Right Click Menu is clicked without selecting a startup item) -----------------------------------
def environment_variables_no_variable_selected_dialog():

    dialog7101 = Gtk.MessageDialog(transient_for=MainGUI.window1, title=_tr("Warning"), flags=0, message_type=Gtk.MessageType.WARNING,
    buttons=Gtk.ButtonsType.CLOSE, text=_tr("Select A Variable"), )
    dialog7101.format_secondary_text(_tr("Please select a variable and try again for opening the menu"))
    dialog7101.run()
    dialog7101.destroy()