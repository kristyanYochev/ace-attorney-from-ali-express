from dataclasses import dataclass

import rendering.commands


@dataclass
class Statement:
    text: str
    character_name: str = None

    def animate(self, render_command_queue: rendering.commands.CommandQueue) -> None:
        self.display_name(render_command_queue)
        render_command_queue.animate_text(self.text)
        render_command_queue.show_text("\n")

    def show(self, render_command_queue: rendering.commands.CommandQueue, highlighted: bool = False) -> None:
        self.display_name(render_command_queue)
        if highlighted:
            render_command_queue.show_colored_text(self.text, "red")
        else:
            render_command_queue.show_text(self.text)
        render_command_queue.show_text("\n")

    def display_name(self, render_command_queue: rendering.commands.CommandQueue):
        if self.character_name != "":
            render_command_queue.show_text("[")
            render_command_queue.show_colored_text(self.character_name, "cyan")
            render_command_queue.show_text("] ")

