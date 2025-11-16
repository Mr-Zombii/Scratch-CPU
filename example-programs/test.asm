GOTO @ProgramStart

LABEL PixelColorA
    PSH 100
    SHFT_L 8
    PSH 1
    ADD
    GOTO @Resume

LABEL PixelColorB
    PSH 100
    SHFT_L 8
    # PSH 2
    # ADD

    PSH 1
    PSH 15
    RND 3
    ADD
    GOTO @Resume

LABEL checkForKeyPress
    PSH_DY 64445
    RFA 0
    PSH 4
    AND
    GOTO_NZ @EXIT

    PSH_DY 64445
    RFA 0
    PSH 1
    AND
    DUP

    GOTO_EZ @PixelColorA
    DUP
    GOTO_NZ @PixelColorB
    
    LABEL Resume
        SWP
        POP
        GOTO @ResumeCounter

LABEL ProgramStart
    PSH_DY 64453
    LABEL Counter
        PSH 2
        ADD
    DUP
    PSH_DY 65535
    GOTO_NE @SKIP
    GOTO @SKIP2
    LABEL SKIP

    DUP
    GOTO @checkForKeyPress
    LABEL ResumeCounter
    SWP
    STA 1

    DUP
    PSH_DY 65535
    GOTO_NE @Counter
    POP
    LABEL SKIP2
    GOTO @ProgramStart

LABEL EXIT