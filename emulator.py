import math
import threading, pygame, random, sys

def col(s):
    s = s.replace("#", "")
    a = int(s, 16)
    return ((a & 0xFF0000) >> 16, (a & 0x00FF00) >> 8, a & 0xFF)

def decomp(a):
    match a:
        case 0: return "NOP"
        case 1: return "PSH"
        case 2: return "SWP"
        case 3: return "DUP"
        case 4: return "DUP"
        case 5: return "AND"
        case 6: return "NOT"
        case 7: return "ADD"
        case 8: return "SUB"
        case 9: return "MUL"
        case 10: return "DIV"
        case 11: return "STA"
        case 12: return "RFA"
        case 13: return "RND"
        case 14: return "JNC"
        case 15: return "CAL"
        case 16: return "RET"

class VM():

    instructions = []
    instrPtr = 0
    stack = []
    callStack = []
    mem = [0] * 65536
    doWork = True

    def __init__(self):
        pass

    def push(self, o):
        self.stack.append(o)

    def pop(self):
        if len(self.stack) == 0:
            return 0
        v = self.stack.pop()
        return v
    
    def pushCall(self, o):
        self.callStack.append(o)

    def popCall(self):
        v = self.callStack.pop()
        return v

    def decode_file(self, file):
        f = open(file, "r")

        lines = f.readlines()
        f.close()

        self.instructions = []
        for x in lines:
            x = int(x)
            self.instructions.append([x >> 11, x & 0x7FF])

    def decode_file2(self, file):
        f = open(file, "r")

        lines = f.read().split(";")
        f.close()

        self.instructions = []
        for x in lines:
            x = int(x)
            self.instructions.append([x >> 11, x & 0x7FF])

    def exec(self, instr):
        match instr[0]:
            case 1:
                self.push(instr[1] & 0xFF)
                return
            case 2:
                self.pop()
                return
            case 3:
                a = self.pop()
                b = self.pop()
                self.push(a)
                self.push(b)
                return
            case 4:
                a = self.pop()
                self.push(a)
                self.push(a)
                return
            case 5:
                self.push(self.pop() & self.pop())
                return
            case 6:
                self.push((~self.pop()) & 0xFFFF)
                return
            case 7:
                a = self.pop()
                b = self.pop()
                self.push((a + b) & 0xFFFF)
                return
            case 8:
                a = self.pop()
                b = self.pop()
                self.push((b - a) & 0xFFFF)
                return
            case 9:
                a = self.pop()
                b = self.pop()
                self.push((b * a) & 0xFFFF)
                return
            case 10:
                a = self.pop()
                b = self.pop()
                self.push((b / a) & 0xFFFF)
                return
            case 11:
                a = instr[1] & 0x1
                b = self.pop()
                c = self.pop()

                if a == 0:
                    self.mem[b] = c & 0xFF
                    return

                self.mem[b] = c & 0xFF
                self.mem[b + 1] = (c >> 8) & 0xFF
                return
            case 12:
                a = instr[1] & 0x1
                b = self.pop()

                if a == 0:
                    self.push(self.mem[b] & 0xFF)
                    return

                self.push(self.mem[b] | self.mem[b + 1] << 8)
                return
            case 13:
                a = instr[1] & 0xF
                b = self.pop()

                if a > 4:
                    a -= 5
                    b = -b

                if a == 0:
                    self.instrPtr += b
                    return

                c = self.pop()

                if a == 1:
                    if c == 0:
                        self.instrPtr += b
                    return

                if a == 2:
                    if c != 0:
                        self.instrPtr += b
                    return

                if a == 3:
                    if c > 0:
                        self.instrPtr += b
                    return

                if a == 4:
                    if c >= 0:
                        self.instrPtr += b
                    return

            case 14:
                a = instr[1] & 0x3
                if a == 0:
                    self.push(random.randint(0, 255))
                    return
                if a == 1:
                    self.push(random.randint(0, 65535))
                    return
                if a == 2:
                    b = self.pop()
                    self.push(random.randint(b & 0xF, (b & 0xF0) >> 8))
                    return
                if a == 3:
                    b = self.pop()
                    c = self.pop()
                    i = random.randint(c, b)
                    self.push(i)
                    return
                return

            case 15:
                a = instr[1] & 0xF
                self.pushCall(a + self.instrPtr)
                return
            case 16:
                self.instrPtr = self.popCall()
                return

    def run(self):
        while self.instrPtr < len(self.instructions) and self.doWork:
            instr = self.instructions[self.instrPtr]

            backStack = self.stack
            try:
                self.exec(instr)
            except:
                print("Error on instruction:", decomp(instr[0]), (instr[1]), "ptr:", self.instrPtr, "currentStack", self.stack, "oldStack", backStack)
                exit()
            self.instrPtr += 1

vm = VM()
vm.decode_file2(sys.argv[1])

scale = 400 / 100
width  = int(216 * scale)
height = int(160 * scale)

def drawPixel(brightness, color, x, y):
    if (color >= len(colors)):
        color = (255, 0, 0)
    else:
        color = colors[color]

    color = [color[0], color[1], color[2]]

    color[0] = (int(color[0] * (brightness / 100)))
    color[1] = (int(color[1] * (brightness / 100)))
    color[2] = (int(color[2] * (brightness / 100)))
    if color[0] > 255: color[0] = 255
    if color[1] > 255: color[1] = 255
    if color[2] > 255: color[2] = 255

    pw = int(8 * scale)
    ph = int(8 * scale)
    for z in range(ph):
        pygame.draw.line(screen, (color[0], color[1], color[2]), ((x * pw), (y * ph) + z), ((x * pw) + (pw - 1), (y * ph) + z))

screen = pygame.display.set_mode((width, height))

colors = [
    col("#000000"),
    col("#ff2828"),
    col("#ff6300"),
    col("#ff9300"),
    col("#faff00"),
    col("#96ff00"),
    col("#0dff00"),
    col("#00ff81"),
    col("#00fffb"),
    col("#0088ff"),
    col("#000dff"),
    col("#6200ff"),
    col("#8700ff"),
    col("#c600ff"),
    col("#ff00e0"),
    col("#ff0097"),
    col("#ffffff"),
]

def draw(mem):
    pygame.display.set_caption('VM')
    screen.fill((255, 255, 255))
    q = 64455
    for y in range(20):
        for x in range(27):
            brightness = mem[q + 1]
            color = mem[q]
            drawPixel(brightness, color, x, y)
            q += 2

    pygame.display.flip()

def startVM(t):
    vm.run()
my_thread = threading.Thread(target=startVM, args=("VM Thread",))

my_thread.start()

def setBit(q, n, v):
    byte = vm.mem[q]
    byte &= (~(0x1 << n) & 0xFF)
    if v:
        byte |= 1 << n
    vm.mem[q] = byte
    
def registerKeys():
    keys = pygame.key.get_pressed()
    b = 64445

    shift = (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT])

    setBit(b, 1, keys[pygame.K_SPACE])
    setBit(b, 2, keys[pygame.K_UP])
    setBit(b, 3, keys[pygame.K_DOWN])
    setBit(b, 4, keys[pygame.K_LEFT])
    setBit(b, 5, keys[pygame.K_RIGHT])
    setBit(b, 6, keys[pygame.K_a])
    setBit(b, 7, keys[pygame.K_b])
    
    b = 64446
    setBit(b, 0, keys[pygame.K_c])
    setBit(b, 1, keys[pygame.K_d])
    setBit(b, 2, keys[pygame.K_e])
    setBit(b, 3, keys[pygame.K_f])
    setBit(b, 4, keys[pygame.K_g])
    setBit(b, 5, keys[pygame.K_h])
    setBit(b, 6, keys[pygame.K_i])
    setBit(b, 7, keys[pygame.K_j])

    b = 64447
    setBit(b, 0, keys[pygame.K_k])
    setBit(b, 1, keys[pygame.K_l])
    setBit(b, 2, keys[pygame.K_m])
    setBit(b, 3, keys[pygame.K_n])
    setBit(b, 4, keys[pygame.K_o])
    setBit(b, 5, keys[pygame.K_p])
    setBit(b, 6, keys[pygame.K_q])
    setBit(b, 7, keys[pygame.K_r])

    b = 64448
    setBit(b, 0, keys[pygame.K_s])
    setBit(b, 1, keys[pygame.K_t])
    setBit(b, 2, keys[pygame.K_u])
    setBit(b, 3, keys[pygame.K_v])
    setBit(b, 4, keys[pygame.K_w])
    setBit(b, 5, keys[pygame.K_x])
    setBit(b, 6, keys[pygame.K_y])
    setBit(b, 7, keys[pygame.K_z])


    b = 64449
    setBit(b, 0, keys[pygame.K_0])
    setBit(b, 1, keys[pygame.K_1])
    setBit(b, 2, keys[pygame.K_2])
    setBit(b, 3, keys[pygame.K_3])
    setBit(b, 4, keys[pygame.K_4])
    setBit(b, 5, keys[pygame.K_5])
    setBit(b, 6, keys[pygame.K_6])
    setBit(b, 7, keys[pygame.K_7])

    b = 64450
    setBit(b, 0, keys[pygame.K_8])
    setBit(b, 1, keys[pygame.K_9])
    setBit(b, 2, keys[pygame.K_KP_ENTER])
    setBit(b, 3, keys[pygame.K_BACKQUOTE])
    setBit(b, 4, shift and keys[pygame.K_BACKQUOTE])
    setBit(b, 5, keys[pygame.K_EXCLAIM])
    setBit(b, 6, keys[pygame.K_AT])
    setBit(b, 7, keys[pygame.K_HASH])

    b = 64451
    setBit(b, 0, keys[pygame.K_DOLLAR])
    setBit(b, 1, keys[pygame.K_PERCENT])
    setBit(b, 2, keys[pygame.K_CARET])
    setBit(b, 3, keys[pygame.K_AMPERSAND])
    setBit(b, 4, shift and keys[pygame.K_8])
    setBit(b, 5, keys[pygame.K_LEFTPAREN])
    setBit(b, 6, keys[pygame.K_RIGHTPAREN])
    setBit(b, 7, keys[pygame.K_UNDERSCORE])

    b = 64452
    setBit(b, 0, keys[pygame.K_MINUS])
    setBit(b, 1, keys[pygame.K_KP_MINUS])
    setBit(b, 2, keys[pygame.K_EQUALS])
    setBit(b, 3, shift and keys[pygame.K_LEFTBRACKET])
    setBit(b, 4, keys[pygame.K_LEFTBRACKET])
    setBit(b, 5, shift and keys[pygame.K_RIGHTBRACKET])
    setBit(b, 6, keys[pygame.K_RIGHTBRACKET])
    setBit(b, 7, shift and pygame.K_BACKSLASH)

    b = 64453
    setBit(b, 0, keys[pygame.K_BACKSLASH])
    setBit(b, 1, keys[pygame.K_COLON])
    setBit(b, 2, keys[pygame.K_SEMICOLON])
    setBit(b, 3, keys[pygame.K_QUOTEDBL])
    setBit(b, 4, keys[pygame.K_QUOTE])
    setBit(b, 5, keys[pygame.K_LESS])
    setBit(b, 5, keys[pygame.K_COMMA])
    setBit(b, 5, keys[pygame.K_GREATER])
    setBit(b, 5, keys[pygame.K_PERIOD])

    b = 64454
    setBit(b, 0, keys[pygame.K_GREATER])
    setBit(b, 1, keys[pygame.K_SLASH])
    setBit(b, 2, keys[pygame.K_QUESTION])


while True:
    draw(vm.mem)

    registerKeys()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: setBit(64445, 0, True)
        if event.type == pygame.KEYUP: setBit(64445, 0, False)
        if event.type == pygame.QUIT:
            vm.doWork = False
            exit()
