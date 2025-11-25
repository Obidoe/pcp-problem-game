import time
from domino import Domino
import pygame


class Game:

    def __init__(self):
        # pygame setup
        pygame.init()
        self.clock = pygame.time.Clock()

        self.delta_time = 0.1
        self.screen_width = 1280
        self.screen_height = 720
        self.fps = 60

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PCP Problem Game")
        
        # Domino Generation
        self.domino_index = 0
        self.dominos = [Domino() for i in range(10)]
        self.frameDone = False
        # set initial positions for dominoes in the set area
        for i, d in enumerate(self.dominos):
            d.x = 50 + i * 120
            d.y = 100
        
        # working area dominoes
        self.working_area_dominos = []
        # drag state
        self.dragged_domino = None
        # define areas
        self.working_area_y = 400
        self.working_area_height = 200
        
        # button for clear/reset
        self.difficulty_button_rect = pygame.Rect(self.screen_width - 400, 20, 120, 40)
        self.difficulty_button_rect = pygame.Rect(self.screen_width - 400, 20, 120, 40)
        self.clear_button_rect = pygame.Rect(self.screen_width - 250, 20, 100, 40)
        self.new_game_button_rect = pygame.Rect(self.screen_width - 130, 20, 110, 40)
        
        # time variables
        self.timer_start = None
        self.timer_running = False
        self.elapsed_time = 0
        self.last_time = 0

        self.running = True

    def start_timer(self):
            # start timer when first domino is placed
            if not self.timer_running and len(self.working_area_dominos) == 0:
                self.timer_start = time.time()
                self.timer_running = True
                self.elapsed_time = 0
                print("Timer started")

    def stop_timer(self):
            # stop timer when sequences match 
            if self.timer_running:
                self.timer_running = False
                self.elapsed_time = time.time() - self.timer_start
                self.last_time = self.elapsed_time
                print(f"Time taken to win: {self.last_time:.2f} seconds")

    def reset_timer(self):
            # reset timer when working area is cleared or new game button is pressed
            self.timer_running = False
            self.elapsed_time = 0
            self.timer_start = None
            self.last_time = 0
            print("Timer reset")
    
    def get_current_time(self):
        # get current elapsed time in seconds
        if self.timer_running:
            return time.time() - self.timer_start 
        else:
            return self.elapsed_time

    def is_in_working_area(self, y):
        # check if y cord is in working area
        return self.working_area_y <= y <= self.working_area_y + self.working_area_height
    
    def get_concatenated_sequences(self):
        """Get the concatenated top and bottom sequences from working area dominoes"""
        top_sequence = []
        bottom_sequence = []
        for domino in self.working_area_dominos:
            top_sequence.extend(domino.top)
            bottom_sequence.extend(domino.bottom)
        return top_sequence, bottom_sequence
    
    def get_current_bottom_sequence(self):
        """Get the current concatenated bottom sequence"""
        _, bottom_sequence = self.get_concatenated_sequences()
        return bottom_sequence
    
    def update_highlights(self):
        """Update which dominoes in the set should be highlighted as valid next moves"""
        # Reset all highlights
        for d in self.dominos:
            d.highlighted = False
        
        # If working area is empty, all dominoes are valid (can start with anything)
        if not self.working_area_dominos:
            for d in self.dominos:
                d.highlighted = True
            return
        
        # Get the current bottom sequence
        current_bottom = self.get_current_bottom_sequence()
        
        # Highlight dominoes whose top matches the current bottom
        # This means they can be placed next to continue the sequence
        for d in self.dominos:
            if d.top == current_bottom:
                d.highlighted = True

    def handle_mouse_down(self, pos):
        # check if clicking clear button
        if self.clear_button_rect.collidepoint(pos):
            self.clear_working_area()
            return
        
        # check if clicking new game button
        if self.new_game_button_rect.collidepoint(pos):
            self.new_game()
            return
        
        # check if clicking new game button
        if self.new_game_button_rect.collidepoint(pos):
            self.new_game()
            return

        if self.difficulty_button_rect.collidepoint(pos):
            self.resetDifficulty()
            return

        # check if clicking on a domino in the set 
        for d in self.dominos:
            if d.contains_point(pos[0], pos[1]):
                # create a copy of the domino for dragging
                new_domino = Domino()
                new_domino.top = d.top.copy()
                new_domino.bottom = d.bottom.copy()
                new_domino.x = d.x
                new_domino.y = d.y
                new_domino.start_drag(pos[0], pos[1])
                self.dragged_domino = new_domino
                return
        
        # check if clicking on a domino in the working area
        for d in self.working_area_dominos:
            if d.contains_point(pos[0], pos[1]):
                d.start_drag(pos[0], pos[1])
                self.dragged_domino = d
                # remove from working area for repositioning
                self.working_area_dominos.remove(d)
                return

    def handle_mouse_up(self, pos):
        if self.dragged_domino:
            # check if domino was dropped in working area
            if self.is_in_working_area(self.dragged_domino.y):
                if len(self.working_area_dominos) == 0:
                    # start timer on first domino placed
                    self.start_timer()
                if self.dragged_domino not in self.working_area_dominos:
                    self.working_area_dominos.append(self.dragged_domino)
                self.dragged_domino.in_working_area = True
                # reposition dominoes in sequence
                self.reposition_working_area_dominos()
                # stop timer if sequences match
                top_seq, bottom_seq = self.get_concatenated_sequences()
                if top_seq == bottom_seq and len(top_seq) > 0:
                    self.stop_timer()
            else:
                # if not in working area, don't add it (it's discarded)
                pass
            
            self.dragged_domino.stop_drag()
            self.dragged_domino = None
            # update highlights after any change
            self.update_highlights()

    def handle_mouse_motion(self, pos):
        if self.dragged_domino:
            self.dragged_domino.update_drag(pos[0], pos[1])
    
    def reposition_working_area_dominos(self):
        """Position dominoes in working area from left to right"""
        x_start = 50
        y_pos = self.working_area_y + 20  # Position dominoes higher in working area
        spacing = 20
        
        for i, domino in enumerate(self.working_area_dominos):
            domino.x = x_start + i * (domino.width + spacing)
            domino.y = y_pos
    
    def clear_working_area(self):
        """Clear all dominoes from working area and reset timer"""
        self.working_area_dominos = []
        self.reset_timer()
        self.update_highlights()


    def new_game(self):
        """Generate new set of dominoes"""
        if self.frameDone:
            self.frameDone = False
            Domino.difficulty = (Domino.difficulty[0] + 1, Domino.difficulty[1] + 1)
        Domino.generated.clear()
        self.dominos = [Domino() for i in range(10)]
        # set initial positions for dominoes in the set area
        for i, d in enumerate(self.dominos):
            d.x = 50 + i * 120
            d.y = 100
        self.clear_working_area()

    def resetDifficulty(self):
        if Domino.difficulty != (0,0):
            Domino.difficulty = (Domino.difficulty[0] - 1, Domino.difficulty[1] - 1)
            self.new_game()

    def check_win_condition(self):
        """Check if top and bottom sequences match"""
        if not self.working_area_dominos:
            return False
        top_seq, bottom_seq = self.get_concatenated_sequences()
        playerWon = top_seq == bottom_seq and len(top_seq) > 0
        if playerWon:
            self.frameDone = True
        return playerWon
    
    def draw_timer(self):
        """Draw the timer display"""
        timer_font = pygame.font.Font(None, 36)
        bg_color = (0, 100, 0) # Dark green background

        if self.timer_running:
            current_time = self.get_current_time()
            timer_text = f"Timer: {current_time:.2f}s"
            color = (255, 255, 100)  # Yellow for running timer
            
        else:
            if self.last_time > 0:
                timer_text = f"Win time: {self.last_time:.2f}s"
                color = (255, 215, 0)  # Gold for final time
            else:
                timer_text = "Timer: 0.00s"
                color = (150, 255, 150)  # Green for timer not started
        
        text_surface = timer_font.render(timer_text, True, color)
        timer_rect = text_surface.get_rect()
        timer_rect.midtop = (self.screen_width // 2, 25) # center top position   

        # Draw background rectangle for better visibility
        bg_rect = timer_rect.inflate(15, 8)
        pygame.draw.rect(self.screen, bg_color, bg_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), bg_rect, 2) # white border
        self.screen.blit(text_surface, timer_rect)

    def run(self):
        print('Starting game...')

        # Domino Debug
        for d in self.dominos:
            print(f'Domino {self.domino_index}:')
            print(f'Top: {d.top}')
            print(f'Bottom: {d.bottom}\n')
            self.domino_index += 1
        
        # initialize highlights (all valid at start)
        self.update_highlights()
        
        while self.running:
            
            # frame rate timing
            self.delta_time = self.clock.tick(self.fps) / 1000
            self.delta_time = max(0.001, min(0.1, self.delta_time))
            
            # EVENT HANDLER
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_down(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_up(event.pos)
                elif event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_motion(event.pos)
            
            self.screen.fill((0, 135, 0))

            #draw working area background
            pygame.draw.rect(self.screen, (50, 100, 50), (0, self.working_area_y, self.screen_width, self.working_area_height))

            # label for set area
            font = pygame.font.Font(None, 36)
            text = font.render("Domino Set (Click and Drag)", True, (255, 255, 255))
            self.screen.blit(text, (20, 20))
            
            # Draw buttons
            # Clear button
            pygame.draw.rect(self.screen, (200, 50, 50), self.clear_button_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.clear_button_rect, 2)
            button_font = pygame.font.Font(None, 28)
            clear_text = button_font.render("Clear", True, (255, 255, 255))
            text_rect = clear_text.get_rect(center=self.clear_button_rect.center)
            self.screen.blit(clear_text, text_rect)
            
            # New Game button
            pygame.draw.rect(self.screen, (50, 50, 200), self.new_game_button_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.new_game_button_rect, 2)
            new_game_text = button_font.render("New Game", True, (255, 255, 255))
            text_rect = new_game_text.get_rect(center=self.new_game_button_rect.center)
            self.screen.blit(new_game_text, text_rect)

            pygame.draw.rect(self.screen, (190, 140, 35), self.difficulty_button_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.difficulty_button_rect, 2)
            new_game_text2 = button_font.render("Lower Level", True, (255, 255, 255))
            text_rect2 = new_game_text2.get_rect(center=self.difficulty_button_rect.center)
            self.screen.blit(new_game_text2, text_rect2)

            # label for working area
            text = font.render("Working Area (Drop Here)", True, (255, 255, 255))
            self.screen.blit(text, (20, self.working_area_y - 40))
            
            # Draw timer
            self.draw_timer()

            # Update highlights every frame to ensure they're current
            self.update_highlights()
            
            # Draw current sequences if there are dominoes in working area
            if self.working_area_dominos:
                top_seq, bottom_seq = self.get_concatenated_sequences()
                self.draw_sequence_display(top_seq, bottom_seq)
            else:
                # Show instructions when working area is empty
                instruction_font = pygame.font.Font(None, 26)
                inst_text = instruction_font.render("Drag any domino to start! (Yellow border = valid next move)", True, (255, 255, 0))
                self.screen.blit(inst_text, (self.screen_width // 2 - 330, self.working_area_y + 90))
            
            # Check and display win condition
            if self.check_win_condition():
                self.draw_win_message()
            
            for d in self.dominos:
                d.draw(self.screen)
            
            # draw dominoes in working area
            for d in self.working_area_dominos:
                if d != self.dragged_domino:  # don't draw if currently being dragged
                    d.draw(self.screen)
            
            # draw dragged domino on top
            if self.dragged_domino:
                self.dragged_domino.draw(self.screen)

            # Draw dominos
            # for i, d in enumerate(self.dominos):
            #     d.draw(self.screen, 50 + i * 120, 100)
                
            pygame.display.flip()
            
        pygame.quit()
    
    def draw_sequence_display(self, top_seq, bottom_seq):
        """Draw the concatenated sequences as colored squares"""
        square_size = 20
        spacing = 4
        start_x = 50
        # Position sequence display BELOW the working area
        # Working area: y=400 to y=600 (height=200)
        # Place labels below the working area with some padding
        top_y = self.working_area_y + self.working_area_height + 30  # 630
        bottom_y = self.working_area_y + self.working_area_height + 75  # 675
        
        label_font = pygame.font.Font(None, 30)
        
        # Draw top sequence label
        label = label_font.render("Top:", True, (255, 255, 255))
        self.screen.blit(label, (start_x, top_y))
        
        # Draw top sequence colored squares (aligned with label)
        x_offset = start_x + 70  # Space after "Top:" label
        for i, color in enumerate(top_seq):
            x = x_offset + i * (square_size + spacing)
            pygame.draw.rect(self.screen, Domino.colors[color], (x, top_y + 2, square_size, square_size))
            pygame.draw.rect(self.screen, (0, 0, 0), (x, top_y + 2, square_size, square_size), 2)
        
        # Draw bottom sequence label
        label = label_font.render("Bottom:", True, (255, 255, 255))
        self.screen.blit(label, (start_x, bottom_y))
        
        # Draw bottom sequence colored squares (aligned with label)
        x_offset_bottom = start_x + 95  # Space after "Bottom:" label (longer text)
        for i, color in enumerate(bottom_seq):
            x = x_offset_bottom + i * (square_size + spacing)
            pygame.draw.rect(self.screen, Domino.colors[color], (x, bottom_y + 2, square_size, square_size))
            pygame.draw.rect(self.screen, (0, 0, 0), (x, bottom_y + 2, square_size, square_size), 2)
        
        # Draw match indicator
        max_offset = max(x_offset + len(top_seq) * (square_size + spacing), 
                         x_offset_bottom + len(bottom_seq) * (square_size + spacing))
        
        if top_seq == bottom_seq and len(top_seq) > 0:
            match_text = label_font.render("✓ MATCH!", True, (255, 215, 0))
            self.screen.blit(match_text, (max_offset + 30, top_y + 20))
        elif len(top_seq) > 0 and len(bottom_seq) > 0:
            # Show if they're getting close
            match_text = label_font.render("No match yet...", True, (255, 100, 100))
            self.screen.blit(match_text, (max_offset + 30, top_y + 20))
    
    def draw_win_message(self):
        """Draw a win message when sequences match"""
        font = pygame.font.Font(None, 72)
        text = font.render("MATCH! YOU WIN!", True, (255, 215, 0))
        text_rect = text.get_rect(center=(self.screen_width // 2, 300))
        
        # Draw background for text
        bg_rect = text_rect.inflate(40, 20)
        pygame.draw.rect(self.screen, (0, 100, 0), bg_rect)
        pygame.draw.rect(self.screen, (255, 215, 0), bg_rect, 5)
        
        self.screen.blit(text, text_rect)
