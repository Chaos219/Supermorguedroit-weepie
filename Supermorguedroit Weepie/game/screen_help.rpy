## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("CONTROLS")):

        style_prefix "help"

        vbox:
            xalign 0.5 ypos 200
            spacing 25

            hbox:
                xalign 0.5
                spacing 25

                hbox:

                    textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                    textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                    if GamepadExists():
                        textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            viewport id "helpvp":
                draggable True pagekeys True mousewheel True
                scrollbars None

                xysize (530, 600)

                

                has vbox:
                    spacing 25

                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help
            
            if GamepadExists() and device == "gamepad":
                textbutton _("Calibrate"):
                    style "pref_button"
                    xalign 0.5
                    ypos -80
                    action GamepadCalibrate()


        ## SCROLLBAR ##
        vbar value YScrollValue("helpvp"):
            ysize 520
            align (1.0, 0.5) xoffset 35




screen keyboard_help():
    style_prefix "helpsub"

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():
    style_prefix "helpsub"

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():
    style_prefix "helpsub"

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    

style help_button:
    xsize 185
    background None
    foreground None
    selected_foreground "gui/button/underline_selected_foreground.png"

style help_button_text:
    size 35
    font BADSCRIPT

    color GRAY
    hover_color BLACK
    selected_color RED

    xalign 0.5


style helpsub_hbox:
    xfill True
style helpsub_label_text:
    font LIBREBOLD
    size 25
    underline True
    color GREEN
    xsize 200

style helpsub_text:
    font LIBREREG
    size 20
    xsize 300
    xalign 1.0

