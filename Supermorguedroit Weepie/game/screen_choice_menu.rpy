
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    default selected_action = None

    vbox:
        xalign 0.5
        ypos 200
        spacing 25

        hbox:
            spacing 35

            for i in items:
                button:
                    text i.caption ypos 4
                    action SetScreenVariable("selected_action", i.action)

        button:
            xysize (390, 90)
            xalign 0.5
            padding (0, 0)

            insensitive_background Transform("gui/button/button_idle_background.png", matrixcolor=BrightnessMatrix(-0.1))
            background "gui/button/button_[prefix_]background.png"
            foreground None
            text _("CONFIRM"):
                line_spacing 0
                align (0.5, 0.5)
                color BLACK
                hover_color WHITE
                insensitive_color GRAY

            sensitive selected_action is not None

            action selected_action

            



style choice_button is default:
    background "gui/button/choice_hover_background.png"
    idle_foreground "gui/button/choice_idle_foreground.png"
    hover_foreground None
    selected_foreground None

    xysize (281, 385)
    padding (25, 45)


style choice_text:
    xsize 240
    color BLACK
    hover_color RED
    insensitive_color GRAY
    # ypos 45
    line_spacing 15
    size 30

# style choice_vbox is vbox
# style choice_button is button
# style choice_button_text is button_text

# style choice_vbox:
#     xalign 0.5
#     ypos 405
#     yanchor 0.5

#     spacing gui.choice_spacing

# style choice_button is default:
#     properties gui.button_properties("choice_button")

# style choice_button_text is default:
#     properties gui.text_properties("choice_button")

