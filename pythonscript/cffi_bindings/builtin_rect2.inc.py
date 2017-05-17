class Rect2:
    GD_TYPE = lib.GODOT_VARIANT_TYPE_RECT2

    @classmethod
    def build_from_gd_obj(cls, gd_obj):
        # TODO: optimize this
        v = cls()
        v._gd_obj = gd_obj
        v._gd_obj_ptr = ffi.addressof(gd_obj)
        return v

    @staticmethod
    def check_param_type(argname, arg, type):
        if not isinstance(arg, type):
            raise TypeError('Param `%s` should be of type `%s`' % (argname, type))

    @staticmethod
    def check_param_float(argname, arg):
        if not isinstance(arg, (int, float)):
            raise TypeError('Param `%s` should be of type `float`' % argname)

    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0):
        self._gd_obj_ptr = ffi.new('godot_rect2*')
        lib.godot_rect2_new(self._gd_obj_ptr, x, y, width, height)
        self._gd_obj = self._gd_obj_ptr[0]

    def __eq__(self, other):
        return isinstance(other, Rect2) and lib.godot_rect2_equals(self._gd_obj_ptr, other._gd_obj_ptr)

    def __repr__(self):
        gd_repr = lib.godot_rect2_to_string(self._gd_obj_ptr)
        raw_str = lib.godot_string_unicode_str(ffi.addressof(gd_repr))
        return "<%s%s>" % (type(self).__name__, ffi.string(raw_str))

    # Properties

    @property
    def pos(self):
        return Vector2.build_from_gd_obj(lib.godot_rect2_get_pos(self._gd_obj_ptr))

    @property
    def size(self):
        return Vector2.build_from_gd_obj(lib.godot_rect2_get_size(self._gd_obj_ptr))

    @pos.setter
    def pos(self, val):
        self.check_param_type('val', val, Vector2)
        lib.godot_rect2_set_pos(self._gd_obj_ptr, val._gd_obj)

    @size.setter
    def size(self, val):
        self.check_param_type('val', val, Vector2)
        lib.godot_rect2_set_size(self._gd_obj_ptr, val._gd_obj)

    # Methods
    def clip(self, b):
        self.check_param_type('b', b, Rect2)
        return Rect2.build_from_gd_obj(lib.godot_rect2_clip(self._gd_obj_ptr, b._gd_obj))

    def encloses(self, b):
        self.check_param_type('b', b, Rect2)
        return bool(lib.godot_rect2_encloses(self._gd_obj_ptr, b._gd_obj))

    def expand(self, to):
        self.check_param_type('to', to, Vector2)
        return Rect2.build_from_gd_obj(lib.godot_rect2_expand(self._gd_obj_ptr, to._gd_obj))

    def get_area(self):
        return lib.godot_rect2_get_area(self._gd_obj_ptr)

    def grow(self, by):
        self.check_param_float('by', by)
        return Rect2.build_from_gd_obj(lib.godot_rect2_grow(self._gd_obj_ptr, by))

    def has_no_area(self):
        return bool(lib.godot_rect2_has_no_area(self._gd_obj_ptr))

    def has_point(self, point):
        self.check_param_type('point', point, Vector2)
        return bool(lib.godot_rect2_has_point(self._gd_obj_ptr, point._gd_obj))

    def intersects(self, b):
        self.check_param_type('b', b, Rect2)
        return bool(lib.godot_rect2_intersects(self._gd_obj_ptr, b._gd_obj))

    def merge(self, b):
        self.check_param_type('b', b, Rect2)
        return Rect2.build_from_gd_obj(lib.godot_rect2_merge(self._gd_obj_ptr, b._gd_obj))