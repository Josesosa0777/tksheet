from __future__ import annotations

from .other_classes import (
    DotDict,
    FontTuple,
)
from .themes import (
    theme_light_blue,
)
from .vars import (
    USER_OS,
    ctrl_key,
)


def new_sheet_options() -> DotDict:
    return DotDict(
        {
            "popup_menu_font": FontTuple(
                "Calibri",
                13 if USER_OS == "darwin" else 11,
                "normal",
            ),
            "table_font": FontTuple(
                "Calibri",
                13 if USER_OS == "darwin" else 11,
                "normal",
            ),
            "header_font": FontTuple(
                "Calibri",
                13 if USER_OS == "darwin" else 11,
                "normal",
            ),
            "index_font": FontTuple(
                "Calibri",
                13 if USER_OS == "darwin" else 11,
                "normal",
            ),
            "edit_header_label": "Edit header",
            "edit_header_accelerator": "",
            "edit_index_label": "Edit index",
            "edit_index_accelerator": "",
            "edit_cell_label": "Edit cell",
            "edit_cell_accelerator": "",
            "cut_label": "Cut",
            "cut_accelerator": "Ctrl+X",
            "cut_contents_label": "Cut contents",
            "cut_contents_accelerator": "Ctrl+X",
            "copy_label": "Copy",
            "copy_accelerator": "Ctrl+C",
            "copy_contents_label": "Copy contents",
            "copy_contents_accelerator": "Ctrl+C",
            "paste_label": "Paste",
            "paste_accelerator": "Ctrl+V",
            "delete_label": "Delete",
            "delete_accelerator": "Del",
            "clear_contents_label": "Clear contents",
            "clear_contents_accelerator": "Del",
            "delete_columns_label": "Delete columns",
            "delete_columns_accelerator": "",
            "insert_columns_left_label": "Insert columns left",
            "insert_columns_left_accelerator": "",
            "insert_column_label": "Insert column",
            "insert_column_accelerator": "",
            "insert_columns_right_label": "Insert columns right",
            "insert_columns_right_accelerator": "",
            "delete_rows_label": "Delete rows",
            "delete_rows_accelerator": "",
            "insert_rows_above_label": "Insert rows above",
            "insert_rows_above_accelerator": "",
            "insert_rows_below_label": "Insert rows below",
            "insert_rows_below_accelerator": "",
            "insert_row_label": "Insert row",
            "insert_row_accelerator": "",
            "select_all_label": "Select all",
            "select_all_accelerator": "Ctrl+A",
            "undo_label": "Undo",
            "undo_accelerator": "Ctrl+Z",
            "copy_bindings": [
                f"<{ctrl_key}-c>",
                f"<{ctrl_key}-C>",
            ],
            "cut_bindings": [
                f"<{ctrl_key}-x>",
                f"<{ctrl_key}-X>",
            ],
            "paste_bindings": [
                f"<{ctrl_key}-v>",
                f"<{ctrl_key}-V>",
            ],
            "undo_bindings": [
                f"<{ctrl_key}-z>",
                f"<{ctrl_key}-Z>",
            ],
            "redo_bindings": [
                f"<{ctrl_key}-Shift-z>",
                f"<{ctrl_key}-Shift-Z>",
            ],
            "delete_bindings": [
                "<Delete>",
                "<Delete>",
            ],
            "select_all_bindings": [
                f"<{ctrl_key}-a>",
                f"<{ctrl_key}-A>",
            ],
            "tab_bindings": [
                "<Tab>",
            ],
            "up_bindings": [
                "<Up>",
            ],
            "right_bindings": [
                "<Right>",
            ],
            "down_bindings": [
                "<Down>",
            ],
            "left_bindings": [
                "<Left>",
            ],
            "prior_bindings": [
                "<Prior>",
            ],
            "next_bindings": [
                "<Next>",
            ],
            "popup_menu_fg": theme_light_blue["popup_menu_fg"],
            "popup_menu_bg": theme_light_blue["popup_menu_bg"],
            "popup_menu_highlight_bg": theme_light_blue["popup_menu_highlight_bg"],
            "popup_menu_highlight_fg": theme_light_blue["popup_menu_highlight_fg"],
            "index_hidden_rows_expander_bg": theme_light_blue["index_hidden_rows_expander_bg"],
            "header_hidden_columns_expander_bg": theme_light_blue["header_hidden_columns_expander_bg"],
            "header_bg": theme_light_blue["header_bg"],
            "header_border_fg": theme_light_blue["header_border_fg"],
            "header_grid_fg": theme_light_blue["header_grid_fg"],
            "header_fg": theme_light_blue["header_fg"],
            "header_selected_cells_bg": theme_light_blue["header_selected_cells_bg"],
            "header_selected_cells_fg": theme_light_blue["header_selected_cells_fg"],
            "index_bg": theme_light_blue["index_bg"],
            "index_border_fg": theme_light_blue["index_border_fg"],
            "index_grid_fg": theme_light_blue["index_grid_fg"],
            "index_fg": theme_light_blue["index_fg"],
            "index_selected_cells_bg": theme_light_blue["index_selected_cells_bg"],
            "index_selected_cells_fg": theme_light_blue["index_selected_cells_fg"],
            "top_left_bg": theme_light_blue["top_left_bg"],
            "top_left_fg": theme_light_blue["top_left_fg"],
            "top_left_fg_highlight": theme_light_blue["top_left_fg_highlight"],
            "table_bg": theme_light_blue["table_bg"],
            "table_grid_fg": theme_light_blue["table_grid_fg"],
            "table_fg": theme_light_blue["table_fg"],
            "tree_arrow_fg": theme_light_blue["tree_arrow_fg"],
            "selected_cells_tree_arrow_fg": theme_light_blue["selected_cells_tree_arrow_fg"],
            "selected_rows_tree_arrow_fg": theme_light_blue["selected_rows_tree_arrow_fg"],
            "table_selected_box_cells_fg": theme_light_blue["table_selected_box_cells_fg"],
            "table_selected_box_rows_fg": theme_light_blue["table_selected_box_rows_fg"],
            "table_selected_box_columns_fg": theme_light_blue["table_selected_box_columns_fg"],
            "table_selected_cells_border_fg": theme_light_blue["table_selected_cells_border_fg"],
            "table_selected_cells_bg": theme_light_blue["table_selected_cells_bg"],
            "table_selected_cells_fg": theme_light_blue["table_selected_cells_fg"],
            "resizing_line_fg": theme_light_blue["resizing_line_fg"],
            "drag_and_drop_bg": theme_light_blue["drag_and_drop_bg"],
            "outline_color": theme_light_blue["outline_color"],
            "header_selected_columns_bg": theme_light_blue["header_selected_columns_bg"],
            "header_selected_columns_fg": theme_light_blue["header_selected_columns_fg"],
            "index_selected_rows_bg": theme_light_blue["index_selected_rows_bg"],
            "index_selected_rows_fg": theme_light_blue["index_selected_rows_fg"],
            "table_selected_rows_border_fg": theme_light_blue["table_selected_rows_border_fg"],
            "table_selected_rows_bg": theme_light_blue["table_selected_rows_bg"],
            "table_selected_rows_fg": theme_light_blue["table_selected_rows_fg"],
            "table_selected_columns_border_fg": theme_light_blue["table_selected_columns_border_fg"],
            "table_selected_columns_bg": theme_light_blue["table_selected_columns_bg"],
            "table_selected_columns_fg": theme_light_blue["table_selected_columns_fg"],
            "vertical_scroll_background": theme_light_blue["vertical_scroll_background"],
            "horizontal_scroll_background": theme_light_blue["horizontal_scroll_background"],
            "vertical_scroll_troughcolor": theme_light_blue["vertical_scroll_troughcolor"],
            "horizontal_scroll_troughcolor": theme_light_blue["horizontal_scroll_troughcolor"],
            "vertical_scroll_lightcolor": theme_light_blue["vertical_scroll_lightcolor"],
            "horizontal_scroll_lightcolor": theme_light_blue["horizontal_scroll_lightcolor"],
            "vertical_scroll_darkcolor": theme_light_blue["vertical_scroll_darkcolor"],
            "horizontal_scroll_darkcolor": theme_light_blue["horizontal_scroll_darkcolor"],
            "vertical_scroll_relief": theme_light_blue["vertical_scroll_relief"],
            "horizontal_scroll_relief": theme_light_blue["horizontal_scroll_relief"],
            "vertical_scroll_troughrelief": theme_light_blue["vertical_scroll_troughrelief"],
            "horizontal_scroll_troughrelief": theme_light_blue["horizontal_scroll_troughrelief"],
            "vertical_scroll_bordercolor": theme_light_blue["vertical_scroll_bordercolor"],
            "horizontal_scroll_bordercolor": theme_light_blue["horizontal_scroll_bordercolor"],
            "vertical_scroll_active_bg": theme_light_blue["vertical_scroll_active_bg"],
            "horizontal_scroll_active_bg": theme_light_blue["horizontal_scroll_active_bg"],
            "vertical_scroll_not_active_bg": theme_light_blue["vertical_scroll_not_active_bg"],
            "horizontal_scroll_not_active_bg": theme_light_blue["horizontal_scroll_not_active_bg"],
            "vertical_scroll_pressed_bg": theme_light_blue["vertical_scroll_pressed_bg"],
            "horizontal_scroll_pressed_bg": theme_light_blue["horizontal_scroll_pressed_bg"],
            "vertical_scroll_active_fg": theme_light_blue["vertical_scroll_active_fg"],
            "horizontal_scroll_active_fg": theme_light_blue["horizontal_scroll_active_fg"],
            "vertical_scroll_not_active_fg": theme_light_blue["vertical_scroll_not_active_fg"],
            "horizontal_scroll_not_active_fg": theme_light_blue["horizontal_scroll_not_active_fg"],
            "vertical_scroll_pressed_fg": theme_light_blue["vertical_scroll_pressed_fg"],
            "horizontal_scroll_pressed_fg": theme_light_blue["horizontal_scroll_pressed_fg"],
            "vertical_scroll_borderwidth": 1,
            "horizontal_scroll_borderwidth": 1,
            "vertical_scroll_gripcount": 0,
            "horizontal_scroll_gripcount": 0,
            "vertical_scroll_arrowsize": "",
            "horizontal_scroll_arrowsize": "",
            "set_cell_sizes_on_zoom": False,
            "auto_resize_columns": None,
            "auto_resize_rows": None,
            "to_clipboard_delimiter": "\t",
            "to_clipboard_quotechar": '"',
            "to_clipboard_lineterminator": "\n",
            "from_clipboard_delimiters": ["\t"],
            "show_dropdown_borders": False,
            "show_default_header_for_empty": True,
            "show_default_index_for_empty": True,
            "default_header_height": "1",
            "default_row_height": "1",
            "default_column_width": 120,
            "default_row_index_width": 70,
            "default_row_index": "numbers",
            "default_header": "letters",
            "page_up_down_select_row": True,
            "paste_can_expand_x": False,
            "paste_can_expand_y": False,
            "paste_insert_column_limit": None,
            "paste_insert_row_limit": None,
            "arrow_key_down_right_scroll_page": False,
            "cell_auto_resize_enabled": True,
            "auto_resize_row_index": True,
            "max_undos": 30,
            "column_drag_and_drop_perform": True,
            "row_drag_and_drop_perform": True,
            "empty_horizontal": 50,
            "empty_vertical": 50,
            "selected_rows_to_end_of_window": False,
            "horizontal_grid_to_end_of_window": False,
            "vertical_grid_to_end_of_window": False,
            "show_vertical_grid": True,
            "show_horizontal_grid": True,
            "display_selected_fg_over_highlights": False,
            "show_selected_cells_border": True,
            "treeview": False,
            "treeview_indent": "6",
            "rounded_boxes": True,
            "alternate_color": "",
        }
    )
