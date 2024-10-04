import pygame
import math  # Thêm thư viện toán học để tính khoảng cách
import random
import numpy

# Hàm tạo nút trò chơi mới
# màu
width_number = 180
height_number = 180
before_event_color = (234,238,244)
after_event_color = (220,227,237)
border_radius_number = 10
textcolor = (60,121,215)
textsize = 150

def draw_button(screen, text, x, y, w, h, inactive_color, active_color, radius,text_color,text_size):
    mouse = pygame.mouse.get_pos()

    # Kiểm tra nếu con trỏ chuột đang nằm trong nút
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h), border_radius=radius)  # Màu sáng khi di chuột qua
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

    # Tính khoảng cách giữa chuột và tâm hình tròn
    distance = math.sqrt((mouse[0] - x) ** 2 + (mouse[1] - y) ** 2)

    # Kiểm tra nếu khoảng cách nhỏ hơn bán kính
    if distance < radius:
        pygame.draw.circle(screen, active_color, (x, y), radius)  # Màu sáng khi di chuột qua
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

def draw_number_and_new_game_button(window):
    # Vẽ các số từ 1->9 và Nút  NewGame
    draw_button(window, '1', 1030, 230, width_number, height_number, before_event_color, after_event_color, border_radius_number,textcolor,textsize)
    draw_button(window, '2', 1230, 230, width_number, height_number, before_event_color, after_event_color, border_radius_number,textcolor,textsize)
    draw_button(window, '3', 1430, 230, width_number, height_number,  before_event_color, after_event_color, border_radius_number,textcolor,textsize)
    draw_button(window, '4', 1030, 430, width_number, height_number,  before_event_color, after_event_color, border_radius_number,textcolor,textsize)
    draw_button(window, '5', 1230, 430, width_number, height_number,  before_event_color, after_event_color, border_radius_number,textcolor,textsize)
    draw_button(window, '6', 1430, 430, width_number, height_number,  before_event_color, after_event_color, border_radius_number,textcolor,textsize)
    draw_button(window, '7', 1030, 630, width_number, height_number,  before_event_color, after_event_color, border_radius_number,textcolor,textsize)
    draw_button(window, '8', 1230, 630, width_number, height_number,  before_event_color, after_event_color, border_radius_number,textcolor,textsize)
    draw_button(window, '9', 1430, 630, width_number, height_number,  before_event_color, after_event_color, border_radius_number,textcolor,textsize)
    draw_button(window, 'New Game', 1030, 830, 580, 100, (90, 123, 192), (90, 123, 200), 30, 'white',100)
    # vẽ nút xóa quay lại
    img_delete = pygame.image.load('Image/delete.png').convert_alpha()
    img_return = pygame.image.load('Image/return.png').convert_alpha()
    img_idea = pygame.image.load('Image/answer.png').convert_alpha()
    draw_circle(window,'DELETE',1120,100,before_event_color,after_event_color,45,img_delete)
    draw_circle(window, 'HINT', 1320, 100, before_event_color, after_event_color, 45,img_return)
    draw_circle(window, 'ANSWER', 1520, 100, before_event_color, after_event_color, 45,img_idea)

# Điền số
# Sudoku grid matrix (9x9), 0 means empty, 1-9 are the numbers to be printed

# Sinh đề
b = numpy.load('data.npz')['data']

test_code = random.randint(1, 5000)

grid = b[test_code].tolist()
# grid = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# Hàm xác định cho tuple cố định, để tránh thao tác lên đề
def define_control_grid(grid):
    control_grid = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                control_grid[i][j] = -1  
            else:
                control_grid[i][j] = 0
    return control_grid

control_grid = define_control_grid(grid)

# hàm in số lên màn hình
def draw_numbers(screen,selected = None):
    font = pygame.font.SysFont(None, 90)  # Kích thước font là 90
    for i in range(9):
        for j in range(9):
            color = 'white'
            # Nếu có ô được chọn
            if selected:
                selected_row, selected_col = selected
                # Đổi màu các ô cùng dòng, cùng cột
                if i == selected_row or j == selected_col:
                    color = (226, 235, 251)
                # Đổi màu các ô cùng khối 3x3
                if (i // 3 == selected_row // 3) and (j // 3 == selected_col // 3):
                    color = (226, 235, 251)
                # Đổi màu ô được chọn
                if i == selected_row and j == selected_col:
                    color = (187, 222, 251)
            # Vẽ ô vuông
            pygame.draw.rect(screen, color, (j * CELL_SIZE + 30, i * CELL_SIZE + 30, CELL_SIZE, CELL_SIZE))
            number = grid[i][j]
            if number != 0:  # Kiểm tra nếu ô không rỗng
                # Đặt màu tương ứng dựa trên trạng thái của control_grid
                if control_grid[i][j] == -1:
                    text_color = (0, 25, 51)  # Màu xám cho các ô không thể thay đổi
                elif control_grid[i][j] == -2 or -3:
                    text_color = (0, 76, 153)  # Màu cho các số đã điền
                elif control_grid[i][j] == -4:
                    text_color = (255, 0, 0) # màu đỏ cho số điền sai
                else:
                    text_color = (0, 0, 0)  # Màu đen cho các ô trống

                text_surf = font.render(str(number), True, text_color)
                text_rect = text_surf.get_rect(center=(j * 100 + 80, i * 100 + 80))  # Tính vị trí trung tâm
                screen.blit(text_surf, text_rect)  # Vẽ số lên màn hình


GRID_SIZE = 9
CELL_SIZE = 100  # Kích thước của mỗi ô lưới

# Hàm lấy vị trí cell lưới
def get_cell_index(mouse_pos):
    mouse_x, mouse_y = mouse_pos
    # Tính chỉ số hàng và cột dựa vào vị trí chuột
    grid_x = (mouse_x - 30) // CELL_SIZE  # Điều chỉnh để bỏ qua khoảng cách 30 pixel
    grid_y = (mouse_y - 30) // CELL_SIZE  # Điều chỉnh để bỏ qua khoảng cách 30 pixel

    # Kiểm tra xem chỉ số có nằm trong giới hạn không
    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
        return (grid_y, grid_x)  # Trả về tuple (hàng, cột)
    return None  # Trả về None nếu không có ô nào được nhấp


def get_clicked_number(mouse):
    click = pygame.mouse.get_pressed()

    # Danh sách chứa thông tin vị trí của các nút số (tọa độ x, y, số hiển thị)
    number_buttons = [
        (1030, 230, '1'), (1230, 230, '2'), (1430, 230, '3'),
        (1030, 430, '4'), (1230, 430, '5'), (1430, 430, '6'),
        (1030, 630, '7'), (1230, 630, '8'), (1430, 630, '9')
    ]

    if click[0] == 1:  # Nếu nhấn chuột trái
        for button in number_buttons:
            x, y, number = button
            if x + width_number > mouse[0] > x and y + height_number > mouse[1] > y:
                return int(number)  # Trả về giá trị của số được nhấn (1 -> 9)

    return None  # Nếu không nhấn vào nút nào, trả về None

# hàm thêm lên ma trận lưới
def insert_into_grid(value, row, col):
    if row is not None and col is not None:
        if control_grid[row][col] == 0:
            grid[row][col] = value
            control_grid[row][col] = -2
        else:
            pass

# nhận biết phím chức năng được bấm
def get_clicked_circle(mouse_pos):
    click = pygame.mouse.get_pressed()
    # Danh sách chứa thông tin của các nút (tọa độ x, y, bán kính, tên nút)
    circle_buttons = [
        (1120, 100, 45, 'delete'),  # Tọa độ và bán kính của nút delete
        (1320, 100, 45, 'hint'),  # Tọa độ và bán kính của nút hint
        (1520, 100, 45, 'answer')     # Tọa độ và bán kính của nút idea
    ]

    if click[0] == 1:  # Nếu nhấn chuột trái
        for button in circle_buttons:
            x, y, radius, name = button
            # Tính khoảng cách từ vị trí chuột tới tâm của nút
            distance = math.sqrt((mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2)
            if distance < radius:  # Kiểm tra nếu khoảng cách nhỏ hơn bán kính
                # print(f'Bạn đã bấm vào nút {name}')
                return name  # Trả về tên của nút đã bấm

    return None  # Nếu không bấm vào nút nào

# hàm test nút delete
def change(row, col):
    if row is not None and col is not None:
        if control_grid[row][col] == -2:
            grid[row][col] = 0
            control_grid[row][col] = 0

# các hàm xử lý nút trò chơi mới
def get_clicked_new_game(mouse_pos):
    click = pygame.mouse.get_pressed()

    # Thông tin về nút "New Game"
    new_game_x = 1030
    new_game_y = 830
    new_game_width = 580
    new_game_height = 100

    if click[0] == 1:  # Nếu nhấn chuột trái
        if new_game_x + new_game_width > mouse_pos[0] > new_game_x and new_game_y + new_game_height > mouse_pos[1] > new_game_y:
            print('Bạn đã bấm vào nút New Game')
            return True  # Trả về True nếu nút được nhấn

    return False  # Nếu không nhấn vào nút "New Game", trả về False

def set_new_game():
    global grid, control_grid  # Đảm bảo bạn có quyền truy cập vào biến toàn cục
    # Sinh lại đề mới (sử dụng dữ liệu từ file hoặc tạo mới)
    b = numpy.load('data.npz')['data']
    test_code = random.randint(1, 10000)
    grid = b[test_code].tolist()
    control_grid = define_control_grid(grid)  # Cập nhật control_grid theo đề mới


# Hàm giải đề
N = 9

def isSafe(row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

# hàm đã được điền full:
def check_full():
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False
    return True

def solveSudoku(row, col):
    global grid
    if (row == N - 1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(row, col + 1)
    for num in range(1, N + 1, 1):
        if isSafe(row, col, num):
            grid[row][col] = num
            control_grid[row][col] = -3
            for i in range(0, 9):
                for j in range(0, 9):
                    if check_full():
                        if control_grid[i][j] == -2:
                            control_grid[i][j] = -3
            if solveSudoku(row, col + 1):
                return True

        grid[row][col] = 0
    return False
