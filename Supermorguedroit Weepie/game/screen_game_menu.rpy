################################################################################
## Main and Game Menu Screens
################################################################################
##

## Game menu screen ###########################################################
# Not using the nav screen
transform ts_gmnavbtn():
    on hover:
        xoffset 0
        linear 0.5 xoffset -100
    on idle:
        linear 0.5 xoffset 0
    on selected_hover:
        xoffset 0


screen game_menu(title=None, scroll=None,yinitial=0.0, spacing=0):
    add gui.main_menu_background size (1920, 1080)
    add OVERLAY

    fixed:
        xysize (782, 965)
        align (0.5, 0.5) xoffset 70
        at ts_main_menu()

        # Back
        add "gui/overlay/notepad_background.png"


        ## TABS ##
        vbox:
            xanchor 1.0 xpos 100
            yalign 0.5
            spacing 15

            style_prefix "gmnav"

            button:
                at ts_gmnavbtn()
                if renpy.get_screen("load"):
                    foreground Transform("gui/overlay/load_[prefix_]icon.png", yalign=0.5, xpos=50)
                    selected_foreground Transform("gui/overlay/load_selected_icon.png", yalign=0.5, xpos=50)
                    selected renpy.get_screen("load")
                    action ShowMenu("load")
                else:
                    foreground Transform("gui/overlay/save_[prefix_]icon.png", yalign=0.5, xpos=50)
                    selected_foreground Transform("gui/overlay/save_selected_icon.png", yalign=0.5, xpos=50)
                    selected renpy.get_screen("save")
                    action ShowMenu("save")

            button:
                at ts_gmnavbtn()
                foreground Transform("gui/overlay/settings_[prefix_]icon.png", yalign=0.5, xpos=50)
                selected_foreground Transform("gui/overlay/settings_selected_icon.png", yalign=0.5, xpos=50)
                selected renpy.get_screen("preferences")
                action ShowMenu("preferences")

            button:
                at ts_gmnavbtn()
                foreground Transform("gui/overlay/controls_[prefix_]icon.png", yalign=0.5, xpos=50)
                selected_foreground Transform("gui/overlay/controls_selected_icon.png", yalign=0.5, xpos=50)
                selected renpy.get_screen("help")
                action ShowMenu("help")


        # Front
        add "gui/overlay/top_page.png"


        ## STUFF ##
        

        label title style "gmnav_title" ypos 90

        transclude


        ## RETURN ##
        imagebutton auto "gui/button/return2_%s_background.png":
            xalign 1.0 xoffset -25
            ypos 120
            action Return()

        ## HOME ##
        imagebutton auto "gui/button/home_%s_background.png":
            xalign 1.0 xoffset -25
            ypos 215
            action MainMenu()
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    

style gmnav_button:
    xysize (200, 95)
    background "gui/overlay/tab_idle_background.png"
    selected_background "gui/overlay/tab_selected_background.png"

    
style gmnav_title:
    xalign 0.5

style gmnav_title_text:
    font BADSCRIPT
    size 65
    color BLACK




# ## Navigation screen ###########################################################
# ##
# ## This screen is included in the main and game menus, and provides navigation
# ## to other menus, and to start the game.

# screen navigation():

#     vbox:
#         style_prefix "navigation"

#         xpos gui.navigation_xpos
#         yalign 0.5

#         spacing gui.navigation_spacing

#         if main_menu:

#             textbutton _("Start") action Start()

#         else:

#             textbutton _("History") action ShowMenu("history")

#             textbutton _("Save") action ShowMenu("save")

#         textbutton _("Load") action ShowMenu("load")

#         textbutton _("Settings") action ShowMenu("preferences")

#         if _in_replay:

#             textbutton _("End Replay") action EndReplay(confirm=True)

#         elif not main_menu:

#             textbutton _("Main Menu") action MainMenu()

#         textbutton _("About") action ShowMenu("about")

#         if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

#             ## Help isn't necessary or relevant to mobile devices.
#             textbutton _("Help") action ShowMenu("help")

#         if renpy.variant("pc"):

#             ## The quit button is banned on iOS and unnecessary on Android and
#             ## Web.
#             textbutton _("Quit") action Quit(confirm=not main_menu)


# style navigation_button is gui_button
# style navigation_button_text is gui_button_text

# style navigation_button:
#     size_group "navigation"
#     properties gui.button_properties("navigation_button")

# style navigation_button_text:
#     properties gui.text_properties("navigation_button")





# ## Game Menu screen ############################################################
# ##
# ## This lays out the basic common structure of a game menu screen. It's called
# ## with the screen title, and displays the background, title, and navigation.
# ##
# ## The scroll parameter can be None, or one of "viewport" or "vpgrid".
# ## This screen is intended to be used with one or more children, which are
# ## transcluded (placed) inside it.

# screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

#     style_prefix "game_menu"

#     if main_menu:
#         add gui.main_menu_background size (1920, 1080)
#     elif renpy.get_screen("history"):
#         add gui.main_menu_background size (1920, 1080)
#         add gui.log_background xpos 570 ypos 40
#     elif renpy.get_screen("save"):
#         add gui.main_menu_background size (1920, 1080)
#     elif renpy.get_screen("load"):
#         add gui.main_menu_background size (1920, 1080)
#     elif renpy.get_screen("preferences"):
#         add gui.main_menu_background size (1920, 1080)
#         add "gui/overlay/notepad_background.png" align (0.5, 0.5)
        
#         add "gui/overlay/tab_idle_background.png" align (0.34, 0.2)

#         imagebutton:
#             idle "gui/overlay/save_idle_icon.png"
#             hover "gui/overlay/save_hover_icon.png"
#             align (0.29, 0.2)
#             action ShowMenu("save")

#         add "gui/overlay/tab_selected_background.png" align (0.3, 0.3)
#         add "gui/overlay/settings_selected_icon.png" align (0.27, 0.3)
#         add "gui/overlay/tab_idle_background.png" align (0.34, 0.4)

#         imagebutton:
#             idle "gui/overlay/controls_idle_icon.png"
#             hover "gui/overlay/controls_hover_icon.png"
#             align (0.29, 0.4)
#             action ShowMenu("help")

#         add "gui/overlay/top_page.png" align (0.5, 0.5)


#     elif renpy.get_screen("about"):
#         add gui.main_menu_background size (1920, 1080)
#     elif renpy.get_screen("help"):
#         add gui.main_menu_background size (1920, 1080)

#     else:
#         add gui.game_menu_background size (1920, 1080)

#     frame:
#         style "game_menu_outer_frame"

#         hbox:

#             ## Reserve space for the navigation section.
#             frame:
#                 style "game_menu_navigation_frame"

#             frame:
#                 style "game_menu_content_frame"

#                 if scroll == "viewport":

#                     viewport:
#                         yinitial yinitial
#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True
#                         pagekeys True

#                         side_yfill True

#                         vbox:
#                             spacing spacing

#                             transclude

#                 elif scroll == "vpgrid":

#                     vpgrid:
#                         cols 1
#                         yinitial yinitial

#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True
#                         pagekeys True

#                         ypos 80
#                         ysize 770

#                         # side_yfill True

#                         spacing spacing

#                         transclude

#                 else:

#                     transclude

#     use navigation

#     textbutton _("Return"):
#         style "return_button"

#         action Return()

#     label title

#     if main_menu:
#         key "game_menu" action ShowMenu("main_menu")


# style game_menu_outer_frame is empty
# style game_menu_navigation_frame is empty
# style game_menu_content_frame is empty
# style game_menu_viewport is gui_viewport
# style game_menu_side is gui_side
# style game_menu_scrollbar is gui_vscrollbar

# style game_menu_label is gui_label
# style game_menu_label_text is gui_label_text

# style return_button is navigation_button
# style return_button_text is navigation_button_text

# style game_menu_outer_frame:
#     bottom_padding 45
#     top_padding 180


# style game_menu_navigation_frame:
#     xsize 420
#     yfill True

# style game_menu_content_frame:
#     left_margin 60
#     right_margin 30
#     top_margin 15

# style game_menu_viewport:
#     xsize 1380

# style game_menu_vscrollbar:
#     unscrollable gui.unscrollable

# style game_menu_side:
#     spacing 15

# style game_menu_label:
#     xpos 75
#     ysize 180

# style game_menu_label_text:
#     size 75
#     color gui.accent_color
#     yalign 0.5

# style return_button:
#     xpos gui.navigation_xpos
#     yalign 1.0
#     yoffset -45

