## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    
    tag menu
    
    use game_menu(_("SETTINGS")):

        viewport id "prefvp":
            draggable True pagekeys True mousewheel True
            scrollbars None

            xysize (530, 600)

            xalign 0.5 ypos 225

            has vbox:
                spacing 10


            style_prefix "pref"

            ## DISPLAY ##
            hbox:
                # if preferences.fullscreen:
                #     text("WINDOWED") ypos 5 
                # else:
                #     text("WINDOWED") color "#ff0000" ypos 5

                # imagebutton:
                #     idle "gui/button/switch_left.png"
                #     hover "gui/button/switch_left.png"
                #     selected_idle "gui/button/switch_right.png"
                #     selected_hover "gui/button/switch_right.png"
                #     padding 10,0,10,0
                #     action Preference("display", "toggle")

                # if preferences.fullscreen:
                #     text("FULLSCREEN") color "#ff0000" ypos 5 
                # else:
                #     text("FULLSCREEN") ypos 5 




                xfill True
                textbutton _("WINDOWED"):
                    selected preferences.fullscreen == False
                    action Preference("display", "window")

                if preferences.fullscreen == False:
                    add "gui/button/switch_left.png"
                    
                else:
                    add "gui/button/switch_right.png"
                    
                textbutton _("FULLSCREEN"):
                    selected preferences.fullscreen
                    action Preference("display", "fullscreen")


            ## TEXT STUFF ##
            null height 45
            vbox:
                spacing 0
                label _("TEXT SPEED")
                bar value Preference("text speed") style "prefbar"

                null height 5

                label _("AUTO WAIT TIME")
                bar value Preference("auto-forward time") style "prefbar"
                


            ## SKIP ##
            null height 45
            vbox:
                spacing 8
                style_prefix "prefcheck"

                textbutton _("SKIP UNREAD TEXT") action Preference("skip", "toggle")
                textbutton _("SKIP AFTER CHOICES") action Preference("after choices", "toggle")
                textbutton _("SKIP TRANSITIONS") action InvertSelected(Preference("transitions", "toggle"))

            ## BGM ##
            null height 45
            vbox:
                spacing 0
                label _("MAIN")
                bar value Preference("main volume") style "prefbar"

                null height 5

                label _("BGM")
                bar value Preference("music volume") style "prefbar"

                null height 5

                label _("SFX")
                bar value Preference("sound volume") style "prefbar"

                textbutton _("MUTE"):
                    action Preference("all mute", "toggle")
                    style_prefix "prefcheck"
                            





        ## SCROLLBAR ##
        vbar value YScrollValue("prefvp"):
            ysize 520
            align (1.0, 0.5) xoffset 35


style pref_label_text:
    font BADSCRIPT
    size 35
    color BLACK   

style pref_button:
    yalign 0.5


style pref_button_text:
    font LIBREREG
    size 25

    color GRAY
    hover_color BLACK
    selected_color RED


style prefcheck_button:
    is pref_button
    foreground "gui/button/check_[prefix_]foreground.png"
    left_padding 65

style prefcheck_button_text:
    is pref_button_text



style prefbar:
    xysize (531, 45)
    left_bar "gui/bar/left.png"
    right_bar "gui/bar/right.png"


