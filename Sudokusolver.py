import tkinter as tk
from tkinter import messagebox

class SudokuSolverUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 Sudoku Solver")
        self.entries = []

        self.build_grid()
        self.add_buttons()

    def build_grid(self):
        for i in range(9):
            row_entries = []
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.config(bg="#edf2f4")
                row_entries.append(entry)
            self.entries.append(row_entries)

    def add_buttons(self):
        solve_btn = tk.Button(self.root, text="Solve", command=self.solve_puzzle, bg="#2b9348", fg="white", font=("Arial", 12, "bold"))
        solve_btn.grid(row=9, column=0, columnspan=4, pady=10)

        clear_btn = tk.Button(self.root, text="Clear", command=self.clear_grid, bg="#ef233c", fg="white", font=("Arial", 12, "bold"))
        clear_btn.grid(row=9, column=5, columnspan=4, pady=10)

    def get_grid(self):
        grid = []
        for row in self.entries:
            current_row = []
            for cell in row:
                val = cell.get()
                if val.isdigit() and 1 <= int(val) <= 9:
                    current_row.append(int(val))
                else:
                    current_row.append(0)
            grid.append(current_row)
        return grid

    def set_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(grid[i][j]))

    def solve_puzzle(self):
        grid = self.get_grid()
        if self.solve(grid):
            self.set_grid(grid)
        else:
            messagebox.showerror("No Solution", "This Sudoku puzzle cannot be solved.")

    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.valid(board, num, (row, col)):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = 0
        return False

    def valid(self, board, num, pos):
        row, col = pos
        # Row
        if num in board[row]:
            return False
        # Column
        if num in [board[i][col] for i in range(9)]:
            return False
        # Box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if board[i][j] == num:
                    return False
        return True

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def clear_grid(self):
        for row in self.entries:
            for cell in row:
                cell.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverUI(root)
    root.mainloop()
