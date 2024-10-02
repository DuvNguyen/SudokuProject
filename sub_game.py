import pygame
import math

# Tạo pygame
pygame.init()

# Tạo cửa sổ trò chơi
width = 1800
hight = 1000
color = (255, 255, 255)
window = pygame.display.set_mode((width, hight))
window.fill(color)
pygame.display.set_caption("Sudoku Highlighter")

# Hàm tạo nút trò chơi mới
# màu
width_number = 180
height_number = 180
before_event_color = (234, 238, 244)
after_event_color = (220, 227, 237)
border_radius_number = 10
textcolor = (60, 121, 215)
textsize = 150


def draw_button(screen, text, x, y, w, h, inactive_color, active_color, radius, text_color, text_size):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Kiểm tra nếu con trỏ chuột đang nằm trong nút
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h), border_radius=radius)  # Màu sáng khi di chuột qua
        if click[0] == 1:  # Kiểm tra nếu chuột được nhấn\
            print(text)
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h), border_radius=radius)  # Màu bình thường
    # Vẽ chữ lên nút
    font = pygame.font.SysFont(None, text_size)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=((x + w // 2), (y + h // 2)))
    screen.blit(text_surf, text_rect)


# Vẽ các nút hình tròn
def draw_circle(screen, text, x, y, inactive_color, active_color, radius, img):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Kiểm tra nếu con trỏ chuột đang nằm trong nút
    if math.sqrt((mouse[0] - x) ** 2 + (mouse[1] - y) ** 2) < 45:
        pygame.draw.circle(screen, active_color, (x, y), radius)  # Màu sáng khi di chuột qua
        if click[0] == 1:  # Kiểm tra nếu chuột được nhấn
            print(mouse[0], mouse[1])
    else:
        pygame.draw.circle(screen, inactive_color, (x, y), radius)  # Màu bình thường
    # Vẽ icon lên nút
    screen.blit(img, (x - 45, y - 45))
    # vẽ chữ cho nút
    font = pygame.font.SysFont(None, 35)
    text_surf = font.render(text, True, textcolor)
    text_rect = text_surf.get_rect(center=(x, y + 70))
    screen.blit(text_surf, text_rect)

    # Đưa đề
    # sử dụng cỡ chữ
    font = pygame.font.SysFont('Kometa Unicase Light', 125)
    text_surf = font.render('8', True, (52, 72, 97))
    text_rect = text_surf.get_rect(center=((30 + 100 // 2), (30 + 100 // 2)))
    screen.blit(text_surf, text_rect)


# Vẽ hình vuông
rows, cols = 9, 9
cell_size = 100


def draw_hv(selected=None):
    pygame.draw.rect(window, 'white', (30, 30, 900, 900))
    for row in range(rows):

        for col in range(cols):
            # Xác định màu của ô
            color = 'white'
            width_line = 2
            color_line = (198, 204, 206)

            # Nếu có ô được chọn
            if selected:
                selected_row, selected_col = selected

                # Đổi màu các ô cùng dòng, cùng cột
                if row == selected_row or col == selected_col:
                    color = (226, 235, 251)

                # Đổi màu các ô cùng khối 3x3
                if (row // 3 == selected_row // 3) and (col // 3 == selected_col // 3):
                    color = (226, 235, 251)

                # Đổi màu ô được chọn
                if row == selected_row and col == selected_col:
                    color = (187, 222, 251)
            # Vẽ ô vuông
            pygame.draw.rect(window, color, (col * cell_size + 30, row * cell_size + 30, cell_size, cell_size))
            # kẻ line ngang
            pygame.draw.line(window, color_line, (col * cell_size + 28, row * cell_size + 30),
                             (col * cell_size + 28 + cell_size, row * cell_size + 30), width_line)
            # kẻ line dọc
            pygame.draw.line(window, color_line, (col * cell_size + 28, row * cell_size + 28),
                             (col * cell_size + 28, row * cell_size + 28 + cell_size), width_line)
    for i in range(0, 10):
        # vẽ đậm những đường 0 | 3 | 6 | 9
        if i % 3 == 0:
            pygame.draw.line(window, (52, 72, 97), (28, (i * 100) + 30), (932, (i * 100 + 30)), 5)
            pygame.draw.line(window, (52, 72, 97), (100 * i + 30, 28), ((i * 100 + 30), 930), 5)
        else:
            continue


# lấy tọa độ cell
def get_cell(pos):
    x, y = pos
    row = (y - 30) // cell_size
    col = (x - 30) // cell_size
    return row, col


# Main loop
def desktop():
    # Vòng lặp chính
    running = True
    selected_cell = None
    while running:
        # Vẽ các số từ 1->9 và Nút  NewGame
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
        # vẽ nút xóa quay lại
        img_delete = pygame.image.load('delete.png').convert_alpha()
        img_return = pygame.image.load('return.png').convert_alpha()
        img_idea = pygame.image.load('idea.png').convert_alpha()
        draw_circle(window, 'DELETE', 1120, 100, before_event_color, after_event_color, 45, img_delete)
        draw_circle(window, 'RETURN', 1320, 100, before_event_color, after_event_color, 45, img_return)
        draw_circle(window, 'IDEA', 1520, 100, before_event_color, after_event_color, 45, img_idea)
        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (930 > mouse[0] > 30 and 930 > mouse[1] > 30):
                    selected_cell = get_cell(pygame.mouse.get_pos())
        draw_hv(selected_cell)
        # Update the display
        pygame.display.update()


def main():
    print("Hello World!")
    desktop()


if __name__ == "__main__":
    main()
