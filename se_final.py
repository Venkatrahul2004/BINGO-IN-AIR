import cv2
import numpy as np
import random
import time
import pygame
import mediapipe as mp

# Initialize Pygame for sound effects
pygame.init()
pop_sound = pygame.mixer.Sound('pop.wav')
applause_sound = pygame.mixer.Sound('applause.wav')

# Initialize MediaPipe Hand Detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Function to generate a Bingo board with blocked cells
def generate_bingo_board():
    board = np.zeros((6, 2), dtype=int)
    blocked_cells = random.sample(range(12), 6)  # 6 blocked cells out of 12
    numbers = list(range(1, 13))  # Numbers 1 to 12

    index = 0
    for i in range(6):
        for j in range(2):
            if index in blocked_cells:
                board[i, j] = 0  # Blocked cell
            else:
                board[i, j] = numbers.pop(random.randint(0, len(numbers) - 1))
            index += 1

    return board

# Function to draw the Bingo board on a frame with centered, bold numbers and bold borders
def draw_bingo_board(frame, board, start_point):
    x_start, y_start = start_point
    cell_size = 100
    for i in range(6):
        for j in range(2):
            number = board[i, j]
            x = x_start + j * cell_size
            y = y_start + i * cell_size
            # Draw a thicker border around each cell
            cv2.rectangle(frame, (x, y), (x + cell_size, y + cell_size), (50, 50, 50), 4)  # Border thickness set to 4
            if number != 0:
                # Draw number with bolder font
                text_size = cv2.getTextSize(str(number), cv2.FONT_HERSHEY_SIMPLEX, 1.5, 3)[0]  # Font thickness set to 3
                text_x = x + (cell_size - text_size[0]) // 2
                text_y = y + (cell_size + text_size[1]) // 2
                cv2.putText(frame, str(number), (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
            else:
                # Draw blocked cell indicator ("X") with bolder font
                text_size = cv2.getTextSize("X", cv2.FONT_HERSHEY_SIMPLEX, 1.5, 3)[0]  # Font thickness set to 3
                text_x = x + (cell_size - text_size[0]) // 2
                text_y = y + (cell_size + text_size[1]) // 2
                cv2.putText(frame, "X", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)


# Function to detect the index finger tip using MediaPipe
def detect_fingers(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)
    finger_positions = []

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, _ = frame.shape
            finger_positions.append((int(index_tip.x * w), int(index_tip.y * h)))

    return finger_positions

# Function to check and update the board
def update_board(board, number, finger_pos, board_start):
    x_start, y_start = board_start
    cell_size = 100
    for i in range(6):
        for j in range(2):
            x = x_start + j * cell_size
            y = y_start + i * cell_size
            if board[i, j] == number and x < finger_pos[0] < x + cell_size and y < finger_pos[1] < y + cell_size:
                board[i, j] = 0
                pygame.mixer.Sound.play(pop_sound)
                return True
    return False

# Function to get a number from the cycle
def get_next_number(cycle, popped_numbers):
    available_numbers = [num for num in cycle if num not in popped_numbers]
    if not available_numbers:
        # Reset cycle if all numbers are popped
        popped_numbers.clear()
        available_numbers = cycle

    number = random.choice(available_numbers)
    popped_numbers.add(number)
    return number

# Function to restart the game
def restart_game():
    global player1_board, player2_board, cycle, popped_numbers, missed_numbers, number, start_time, game_over
    player1_board = generate_bingo_board()
    player2_board = generate_bingo_board()
    cycle = list(range(1, 13))
    popped_numbers = set()
    missed_numbers = 0
    number = get_next_number(cycle, popped_numbers)  # Initialize the first number
    start_time = time.time()
    game_over = False

def display_winner_prompt(winner):
    frame = np.zeros((1080, 1920, 3), dtype=np.uint8)
    # Adjusted position for centering the winner text better
    text_size = cv2.getTextSize(f'{winner} WINS!', cv2.FONT_HERSHEY_SIMPLEX, 3, 8)[0]
    text_x = (frame.shape[1] - text_size[0]) // 2-200  # Center horizontally
    text_y = (frame.shape[0] + text_size[1]) // 2-200  # Center vertically (adjusted for better appearance)
    
    cv2.putText(frame, f'{winner} WINS!', (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 8)
    cv2.imshow('Bingo Game', frame)
    pygame.mixer.Sound.play(applause_sound)  # Play applause sound
    cv2.waitKey(3000)  # Show for 3 seconds


# Function to display the logo with adjustable coordinates
def display_logo():
    frame = np.zeros((1080, 1920, 3), dtype=np.uint8)  # Create a blank frame with your screen resolution
    logo = cv2.imread('logo.png')

    if logo is not None:
        logo_height, logo_width = logo.shape[:2]
        
        # You can adjust these values to change the logo's position on the screen
        x_offset = 600  # Adjust the horizontal position (increase for right, decrease for left)
        y_offset = 200  # Adjust the vertical position (increase for down, decrease for up)
        
        # Make sure the logo fits inside the frame
        if x_offset + logo_width > frame.shape[1]:
            x_offset = frame.shape[1] - logo_width  # Keep the logo within the screen width
        if y_offset + logo_height > frame.shape[0]:
            y_offset = frame.shape[0] - logo_height  # Keep the logo within the screen height
        
        frame[y_offset:y_offset+logo_height, x_offset:x_offset+logo_width] = logo

    # Display the frame with the logo
    cv2.imshow('Bingo Game', frame)

    # Resize the window to fit the screen resolution (e.g., 1920x1080)
    cv2.resizeWindow('Bingo Game', 1920, 1080)

    cv2.waitKey(5000)  # Display the logo for 5 seconds
    cv2.destroyAllWindows()


# Main game loop
def main():
    global player1_board, player2_board, cycle, popped_numbers, missed_numbers, number, start_time, game_over
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    display_logo()
    restart_game()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (1920, 1080))

        finger_positions = detect_fingers(frame)
        if finger_positions:
            for finger_pos in finger_positions:
                if number is not None:
                    if update_board(player1_board, number, finger_pos, (frame.shape[1]//4 - 75, frame.shape[0]//2 - 375)):
                        number = get_next_number(cycle, popped_numbers)
                        start_time = time.time()
                    elif update_board(player2_board, number, finger_pos, (frame.shape[1]//4 + 600 - 75, frame.shape[0]//2 - 375)):
                        number = get_next_number(cycle, popped_numbers)
                        start_time = time.time()

        if number is None or time.time() - start_time >= 7:
            if missed_numbers < 3:
                number = get_next_number(cycle, popped_numbers)
                start_time = time.time()
            else:
                missed_numbers = 0

        # Check for a winner
        if not np.any(player1_board):
            winner = "Player 1"
            display_winner_prompt(winner)
            restart_game()
            continue
        elif not np.any(player2_board):
            winner = "Player 2"
            display_winner_prompt(winner)
            restart_game()
            continue

        # Display number, shifted slightly to the left for better centering
        cv2.putText(frame, f'Number: {number}', (frame.shape[1]//2 - 305, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        
        draw_bingo_board(frame, player1_board, (frame.shape[1]//4 - 75, frame.shape[0]//2 - 375))
        draw_bingo_board(frame, player2_board, (frame.shape[1]//4 + 600 - 75, frame.shape[0]//2 - 375))

        cv2.imshow('Bingo Game', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):  # Restart game when 'r' key is pressed
            restart_game()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
