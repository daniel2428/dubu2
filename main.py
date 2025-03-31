import flet as ft

 

from db import main_db
 

from datetime import datetime
 


 

def main(page: ft.Page):
 

    page.title = 'Task Manager'
 

    page.padding = 75
 

    page.bgcolor = ft.Colors.DEEP_ORANGE_ACCENT
 

    page.theme_mode = ft.ThemeMode.DARK
 


 

    task_list = ft.Column(spacing=10)
 


 

    def load_tasks():
 

        task_list.controls.clear()
 

        for task_id, task_text, created_at in main_db.get_tasks():
 

            task_list.controls.append(create_task_row(task_id, task_text, created_at))
 

        page.update()
 


 

    def create_task_row(task_id, task_text, created_at):
 

        task_field = ft.TextField(value=task_text, expand=True, dense=True, read_only=True)
 

        timestamp = ft.Text(created_at, color=ft.Colors.BLACK, size=12)
 


 


 

        def enable_edit(e):
 

            task_field.read_only = False
 

            page.update()
 


 

        def save_edit(e):
 

            main_db.update_task_db(task_id, task_field.value)
 

            task_field.read_only = True
 

            page.update()
 


 

        return ft.Row([
 

            task_field, 
 

            timestamp,
 

            ft.IconButton(ft.Icons.DELETE, icon_color=ft.Colors.RED_500, on_click=lambda e: delete_task(task_id)),
 

            ft.IconButton(ft.Icons.EDIT, icon_color=ft.Colors.YELLOW_300, on_click=enable_edit),
 

            ft.IconButton(ft.Icons.SAVE, icon_color=ft.Colors.GREEN_500, on_click=save_edit)
 

        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
 

        
 


 

    def add_task(e):
 

        if task_input.value.strip():
 

            task_id = main_db.add_task_db(task_input.value)
 

            created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 

            task_list.controls.append(create_task_row(task_id, task_input.value, created_at))
 

            task_input.value = ''
 

            page.update()
 


 


 

    def delete_task(task_id):
 

        main_db.delete_task_db(task_id)
 

        load_tasks()
 

        
 


 


 

    task_input = ft.TextField(label='Add your task', dense=True, expand=True, on_submit=add_task)
 

    add_button = ft.ElevatedButton('Add', on_click=add_task, icon=ft.icons.ADD)
 


 

    page.add(
 

        ft.Column([
 

            ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
 

            task_list
 

        ])
 

    )
 


 

    load_tasks()
 


 

if __name__ == '__main__':
 

    main_db.init_db()
 

    ft.app(target=main)