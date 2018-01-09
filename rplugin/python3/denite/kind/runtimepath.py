
from .directory import Kind as Directory


class Kind(Directory):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'runtimepath'
        self.redraw_actions += ['delete']
        self.persist_actions += ['delete']

    def action_delete(self, context):
        for target in context['targets']:
            self.vim.command(
                'set runtimepath-={}'.format(target['action__path'])
            )
