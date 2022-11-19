from PyQt5.QtSql import QSqlTableModel


def set_model_to_table(self, widget, table_name, filter_):
    ''' Set a model with selected filter.
    Attach that model to selected table '''

    # Set model
    model = QSqlTableModel();
    model.setTable(table_name)
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.setFilter(filter_)
    model.select()
    print("213")
    # Check for errors
    if model.lastError().isValid():
        self.controller.show_warning(model.lastError().text())

        # Attach model to table view
    widget.setModel(model)

set_model_to_table()