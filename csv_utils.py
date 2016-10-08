
import datetime
import collections
import csv


def get_headers(header_row):
    return { name: loc for loc, name in enumerate(header_row) }


def cdate(val, fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.strptime(val, fmt)


def _rename(field):
    rename_map = (
      ('#'   , '_num'    ),
      ('. '  , '_'       ),
      ('- '  , ''        ),
      (' '   , '_'       ),
      ('.'   , '_'       ),
      ('/'   , '_'       ),
      ('"'   , ''        ),
      ('%'   , 'pct'     ),
      ('$'   , 'dollars' ),
      ('('   , ''        ),
      (')'   , ''        ),
    )
    for fr, to in rename_map:
        field = field.replace(fr, to)
    return (field if field[-1] != '.' else field[:-1]).lower()


def read(csv_filename, headers=True):
    c = csv.reader(open(csv_filename, 'rb'))
    # Headers / get function
    if headers:
        hdr = { nam : pos for pos, nam in enumerate(c.next()) }
        get = lambda row, nam: row[hdr[nam]] if type(nam) == str else row[nam]
    else:
        hdr = {}
        def get(row, nam):
            raise NotImplementedError("No headers, no get")
    # Data
    rows = []
    for r in c:
        rows.append(r)
    return rows, get
