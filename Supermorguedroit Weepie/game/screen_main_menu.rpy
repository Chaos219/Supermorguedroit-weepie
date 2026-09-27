
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
transform ts_main_menu():
    yoffset 500
    ease 1.0 yoffset 0

screen main_menu():
    default credits_page = False

    # add "Diner_Background.png" zoom 0.5
    # add "gui/title_card_front.png" align (0.9, 1.0)

    # label("The Supermorguedroit Weepie") align (0.8, 0.2)

    


    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background size (1920, 1080)


    fixed:
        xysize (889, 989)
        pos (950, 92)

        at ts_main_menu()

        if credits_page:
            add "gui/title_card_back.png"
            label _("Meet the Staff!")

            button:
                xalign 0.5
                ypos 700
                style_prefix "mmbtn"
                # TODO: Remember to update with link
                
                text _("FLIP\nBACK")

                action Return()
        else:
            add "gui/title_card_front.png"

            label _("The Supermorguedroit Weepie")

            vbox:
                xalign 0.5
                ypos 300
                spacing 25


                textbutton ("Start Game . . . . . . . . . . .1.50") action Start()  #xpos 1000 ypos 400 action Start()
                textbutton ("Load Game . . . . . . . . . . . 1.50") action NullAction()#xpos 1000 ypos 450 action Jump("load")
                textbutton ("Settings . . . . . . . . . . . .1.50") action ShowMenu("preferences")#xpos 1000 ypos 500 action Jump("preferences")
                textbutton ("Credits . . . . . . . . . . . . 1.50") action SetScreenVariable("credits_page", True)#xpos 1000 ypos 550 action Jump("help")
                textbutton ("Quit . . . . . . . . . . . . . .1.50") action Quit()#xpos 1000 ypos 600 action Quit(confirm=not main_menu)

            button:
                xalign 0.5
                ypos 700
                style_prefix "mmbtn"
                # TODO: Remember to update with link
                
                text _("RATE OUR GAME")

                action NullAction()

        text "VESION [config.version]":
            style "main_menu_version"
            xalign 0.5
            yalign 1.0 yoffset -25


style main_menu_label:
    xalign 0.5
    ypos 80

style main_menu_label_text:
    color RED
    size 60
    font LOBSTER

style main_menu_button_text:
    font "gui/CourierPrime-Regular.ttf"
    hover_font "gui/CourierPrime-Italic.ttf"

    color "#000000"
    hover_color RED


style mmbtn_button:
    xysize (517, 195)
    background "gui/title_rate_flip_btn_background.png"
    hover_background Transform("gui/title_rate_flip_btn_background.png", matrixcolor=ColorizeMatrix(RED, RED))

style mmbtn_text:
    align (0.5, 0.5)
    size 65
    font VASTSHAD

    text_align 0.5

    color "#000"
    hover_color RED


style main_menu_version:
    xalign 0.5
    size 25
    font "gui/CourierPrime-Regular.ttf"

#     ## This empty frame darkens the main menu.
#     frame:
#         style "main_menu_frame"

#     ## The use statement includes another screen inside this one. The actual
#     ## contents of the main menu are in the navigation screen.
#     use navigation

#     if gui.show_name:

#         vbox:
#             style "main_menu_vbox"

#             text "[config.name!t]":
#                 style "main_menu_title"

#             text "[config.version]":
#                 style "main_menu_version"


# style main_menu_frame is empty
# style main_menu_vbox is vbox
# style main_menu_text is gui_text
# style main_menu_title is main_menu_text
# style main_menu_version is main_menu_text

# style main_menu_frame:
#     xsize 420
#     yfill True

#     background "gui/overlay/main_menu.png"

# style main_menu_vbox:
#     xalign 1.0
#     xoffset -30
#     xmaximum 1200
#     yalign 1.0
#     yoffset -30

# style main_menu_text:
#     properties gui.text_properties("main_menu", accent=True)

# style main_menu_title:
#     properties gui.text_properties("title")

# style main_menu_version:
#     properties gui.text_properties("version")

    