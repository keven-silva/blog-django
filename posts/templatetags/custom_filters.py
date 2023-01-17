from django import template


register = template.Library()


@register.filter(name='plural_comments')
def plural_comments(num_commments):
    try:
        num_commments = int(num_commments)

        if num_commments == 0:
            return 'Nenhum comentário'

        elif num_commments == 1:
            return f'{num_commments} comentário'

        else:
            return f'{num_commments} comentários(s)'

    except Exception as e:
        return f'Error: {e}'
