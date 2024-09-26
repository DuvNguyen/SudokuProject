import pygame
import math

# Hàm tạo nút trò chơi mới
width_number = 180
height_number = 180
before_event_color = (234, 238, 244)
after_event_color = (220, 227, 237)
border_radius_number = 10
textcolor = (60, 121, 215)
textsize = 150

# Kích thước ô
CELL_SIZE = 100
GRID_SIZE = 9


def draw_button(screen, text, x, y, w, h, inactive_color, active_color, radius, text_color, text_size):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h), border_radius=radius)  # Màu sáng khi di chuột qua
        if click[0] == 1:  # Kiểm tra nếu chuột được nhấn
            print(text)
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h), border_radius=radius)  # Màu bình thường

    # Vẽ chữ lên nút
    font = pygame.font.SysFont(None, text_size)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=((x + w // 2), (y + h // 2)))
    screen.blit(text_surf, text_rect)


# Hàm vẽ nút tròn
def draw_circle(screen, text, x, y, inactive_color, active_color, radius, img):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    distance = math.sqrt((mouse[0] - x) ** 2 + (mouse[1] - y) ** 2)

    if distance < radius:
        pygame.draw.circle(screen, active_color, (x, y), radius)  # Màu sáng khi di chuột qua
        if click[0] == 1:  # Kiểm tra nếu chuột được nhấn
            print(text)
    else:
        pygame.draw.circle(screen, inactive_color, (x, y), radius)  # Màu bình thường

    # Vẽ icon lên nút
    screen.blit(img, (x - img.get_width() // 2, y - img.get_height() // 2))

    # Vẽ chữ cho nút
    font = pygame.font.SysFont(None, 35)
    text_surf = font.render(text, True, (60, 121, 215))
    text_rect = text_surf.get_rect(center=(x, y + 70))
    screen.blit(text_surf, text_rect)


def draw_exercise():
    return


def draw(window):
    # Vẽ các số từ 1->9 và Nút New Game
    draw_button(window, '1', 1030, 230, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '2', 1230, 230, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '3', 1430, 230, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '4', 1030, 430, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '5', 1230, 430, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '6', 1430, 430, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '7', 1030, 630, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '8', 1230, 630, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, '9', 1430, 630, width_number, height_number, before_event_color, after_event_color,
                border_radius_number, textcolor, textsize)
    draw_button(window, 'New Game', 1030, 830, 580, 100, (90, 123, 192), (90, 123, 200), 30, 'white', 100)

    # Vẽ nút xóa quay lại
    img_delete = pygame.image.load('Image/delete.png').convert_alpha()
    img_return = pygame.image.load('Image/return.png').convert_alpha()
    img_idea = pygame.image.load('Image/idea.png').convert_alpha()
    draw_circle(window, 'DELETE', 1120, 100, before_event_color, after_event_color, 45, img_delete)
    draw_circle(window, 'RETURN', 1320, 100, before_event_color, after_event_color, 45, img_return)
    draw_circle(window, 'IDEA', 1520, 100, before_event_color, after_event_color, 45, img_idea)


# Hàm vẽ lưới Sudoku
def draw_grid(window):
    # Vẽ lưới
    for i in range(0, 10):
        pygame.draw.line(window, (198, 204, 206), (30, (i * 100) + 30), (930, (i * 100 + 30)), 2)
        pygame.draw.line(window, (198, 204, 206), (100 * i + 30, 30), ((i * 100 + 30), 930), 2)

    for i in range(0, 10):
        # Vẽ đậm những đường 0 | 3 | 6 | 9
        if i % 3 == 0:
            pygame.draw.line(window, (52, 72, 97), (28, (i * 100) + 30), (932, (i * 100 + 30)), 5)
            pygame.draw.line(window, (52, 72, 97), (100 * i + 30, 28), ((i * 100 + 30), 930), 5)


# Điền số
def draw_numbers(screen, grid, fixed_cells):
    font = pygame.font.SysFont(None, 90)  # Kích thước font là 90
    for i in range(9):
        for j in range(9):
            number = grid[i][j]
            if number != 0:  # Kiểm tra nếu ô không rỗng
                text_surf = font.render(str(number), True, (0, 0, 0))  # Màu chữ là đen
                text_rect = text_surf.get_rect(center=(j * 100 + 80, i * 100 + 80))  # Tính vị trí trung tâm
                screen.blit(text_surf, text_rect)  # Vẽ số lên màn hình


# Hàm xác định
def define_control_grid(grid):
    control_grid = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                control_grid[i][j] = -1  # Sửa lại từ control_grid thành control_grid
            else:
                control_grid[i][j] = 0
    return control_grid  # Trả về control_grid


# Hàm xử lý di chuột
def handle_mouse_events(mouse_pos, fixed_cells):
    mouse_x, mouse_y = mouse_pos
    grid_x = mouse_x // CELL_SIZE
    grid_y = mouse_y // CELL_SIZE

    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
        if (grid_y, grid_x) not in fixed_cells:
            # Đổ màu xám cho các ô cùng hàng, cột và ô 3x3
            highlight_cells = set()
            for i in range(GRID_SIZE):
                highlight_cells.add((grid_y, i))  # Cùng hàng
                highlight_cells.add((i, grid_x))  # Cùng cột

            start_row = (grid_y // 3) * 3
            start_col = (grid_x // 3) * 3
            for i in range(3):
                for j in range(3):
                    highlight_cells.add((start_row + i, start_col + j))  # Hình vuông 3x3

            return highlight_cells
    return set()  # Trả về một tập rỗng nếu không có ô nào được chọn


# Hàm xử lý nhấp chuột
def toggle_fixed_cell(mouse_pos, fixed_cells):
    mouse_x, mouse_y = mouse_pos
    grid_x = (mouse_x - 30) // CELL_SIZE
    grid_y = (mouse_y - 30) // CELL_SIZE

    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
        cell = (grid_y, grid_x)
        if cell in fixed_cells:
            fixed_cells.remove(cell)  # Bỏ ô ra khỏi danh sách đã cố định
        else:
            fixed_cells.add(cell)  # Thêm ô vào danh sách đã cố định


# Hàm chính
def main():
    # Tạo pygame
    pygame.init()

    # Tạo cửa sổ trò chơi
    width = 1800
    height = 1000
    color = (255, 255, 255)
    window = pygame.display.set_mode((width, height))
    window.fill(color)

    # Khởi tạo lưới Sudoku
    grid = [[0 for _ in range(9)] for _ in range(9)]  # Lưới Sudoku ban đầu
    fixed_cells = set()  # Tập hợp các ô đã cố định
    highlight_cells = set()  # Tập hợp các ô đang được làm sáng

    running = True
    while running:
        window.fill((255, 255, 255))  # Màu nền trắng
        draw_grid(window)  # Vẽ lưới
        draw(window)  # Vẽ các nút và số

        # Vẽ số từ lưới Sudoku
        draw_numbers(window, grid, fixed_cells)

        # Xử lý sự kiện chuột
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                highlight_cells = handle_mouse_events(event.pos, fixed_cells)  # Xác định ô được làm sáng
            if event.type == pygame.MOUSEBUTTONDOWN:
                toggle_fixed_cell(event.pos, fixed_cells)  # Xử lý việc nhấp chuột

        # Vẽ các ô được làm sáng
        for (row, col) in highlight_cells:
            pygame.draw.rect(window, (220, 220, 220, 128),
                             (col * CELL_SIZE + 30, row * CELL_SIZE + 30, CELL_SIZE, CELL_SIZE))  # Ô sáng lên

        pygame.display.flip()  # Cập nhật màn hình

    pygame.quit()


if __name__ == "__main__":
    main()
