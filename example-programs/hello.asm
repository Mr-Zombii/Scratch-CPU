GOTO @ProgramStart

# TAKES IN (COLOR, X, Y)
# https://ennogames.com/blog/3d-and-2d-coordinates-to-1d-indexes
LABEL WritePixel
    # ORDER
    # 1. Y
    # 2. X
    # 3. COLOR

    PSH 27
    MUL
    ADD

    PSH 2
    MUL

    PSH_DY 64455
    ADD

    STA 1
    RET

# SCREEN X goes from 0 - 19
# SCREEN Y goes from 0 - 26

LABEL ProgramStart
    # Square Size X
    PSH 21

    # Square Size Y
    PSH 14

    # Square A Brightness
    PSH 100

    # Square A Color
    PSH 1

    # Square B Brightness
    PSH 100

    # Square B Color
    PSH 2

    # Square Start X
    PSH 3

    # Square Start Y
    PSH 3

    # Mov Vars to Memory
    # DON'T MODIFY Tmp Loop Index
    # I = 8
    PSH 8
    PSH 0
    STA 0

    LABEL MovVars
        PSH 0
        RFA 0

        PSH 1
        SUB
        DUP

        PSH 0
        STA 0

        PSH 4
        ADD
        STA 0

        PSH 0
        RFA 0

        GOTO_NZ @MovVars
    
    # Loop Toggle
    PSH 0
    PSH 3
    STA 0

    # Y = 0
    PSH 0
    PSH 1
    STA 0

    LABEL YCounter
        # X = 0
        PSH 0
        PSH 2
        STA 0

        LABEL XCounter
            GOTO @CheckColorAndToggle
            LABEL GET_COLOR_A
                POP

                PSH 6
                RFA 0
                SHFT_L 8
                PSH 7
                RFA 0
                ADD

                PSH 1
                PSH 3
                STA 0
                GOTO @C_SKIP

            LABEL GET_COLOR_B
                PSH 8
                RFA 0
                SHFT_L 8
                PSH 9
                RFA 0
                ADD

                PSH 0
                PSH 3
                STA 0
                GOTO @C_SKIP

            LABEL CheckColorAndToggle
                PSH 3
                RFA 0
                DUP
                GOTO_EZ @GET_COLOR_A
                GOTO_NZ @GET_COLOR_B

            LABEL C_SKIP

            # StartX
            PSH 10
            RFA 0
            # CurrentX
            PSH 2
            RFA 0
            ADD

            # StartY
            PSH 11
            RFA 0
            # CurrentY
            PSH 1
            RFA 0
            ADD
            
            CALL @WritePixel

            PSH 2
            RFA 0

            PSH 1
            ADD
            DUP

            PSH 2
            STA 0

            PSH 4
            RFA 0
            SUB
            GOTO_NZ @XCounter

        PSH 1
        RFA 0

        PSH 1
        ADD
        DUP

        PSH 1
        STA 0

        PSH 5
        RFA 0
        SUB
        GOTO_NZ @YCounter

    ### H
    PSH 0
    PSH 4
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 4
    PSH 5
    CALL @WritePixel

    PSH 0
    PSH 4
    PSH 6
    CALL @WritePixel

    PSH 0
    PSH 4
    PSH 7
    CALL @WritePixel

    PSH 0
    PSH 4
    PSH 8
    CALL @WritePixel

    #
    PSH 0
    PSH 5
    PSH 6
    CALL @WritePixel
    #

    PSH 0
    PSH 6
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 6
    PSH 5
    CALL @WritePixel

    PSH 0
    PSH 6
    PSH 6
    CALL @WritePixel

    PSH 0
    PSH 6
    PSH 7
    CALL @WritePixel

    PSH 0
    PSH 6
    PSH 8
    CALL @WritePixel

    ### E
    PSH 0
    PSH 8
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 8
    PSH 5
    CALL @WritePixel

    PSH 0
    PSH 8
    PSH 6
    CALL @WritePixel

    PSH 0
    PSH 8
    PSH 7
    CALL @WritePixel

    PSH 0
    PSH 8
    PSH 8
    CALL @WritePixel

    #

    PSH 0
    PSH 9
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 9
    PSH 6
    CALL @WritePixel

    PSH 0
    PSH 9
    PSH 8
    CALL @WritePixel

    PSH 0
    PSH 10
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 10
    PSH 6
    CALL @WritePixel

    PSH 0
    PSH 10
    PSH 8
    CALL @WritePixel

    ### L
    PSH 0
    PSH 12
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 12
    PSH 5
    CALL @WritePixel

    PSH 0
    PSH 12
    PSH 6
    CALL @WritePixel

    PSH 0
    PSH 12
    PSH 7
    CALL @WritePixel

    PSH 0
    PSH 12
    PSH 8
    CALL @WritePixel

    ### L
    PSH 0
    PSH 14
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 14
    PSH 5
    CALL @WritePixel

    PSH 0
    PSH 14
    PSH 6
    CALL @WritePixel

    PSH 0
    PSH 14
    PSH 7
    CALL @WritePixel

    PSH 0
    PSH 14
    PSH 8
    CALL @WritePixel

    ### O
    PSH 0
    PSH 16
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 16
    PSH 5
    CALL @WritePixel

    PSH 0
    PSH 16
    PSH 6
    CALL @WritePixel

    PSH 0
    PSH 16
    PSH 7
    CALL @WritePixel

    PSH 0
    PSH 16
    PSH 8
    CALL @WritePixel

    #

    PSH 0
    PSH 17
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 17
    PSH 8
    CALL @WritePixel

    #

    PSH 0
    PSH 18
    PSH 4
    CALL @WritePixel

    PSH 0
    PSH 18
    PSH 5
    CALL @WritePixel

    PSH 0
    PSH 18
    PSH 6
    CALL @WritePixel

    PSH 0
    PSH 18
    PSH 7
    CALL @WritePixel

    # Color
    # first 8 bits are Brightness
    # last 8 bits are Tile Type
    PSH 0
    # X position
    PSH 18
    # Y position
    PSH 8
    CALL @WritePixel

LABEL END