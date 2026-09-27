## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

transform ts_hist_fadein():
    yoffset 800 
    ease 1.0 yoffset 0


image hist_mc = Composite(
    (216, 237),
    (0, 0),Transform(Crop((447, 127, 693, 760), "mc_main.png"), xsize=216, fit="contain"),
    (0, 0), "gui/log_speaker_foreground.png"
)
image hist_leeroy = Composite(
    (216, 237),
    (0, 0), Transform(Crop((722, 100, 693, 760), "LeeRoy_main.png"), xsize=216, fit="contain"),
    (0, 0), "gui/log_speaker_foreground.png"
)

image hist_adelaide = Composite(
    (216, 237),
    (0, 0), Transform(Crop((417, 178, 693, 760), "adelaide_main.png"), xsize=216, fit="contain"),
    (0, 0), "gui/log_speaker_foreground.png"
)

image hist_oe = Composite(
    (216, 237),
    (0, 0), Transform(Crop((417, 178, 693, 760), "oe_main.png"), xsize=216, fit="contain"),
    (0, 0), "gui/log_speaker_foreground.png"
)



screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    

    add OVERLAY

    fixed:
        at ts_hist_fadein()
        xysize (1345, 1044)
        align (0.5, 1.0)
        add "gui/log_background.png"

        ## RETURN BUTTON ##
        imagebutton auto "gui/button/return1_%s_background.png":
            action Return()
            align (1.0, 0.0) offset (-20,15)

        vbox:
            xsize 1200
            pos (80, 30)
            spacing 15

            label _("DAILY READER") style "hist_title"


            text _("Reread today's conversation.") style "hist_subtitle"

            null height 25

            ## THE LOG ##
            viewport id "histvp":
                draggable True mousewheel True pagekeys True
                scrollbars None yinitial 1.0

                ysize 750
                xoffset 25
                

                style_prefix "history"

                has vbox:
                    spacing 15
                    

                for h in _history_list:
                    if h.who:
                        hbox:
                            if h.who == "Dorothy":
                                add "hist_mc"
                            elif h.who == "Adelaide":
                                add "hist_adelaide"
                            elif h.who == "LeeRoy":
                                add "hist_leeroy"
                            elif h.who == "Ōe":
                                add "hist_oe"

                            else:
                                fixed:
                                    xysize (216, 237)
                                    add "gui/log_speaker_foreground.png"
                                    if h.who == "Mr. Hollis":
                                        text "H" align (0.5, 0.5) size 60 
                                    else:
                                        text h.who[0] align (0.5, 0.5) size 60 

                            null width 35
                            vbox:
                                spacing 10
                                label h.who
                                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                                text what:
                                    substitute False

                    else:
                        hbox:
                            null width 216

                            $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                            text what:
                                xalign 0.5
                                substitute False

                    null height 35

                    add "gui/log_line_divider.png" xalign 0.5 xoffset 65

                    null height 35
                        

                

    ## SCROLLBAR ##
    vbar value YScrollValue("histvp"):
        ysize 735
        yalign 0.5
        xpos 1685

    


        



style hist_title:
    xalign 0.5

style hist_title_text:
    color BROWN
    font LIBREBOLD
    size 90

style hist_subtitle:
    xalign 0.5
    size 25
    font LIBREREG
    color BROWN

style history_label_text:
    color BROWN
    font LIBREREG
    size 45

style history_text:
    color BROWN
    size 25

    font LIBREREG
    xsize 800
    


    # use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

    #     style_prefix "history"

    #     for h in _history_list:

    #         window:

    #             ## This lays things out properly if history_height is None.
    #             has fixed:
    #                 yfit True

    #             if h.who:

    #                 label h.who:
    #                     style "history_name"
    #                     substitute False

    #                     ## Take the color of the who text from the Character, if
    #                     ## set.
    #                     if "color" in h.who_args:
    #                         text_color h.who_args["color"]

    #             $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
    #             text what:
    #                 substitute False

    #     if not _history_list:
    #         label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


# style history_window is empty

# style history_name is gui_label
# style history_name_text is gui_label_text
# style history_text is gui_text

# style history_label is gui_label
# style history_label_text is gui_label_text

# style history_window:
#     xfill True
#     ysize gui.history_height

# style history_name:
#     xpos gui.history_name_xpos
#     xanchor gui.history_name_xalign
#     ypos gui.history_name_ypos
#     xsize gui.history_name_width

# style history_name_text:
#     min_width gui.history_name_width
#     textalign gui.history_name_xalign

# style history_text:
#     xpos gui.history_text_xpos
#     ypos gui.history_text_ypos
#     xanchor gui.history_text_xalign
#     xsize gui.history_text_width
#     min_width gui.history_text_width
#     textalign gui.history_text_xalign
#     layout ("subtitle" if gui.history_text_xalign else "tex")

# style history_label:
#     xfill True

# style history_label_text:
#     xalign 0.5

