GOTO @ProgramStart

LABEL ExecuteUpArrowKeyPress
    PSH 11
    RFA 0
    PSH 1
    SUB

    PSH 11
    STA 0
    ret

LABEL ExecuteDownArrowKeyPress
    PSH 11
    RFA 0
    PSH 1
    ADD

    PSH 11
    STA 0
    ret

LABEL ExecuteLeftArrowKeyPress
    PSH 10
    RFA 0
    PSH 1
    SUB

    PSH 10
    STA 0
    ret

LABEL ExecuteRightArrowKeyPress
    PSH 10
    RFA 0
    PSH 1
    ADD

    PSH 10
    STA 0
    ret

# Arrow keys are stored at 64445
LABEL CheckForKeys
    PSH_DY 64445
    RFA 0
    DUP

    # Up Arrow, 3rd bit
    PSH 4
    AND
    CALL_NZ @ExecuteUpArrowKeyPress
    DUP
    
    # Down Arrow, 4th bit
    PSH 8
    AND
    CALL_NZ @ExecuteDownArrowKeyPress
    DUP
    
    # Left Arrow, 5th bit
    PSH 16
    AND
    CALL_NZ @ExecuteLeftArrowKeyPress
    
    # Right Arrow, 6th bit
    PSH 32
    AND
    CALL_NZ @ExecuteRightArrowKeyPress

    ret

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

LABEL ClearScreen
    # Y = 0
    PSH 0
    PSH 12
    STA 0
    LABEL YCounterClear
        # X = 0
        PSH 0
        PSH 13
        STA 0

        LABEL XCounterClear
            # CurrentX
            PSH 13
            RFA 0
            SHFT_L 8

            # CurrentY
            PSH 12
            RFA 0
            ADD

            # PlayerX
            PSH 10
            RFA 0
            SHFT_L 8
            
            # PlayerY
            PSH 11
            RFA 0
            ADD

            SUB
            GOTO_EZ @ClearScreenSkip

            PUSH 0
 
            # CurrentX
            PSH 13
            RFA 0

            # CurrentY
            PSH 12
            RFA 0
            
            CALL @WritePixel

            LABEL ClearScreenSkip

            PSH 13
            RFA 0

            PSH 1
            ADD
            DUP

            PSH 13
            STA 0

            PSH 27
            SUB
            GOTO_NZ @XCounterClear

        PSH 12
        RFA 0

        PSH 1
        ADD
        DUP

        PSH 12
        STA 0

        PSH 20
        SUB
        GOTO_NZ @YCounterClear
    ret

# SCREEN X goes from 0 - 19
# SCREEN Y goes from 0 - 26

LABEL ProgramStart
    # UNUSED
    PSH 0

    # UNUSED
    PSH 0

    # Square A Brightness
    PSH 255

    # Square A Color
    PSH 16

    # UNUSED
    PSH 0

    # UNUSED
    PSH 0

    # Square Start X
    PSH 13

    # Square Start Y
    PSH 10

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

    LABEL Loop
        CALL @ClearScreen
        CALL @CheckForKeys

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

        # StartX
        PSH 10
        RFA 0

        # StartY
        PSH 11
        RFA 0
        
        CALL @WritePixel

        GOTO @Loop

LABEL END