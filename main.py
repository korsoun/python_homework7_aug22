# Файл для запуска всего проекта.

import database_operations as db
import control as cntr

# cont_intention = True
cont_intention = True
while cont_intention != False:
    request = cntr.get_request()
    cntr.controller(request)

    cont_intention = cntr.wanna_continue()


