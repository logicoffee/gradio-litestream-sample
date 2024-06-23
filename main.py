import gradio as gr

from src import sqlite

with gr.Blocks() as demo:
    # [
    #     {"id": 1, "title": "Install Litestream", "status": "done"},
    #     {"id": 2, "title": "Create database", "status": "todo"},
    # ]
    todo = gr.State([])

    new_todo = gr.Textbox(label="New todo")
    button = gr.Button("create")

    @button.click(inputs=[todo, new_todo], outputs=[todo, new_todo])
    def add_new_todo(todo_list, new_todo):
        new_id = sqlite.add_todo(new_todo)
        return [*todo_list, {"id": new_id, "title": new_todo, "status": "todo"}], ""

    @gr.render(inputs=todo)
    def render_todo_list(todo_list):
        for t in todo_list:
            with gr.Row():
                gr.Textbox(t["title"], show_label=False, container=False)
                gr.Textbox(t["status"], show_label=False, container=False)
                btn = gr.Button("DONE")

                @btn.click(inputs=None, outputs=[todo])
                def get_todo_done(t=t):
                    sqlite.finish_todo(t["id"])
                    t["status"] = "done"
                    return [t if t_["id"] == t["id"] else t_ for t_ in todo_list]

    reset_btn = gr.Button("Delete all")

    @reset_btn.click(inputs=None, outputs=[todo])
    def delete_all_todos():
        sqlite.delete_all_todos()
        return []

    demo.load(sqlite.get_all_todos, inputs=None, outputs=todo)

demo.launch(server_name="0.0.0.0")
