# Create template for tube

from CablingGen import SQLite, Logs


def template_tube(parent, name):
    result = SQLite.sel_all_from_sennit_and_tube(parent, name)

    path = result[0][0] + '.spl'
    f = ''
    try:
        f = open(path, 'w')
    except FileNotFoundError:
        Logs.logger.error('File was not opened!')

    try:
        if f:
            try:
                f.write("! Ввести или изменить параметры для катушки. \n")
                f.write("! Вы можете исп. справку в Pro/TABLE \n")
                f.write("! Ввод предопределенных параметров. \n")
                f.write("! Имя Катушки \n")
                f.write("NAME	" + result[0][0] + '\n')
                f.write("! Тип катушки \n")
                f.write("TYPE	" + result[0][1] + '\n')
                f.write("! Тип оболочки \n")
                f.write("SHEATH_TYPE	" + result[0][2] + '\n')
                f.write("! Толщина стены \n")
                f.write("WALL_THICKNESS	" + result[0][3] + '\n')
                f.write("! Мин. Радиус Изгиба \n")
                f.write("MIN_BEND_RADIUS	" + result[0][4] + '\n')
                f.write("! Единицы измерения \n")
                f.write("UNITS	" + result[0][5] + '\n')
                f.write("! Внутренний диаметр до усадки \n")
                f.write("PRESHRINK_INNER_DIAMETER	" + result[0][6] + '\n')
                f.write("! Наружный диаметр \n")
                f.write("OUTER_DIAMETER	" + result[0][7] + '\n')
                f.write("! Цвет \n")
                f.write("COLOR	" + result[0][10] + '\n')
                f.write("! Плотность Провода \n")
                f.write("DENSITY	" + result[0][9] + '\n')
                f.write("! Единицы измерения массы \n")
                f.write("MASS_UNITS	" + result[0][8] + '\n')
                f.write("НАИМЕНОВАНИЕ	" + '"' + result[0][12] + '"' + '\n')
                f.write("ОБОЗНАЧЕНИЕ	" + result[0][13] + '\n')

            except ValueError:
                Logs.logger.error('Error writing to file!')

        f.close()

    except NameError:
        Logs.logger.error('Variable was not found!')
