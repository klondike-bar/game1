## First screen: Intro, text, pinkie pie on screen, background
## Second screen: Building the cupcake
## Third screen: Pinkie comments on cupcake, put yay sound effect kid

## Put music 

define p = Character(_("Pinkie Pie"), color = "#a3386c")
image blue = "bg_blue.png"
image pink = "bg_pink.png"

transform height:
    xalign 0.5
    yalign 0.3

transform bounce:
    xalign 0.5
    yalign 0.3
    pause .15
    yoffset 0
    easein .175 yoffset -15
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform logo:
    zoom 0.75
    xalign 0.5
    yalign 0.1

transform start:
    xalign 0.295
    yalign 0.745

transform setting:
    xalign 0.432
    yalign 0.745

transform helps:
    xalign 0.57
    yalign 0.745

transform quits:
    xalign 0.701
    yalign 0.745

transform start_button:
    xalign 0.275
    yalign 0.8

transform setting_button:
    xalign 0.425
    yalign 0.8

transform helps_button:
    xalign 0.575
    yalign 0.8

transform quits_button:
    xalign 0.725
    yalign 0.8

transform items_2:
    xalign 0.5
    yalign 0.4

transform items_3:
    xalign 0.5
    yalign 0.6

transform pinkie_position:
    xalign -.1
    yalign 1.0

transform pinkie_reaction:
    xalign -.1
    yalign 0.3

transform button_position:
    xalign 1.0
    yalign 1.0

transform button_x_1:
    xalign 0.96 
    yalign 0.137

transform button_x_2:
    xalign 0.96 
    yalign 0.307

transform button_x_3:
    xalign 0.96 
    yalign 0.477

transform button_topping_1:
    xalign 0.89
    yalign 0.07

transform button_frosting_1:
    xalign 0.89
    yalign 0.27

transform button_base_1:
    xalign 0.89 
    yalign 0.47

label start:

    show blue with dissolve

    show p_neutral at height

    p "Oh! Hello, you came just in time!"

    hide p_neutral

    show p_neutral_up at bounce

    p "I needed help making some cupcakes,"

    hide p_neutral_up
    
    show p_excite_up at height
    
    menu:

        p "would you like to help me?"

        "Yes":

            jump cupcake_maker

            hide blue

        "No":

            hide p_excite_up
            
            show p_sad at height

            p "..."

            return

label cupcake_maker:
    ##SECOND SCREEN

    call screen buildings with dissolve

    
label ending:

    hide blue
    show pink

    show screen ending_real with dissolve

    p "Nice Cupcake!"

