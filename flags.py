from base import MAKEINTRESOURCEW


class WindowExStyles:
    WS_EX_TOPMOST = 0x00000008
    WS_EX_TOOLWINDOW = 0x00000080
    WS_EX_STATICEDGE = 0x00020000
    WS_EX_RTLREADING = 0x00002000
    WS_EX_LEFT = 0x00000000
    WS_EX_RIGHT = 0x00001000
    WS_EX_WINDOWEDGE = 0x00000100
    WS_EX_CLIENTEDGE = 0x00000200
    WS_EX_ACCEPTFILES = 0x00000010
    WS_EX_OVERLAPPEDWINDOW = WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE


class WindowStyles:
    WS_BORDER = 0x00800000
    WS_CAPTION = 0x00C00000
    WS_CHILD = 0x40000000
    WS_DISABLED = 0x08000000
    WS_MAXIMIZE = 0x01000000
    WS_MAXIMIZEBOX = 0x00010000
    WS_MINIMIZE = 0x20000000
    WS_MINIMIZEBOX = 0x00020000
    WS_OVERLAPPED = 0x00000000
    WS_SYSMENU = 0x00080000
    WS_THICKFRAME = 0x00040000
    WS_OVERLAPPEDWINDOW = WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX
    WS_POPUP = 0x80000000
    WS_POPUPWINDOW = WS_POPUP | WS_BORDER | WS_SYSMENU
    WS_VISIBLE = 0x10000000


class ShowModes:
    SW_HIDE = 0
    SW_SHOWNORMAL = 1
    SW_NORMAL = 1
    SW_SHOWMINIMIZED = 2
    SW_SHOWMAXIMIZED = 3
    SW_MAXIMIZE = 3
    SW_SHOWNOACTIVATE = 4
    SW_SHOW = 5
    SW_SHOWMINNOACTIVE = 7
    SW_SHOWNA = 8
    SW_RESTORE = 9
    SW_SHOWDEFAULT = 10
    SW_FORCEMINIMIZE = 11


class WindowMessages:
    WS_NULL = 0x0000
    WM_CREATE = 0x0001
    WM_DESTROY = 0x0002
    WM_MOVE = 0x0003
    WM_SIZE = 0x0005
    WM_ACTIVATE = 0x0006
    WM_SETFOCUS = 0x0007
    WM_KILLFOCUS = 0x0008
    WM_ENABLE = 0x000A
    WM_SETREDRAW = 0x000B
    WM_SETTEXT = 0x000C
    WM_SETGETTEXT = 0x000D
    WM_SETGETTEXTLENGTH = 0x000E
    WM_PAINT = 0x000F
    WM_CLOSE = 0x0010
    WM_QUIT = 0x0012
    WM_ERASEBKGND = 0x0014
    WM_SYSCOLORCHANGE = 0x0015
    WM_SHOWWINDOW = 0x0018
    WM_WININICHANGE = 0x001A
    WM_FONTCHANGE = 0x001D
    WM_TIMECHANGE = 0x001E
    WM_SETCURSOR = 0x0020
    WM_GETMINMAXINFO = 0x0024
    WM_SETFONT = 0x0030
    WM_GETFONT = 0x0031
    WM_WINDOWPOSCHANGED = 0x0047
    WM_SYSKEYDOWN = 0x0104
    WM_SYSKEYUP = 0x0105
    WM_CHAR = 0x0102
    WM_MOUSEMOVE = 0x0200
    WM_LBUTTONDOWN = 0x0201
    WM_LBUTTONUP = 0x0202
    WM_SIZING = 0x214


class SetWindowPos:
    SWP_HIDEWINDOW = 0x0080
    SWP_NOMOVE = 0x0002
    SWP_NOSIZE = 0x0001
    SWP_SHOWWINDOW = 0x0040


class DrawText:
    """
    DrawText formatting
    """
    DT_TOP = 0x00000000
    DT_LEFT = 0x00000000
    DT_CENTER = 0x00000001
    DT_RIGHT = 0x00000002
    DT_VCENTER = 0x00000004
    DT_BOTTOM = 0x00000008
    DT_WORDBREAK = 0x00000010
    DT_SINGLELINE = 0x00000020
    DT_EXPANDTABS = 0x00000040
    DT_TABSTOP = 0x00000080
    DT_NOCLIP = 0x00000100
    DT_EXTERNALLEADING = 0x00000200
    DT_CALCRECT = 0x00000400
    DT_NOPREFIX = 0x00000800
    DT_INTERNAL = 0x00001000
    DT_EDITCONTROL = 0x00002000
    DT_PATH_ELLIPSIS = 0x00004000
    DT_END_ELLIPSIS = 0x00008000
    DT_MODIFYSTRING = 0x00010000
    DT_RTLREADING = 0x00020000
    DT_WORD_ELLIPSIS = 0x00040000
    DT_NOFULLWIDTHCHARBREAK = 0x00080000
    DT_HIDEPREFIX = 0x00100000
    DT_PREFIXONLY = 0x00200000


class IDI:
    IDI_APPLICATION = MAKEINTRESOURCEW(32512)
    IDI_ASTERISK = MAKEINTRESOURCEW(32516)
    IDI_ERROR = MAKEINTRESOURCEW(32513)
    IDI_EXCLAMATION = MAKEINTRESOURCEW(32515)
    IDI_HAND = MAKEINTRESOURCEW(32513)
    IDI_INFORMATION = MAKEINTRESOURCEW(32516)
    IDI_QUESTION = MAKEINTRESOURCEW(32514)
    IDI_SHIELD = MAKEINTRESOURCEW(32518)
    IDI_WARNING = MAKEINTRESOURCEW(32515)
    IDI_WINLOGO = MAKEINTRESOURCEW(32517)


class LR:
    LR_LOADFROMFILE = 0x00000010
    LR_DEFAULTSIZE = 0x00000040
    LR_MONOCHROME = 0x00000001
    LR_VGACOLOR = 0x00000080
    LR_LOADTRANSPARENT = 0x00000020
    LR_DEFAULTCOLOR = 0x00000000

