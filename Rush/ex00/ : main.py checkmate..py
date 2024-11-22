def checkmate(board):
    # ฟังก์ชันที่จะตรวจสอบว่าเป็นเช็คแมตหรือไม่
    # ในตัวอย่างนี้เราจะสมมติให้ 'K' เป็นราชาและ 'R' เป็นเรือ
    king_pos = None
    rook_pos = None

    # ค้นหาตำแหน่งของราชา (K) และเรือ (R) บนกระดาน
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'K':
                king_pos = (row, col)
            elif board[row][col] == 'R':
                rook_pos = (row, col)

    # ถ้าไม่พบตำแหน่งของราชาหรือเรือ
    if not king_pos or not rook_pos:
        print("Invalid board setup")
        return

    # สมมติว่าเราจะตรวจสอบว่าราชา (K) ถูกเช็คแมตโดยเรือ (R)
    k_row, k_col = king_pos
    r_row, r_col = rook_pos

    # ตรวจสอบว่าเรือ (R) สามารถเข้าทำร้ายราชา (K) ได้หรือไม่
    if k_row == r_row or k_col == r_col:
        print(" Success")
    else:
        print("Fall")

def main():
    board = """\
 R...
 .K..
 ..P.
 ....\
 """
    checkmate(board)

    board2 = """\
 ..
 .K\
 """
    checkmate(board2)

if __name__ == "__main__":
    main()

