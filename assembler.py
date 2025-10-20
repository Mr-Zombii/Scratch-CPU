import os, sys

class Stage0():

    def big_push(output, n):
        if n > (2**16 - 1):
            print("Value", n, "too large")
            return
    
        output += "PSH 255\n"
        output += "PSH 1\n"
        output += "ADD\n"
        output += "PSH " + str(n >> 8) + "\n"
        output += "MUL\n"
        output += "PSH " + str(n & 0xFF) + "\n"
        output += "ADD\n"
        return output

    def dynamic_push(output, n):
        if n > (2**16 - 1):
            print("Value", n, "too large")
            return
    
        if n > 255:
            output += "PSH 255\n"
            output += "PSH 1\n"
            output += "ADD\n"
            output += "PSH " + str(n >> 8) + "\n"
            output += "MUL\n"
            output += "PSH " + str(n & 0xFF) + "\n"
            output += "ADD\n"
        else:
            output += "PSH " + str(n & 0xFF) + "\n"
        return output

    def jump(output, n):
        if n > 13:
            print("Value", n, "too large for jump cond type")
            return
        output += "JMC " + str(n) + "\n"
        return output

    def process(text: str):
        lines = text.split("\n")
        outStr = ""
        for x in lines:
            x = x.strip()
            if (x.startswith("#") or x == ""):
                continue

            parts = x.split(" ")
            opcode = parts[0].upper()
            match opcode:
                case "SUB" | "RET" | "CAL" | "RND" | "NOP" | "DUP" | "PSH" | "POP" | "SWP" | "AND" | "NOT" | "ADD" | "MUL" | "DIV" | "STA" | "RFA" | "JMC":
                    outStr += x + "\n"
                case "JMC":
                    outStr = Stage0.jump(outStr, int(parts[1]))
                case "LABEL":
                    outStr += "#PSEUDO LABEL_DECLARE " + parts[1] + "\n"
                case "CALL":
                    if (not parts[1].startswith("@")):
                        print("CALL must be used with a label, EX: CALL @LABEL_NAME")
                    outStr += "#PSEUDO CALL " + parts[1] + " NC\n"
                case "CALL_EQ":
                    if (not parts[1].startswith("@")):
                        print("CALL_EQ must be used with a label, EX: CALL_EQ @LABEL_NAME")
                    outStr += "#PSEUDO CALL " + parts[1] + " EQ\n"
                case "CALL_NE":
                    if (not parts[1].startswith("@")):
                        print("CALL_NE must be used with a label, EX: CALL_NE @LABEL_NAME")
                    outStr += "#PSEUDO CALL " + parts[1] + " NE\n"
                case "CALL_EZ":
                    if (not parts[1].startswith("@")):
                        print("CALL_EZ must be used with a label, EX: CALL_EZ @LABEL_NAME")
                    outStr += "#PSEUDO CALL " + parts[1] + " EZ\n"
                case "CALL_NZ":
                    if (not parts[1].startswith("@")):
                        print("CALL_NZ must be used with a label, EX: CALL_NZ @LABEL_NAME")
                    outStr += "#PSEUDO CALL " + parts[1] + " NZ\n"
                case "CALL_GT":
                    if (not parts[1].startswith("@")):
                        print("CALL_GT must be used with a label, EX: CALL_GT @LABEL_NAME")
                    outStr += "#PSEUDO CALL " + parts[1] + " GT\n"
                case "CALL_LT":
                    if (not parts[1].startswith("@")):
                        print("CALL_LT must be used with a label, EX: CALL_LT @LABEL_NAME")
                    outStr += "#PSEUDO CALL " + parts[1] + " LT\n"
                case "CALL_GE":
                    if (not parts[1].startswith("@")):
                        print("CALL_GE must be used with a label, EX: CALL_GE @LABEL_NAME")
                    outStr += "#PSEUDO CALL " + parts[1] + " GE\n"
                case "CALL_LE":
                    if (not parts[1].startswith("@")):
                        print("CALL_LE must be used with a label, EX: CALL_LE @LABEL_NAME")
                    outStr += "#PSEUDO CALL " + parts[1] + " LE\n"
                case "GOTO":
                    if (not parts[1].startswith("@")):
                        print("GOTO must be used with a label, EX: GOTO @LABEL_NAME")
                    outStr += "#PSEUDO JUMP " + parts[1] + " NC\n"
                case "GOTO_EQ":
                    if (not parts[1].startswith("@")):
                        print("GOTO_EQ must be used with a label, EX: GOTO_EQ @LABEL_NAME")
                    outStr += "#PSEUDO JUMP " + parts[1] + " EQ\n"
                case "GOTO_NE":
                    if (not parts[1].startswith("@")):
                        print("GOTO_NE must be used with a label, EX: GOTO_NE @LABEL_NAME")
                    outStr += "#PSEUDO JUMP " + parts[1] + " NE\n"
                case "GOTO_EZ":
                    if (not parts[1].startswith("@")):
                        print("GOTO_EZ must be used with a label, EX: GOTO_EZ @LABEL_NAME")
                    outStr += "#PSEUDO JUMP " + parts[1] + " EZ\n"
                case "GOTO_NZ":
                    if (not parts[1].startswith("@")):
                        print("GOTO_NZ must be used with a label, EX: GOTO_NZ @LABEL_NAME")
                    outStr += "#PSEUDO JUMP " + parts[1] + " NZ\n"
                case "GOTO_GT":
                    if (not parts[1].startswith("@")):
                        print("GOTO_GT must be used with a label, EX: GOTO_GT @LABEL_NAME")
                    outStr += "#PSEUDO JUMP " + parts[1] + " GT\n"
                case "GOTO_LT":
                    if (not parts[1].startswith("@")):
                        print("GOTO_LT must be used with a label, EX: GOTO_LT @LABEL_NAME")
                    outStr += "#PSEUDO JUMP " + parts[1] + " LT\n"
                case "GOTO_LE":
                    if (not parts[1].startswith("@")):
                        print("GOTO_LE must be used with a label, EX: GOTO_LE @LABEL_NAME")
                    outStr += "#PSEUDO JUMP " + parts[1] + " LE\n"
                case "GOTO_GE":
                    if (not parts[1].startswith("@")):
                        print("GOTO_GE must be used with a label, EX: GOTO_GE @LABEL_NAME")
                    outStr += "#PSEUDO JUMP " + parts[1] + " GE\n"
                case "PSH_DY":
                    outStr = Stage0.dynamic_push(outStr, int(parts[1]))
                case "SHFT_L": # PSEUDO
                    outStr = Stage0.dynamic_push(outStr, 2 ** int(parts[1]))
                    outStr += "MUL\n"
                case "SHFT_R": # PSEUDO
                    outStr = Stage0.dynamic_push(outStr, 2 ** int(parts[1]))
                    outStr += "DIV\n"
        return outStr

class Stage1():

    def dynamic_push_guess(n):
        if n > (2**16 - 1):
            print("Value", n, "too large")
            return
    
        if n > 255:
            return 7
        
        return 1;

    def process(text: str):
        lines = text.split("\n")
        outStr = ""
        labelAddresses = {}

        for i in range(len(lines)):
            x = lines[i].strip()
            if (x.startswith("#PSEUDO LABEL_DECLARE")):
                labelAddresses[x.replace("#PSEUDO LABEL_DECLARE ", "")] = i
                continue
          
        for i in range(len(lines)):
            x = lines[i].strip()
            if (x.startswith("#PSEUDO JUMP @")):
                outStr += x + "\n"
                continue

            if (x.startswith("#PSEUDO CALL @")):
                outStr += x + "\n"
                continue

            if (x.startswith("#PSEUDO LABEL_DECLARE")):
                outStr += x + "\n"
                continue
            
            if (x.startswith("#") or x == ""):
                continue

            parts = x.split(" ")
            opcode = parts[0].upper()
            match opcode:
                case "SUB" | "RET" | "CAL" | "RND" | "NOP" | "DUP" | "PSH" | "POP" | "SWP" | "AND" | "NOT" | "ADD" | "MUL" | "DIV" | "STA" | "RFA" | "JMC":
                    outStr += x + "\n"
        return outStr

class Stage2():

    def process(text: str):
        lines = text.split("\n")
        outStr = ""
        labelAddresses = {}

        for i in range(len(lines)):
            x = lines[i].strip()
            if (x.startswith("#PSEUDO LABEL_DECLARE")):
                labelAddresses[x.replace("#PSEUDO LABEL_DECLARE ", "")] = i
                continue

        for i in range(len(lines)):
            x = lines[i].strip()
            if (x.startswith("#PSEUDO TAKE_SPACE")):
                continue
            if (x.startswith("#PSEUDO CALL @")):
                parts2 = x.replace("#PSEUDO CALL @", "").split(" ")
                space = labelAddresses[parts2[0]] - i
                cond = 0
                if space < 0:
                    cond += 5
                space = abs(space)
                match (parts2[1]):
                    case "LT" | "LE": 
                        outStr += "#PSEUDO TAKE_SPACE\n"
                        parts2[1] = "G" + parts2[1][1]
                    case "EQ" | "NE":
                        outStr += "#PSEUDO TAKE_SPACE\n"
                        parts2[1] = parts2[1][0] + "Z"

                match (parts2[1]):
                    case "EZ": cond += 1;
                    case "NZ": cond += 2;
                    case "GT": cond += 3;
                    case "GE": cond += 4;

                outStr += Stage1.dynamic_push_guess(space) * "#PSEUDO TAKE_SPACE\n"
                outStr += "#PSEUDO TAKE_SPACE\n"
                outStr += x + "\n"
                continue
           
            if (x.startswith("#PSEUDO JUMP @")):
                parts2 = x.replace("#PSEUDO JUMP @", "").split(" ")
                space = labelAddresses[parts2[0]] - i
                cond = 0
                if space < 0:
                    cond += 5
                space = abs(space)
                match (parts2[1]):
                    case "LT" | "LE": 
                        outStr += "#PSEUDO TAKE_SPACE\n"
                        parts2[1] = "G" + parts2[1][1]
                    case "EQ" | "NE":
                        outStr += "#PSEUDO TAKE_SPACE\n"
                        parts2[1] = parts2[1][0] + "Z"

                match (parts2[1]):
                    case "EZ": cond += 1;
                    case "NZ": cond += 2;
                    case "GT": cond += 3;
                    case "GE": cond += 4;

                outStr += Stage1.dynamic_push_guess(space) * "#PSEUDO TAKE_SPACE\n"
                outStr += x + "\n"
                continue
           
            if (x.startswith("#PSEUDO LABEL_DECLARE")):
                outStr += x + "\n"
                continue
            
            if (x.startswith("#") or x == ""):
                continue

            for v in labelAddresses.keys():
                x.replace("@" + v, str(labelAddresses[v]))

            parts = x.split(" ")
            opcode = parts[0].upper()
            match opcode:
                case "SUB" | "RET" | "CAL" | "RND" | "NOP" | "DUP" | "PSH" | "POP" | "SWP" | "AND" | "NOT" | "ADD" | "MUL" | "DIV" | "STA" | "RFA" | "JMC":
                    outStr += x + "\n"
        return outStr

class Stage3():

    def process(text: str):
        lines = text.split("\n")
        outStr = ""
        labelAddresses = {}

        for i in range(len(lines)):
            x = lines[i].strip()
            if (x.startswith("#PSEUDO LABEL_DECLARE")):
                labelAddresses[x.replace("#PSEUDO LABEL_DECLARE ", "")] = i
                continue

        for i in range(len(lines)):
            x = lines[i].strip()
            if (x.startswith("#PSEUDO TAKE_SPACE")):
                continue
            if (x.startswith("#PSEUDO CALL @")):
                parts2 = x.replace("#PSEUDO CALL @", "").split(" ")
                space = labelAddresses[parts2[0]] - i
                cond = 0
                if space < 0:
                    cond += 5
                space = abs(space)
                match (parts2[1]):
                    case "LT" | "LE": 
                        outStr += "SWP\n"
                        parts2[1] = "G" + parts2[1][1]
                    case "EQ" | "NE":
                        outStr += "SUB\n"
                        parts2[1] = parts2[1][0] + "Z"

                match (parts2[1]):
                    case "EZ": cond += 1;
                    case "NZ": cond += 2;
                    case "GT": cond += 3;
                    case "GE": cond += 4;

                outStr = Stage0.dynamic_push(outStr, space)
                outStr += "CAL 1\n"
                outStr += "JMC " + str(cond) + "\n"
                continue
           
            if (x.startswith("#PSEUDO JUMP @")):
                parts2 = x.replace("#PSEUDO JUMP @", "").split(" ")
                space = labelAddresses[parts2[0]] - i
                cond = 0
                if space < 0:
                    cond += 5
                space = abs(space)
                match (parts2[1]):
                    case "LT" | "LE": 
                        outStr += "SWP\n"
                        parts2[1] = "G" + parts2[1][1]
                    case "EQ" | "NE":
                        outStr += "SUB\n"
                        parts2[1] = parts2[1][0] + "Z"

                match (parts2[1]):
                    case "EZ": cond += 1;
                    case "NZ": cond += 2;
                    case "GT": cond += 3;
                    case "GE": cond += 4;

                outStr = Stage0.dynamic_push(outStr, space)
                outStr += "JMC " + str(cond) + "\n"
                continue
           
            if (x.startswith("#PSEUDO LABEL_DECLARE")):
                outStr += "NOP\n"
                continue
            
            if (x.startswith("#") or x == ""):
                continue

            for v in labelAddresses.keys():
                x.replace("@" + v, str(labelAddresses[v]))

            parts = x.split(" ")
            opcode = parts[0].upper()
            match opcode:
                case "SUB" | "RET" | "CAL" | "RND" | "NOP" | "DUP" | "PSH" | "POP" | "SWP" | "AND" | "NOT" | "ADD" | "MUL" | "DIV" | "STA" | "RFA" | "JMC":
                    outStr += x + "\n"
        return outStr

class StageFinal():

    def bprint(output, notEnd, n):
        #output += "0b" + format(n, "016b") + "\n"
        output += str(n)
        if notEnd:
            output += ";"
            #output += "\n"

        return output

    def process(text: str):
        lines = text.split("\n")
        outStr = ""

        realCount = 0
        for i in range(len(lines)):
            x = lines[i].strip()

            if (x.startswith("#") or x == ""):
                continue

            realCount += 1
        
        realIdx = 0
        for i in range(len(lines)):
            x = lines[i].strip()

            if (x.startswith("#") or x == ""):
                continue
            realIdx += 1

            parts = x.split(" ")
            opcode = parts[0].upper()
            notEnd = realIdx < realCount
            match opcode:
                case "NOP": outStr = StageFinal.bprint(outStr, notEnd, 0)
                case "PSH": outStr = StageFinal.bprint(outStr, notEnd, (1 << 11) | int(parts[1]))
                case "POP": outStr = StageFinal.bprint(outStr, notEnd, (2 << 11))
                case "SWP": outStr = StageFinal.bprint(outStr, notEnd, (3 << 11))
                case "DUP": outStr = StageFinal.bprint(outStr, notEnd, (4 << 11))
                case "AND": outStr = StageFinal.bprint(outStr, notEnd, (5 << 11))
                case "NOT": outStr = StageFinal.bprint(outStr, notEnd, (6 << 11))
                case "ADD": outStr = StageFinal.bprint(outStr, notEnd, (7 << 11))
                case "SUB": outStr = StageFinal.bprint(outStr, notEnd, (8 << 11))
                case "MUL": outStr = StageFinal.bprint(outStr, notEnd, (9 << 11))
                case "DIV": outStr = StageFinal.bprint(outStr, notEnd, (10 << 11))
                case "STA": outStr = StageFinal.bprint(outStr, notEnd, (11 << 11) | int(parts[1]))
                case "RFA": outStr = StageFinal.bprint(outStr, notEnd, (12 << 11) | int(parts[1]))
                case "JMC": outStr = StageFinal.bprint(outStr, notEnd, (13 << 11) | int(parts[1]))
                case "RND": outStr = StageFinal.bprint(outStr, notEnd, (14 << 11) | int(parts[1]))
                case "CAL": outStr = StageFinal.bprint(outStr, notEnd, (15 << 11) | int(parts[1]))
                case "RET": outStr = StageFinal.bprint(outStr, notEnd, (16 << 11))
        return outStr

fileName = sys.argv[1]
readFileName = sys.argv[1]

dir = os.path.dirname(os.path.basename(fileName))

fileName = os.path.basename(fileName).replace(os.path.dirname(os.path.basename(fileName)), "")

fileName = fileName.split(".")[0]

file = open(readFileName, "r")
contents = file.read()
file.close()

def debugOut(contents, stage, ext = "asm"):
    return
    file = None
    if os.path.exists(os.path.join(dir, fileName + "-stage" + stage + "-out." + ext)):
        file = open(os.path.join(dir, fileName + "-stage" + stage + "-out." + ext), "w")
    else:
        file = open(os.path.join(dir, fileName + "-stage" + stage + "-out." + ext), "x")

    file.write(contents)
    file.close()

contents = Stage0.process(contents)
debugOut(contents, "0")
contents = Stage1.process(contents)
debugOut(contents, "1")
contents = Stage2.process(contents)
contents = Stage2.process(contents) # Requires repeat for jump accuracy
debugOut(contents, "2")
contents = Stage3.process(contents)
debugOut(contents, "3")
contents = StageFinal.process(contents)
debugOut(contents.replace(";", "\n"), "final", "txt")

file = None
if os.path.exists(os.path.join(dir, fileName + ".txt")):
    file = open(os.path.join(dir, fileName + ".txt"), "w")
else:
    file = open(os.path.join(dir, fileName + ".txt"), "x")

file.write(contents)
file.close()