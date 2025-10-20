GOTO @ProgramStart

# INSTR-PTR ADDR 64443 -> 64444
#
#

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
    PSH 0
    PSH 0
    STA 0

    PSH 0
    PSH 1
    STA 0

    # Square Size X
    PSH 20
    PSH 2
    STA 0

    # Square Size Y
    PSH 5
    PSH 3
    STA 0

    LABEL YCounter
        PSH 0
        PSH 0
        STA 0

        LABEL XCounter
            PSH_DY 25601
            
            PSH 0
            RFA 0

            PSH 1
            RFA 0
            
            CALL @WritePixel

            PSH 0
            RFA 0

            PSH 1
            ADD
            DUP

            PSH 0
            STA 0

            PSH 2
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

        PSH 3
        RFA 0
        SUB
        GOTO_NZ @YCounter

    GOTO @END

LABEL END