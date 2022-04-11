from PySide2 import QtCore, QtWidgets


class VisibilityChangingElementsQHBoxLayout(QtWidgets.QHBoxLayout):
    """Basic QHBoxLayout class. Used in visibility changing objects to adjust their elements maximumWidth before layout
     geometry to prevent conflicts."""
    def __init__(self, arg__1: QtWidgets.QBoxLayout.Direction):
        super().__init__(arg__1)

    def setGeometry(self, arg__1: QtCore.QRect) -> None:
        """Call element's adjust_visible_data_elements_maximum_size to adjust element's objects maximum width
        before setting geometry."""
        self.parent().adjust_visible_data_elements_maximum_size()
        super(VisibilityChangingElementsQHBoxLayout, self).setGeometry(arg__1)
