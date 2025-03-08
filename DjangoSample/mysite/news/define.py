#define default value
APP_VALUE_LAYOUT_DEFAULT = 'list'
APP_VALUE_STATUS_DEFAULT = 'list'

TABLE_CATEGORY_SHOW = 'Category'
TABLE_ARTICLE_SHOW = 'Article'
TABLE_FEED_SHOW = 'Feed'

APP_VALUE_LAYOUT_CHOICE = (
        ('list', 'List'),
        ('grid', 'Grid')
    )
APP_VALUE_STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

ADMIN_SRC_JS = ('my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js', 'my_admin/js/general.js')
ADMIN_SRC_CSS = {'all' : ('my_admin/css/custom.css', ) }
ADMIN_HEADER_NAME = 'LUONGTD Admin'