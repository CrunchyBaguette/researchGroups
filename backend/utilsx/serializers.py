class QuerySerializerMixin:
    PREFETCH_FIELDS = []
    RELATED_FIELDS = []

    @classmethod
    def get_related_queries(cls, queryset):
        if cls.RELATED_FIELDS:
            queryset = queryset.select_related(*cls.RELATED_FIELDS)
        if cls.PREFETCH_FIELDS:
            queryset = queryset.prefetch_related(*cls.PREFETCH_FIELDS)
        return queryset
