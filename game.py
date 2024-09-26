import pygame
from new import draw
from new import draw_numbers
from new import define_control_grid
from new import get_cell_index
# Tạo pygame
pygame.init()

#Tạo cửa sổ trò chơi
width = 1800
hight =1000
color = (255,255,255)
window = pygame.display.set_mode((width, hight))
window.fill(color)

# vẽ lưới
for i in range(0,10):
    pygame.draw.line(window, (198, 204, 206), (30, (i * 100) + 30), (930, (i * 100 + 30)), 2)
    pygame.draw.line(window, (198, 204, 206), (100 * i + 30, 30), ((i * 100 + 30), 930), 2)
for i in range(0,10):
    # vẽ đậm những đường 0 | 3 | 6 | 9
    if i % 3 == 0 :
        pygame.draw.line(window, (52, 72, 97), (28, (i * 100) + 30), (932, (i * 100 + 30)), 5)
        pygame.draw.line(window, (52, 72, 97), (100 * i + 30, 28), ((i * 100 + 30), 930), 5)
    else:
        continue

# Biến chạy game
running = True

# ma trận trạng thái lưới
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
control_grid = tuple(define_control_grid(grid))

# Vòng lặp chính
def desktop():
    while running:
        # vẽ
        draw(window)

        # sự kiện điền số lên lưới
        draw_numbers(window, grid)

        # sự kiện thoát game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell_index = get_cell_index(event.pos)  # Lấy chỉ số hàng và cột
                if cell_index:
                    print(f"Clicked on cell: {cell_index}")  # In ra chỉ số hàng và cột

        # cập nhật hiển thị
        pygame.display.update()

def main():
    desktop()

if __name__ == "__main__":

    for i in range(9):
        for j in range(9):
            print(control_grid[i][j], end=" ")  # Sử dụng end để không xuống dòng
        print()  # Xuống dòng sau khi in một hàng

    main()
