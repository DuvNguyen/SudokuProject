import pygame
import math  # Thêm thư viện toán học để tính khoảng cách

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
    click = pygame.mouse.get_pressed()

    # Kiểm tra nếu con trỏ chuột đang nằm trong nút
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

    # Tính khoảng cách giữa chuột và tâm hình tròn
    distance = math.sqrt((mouse[0] - x) ** 2 + (mouse[1] - y) ** 2)

    # Kiểm tra nếu khoảng cách nhỏ hơn bán kính
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
    img_idea = pygame.image.load('Image/idea.png').convert_alpha()
    draw_circle(window,'DELETE',1120,100,before_event_color,after_event_color,45,img_delete)
    draw_circle(window, 'RETURN', 1320, 100, before_event_color, after_event_color, 45,img_return)
    draw_circle(window, 'IDEA', 1520, 100, before_event_color, after_event_color, 45,img_idea)

# Điền số
# Sudoku grid matrix (9x9), 0 means empty, 1-9 are the numbers to be printed
def draw_numbers(screen, grid):
    # Sử dụng định dạng font giống như các ô phụ bên phải
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
                control_grid[i][j] = -1  # Sửa lại từ control_gird thành control_grid
            else:
                control_grid[i][j] = 0
    return control_grid  # Trả về control_grid

GRID_SIZE = 9
CELL_SIZE = 100  # Kích thước của mỗi ô lưới

def get_cell_index(mouse_pos):
    mouse_x, mouse_y = mouse_pos
    # Tính chỉ số hàng và cột dựa vào vị trí chuột
    grid_x = (mouse_x - 30) // CELL_SIZE  # Điều chỉnh để bỏ qua khoảng cách 30 pixel
    grid_y = (mouse_y - 30) // CELL_SIZE  # Điều chỉnh để bỏ qua khoảng cách 30 pixel

    # Kiểm tra xem chỉ số có nằm trong giới hạn không
    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
        return (grid_y, grid_x)  # Trả về tuple (hàng, cột)
    return None  # Trả về None nếu không có ô nào được nhấp

