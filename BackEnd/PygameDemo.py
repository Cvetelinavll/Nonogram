import pygame
import requests
import time
# Initialize Pygame
pygame.init()

# Window settings
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Nonogram Puzzle')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Game settings
FPS = 60
font = pygame.font.Font(None, 24)
current_puzzle_size = 5  # Starting puzzle size
lives = 3  # Starting lives

# API Settings
API_URL = "http://127.0.0.1:5000/data"

def fetch_puzzle_data(size):
    try:
        response = requests.get(API_URL, params={'size': size})
        if response.status_code == 200:
            data = response.json()
            return data['Grid'], data['Row_hints'], data['Col_hints']
        else:
            print(f"Error fetching data: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred: {e}")
    return None, None, None

def draw_grid(grid, box_size, offset):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            rect = pygame.Rect(x * box_size + offset, y * box_size + offset, box_size, box_size)
            pygame.draw.rect(win, GRAY, rect, 1)
            if grid[y][x] == 1:
                pygame.draw.rect(win, BLACK, rect)

def draw_hints(row_hints, col_hints, grid_size, box_size, offset):
    for index, hint in enumerate(row_hints):
        hint_text = ' '.join(str(num) for num in hint)
        hint_surface = font.render(hint_text, True, BLACK)
        win.blit(hint_surface, (grid_size * box_size + offset + 5, index * box_size + offset))
    
    for index, hint in enumerate(col_hints):
        hint_text = ' '.join(str(num) for num in hint)
        hint_surface = font.render(hint_text, True, BLACK)
        win.blit(hint_surface, (index * box_size + offset, grid_size * box_size + offset + 5))

def check_solution(player_grid, solution_grid):
    return player_grid == solution_grid

def game_loop():
    global current_puzzle_size, lives
    lives = 3  # Reset lives to 3 at the start of each game loop
    solution_grid, row_hints, col_hints = fetch_puzzle_data(current_puzzle_size)
    if not solution_grid:
        print("Failed to get a puzzle from the server.")
        return  # Exit the game loop if no puzzle is fetched

    # Print the server grid to the terminal
    print(f"Server Grid for size {current_puzzle_size}x{current_puzzle_size}:")
    for row in solution_grid:
        print(' '.join(str(cell) for cell in row))

    player_grid = [[0 for _ in range(current_puzzle_size)] for _ in range(current_puzzle_size)]
    box_size = (min(win_width, win_height) - 100) // current_puzzle_size  # Padding for borders
    offset = 50  # Offset for border
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return  # Exit the game completely

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x = (x - offset) // box_size
                y = (y - offset) // box_size
                if 0 <= x < current_puzzle_size and 0 <= y < current_puzzle_size:
                    # Toggle cell
                    player_grid[y][x] = 1 - player_grid[y][x]
                    # Check if the move was incorrect
                    if solution_grid[y][x] != player_grid[y][x]:
                        lives -= 1  # Deduct a life for wrong guess
                        print(f"Wrong move! Lives remaining: {lives}")
                        if lives == 0:
                            print("Out of lives! Starting over...")
                            running = False  # End the current game loop
                            current_puzzle_size = 5  # Reset puzzle size
                            break  # Exit the event loop
                    elif check_solution(player_grid, solution_grid):
                        print("Puzzle solved! Moving to the next size.")
                        running = False  # End the current game loop
                        current_puzzle_size += 1  # Increase puzzle size for next game
                        break  # Skip the rest of the loop and restart

        win.fill(WHITE)
        draw_grid(player_grid, box_size, offset)
        draw_hints(row_hints, col_hints, current_puzzle_size, box_size, offset)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    while True:
        game_loop()
        pygame.time.delay(3000)  # Pause before starting a new puzzle

