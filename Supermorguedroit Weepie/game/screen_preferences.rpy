## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    
    tag menu

    use game_menu(_("Preferences"), scroll="vpgrid"):

        vbox:

            vbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        hbox:
                            if preferences.fullscreen:
                                text("window") ypos 5 
                            else:
                                text("window") color "#ff0000" ypos 5 

                            imagebutton:
                                idle "gui/button/switch_left.png"
                                hover "gui/button/switch_left.png"
                                selected_idle "gui/button/switch_right.png"
                                selected_hover "gui/button/switch_right.png"
                                padding 25,0,25,0
                                action Preference("display", "toggle")

                            if preferences.fullscreen:
                                text("Fullscreen") color "#ff0000" ypos 5 
                            else:
                                text("Fullscreen") ypos 5 
                            # textbutton _("Window") action Preference("display", "window")
                            # textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            vbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

    # add "images/Diner_Background.png" align (0.0, 0.0) zoom 0.5
    # add "gui/overlay/notepad_background.png" align (0.5, 0.5)
    # imagebutton:
        
    #     idle "gui/overlay/tab_idle_background.png"
    #     hover "gui/overlay/tab_selected_background.png"
    #     align (0.36, 0.3)
    #     action ShowMenu("save")
    # add "gui/overlay/top_page.png" align (0.5, 0.5)
    
    # textbutton _("Main Menu") action MainMenu()


    # if renpy.variant("pc") or renpy.variant("web"):
    #     hbox:        
    #         text "Windowed" color "FF0000"
    #         imagebutton:
    #             idle "gui/button/switch_left.png"
    #             hover "gui/button/switch_left.png"
    #             selected_idle "gui/button/switch_right.png"
    #             selected_hover "gui/button/switch_right.png"
    #             action Preference("display", "toggle")
    #         text "Fullscreen" color "C4C4C4"
    #         xalign 0.5
    #         yalign 0.3
                    

    #     vbox:
    #         label _("")
    #         textbutton _("Skip Unseen Text") action Preference("skip", "toggle") style ("check_button")
    #         textbutton _("Skip After Choices") action Preference("after choices", "toggle") style ("check_button")
    #         textbutton _("Skip Transitions") action InvertSelected(Preference("transitions", "toggle")) style ("check_button")
    #         xalign 0.44
    #         yalign 0.395
    #         spacing 6 


    #         ## Additional vboxes of type "radio_pref" or "check_pref" can be
    #         ## added here, to add additional creator-defined preferences.

    #     null height (4 * gui.pref_spacing)

    #     vbox:
    #         style_prefix "slider"
    #         box_wrap True


    #         vbox:

    #             if config.has_music:
    #                 label _("Music Volume")

    #                 hbox:
    #                     bar value Preference("music volume")

    #             if config.has_sound:

    #                 label _("Sound Volume")

    #                 hbox:
    #                     bar value Preference("sound volume")

    #                     if config.sample_sound:
    #                         textbutton _("Test") action Play("sound", config.sample_sound)
            


    #             if config.has_voice:
    #                 label _("Voice Volume")

    #                 hbox:
    #                     bar value Preference("voice volume")

    #                     if config.sample_voice:
    #                         textbutton _("Test") action Play("voice", config.sample_voice)

    #             if config.has_music or config.has_sound or config.has_voice:
    #                 null height gui.pref_spacing

    #                 textbutton _("Mute All"):
    #                     action Preference("all mute", "toggle")
    #                     style "mute_all_button"

    #         vbox:

    #             label _("Text Speed")

    #             bar value Preference("text speed")

    #             label _("Auto-Forward Time")

    #             bar value Preference("auto-forward time")
            
    #         xalign 0.56
    #         yalign 1.0

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"


style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675

