import pygame
from new import draw_number_and_new_game_button, control_grid, isSafe
from new import draw_numbers
from new import get_cell_index
from new import get_clicked_number
from new import insert_into_grid
from new import get_clicked_circle  # Hàm này để xóa giá trị từ lưới
from new import get_clicked_new_game
from new import change
from new import set_new_game
from new import solveSudoku
from new import grid
from new import highlight_selected_cell
from new import check_full, display_win

# Tạo pygame
pygame.init()

# Tạo cửa sổ trò chơi
width = 1900
height = 1000
color = (255, 255, 255)
window = pygame.display.set_mode((width, height))
window.fill(color)

# Vẽ lưới
def draw_grid():
    for i in range(0, 10):
        pygame.draw.line(window, (198, 204, 206), (30, (i * 100) + 30), (930, (i * 100 + 30)), 2)
        pygame.draw.line(window, (198, 204, 206), (100 * i + 30, 30), ((i * 100 + 30), 930), 2)

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(window, (52, 72, 97), (28, (i * 100) + 30), (932, (i * 100 + 30)), 5)
            pygame.draw.line(window, (52, 72, 97), (100 * i + 30, 28), ((i * 100 + 30), 930), 5)

# Biến chạy game
running = True

# Vòng lặp chính
def desktop():
    row, col = None, None
    cell_id =None
    tmp =None
    waiting = True
    while running:
        # Vẽ
        window.fill((255, 255, 255))  # Làm mới màn hình
        draw_grid()  # Vẽ lại lưới
        draw_number_and_new_game_button(window)
        draw_numbers(window)

        if check_full():
            display_win(window, waiting)
             # Thoát khỏi vòng lặp sau khi hiển thị màn hình chiến thắng

        for event in pygame.event.get():
            # Sự kiện thoát game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Sự kiện chuột
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (930 > mouse[0] > 30 and 930 > mouse[1] > 30):
                    cell_id = get_cell_index(pygame.mouse.get_pos())
                    tmp = cell_id
                else:
                    # Phần 1: lấy vị trí của cell lưới
                    # Lấy chỉ số hàng và cột
                    if cell_id:  # Kiểm tra nếu cell_index hợp lệ
                        print(f"Đã chọn ô ({cell_id[0]}, {cell_id[1]})")
                        row, col = cell_id

                    # Phần 2: chọn số để thêm vào grid
                    value = get_clicked_number(event.pos)
                    if value:  # Kiểm tra nếu value không phải là None
                        print(f"Chọn số: {value}")
                        if isSafe(row, col, value):
                            insert_into_grid(value, row, col)  # Điền giá trị vào ô
                        else:
                            pass

                    # Phần 3: kiểm tra click vào các nút delete, return, idea
                    mouse_pos = pygame.mouse.get_pos()  # Lấy tọa độ của chuột
                    button_clicked = get_clicked_circle(mouse_pos)  # Kiểm tra nút nào đã được click
                    if button_clicked:
                        print(f"Đã bấm nút: {button_clicked}")
                        if button_clicked == "delete":
                            change(row, col)  # Gọi hàm để xóa giá trị
                            print(f"Đã xóa giá trị tại ô ({row}, {col})")
                        if button_clicked == "answer":
                            if solveSudoku(0, 0):
                                for i in range(0, 9):
                                    for j in range(0, 9):
                                        print(grid[i][j], end=' ')
                                    print()
                            else:
                                print("no solution exists ")
                        if button_clicked == "hint":
                            # highlight_selected_cell(window, 1, 1)
                            pass

                    new_game_clicked = get_clicked_new_game(event.pos)
                    if new_game_clicked:
                        print("clicked new game button")
                        # Thực hiện hành động khi nhấn nút New Game
                        set_new_game()

        draw_numbers(window, tmp)
        draw_grid()
        # Cập nhật hiển thị
        pygame.display.update()

def main():
    # In trạng thái ban đầu của lưới
    for i in range(9):
        for j in range(9):
            print(control_grid[i][j], end=" ")
        print()  # Xuống dòng sau khi in một hàng

    desktop()

if __name__ == "__main__":
    main()
