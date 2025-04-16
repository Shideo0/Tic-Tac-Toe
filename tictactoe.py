import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        self.master.geometry("400x500")
        self.master.resizable(False, False)
        self.master.configure(bg='#f0f0f0')

        # Настройки игры
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Заголовок с текущим игроком
        self.header = tk.Label(
            self.master,
            text=f"Сейчас ходит: {self.current_player}",
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        self.header.pack(pady=20)

        # Игровое поле
        self.game_frame = tk.Frame(self.master, bg='#f0f0f0')
        self.game_frame.pack()

        self.buttons = []
        for i in range(9):
            button = tk.Button(
                self.game_frame,
                text="",
                width=6,
                height=3,
                font=('Arial', 24, 'bold'),
                bg='#ffffff',
                fg='#333333',
                relief='groove',
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        # Кнопка сброса
        self.reset_btn = tk.Button(
            self.master,
            text="Новая игра",
            font=('Arial', 12),
            bg='#4CAF50',
            fg='white',
            padx=20,
            pady=5,
            command=self.reset_game
        )
        self.reset_btn.pack(pady=20)

    def make_move(self, index):
        if not self.game_active:
            messagebox.showwarning("Игра завершена", "Начните новую игру!")
            return

        if self.board[index] != "":
            return

        # Делаем ход
        self.board[index] = self.current_player
        color = '#ff4444' if self.current_player == "X" else '#4444ff'
        self.buttons[index].config(text=self.current_player, fg=color, state='disabled')

        # Проверяем результат
        if self.check_winner():
            self.highlight_win()
            self.game_active = False
            messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
        elif "" not in self.board:
            self.game_active = False
            messagebox.showinfo("Ничья", "Игра завершена вничью!")
        else:
            # Передаем ход другому игроку
            self.current_player = "O" if self.current_player == "X" else "X"
            self.header.config(text=f"Сейчас ходит: {self.current_player}")

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
            [0, 4, 8], [2, 4, 6]  # Диагонали
        ]

        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] ==
                    self.board[condition[2]] != ""):
                return True
        return False

    def highlight_win(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] ==
                    self.board[condition[2]] != ""):
                for i in condition:
                    self.buttons[i].config(bg='#a0ffa0')  # Подсветка зеленым
                return

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.game_active = True
        self.header.config(text=f"Сейчас ходит: {self.current_player}")

        for button in self.buttons:
            button.config(text="", state='normal', bg='#ffffff', fg='#333333')


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()