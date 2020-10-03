import sqlite3

conn = sqlite3.connect('./SQLite/material.db')

cursor = conn.cursor()


# Create table material
def create_table_material():
    cursor.execute("""create table material
                (id integer not null primary key,
                element text,
                parent text,
                child_index integer)""")

    material = [('Coil', '', 0),
                ('Shell', 'Coil', 0),
                ('Sennit', 'Shell', 0),
                ('TU 16.K18-093-2007', 'Sennit', 0),
                ('TU4833-002-08558606-95', 'Sennit', 1),
                ('Tube', 'Shell', 1),
                ('GOST 19034-82', 'Tube', 0),
                ('Conductor', 'Coil', 1),
                ('Cable', 'Conductor', 0),
                ('Wire', 'Conductor', 1),
                ('GOST 6323-79', 'Wire', 0),
                ('TU 16-505.945-76', 'Wire', 1)]

    cursor.executemany("""insert into material 
                        (element, parent, child_index)
                        values (?, ?, ?)""", material)


# Create table for sennit and tube
def create_table_sennit_and_tube():
    cursor.execute("""create table sennit_and_tube
                    (coil_name text not null,
                    coil_type text not null,
                    shell_type text not null,
                    wall_thickness text not null,
                    min_bending_radius text not null,
                    unit text not null,
                    diameter_in text not null,
                    diameter_out text not null,
                    mass_unit text not null,
                    wire_density text not null,
                    color text not null,
                    standard text not null,
                    name text not null,
                    designation text not null,
                    parent text not null)""")

    material = [('PLETENKA_PML_2X4UZ_T16K18093', 'SHEATH', 'SHRINK', '0.22', '4', 'MM', '2x4', '4.44', 'KILOGRAM',
                 '7.2e-06', 'Серый', 'ТУ16.К18-093-2007', 'Плетенка ПМЛ 2х4 УЗ ТУ16.К18-093-2007',
                 'pletenka_pml_2x4uz_t16k18093', 'sennit'),
                ('PLETENKA_PML_3X6UZ_T16K18093', 'SHEATH', 'SHRINK', '0.28', '5', 'MM', '3x6', '6.56', 'KILOGRAM',
                 '1.7e-05', 'Серый', 'ТУ16.К18-093-2007', 'Плетенка ПМЛ 3х6 УЗ ТУ16.К18-093-2007',
                 'pletenka_pml_3x6uz_t16k18093', 'sennit'),
                ('PLETENKA_PML_4X5UZ_T16K18093', 'SHEATH', 'SHRINK', '0.22', '4', 'MM', '4x5', '5.44', 'KILOGRAM',
                 '8.8e-06', 'Серый', 'ТУ16.К18-093-2007', 'Плетенка ПМЛ 4х5 УЗ ТУ16.К18-093-2007',
                 'pletenka_pml_4x5uz_t16k18093', 'sennit'),
                ('PLETENKA_PML_6X10UZ_T16K18093', 'SHEATH', 'SHRINK', '0.28', '5', 'MM', '6x10', '10.56', 'KILOGRAM',
                 '3.4e-05', 'Серый', 'ТУ16.К18-093-2007', 'Плетенка ПМЛ 6х10 УЗ ТУ16.К18-093-2007',
                 'pletenka_pml_6x10uz_t16k18093', 'sennit'),
                ('PLETENKA_PML_10X16UZ_T16K18093', 'SHEATH', 'SHRINK', '0.38', '6', 'MM', '10x16', '16.76', 'KILOGRAM',
                 '5.8e-05', 'Серый', 'ТУ16.К18-093-2007', 'Плетенка ПМЛ 10х16 УЗ ТУ16.К18-093-2007',
                 'pletenka_pml_10x16uz_t16k18093', 'sennit'),
                ('PLETENKA_PML_16X24UZ_T16K18093', 'SHEATH', 'SHRINK', '0.58', '10', 'MM', '16x24', '25.16', 'KILOGRAM',
                 '0.000125', 'Серый', 'ТУ16.К18-093-2007', 'Плетенка ПМЛ 16х24 УЗ ТУ16.К18-093-2007',
                 'pletenka_pml_16x24uz_t16k18093', 'sennit'),
                ('PLETENKA_PML_2X4UZ_TU4833', 'SHEATH', 'SHRINK', '0.24', '4', 'MM', '2x4', '4.48', 'KILOGRAM',
                 '7.2e-06', 'Серый', 'ТУ 4833-002-08558606-95', 'Плетенка ПМЛ 2х4 УЗ ТУ 4833-002-08558606-95',
                 'PLETENKA_PML_2X4uz_tu4833', 'sennit'),
                ('PLETENKA_PML_3X6UZ_TU4833', 'SHEATH', 'SHRINK', '0.3', '4', 'MM', '3x6', '6.6', 'KILOGRAM',
                 '1.7e-05', 'Серый', 'ТУ 4833-002-08558606-95', 'Плетенка ПМЛ 3х6 УЗ ТУ 4833-002-08558606-95',
                 'PLETENKA_PML_3X6uz_tu4833', 'sennit'),
                ('PLETENKA_PML_4X5UZ_TU4833', 'SHEATH', 'SHRINK', '0.24', '4', 'MM', '4x5', '5.48', 'KILOGRAM',
                 '8.8e-06', 'Серый', 'ТУ 4833-002-08558606-95', 'Плетенка ПМЛ 4х5 УЗ ТУ 4833-002-08558606-95',
                 'PLETENKA_PML_4X5uz_tu4833', 'sennit'),
                ('PLETENKA_PML_6X10UZ_TU4833', 'SHEATH', 'SHRINK', '0.3', '4', 'MM', '6x10', '10.6', 'KILOGRAM',
                 '3.4e-05', 'Серый', 'ТУ 4833-002-08558606-95', 'Плетенка ПМЛ 6х10 УЗ ТУ 4833-002-08558606-95',
                 'PLETENKA_PML_6X10uz_tu4833', 'sennit'),
                ('PLETENKA_PML_10X16UZ_TU4833', 'SHEATH', 'SHRINK', '0.4', '5', 'MM', '10x16', '16.8', 'KILOGRAM',
                 '5.8e-05', 'Серый', 'ТУ 4833-002-08558606-95', 'Плетенка ПМЛ 10х16 УЗ ТУ 4833-002-08558606-95',
                 'PLETENKA_PML_10X16uz_tu4833', 'sennit'),
                ('PLETENKA_PML_16X24UZ_TU4833', 'SHEATH', 'SHRINK', '0.6', '5', 'MM', '16x24', '25.2', 'KILOGRAM',
                 '0.000125', 'Серый', 'ТУ 4833-002-08558606-95', 'Плетенка ПМЛ 16х24 УЗ ТУ 4833-002-08558606-95',
                 'PLETENKA_PML_16X24uz_tu4833', 'sennit'),
                ('PLETENKA_PML_24X30UZ_TU4833', 'SHEATH', 'SHRINK', '0.6', '5', 'MM', '24x30', '31.2', 'KILOGRAM',
                 '0.000145', 'Серый', 'ТУ 4833-002-08558606-95', 'Плетенка ПМЛ 24х30 УЗ ТУ 4833-002-08558606-95',
                 'PLETENKA_PML_24X30uz_tu4833', 'sennit'),
                ('PLETENKA_PML_30X40UZ_TU4833', 'SHEATH', 'SHRINK', '0.6', '5', 'MM', '30x40', '41.2', 'KILOGRAM',
                 '0.00019', 'Серый', 'ТУ 4833-002-08558606-95', 'Плетенка ПМЛ 30х40 УЗ ТУ 4833-002-08558606-95',
                 'PLETENKA_PML_30X40uz_tu4833', 'sennit'),
                ('PLETENKA_PML_40X55UZ_TU4833', 'SHEATH', 'SHRINK', '0.6', '5', 'MM', '40x55', '56.2', 'KILOGRAM',
                 '0.00026', 'Серый', 'ТУ 4833-002-08558606-95', 'Плетенка ПМЛ 40х55 УЗ ТУ 4833-002-08558606-95',
                 'PLETENKA_PML_40X55uz_tu4833', 'sennit'),
                ('TRUBKA_305_TV-40T_0-75_WHTV', 'SHEATH', 'TUBE', '0.3', '5', 'MM', '0.75', '1.35', 'GRAM', '0.00127',
                 'Белый', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 0,75, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_0-75_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_1_WHTV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '1', '1.8', 'GRAM', '0.00226', 'Белый',
                 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 1, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_1_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_1-5_WHTV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '1.5', '2.3', 'GRAM', '0.00306',
                 'Белый', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 1,5, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_1-5_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_1-75_WHTV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '1.75', '2.55', 'GRAM', '0.00347',
                 'Белый', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 1,75, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_1-75_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_2_WHTV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '2', '2.8', 'GRAM', '0.00387', 'Белый',
                 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 2, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_2_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_2-5_WHTV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '2.5', '3.3', 'GRAM', '0.00468',
                 'Белый', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 2,5, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_2-5_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_3_WHTV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '3', '3.8', 'GRAM', '0.00548', 'Белый',
                 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 3, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_3_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_3-5_WHTV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '3.5', '4.3', 'GRAM', '0.00629',
                 'Белый', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 3,5, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_3-5_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_4_WHTV', 'SHEATH', 'TUBE', '0.6', '7', 'MM', '4', '5.2', 'GRAM', '0.01112', 'Белый',
                 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 4, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_4_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_4-5_WHTV', 'SHEATH', 'TUBE', '0.6', '7', 'MM', '4.5', '5.7', 'GRAM', '0.01233',
                 'Белый', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 4,5, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_4-5_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_5_WHTV', 'SHEATH', 'TUBE', '0.6', '7', 'MM', '5', '6.2', 'GRAM', '0.01354', 'Белый',
                 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 5, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_5_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_6_WHTV', 'SHEATH', 'TUBE', '0.6', '7', 'MM', '6', '7.2', 'GRAM', '0.01596', 'Белый',
                 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 6, белая, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_6_WHTV', 'tube'),
                ('TRUBKA_305_TV-40T_0-5_BLKV', 'SHEATH', 'TUBE', '0.3', '5', 'MM', '0.5', '1.1', 'GRAM', '0.00097',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 0,5, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_0-5_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_0-75_BLKV', 'SHEATH', 'TUBE', '0.3', '5', 'MM', '0.75', '1.35', 'GRAM', '0.00127',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 0,75, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_0-75_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_1_BLKV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '1', '1.8', 'GRAM', '0.00226',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 1, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_1_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_1-5_BLKV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '1.5', '2.3', 'GRAM', '0.00306',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 1,5, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_1-5_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_1-75_BLKV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '1.75', '2.55', 'GRAM', '0.00347',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 1,75, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_1-75_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_2_BLKV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '2', '2.8', 'GRAM', '0.00387',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 2, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_2_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_2-5_BLKV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '2.5', '3.3', 'GRAM', '0.00468',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 2,5, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_2-5_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_3_BLKV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '3', '3.8', 'GRAM', '0.00548',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 3, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_3_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_3-5_BLKV', 'SHEATH', 'TUBE', '0.4', '5', 'MM', '3.5', '4.3', 'GRAM', '0.00629',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 3,5, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_3-5_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_4_BLKV', 'SHEATH', 'TUBE', '0.6', '7', 'MM', '4', '5.2', 'GRAM', '0.01112',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 4, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_4_BLKV', 'tube'),
                ('TRUBKA_305_TV-40T_4-5_BLKV', 'SHEATH', 'TUBE', '0.6', '7', 'MM', '4.5', '5.7', 'GRAM', '0.01233',
                 'Черный', 'ГОСТ 19034-82', 'Трубка 305 ТВ-40Т, 4,5, черная, высшего сорта ГОСТ 19034-82',
                 'TRUBKA_305_TV-40T_4-5_BLKV', 'tube')]

    cursor.executemany("""insert into sennit_and_tube
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", material)


def create_table_wire():
    cursor.execute("""create table wire 
                    (coil_name text not null,
                    coil_type text not null,
                    min_bending_radius text not null,
                    wire_thickness text not null,
                    unit text not null,
                    color text not null,
                    wire_density text not null,
                    mass_unit text not null,
                    brand text not null,
                    name text not null,
                    designation text not null,
                    section text not null,
                    standard text not null,
                    parent text not null)""")

    material = [('PROVOD_APV_2', 'WIRE', '11.1', '3.7', 'MM', 'Черный', '1.35e-05', 'GRAM', 'АПВ',
                 'Провод АПВ 2 ГОСТ 6323-79', 'Provod_APV_2', '2', 'ГОСТ 6323-79', 'wire'),
                ('PROVOD_BIF_1X0_2_BR', 'WIRE', '3.84', '1.28', 'MM', 'Коричневый', '3.9e-06', 'KILOGRAM', 'БИФ',
                 'Провод БИФ 1x0.2 бр ТУ 16-505.945-76', 'Provod_BIF_1x0_2_br', '1x0.2 бр', 'ТУ 16-505.945-76', 'wire')]

    cursor.executemany("""insert into wire
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", material)


# Outputs everything from the material table
def sel_from_material():
    cursor.execute("""select *
                    from material""")

    return cursor.fetchall()


# Outputs name from the sennit_and_tube table where parent = material[0] and standard=material[1]
def output_name_sen_and_tube_s(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from sennit_and_tube
                    where parent = ?
                    and standard = ?""", material)

    return cursor.fetchall()


# Outputs name from the sennit_and_tube table where parent = material[0] and diameter_in=material[1]
def output_name_sen_and_tube_d_i(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from sennit_and_tube
                    where parent = ?
                    and diameter_in = ?""", material)

    return cursor.fetchall()


# Outputs name from the sennit_and_tube table where parent = material[0] and diameter_out=material[1]
def output_name_sen_and_tube_d_o(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from sennit_and_tube
                    where parent = ?
                    and diameter_out = ?""", material)

    return cursor.fetchall()


# Outputs name from the sennit_and_tube table where parent = material[0] and wall_thickness=material[1]
def output_name_sen_and_tube_w_t(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from sennit_and_tube
                    where parent = ?
                    and wall_thickness = ?""", material)

    return cursor.fetchall()


# Outputs name from the sennit_and_tube table where parent = material[0] and color=material[1]
def output_name_sen_and_tube_c(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from sennit_and_tube
                    where parent = ?
                    and color = ?""", material)

    return cursor.fetchall()


# Outputs name from the wire table where parent = material[0] and standard=material[1]
def output_name_wire_s(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from wire
                    where parent = ?
                    and standard = ?""", material)

    return cursor.fetchall()


# Outputs name from the wire table where parent = material[0] and wire_thickness=material[1]
def output_name_wire_w_t(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from wire
                    where parent = ?
                    and wire_thickness = ?""", material)

    return cursor.fetchall()


# Outputs name from the wire table where parent = material[0] and color=material[1]
def output_name_wire_c(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from wire
                    where parent = ?
                    and color = ?""", material)

    return cursor.fetchall()


# Outputs name from the wire table where parent = material[0] and brand=material[1]
def output_name_wire_m(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from wire
                    where parent = ?
                    and brand = ?""", material)

    return cursor.fetchall()


# Outputs name from the wire table where parent = material[0] and section=material[1]
def output_name_wire_sec(parent, element):
    material = [parent, element]

    cursor.execute("""select name
                    from wire
                    where parent = ?
                    and section = ?""", material)

    return cursor.fetchall()


# Outputs standard from the table sennit_and_tube
def sel_standard_from_sennit_and_tube(parent):
    cursor.execute("""select standard
                    from sennit_and_tube
                    where parent = ?
                    GROUP BY standard""", parent)

    return cursor.fetchall()


# Outputs diameter_in from the table sennit_and_tube
def sel_diameter_in_from_sennit_and_tube(parent, standard):
    if standard is not None:
        material = [parent, standard]

        cursor.execute("""select diameter_in
                        from sennit_and_tube
                        where parent = ?
                        and standard = ?
                        GROUP BY diameter_in""", material)
    else:
        cursor.execute("""select diameter_in
                        from sennit_and_tube
                        where parent = ?
                        GROUP BY diameter_in""", [parent, ])

    return cursor.fetchall()


# Outputs wall_thickness from the table sennit_and_tube
def sel_wall_thickness_from_sennit_and_tube(parent, standard):
    material = [parent, standard]

    cursor.execute("""select wall_thickness
                    from sennit_and_tube
                    where parent = ?
                    and standard = ?
                    GROUP BY wall_thickness""", material)

    return cursor.fetchall()


# Outputs diameter_out from the table sennit_and_tube
def sel_diameter_out_from_sennit_and_tube(parent, standard):
    material = [parent, standard]

    cursor.execute("""select diameter_out
                    from sennit_and_tube
                    where parent = ?
                    and standard = ?
                    GROUP BY diameter_out""", material)

    return cursor.fetchall()


# Outputs color from the table sennit_and_tube
def sel_color_from_sennit_and_tube(parent, standard):
    if standard is not None:
        material = [parent, standard]

        cursor.execute("""select color
                            from sennit_and_tube
                            where parent = ?
                            and standard = ?
                            GROUP BY color""", material)
    else:
        cursor.execute("""select color
                        from sennit_and_tube
                        where parent = ?
                        GROUP BY color""", [parent, ])

    return cursor.fetchall()


# Outputs standard from the table wire
def sel_standard_from_wire(parent):
    cursor.execute("""select standard
                    from wire
                    where parent = ?
                    group by standard""", [parent, ])

    return cursor.fetchall()


# Outputs wire_thickness from the table wire
def sel_wire_thickness_from_wire(parent, standard):
    if standard is not None:
        material = [parent, standard]

        cursor.execute("""select wire_thickness
                        from wire
                        where parent = ?
                        and standard = ?
                        group by wire_thickness""", material)
    else:
        cursor.execute("""select wire_thickness
                        from wire
                        where parent = ?
                        group by wire_thickness""", [parent, ])

    return cursor.fetchall()


# Outputs color from the table wire
def sel_color_from_wire(parent, standard):
    if standard is not None:
        material = [parent, standard]

        cursor.execute("""select color
                        from wire
                        where parent = ?
                        and standard = ?
                        group by color""", material)
    else:
        cursor.execute("""select color
                        from wire
                        where parent = ?
                        group by color""", [parent, ])

    return cursor.fetchall()


# Outputs brand from the table wire
def sel_brand_from_wire(parent, standard):
    if standard is not None:
        material = [parent, standard]

        cursor.execute("""select brand
                        from wire
                        where parent = ?
                        and standard = ?
                        group by brand""", material)
    else:
        cursor.execute("""select brand
                        from wire
                        where parent = ?
                        group by brand""", [parent, ])

    return cursor.fetchall()


# Outputs section from the table wire
def sel_section_from_wire(parent, standard):
    if standard is not None:
        material = [parent, standard]

        cursor.execute("""select section
                        from wire
                        where parent = ?
                        and standard = ?
                        group by section""", material)
    else:
        cursor.execute("""select section
                        from wire
                        where parent = ?
                        group by section""", [parent, ])

    return cursor.fetchall()


# Outputs all from sennit_and_tube table where parent=parent and name=name
def sel_all_from_sennit_and_tube(parent, name):
    material = [parent, name]

    cursor.execute("""select *
                    from sennit_and_tube
                    where parent = ?
                    and name = ?""", material)

    return cursor.fetchall()


# Outputs all from wire table where parent=parent and name=name
def sel_all_from_wire(parent, name):
    material = [parent, name]

    cursor.execute("""select *
                    from wire
                    where parent = ?
                    and name = ?""", material)

    return cursor.fetchall()


# conn.commit()
# conn.close()
