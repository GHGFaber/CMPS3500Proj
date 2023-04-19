from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static

class TimeDisplay(Static):
    """A widget to display elapsed time."""

class Stopwatch(Static):
    """A stopwatch widget."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")

class MainMenu(Static):
    """ Create child widgets for Main Menu."""

    # def on_button_pressed(self, event: Button.Pressed) -> None:
    #     """Event handler called when a button is pressed."""
    #     if event.button.id == "start":
    #         self.add_class("started")
    #     elif event.button.id == "stop":
    #         self.remove_class("started")

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("Load Data", id="load_data")
        yield Button("Explore Data", id="explore_data")
        yield Button("Data Analysis", id="data_analysis")
        yield Button("Print Data", id="print_data")
        yield Button("Quit", id="quit")



class CriminalysisApp(App):
    """A Textual app that analyzes crime data in extremely inefficient ways."""

    CSS_PATH = "criminalysis.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield MainMenu()
        #yield Container(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = CriminalysisApp()
    app.run()

# import pandas as pd
# import textual.widget as tw

# # Define a function to read in the CSV file and return a pandas dataframe
# def read_csv():
#     df = pd.read_csv('data.csv')
#     return df

# # Define a function to display the dataframe in a DataTable widget
# def display_df(df):
#     table = tw.DataTable(df)
#     table.show()

# # Define the GUI layout
# layout = tw.Grid(
#     rows=2,
#     columns=1,
#     template=[
#         ["read_csv_button"],
#         ["output"]
#     ]
# )

# # Create the GUI widgets
# read_csv_button = tw.Button("Read CSV")
# output = tw.Output()

# # Define the button click event
# def read_csv_button_click():
#     with output:
#         df = read_csv()
#         display_df(df)

# # Attach the button click event to the button
# read_csv_button.on_click(read_csv_button_click)

# # Add the widgets to the layout
# layout.read_csv_button = read_csv_button
# layout.output = output

# # Show the GUI
# layout.show()